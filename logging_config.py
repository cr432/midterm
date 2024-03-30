# logging_config.py
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def configure_logging():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

    # Create a file handler and set its log level
    file_handler = logging.FileHandler(os.getenv('LOG_FILE_PATH', 'app.log'))
    file_handler.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

    # Create a console handler and set its log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

    # Define the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Set the format for both handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Call the configure_logging function to set up logging
logger = configure_logging()
