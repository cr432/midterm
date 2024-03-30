# calculations.py
import pandas as pd
from typing import List
import logging

from calculator.calculation import Calculation

# Set up logging
logger = logging.getLogger(__name__)

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        logger.info(f'Adding calculation to history: {calculation}')
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        logger.info('Retrieving entire history of calculations')
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        logger.info('Clearing the history of calculations')
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        logger.info('Retrieving the latest calculation')
        if cls.history:
            latest_calculation = cls.history[-1]
            logger.info(f'Latest calculation: {latest_calculation}')
            return latest_calculation
        logger.info('No calculations found in history')
        return None

    @classmethod
    def load_history(cls, file_path: str):
        """Load calculation history from a CSV file."""
        logger.info(f'Loading calculation history from {file_path}')
        try:
            df = pd.read_csv(file_path)
            cls.history = [Calculation(row['a'], row['b'], row['command']) for _, row in df.iterrows()]
            logger.info(f'Calculation history loaded successfully')
        except FileNotFoundError:
            logger.warning(f'File {file_path} not found. Skipping loading history.')
        except Exception as e:
            logger.error(f'Error loading calculation history: {e}')

    @classmethod
    def save_history(cls, file_path: str):
        """Save calculation history to a CSV file."""
        logger.info(f'Saving calculation history to {file_path}')
        try:
            df = pd.DataFrame([{'a': calc.a, 'b': calc.b, 'command': calc.command} for calc in cls.history])
            df.to_csv(file_path, index=False)
            logger.info(f'Calculation history saved successfully')
        except Exception as e:
            logger.error(f'Error saving calculation history: {e}')
