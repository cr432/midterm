"""plugins/divide_plugin.py"""
from decimal import Decimal
from logging_config import logger
from plugins.plugin_interface import CommandPlugin

class DividePlugin(CommandPlugin):
    """Division plugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            result = a / b
            logger.info('Division operation: %s / %s = %s', a, b, result)
            return result
        logger.error("Division by zero error")
        raise ZeroDivisionError("Error: Division by zero.")
