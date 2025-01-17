import os
from dotenv import load_dotenv


load_dotenv()


DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_NAME = os.getenv('DB_NAME')

ALGORITHM = os.getenv('ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')


def get_auth_data() -> dict:
    return {"secret_key": SECRET_KEY, "algorithm": ALGORITHM}
