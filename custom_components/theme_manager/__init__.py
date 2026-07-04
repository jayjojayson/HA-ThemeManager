"""Theme Manager – Home Assistant Integration.

Stellt eine Sammlung von Preset-Themes als YAML-Dateien in /config/themes/ bereit
und sorgt dafür, dass der Themes-Ordner in configuration.yaml registriert ist.

Die Theme-Auswahl erfolgt direkt im HA-Profil unter
'Mein Konto → Erscheinungsbild → Design'.
"""

import logging
import yaml
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PRESET_THEMES
from .services import async_register_services

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Config-Entry einrichten – schreibt Theme-Dateien und patcht configuration.yaml."""
    _LOGGER.info("Theme Manager wird gestartet …")

    themes_dir = Path(hass.config.config_dir) / "themes"
    config_file = Path(hass.config.config_dir) / "configuration.yaml"

    await hass.async_add_executor_job(_setup_themes_dir, themes_dir)
    await hass.async_add_executor_job(_ensure_frontend_themes_config, config_file)

    await async_register_services(hass)

    # Themes neu laden, damit neu geschriebene Preset-Dateien sofort verfügbar sind
    themes_loaded = False
    try:
        await hass.services.async_call("frontend", "reload_themes", blocking=True)
        themes_loaded = True
        _LOGGER.info("frontend.reload_themes erfolgreich aufgerufen")
    except Exception as exc:
        _LOGGER.warning("frontend.reload_themes fehlgeschlagen: %s", exc)

    if not themes_loaded:
        await hass.services.async_call(
            "persistent_notification",
            "create",
            {
                "title": "Theme Manager – Neustart erforderlich",
                "message": (
                    "Die Preset-Themes wurden nach `/config/themes/` kopiert "
                    "und `configuration.yaml` wurde aktualisiert.\n\n"
                    "**Bitte Home Assistant einmal neu starten**, "
                    "damit die Themes geladen werden.\n\n"
                    "Anschließend kannst du das Theme unter "
                    "*Mein Konto → Erscheinungsbild → Design* auswählen."
                ),
                "notification_id": "theme_manager_restart_required",
            },
        )

    _LOGGER.info("Theme Manager erfolgreich gestartet ✅")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Config-Entry entladen."""
    return True


# ---------------------------------------------------------------------------
# Hilfsfunktionen (laufen im Executor)
# ---------------------------------------------------------------------------

def _setup_themes_dir(themes_dir: Path) -> None:
    """Themes-Ordner anlegen und Preset-YAMLs schreiben."""
    themes_dir.mkdir(parents=True, exist_ok=True)

    # Preset-Dateien IMMER überschreiben – stellt aktuelles Format sicher.
    # Eigene User-Dateien bleiben unangetastet.
    for theme_key, theme_data in PRESET_THEMES.items():
        filepath = themes_dir / f"{theme_key}.yaml"
        display_name = theme_data["display_name"]
        theme_yaml = {display_name: theme_data["variables"]}
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(
                theme_yaml,
                f,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False,
            )
        _LOGGER.debug("Preset geschrieben: %s", filepath.name)


def _ensure_frontend_themes_config(config_file: Path) -> None:
    """Fügt 'frontend: themes: !include_dir_merge_named themes' in configuration.yaml ein."""
    if not config_file.exists():
        return

    content = config_file.read_text("utf-8")

    if "include_dir_merge_named themes" in content:
        return

    lines = content.splitlines(keepends=True)

    for i, line in enumerate(lines):
        if line.rstrip("\n\r") == "frontend:":
            lines.insert(i + 1, "  themes: !include_dir_merge_named themes\n")
            config_file.write_text("".join(lines), "utf-8")
            _LOGGER.info(
                "configuration.yaml: 'themes' unter bestehendem 'frontend:' Block ergänzt"
            )
            return

    with open(config_file, "a", encoding="utf-8") as f:
        f.write(
            "\n# Theme Manager – Themes aus /config/themes/ laden\n"
            "frontend:\n"
            "  themes: !include_dir_merge_named themes\n"
        )
    _LOGGER.info("configuration.yaml: 'frontend.themes' Block hinzugefügt")
