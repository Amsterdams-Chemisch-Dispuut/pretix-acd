import logging
from . import __version__

from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from pretix_acd.settings import DEFAULTS


logger = logging.getLogger(__name__)


class PluginApp(AppConfig):
    name = "pretix_acd"
    verbose_name = "Pretix for acd"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix for acd")
        author = "ICT Commissie des ACDs"
        description = gettext_lazy(
            "Study association ACD mollie key setter for pretix"
        )
        visible = True
        version = __version__

    def ready(self):
        from pretix.base.settings import settings_hierarkey

        for k, v in DEFAULTS.items():
            settings_hierarkey.add_default(k, v["default"], v["type"])
            logger.info(f"Adding '{k}' default setting.")


logger.info("Loaded pretix_acd configurations")
