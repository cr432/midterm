"""test_operations.py"""
from decimal import Decimal
import logging
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Set up logging
logger = logging.getLogger(__name__)

def test_add_command():
    """Test add command."""
    logger.info("Testing add command.")
    add_command = AddCommand()
    result = add_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')

def test_subtract_command():
    """Test subtract command."""
    logger.info("Testing subtract command.")
    subtract_command = SubtractCommand()
    result = subtract_command.execute(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')

def test_multiply_command():
    """Test multiply command."""
    logger.info("Testing multiply command.")
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('6')

def test_divide_command():
    """Test divide command."""
    logger.info("Testing divide command.")
    divide_command = DivideCommand()
    result = divide_command.execute(Decimal('6'), Decimal('2'))
    assert result == Decimal('3')
