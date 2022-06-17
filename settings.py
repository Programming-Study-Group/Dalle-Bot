# token (stored in .env file)

from dotenv import load_dotenv
from os import getenv

class Settings:
    load_dotenv()
    TOKEN = getenv('TOKEN')

settings = Settings()