"""test_calculations.py"""
import os
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_add_calculation():
    """Test adding calculation."""
    a = 2
    b = 3
    command = "add"
    calculation = Calculation(a, b, command)

    Calculations.clear_history()
    Calculations.add_calculation(calculation)

    history = Calculations.get_history()
    assert len(history) == 1
    assert history[0] == calculation

def test_clear_history():
    """Test clearing history."""
    Calculations.clear_history()
    history = Calculations.get_history()
    assert len(history) == 0

def test_load_save_history(tmpdir):
    """Test loading and saving history."""
    file_path = os.path.join(tmpdir, 'test_history.csv')

    # Add some calculations to history
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(2, 3, 'add'))
    Calculations.add_calculation(Calculation(4, 5, 'multiply'))

    # Save history
    Calculations.save_history_to_csv(file_path)
