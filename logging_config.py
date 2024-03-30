# logging_config.py
import logging

def configure_logging():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a file handler and set its log level to INFO
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)

    # Create a console handler and set its log level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

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
