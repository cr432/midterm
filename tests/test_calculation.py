"""test_calculation.py"""
from decimal import Decimal
import logging
from calculator.calculation import Calculation
from calculator.operations import Command

# Set up logging
logger = logging.getLogger(__name__)

class MockCommand(Command):
    """MockCommand class"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Executing MockCommand.")
        return a + b

def test_create_calculation():
    """Test the creation of calculation."""
    logger.info("Testing creation of calculation.")
    a = Decimal('2')
    b = Decimal('3')
    command = MockCommand()
    calculation = Calculation.create(a, b, command)
    assert calculation.a == a
    assert calculation.b == b
    assert calculation.command == command

def test_perform_calculation():
    """Test performing calculation."""
    logger.info("Testing performing of calculation.")
    a = Decimal('4')
    b = Decimal('5')
    command = MockCommand()
    calculation = Calculation(a, b, command)
    result = calculation.perform()
    assert result == a + b

def test_repr_calculation():
    """Test string representation of calculation."""
    logger.info("Testing string representation of calculation.")
    a = Decimal('6')
    b = Decimal('7')
    command = MockCommand()
    calculation = Calculation(a, b, command)
    repr_str = repr(calculation)
    assert f"Calculation({a}, {b}, MockCommand)" == repr_str
