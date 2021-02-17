import json
from models import Config


def load_config():
    with open('config.json', 'r') as f:
        settings = json.loads(f.read())
        config = Config(settings)


def write_config(settings):
    config = Config(settings)
    with open('config2.json', 'w') as f:
        f.write(config.to_json())
