# plugin_interface.py
from decimal import Decimal
from abc import ABC, abstractmethod
from logging_config import logger

class CommandPlugin(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Executing plugin command.")
