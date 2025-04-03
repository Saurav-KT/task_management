import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
TOKEN_EXPIRATION_TIME_MINUTES=int(os.getenv("TOKEN_EXPIRATION_TIME_MINUTES"))
# Read DEBUG from environment variables
DEBUG = os.getenv("DEBUG", "False").lower() == "true"