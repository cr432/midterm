"""__init__.py"""
from decimal import Decimal
import logging
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand  # Import the MenuCommand
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.calculation import Calculation  # Represents a single calculation

# Set up logging
logger = logging.getLogger(__name__)

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, command) -> Decimal:
        """Create and perform a calculation, then return the result."""
        logger.info(f'Performing operation with operands {a} and {b} using {command.__class__.__name__} command')
        
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, command)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        logger.info(f'Calculation added to history: {calculation}')
        
        # Perform the calculation and return the result
        result = calculation.perform()
        logger.info(f'Calculation result: {result}')
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        logger.info(f'Performing addition operation with operands {a} and {b}')
        return Calculator._perform_operation(a, b, AddCommand())

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        logger.info(f'Performing subtraction operation with operands {a} and {b}')
        return Calculator._perform_operation(a, b, SubtractCommand())

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        logger.info(f'Performing multiplication operation with operands {a} and {b}')
        return Calculator._perform_operation(a, b, MultiplyCommand())

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        logger.info(f'Performing division operation with operands {a} and {b}')
        return Calculator._perform_operation(a, b, DivideCommand())

    @staticmethod
    def menu(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, MenuCommand())

