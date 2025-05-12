from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import CustomLogger
import AppConfig

# Load environment variables from .env file
load_dotenv()


def create_app(): 
    """ Create and configure the Flask application"""
    app = Flask(__name__, template_folder = 'templates') # Initialize the flask app

    # Load configuration
    app_config = AppConfig()
    app.config.update(app_config.config)

    # Set up logging 
    logger = CustomLogger().get_logger()
    logger.info('Flask application starting....')

    # Import and register routes

