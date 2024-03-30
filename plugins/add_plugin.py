"""plugins/add_plugin.py"""
from decimal import Decimal
from logging_config import logger
from plugins.plugin_interface import CommandPlugin

class AddPlugin(CommandPlugin):
    """Addition plugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        logger.info(f'Addition operation: {a} + {b} = {result}')
        return result
