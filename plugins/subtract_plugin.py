"""plugins/subtract_plugin.py"""
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from logging_config import logger

class SubtractPlugin(CommandPlugin):
    """Subtraction plugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a - b
        logger.info(f'Subtraction operation: {a} - {b} = {result}')
        return result
