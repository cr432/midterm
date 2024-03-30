# calculation.py
from decimal import Decimal
import logging
from calculator.operations import Command  # Assuming you have a commands module

# Set up logging
logger = logging.getLogger(__name__)

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, command: Command):
        self.a = a
        self.b = b
        self.command = command

    @staticmethod    
    def create(a: Decimal, b: Decimal, command: Command):
        logger.info(f'Creating new calculation with operands {a} and {b}, using {command.__class__.__name__} command')
        return Calculation(a, b, command)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        logger.info(f'Performing calculation with operands {self.a} and {self.b}, using {self.command.__class__.__name__} command')
        result = self.command.execute(self.a, self.b)
        logger.info(f'Calculation result: {result}')
        return result

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.command.__class__.__name__})"
