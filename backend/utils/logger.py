import logging

# Set up logging
def setup_logger(name: str):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)  # Change this to INFO or ERROR as needed
    return logger

# Example: Using logger
logger = setup_logger(__name__)
logger.info("Logging setup complete")