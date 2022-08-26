from os import environ

API_VERSION = "1.0.0"
ENVIRONMENT = environ.get("FLASK_ENV", "local")
API_URL = environ.get("API_URL", "http://localhost:5000/api/v1")