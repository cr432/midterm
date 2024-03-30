"""plugins/multiply_plugin.py"""
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from logging_config import logger

class MultiplyPlugin(CommandPlugin):
    """Multiplication plugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a * b
        logger.info(f'Multiplication operation: {a} * {b} = {result}')
        return result
