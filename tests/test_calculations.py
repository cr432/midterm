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
    Calculations.save_history(file_path)

    # Clear history and load from file
    Calculations.clear_history()
    Calculations.load_history(file_path)

    # Check if loaded history matches original history
    loaded_history = Calculations.get_history()
    assert len(loaded_history) == 2
    assert loaded_history[0].a == 2
    assert loaded_history[0].b == 3
    assert loaded_history[0].command == 'add'
    assert loaded_history[1].a == 4
    assert loaded_history[1].b == 5
    assert loaded_history[1].command == 'multiply'
