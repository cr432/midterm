"""test_environment_variables.py"""
import os

# Load environment variables from .env file in the parent directory
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def test_environment_variables():
    """Test environment variables """
    # Access and print the values of environment variables
    log_level = os.getenv('LOG_LEVEL')
    log_file_path = os.getenv('LOG_FILE_PATH')

    print(f'LOG_LEVEL: {log_level}')
    print(f'LOG_FILE_PATH: {log_file_path}')

if __name__ == "__main__":
    test_environment_variables()
