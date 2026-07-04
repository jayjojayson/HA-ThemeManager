# Theme Manager für Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![Validate with hassfest](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/hassfest.yaml)
[![Validate with HACS](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/validate.yaml/badge.svg)](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/validate.yaml)
[![GitHub Release](https://img.shields.io/github/release/jayjojayson/HA-ThemeManager.svg?style=flat-square)](https://github.com/jayjojayson/HA-ThemeManager/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jayjojayson/HA-ThemeManager?style=flat-square)](https://github.com/jayjojayson/HA-ThemeManager/stargazers)
[![Read in English](https://img.shields.io/badge/English-README-blue.svg)](README.md)

Eine Custom Integration, die eine Sammlung hochwertiger Themes als YAML-Dateien in `/config/themes/` bereitstellt. Die Theme-Auswahl erfolgt direkt im HA-Benutzerprofil – kein Dashboard-Card, kein Lovelace-Setup nötig.

---

## Support

Wenn dir diese Integration gefällt und du meine Arbeit unterstützen möchtest:

<a href="https://www.buymeacoffee.com/jayjojayson" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50">
</a>
&nbsp;
<a href="https://ko-fi.com/jayjojayson" target="_blank">
  <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Ko-Fi" height="50">
</a>

---

## Funktionsweise

1. Integration installieren & HA neu starten
2. Theme-Dateien erscheinen automatisch in `/config/themes/`
3. Theme auswählen unter **Mein Konto → Erscheinungsbild → Design**

> **Wichtig:** Damit die Themes sichtbar werden, muss im Profil das Design auf **„Automatisch"** oder **„Backend-Auswahl"** gestellt sein – nicht auf ein fest gewähltes Theme.

---

## Installation

### Via HACS (empfohlen)

Nutze den Link für die Installtion

 [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jayjojayson&repository=HA-ThemeManager&category=integration)

 oder

1. HACS öffnen → **Integrationen** → Drei-Punkte-Menü → **Benutzerdefinierte Repositories**
2. URL `https://github.com/jayjojayson/HA-ThemeManager` eingeben, Kategorie **Integration** wählen → **Hinzufügen**
3. Integration **Theme Manager** suchen und installieren
4. Home Assistant neu starten

### Manuell

```bash
cp -r custom_components/theme_manager /config/custom_components/theme_manager
```

### Integration aktivieren

**Einstellungen → Geräte & Dienste → Integration hinzufügen → „Theme Manager"**

Die Preset-Themes werden automatisch nach `/config/themes/` geschrieben und `frontend.reload_themes` wird aufgerufen.

Die Integration fügt automatisch folgenden Block in `configuration.yaml` ein – falls noch nicht vorhanden:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Theme auswählen

**Mein Konto → Erscheinungsbild → Design** → gewünschtes Theme wählen → sofort aktiv.

---

## Vordefinierte Themes

Alle Themes unterstützen **Auto / Dunkel / Hell** – der Umschalter im HA-Benutzerprofil funktioniert damit wie beim Standard-HA-Theme.

| Theme | Dark-Stil | Light-Variante |
|-------|-----------|----------------|
| Modern Dark | Google Material Dark | Material Light |
| Dracula | Klassisches Dracula | Dracula Hell |
| Catppuccin Mocha | Catppuccin Mocha | Catppuccin Latte (offiziell) |
| Solarized Dark | Solarized Dark | Solarized Light (offiziell) |
| GitHub Dark | GitHub Dark | GitHub Light |
| Nord | Nord Polarnight | Nord Snowstorm |
| Monokai | Monokai Dark | Monokai Hell |
| Oceanic Dark | Ozean Dunkel | Ozean Türkis |
| HA HomeDashboard | Minimalistisch, transparente Karten (erfordert Card-Mod) | – |
| Glass | Halbtransparente Karten, Blur-Effekt, großer Radius ¹ | Frosted-Glass hell |
| Sharp | Geradlinig, 0 px Radius, klares Flat-Design | Sauberes Weiß/Grau |
| Aurora | Radial-Gradient dunkelblau → waldgrün (oben rechts), Nordlichter-Optik ¹ | Blau → Mintgrün (hell) |
| Horizon | Linearer Gradient dunkelblau → warm-orange (Sonnenuntergang, oben→unten) ¹ | Himmelblau → Pfirsich (hell) |
| Mono | Monospace-Schrift, Terminal-Grün auf Schwarz ² | Terminal-Grün auf Weiß |
| Rounded | Gerundete Schrift (`ui-rounded`), sehr große Kartenradien ² | Luftig, Pastellrosé |

> ¹ **Blur-Effekt** benötigt die [Card-Mod](https://github.com/thomasloven/lovelace-card-mod) Custom Component. Gradient und Farben funktionieren auch ohne Card-Mod.
> ² **Font-Themes** wenden die Schriftart via Card-Mod breit an. Ohne Card-Mod gilt nur `mdc-typography-font-family` (Material-Elemente).

---

## Eigene Themes hinzufügen

Ein Preset aus `/config/themes/` kopieren, umbenennen (z.B. `mein_theme.yaml`) und nach Belieben anpassen. Die Datei wird beim nächsten Start nicht überschrieben – nur die Preset-Dateien werden aktualisiert. Danach einmal **Dienste → `frontend.reload_themes`** aufrufen und das Theme erscheint sofort im Profil.

Das Format für Dark- und Light-Unterstützung:

```yaml
Mein Theme:
  # Strukturelle Werte (gelten für beide Modi)
  ha-card-border-radius: "12px"
  ha-card-border-width: "0px"

  modes:
    dark:
      primary-color: "#ff5722"
      primary-background-color: "#1a1a2e"
      primary-text-color: "#eaeaea"
      card-background-color: "#16213e"

    light:
      primary-color: "#d84315"
      primary-background-color: "#ffffff"
      primary-text-color: "#212121"
      card-background-color: "#f5f5f5"
```

---

## `/config/themes/` nach Installation

```
/config/themes/
├── modern_dark.yaml
├── dracula.yaml
├── catppuccin_mocha.yaml
├── solarized_dark.yaml
├── github_dark.yaml
├── nord.yaml
├── monokai.yaml
├── oceanic_dark.yaml
├── ha_homedashboard.yaml
├── glass.yaml
├── sharp.yaml
├── aurora.yaml
├── horizon.yaml
├── mono.yaml
└── rounded.yaml
```

> Preset-Dateien werden bei jedem Start neu geschrieben (immer aktuell). Eigene `.yaml`-Dateien im Ordner bleiben unangetastet.

---

## Unterstützte CSS-Variablen

Alle Preset-Themes setzen folgende HA-Variablen:

### Farben & Hintergründe
| Variable | Beschreibung |
|----------|-------------|
| `primary-color` | Hauptfarbe (Buttons, Links, Highlights) |
| `accent-color` | Akzentfarbe |
| `primary-background-color` | Seiten-Hintergrund |
| `secondary-background-color` | Sekundärer Hintergrund |

### Karten
| Variable | Beschreibung |
|----------|-------------|
| `card-background-color` | Card-Hintergrund |
| `ha-card-background` | Card-Hintergrund (neuere HA-Versionen) |
| `ha-card-border-width` | Card-Rahmenbreite |
| `ha-card-border-radius` | Card-Eckenradius |

### Text
| Variable | Beschreibung |
|----------|-------------|
| `primary-text-color` | Haupttext |
| `secondary-text-color` | Untergeordneter Text |
| `disabled-text-color` | Deaktivierter Text |

### App-Header & Sidebar
| Variable | Beschreibung |
|----------|-------------|
| `app-header-background-color` | Topbar-Hintergrund |
| `app-header-text-color` | Topbar-Text |
| `sidebar-background-color` | Sidebar-Hintergrund |
| `sidebar-icon-color` | Sidebar-Icons |
| `sidebar-selected-icon-color` | Aktiver Eintrag – Icon |

### Status & Icons
| Variable | Beschreibung |
|----------|-------------|
| `state-icon-color` | Standard-Icon-Farbe |
| `error-color` | Fehlerfarbe |
| `success-color` | Erfolgsfarbe |
| `warning-color` | Warnfarbe |

---

## Service-Calls

### Themes neu laden (nach eigenen YAML-Änderungen)
```yaml
service: theme_manager.reload_themes
```

### Globales Standard-Theme setzen
```yaml
service: theme_manager.apply_theme
data:
  theme_name: "Dracula"
```

### Verfügbare Themes ins Log schreiben
```yaml
service: theme_manager.list_themes
```

---

## Projektstruktur

```
custom_components/theme_manager/
├── __init__.py          # Integration-Setup, Theme-Dateien schreiben
├── manifest.json        # Metadaten
├── config_flow.py       # Einmalige Einrichtung
├── const.py             # Preset-Definitionen & Custom-Template
├── services.py          # Service-Handler
├── services.yaml        # Service-Beschreibungen für HA
└── translations/
    ├── de.json
    └── en.json
```

---

## Geplante Erweiterungen

- Weitere Themes (Light-Mode-Varianten, High-Contrast)
- Mehr CSS-Variablen (Klima-Karten, Energie-Dashboard, Map-Card)

---

MIT License – erstellt von [jayjojayson](https://github.com/jayjojayson)



