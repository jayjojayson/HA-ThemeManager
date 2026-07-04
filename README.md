# Theme Manager for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![Validate with hassfest](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/hassfest.yaml)
[![Validate with HACS](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/validate.yaml/badge.svg)](https://github.com/jayjojayson/HA-ThemeManager/actions/workflows/validate.yaml)
[![GitHub Release](https://img.shields.io/github/release/jayjojayson/HA-ThemeManager.svg?style=flat-square)](https://github.com/jayjojayson/HA-ThemeManager/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jayjojayson/HA-ThemeManager?style=flat-square)](https://github.com/jayjojayson/HA-ThemeManager/stargazers)
[![Deutsch lesen](https://img.shields.io/badge/Deutsch-README-blue.svg)](README_de.md)

A custom integration that provides a collection of high-quality themes as YAML files in `/config/themes/`. Themes are selected directly from the HA user profile – no dashboard card, no Lovelace setup required.

---

## Support

If you like this integration and want to support my work:

<a href="https://ko-fi.com/jayjojayson" target="_blank">
  <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Ko-Fi" height="50">
</a>

---

## How it works

1. Install the integration & restart HA
2. Theme files appear automatically in `/config/themes/`
3. Select a theme under **Profile → Appearance → Theme**

> **Important:** For the themes to appear, the profile theme must be set to **"Automatic"** or **"Backend-selected"** – not to a fixed theme.

---

## Installation

### Via HACS (recommended)

use the link to install it:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jayjojayson&repository=HA-ThemeManager&category=integration)

or

1. Open HACS → **Integrations** → three-dot menu → **Custom repositories**
2. Enter URL `https://github.com/jayjojayson/HA-ThemeManager`, choose category **Integration** → **Add**
3. Search for and install **Theme Manager**
4. Restart Home Assistant

### Manual installation

```bash
cp -r custom_components/theme_manager /config/custom_components/theme_manager
```

### Activate the integration

**Settings → Devices & Services → Add Integration → "Theme Manager"**

The preset themes are automatically written to `/config/themes/` and `frontend.reload_themes` is called.

The integration adds the following block to `configuration.yaml` automatically if it is not already present:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Select a theme

**Profile → Appearance → Theme** → choose the theme you want → active immediately.

---

## Predefined themes

All themes support **Auto / Dark / Light** – the toggle in the HA user profile works like the standard HA theme.

| Theme | Dark style | Light variant |
|-------|------------|----------------|
| Modern Dark | Google Material Dark | Material Light |
| Dracula | Classic Dracula | Dracula Hell |
| Catppuccin Mocha | Catppuccin Mocha | Catppuccin Latte (official) |
| Solarized Dark | Solarized Dark | Solarized Light (official) |
| GitHub Dark | GitHub Dark | GitHub Light |
| Nord | Nord Polarnight | Nord Snowstorm |
| Monokai | Monokai Dark | Monokai Hell |
| Oceanic Dark | Ocean Dark | Ocean Turquoise |
| HA HomeDashboard | Minimal, transparent cards (requires Card Mod) | – |
| Glass | Semi-transparent cards, blur effect, large radius ¹ | Frosted-glass light |
| Sharp | Straight lines, 0 px radius, clean flat design |
| Clean white/gray |
| Aurora | Radial gradient dark blue → forest green (top right), northern lights look ¹ | Blue → mint green (light) |
| Horizon | Linear gradient dark blue → warm orange (sunset, top→bottom) ¹ | Sky blue → peach (light) |
| Mono | Monospace font, terminal green on black ² | Terminal green on white |
| Rounded | Rounded font (`ui-rounded`), very large card radii ² | Airy, pastel rose |

> ¹ **Blur effect** requires the [Card Mod](https://github.com/thomasloven/lovelace-card-mod) custom component. Gradient and colors work without Card Mod.
> ² **Font themes** apply the font broadly via Card Mod. Without Card Mod only `mdc-typography-font-family` is applied (Material elements).

---

## Add your own themes

Copy a preset from `/config/themes/`, rename it (for example `my_theme.yaml`), and customize it as desired. The file will not be overwritten on the next restart – only preset files are updated. Then call **Services → `frontend.reload_themes`** once and the theme appears immediately in the profile.

The format for dark and light support:

```yaml
My Theme:
  # Structural values (apply to both modes)
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

## `/config/themes/` after installation

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

> Preset files are rewritten on every startup (always up to date). Custom `.yaml` files in the folder remain untouched.

---

## Supported CSS variables

All preset themes set the following HA variables:

### Colors & backgrounds
| Variable | Description |
|----------|-------------|
| `primary-color` | Primary color (buttons, links, highlights) |
| `accent-color` | Accent color |
| `primary-background-color` | Page background |
| `secondary-background-color` | Secondary background |

### Cards
| Variable | Description |
|----------|-------------|
| `card-background-color` | Card background |
| `ha-card-background` | Card background (newer HA versions) |
| `ha-card-border-width` | Card border width |
| `ha-card-border-radius` | Card border radius |

### Text
| Variable | Description |
|----------|-------------|
| `primary-text-color` | Primary text |
| `secondary-text-color` | Secondary text |
| `disabled-text-color` | Disabled text |

### App header & sidebar
| Variable | Description |
|----------|-------------|
| `app-header-background-color` | Top bar background |
| `app-header-text-color` | Top bar text |
| `sidebar-background-color` | Sidebar background |
| `sidebar-icon-color` | Sidebar icons |
| `sidebar-selected-icon-color` | Active entry – icon |

### Status & icons
| Variable | Description |
|----------|-------------|
| `state-icon-color` | Default icon color |
| `error-color` | Error color |
| `success-color` | Success color |
| `warning-color` | Warning color |

---

## Service calls

### Reload themes (after custom YAML changes)
```yaml
service: theme_manager.reload_themes
```

### Set a global default theme
```yaml
service: theme_manager.apply_theme
data:
  theme_name: "Dracula"
```

### Log available themes
```yaml
service: theme_manager.list_themes
```

---

## Project structure

```
custom_components/theme_manager/
├── __init__.py          # integration setup, writes theme files
├── manifest.json        # metadata
├── config_flow.py       # one-time setup
├── const.py             # preset definitions & custom template
├── services.py          # service handlers
├── services.yaml        # HA service descriptions
└── translations/
    ├── de.json
    └── en.json
```

---

## Planned enhancements

- More themes (light-mode variants, high contrast)
- More CSS variables (climate cards, energy dashboard, map card)

---

MIT License – created by [jayjojayson](https://github.com/jayjojayson)

