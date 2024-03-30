"""test_calculator_operations.py"""
from decimal import Decimal
import logging
from calculator import Calculator

# Set up logging
logger = logging.getLogger(__name__)

def test_addition():
    """Test addition operation."""
    logger.info("Testing addition operation.")
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    """Test subtraction operation."""
    logger.info("Testing subtraction operation.")
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_divide():
    """Test division operation."""
    logger.info("Testing division operation.")
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_multiply():
    """Test multiplication operation."""
    logger.info("Testing multiplication operation.")
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_menu():
    """Test menu operation."""
    logger.info("Testing menu operation.")
    assert Calculator.menu(Decimal('0'), Decimal('0')) == Decimal('0')  # Modify based on your menu command behavior
