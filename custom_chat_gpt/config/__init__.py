import os
import yaml
from dotenv import load_dotenv

# load enviroment variable from .env file

load_dotenv()


class AppConfig:
    """ Class to handle application configuration in yaml file"""
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        """ Load configuration from config.yaml file"""

        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        # Replace API Key placeholder with the acutal values from environment variable
        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('API_KEY') 

        return config

# Load the configuration

app_config = AppConfig()
config = app_config.config 

