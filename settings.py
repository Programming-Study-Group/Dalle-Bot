# token (stored in .env file)
from dotenv import load_dotenv
from os import getenv

class Settings:
    load_dotenv()
    TOKEN = getenv('TOKEN')
    URL = "https://bf.dallemini.ai/generate"

settings = Settings()