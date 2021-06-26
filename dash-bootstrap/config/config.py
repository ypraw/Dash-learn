# config.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = os.getenv("ENVIRONMENT_FILE")
load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST = os.environ.get("HOST")
APP_PORT = os.environ.get("PORT")
APP_DEBUG = os.environ.get("DEBUG")
DEV_TOOLS_PROPS_CHECK = os.environ.get('DEV_TOOLS_PROPS_CHECK')
APP_THREADED = os.environ.get("THREADED")

# DB_HOST = os.environ.get("DB_HOST")
# DB_DATABASE = os.environ.get("DB_DATABASE")
# DB_USER = os.environ.get("DB_USER")
# DB_PASSWORD = os.environ.get("DB_PASSWORD")
