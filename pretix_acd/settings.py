import logging
from pretix.settings import CONFIG_FILE

logger = logging.getLogger(__name__)

mollie_key = CONFIG_FILE.get("pretix_acd", "mollie_api_key", fallback="NOKEY")
logger.info("Mollie key '%s' default setting.", mollie_key)


DEFAULTS = {
    "primary_color": {"default": "#0d6efd", "type": str},
    "invoice_address_asked": {"default": "False", "type": bool},
    "waiting_list_enabled": {"default": "True", "type": bool},
    "payment_giftcard__enabled": {"default": "False", "type": bool},
    "payment_mollie__enabled": {"default": "True", "type": bool},
    "payment_mollie_method_ideal": {"default": "True", "type": bool},
    "attendee_names_asked": {"default": "True", "type": bool},
    "ticket_download": {"default": "True", "type": bool},
    "ticketoutput_pdf__enabled": {"default": "True", "type": bool},
    "payment_mollie_api_key": {"default": mollie_key, "type": str},
    "max_items_per_order": {"default": "1", "type": int},
}
