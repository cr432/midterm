"""menu_plugin.py"""
from logging_config import logger
from decimal import Decimal

class MenuPlugin:
    """Menu plugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Displaying available commands.")
        logger.info("add - Addition")
        logger.info("subtract - Subtraction")
        logger.info("multiply - Multiplication")
        logger.info("divide - Division")
        return Decimal(0)  # Return 0 or any value, as it won't affect the result:
