import logging
import google.cloud.logging

def get_logger(name):
    #Create client from gcp
    client = google.cloud.logging.Client()
    client.setup_logging()
    logger = logging.getLogger(name)

    return logger