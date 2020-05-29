import os

from dotenv import load_dotenv

load_dotenv('.env')

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_PROXY = os.environ.get('PROXY')

