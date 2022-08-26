from os import environ

from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": environ.get('DB_HOST', 'db'),
        "database": environ.get('DB_NAME', 'postgres'),
        "user": environ.get('DB_USER', 'postgres'),
        "password": environ.get('DB_PASSWORD', 'postgres'),
        "prefix": "",
        "port": environ.get('DB_PORT', '5432'),
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)

