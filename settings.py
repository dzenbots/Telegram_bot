import os

from dotenv import load_dotenv

load_dotenv('.env')

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_PROXY = os.environ.get('PROXY')
DB_FILE_PATH = os.environ.get('DB_FILE_PATH')
#
# PROXY_USER = '190737618'
#
# PROXY_PASSWORD = 'TsT9nZls'
#
# PROXY_IP = 'orbtl.s5.opennetwork.cc'

# PROXY_USER = '190737618'
#
# PROXY_PASSWORD = 'TsT9nZls'
#
# PROXY_IP = 'grsst.s5.opennetwork.cc'


# PROXY_PORT = '999'
#
# HTTPS_PROTOCOL = 'https'
#
# BOT_PROXY = 'socks5://{}:{}@{}:{}'.format(PROXY_USER, PROXY_PASSWORD, PROXY_IP, PROXY_PORT)
