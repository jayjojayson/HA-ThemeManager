"""Theme Manager – Services."""

import logging
import yaml
from pathlib import Path

from homeassistant.core import HomeAssistant, ServiceCall

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_register_services(hass: HomeAssistant) -> None:
    """Komfort-Services für Theme-Verwaltung registrieren."""
    if hass.services.has_service(DOMAIN, "apply_theme"):
        return

    hass.services.async_register(DOMAIN, "apply_theme", _service_apply_theme)
    hass.services.async_register(DOMAIN, "reload_themes", _service_reload_themes)
    hass.services.async_register(DOMAIN, "list_themes", _service_list_themes)


async def _service_apply_theme(call: ServiceCall) -> None:
    """Globales Theme via frontend.set_theme setzen."""
    theme_name = call.data.get("theme_name", "default")
    await call.hass.services.async_call(
        "frontend",
        "set_theme",
        {"name": theme_name},
        blocking=True,
    )
    _LOGGER.info("Globales Theme gesetzt: %s", theme_name)


async def _service_reload_themes(call: ServiceCall) -> None:
    """Themes aus /config/themes/ neu laden (Wrapper um frontend.reload_themes)."""
    await call.hass.services.async_call("frontend", "reload_themes", blocking=True)
    _LOGGER.info("Themes neu geladen")


async def _service_list_themes(call: ServiceCall) -> None:
    """Alle Theme-Namen aus /config/themes/ ins Log schreiben."""
    themes_dir = Path(call.hass.config.config_dir) / "themes"
    themes: list[str] = []

    if themes_dir.exists():
        for yaml_file in sorted(themes_dir.glob("*.yaml")):
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                if isinstance(data, dict):
                    themes.extend(
                        name for name, vars_ in data.items() if isinstance(vars_, dict)
                    )
            except Exception as exc:
                _LOGGER.error("Fehler beim Lesen von %s: %s", yaml_file, exc)

    _LOGGER.info("Verfügbare Themes (%d): %s", len(themes), themes)
