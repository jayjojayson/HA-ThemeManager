"""Theme Manager – Config Flow."""

import logging

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ThemeManagerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Einmalige Einrichtung des Theme Managers."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Einrichtungs-Schritt: Nur einmal pro HA-Instanz erlaubt."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return self.async_create_entry(title="Theme Manager", data={})

        return self.async_show_form(step_id="user")
