import os

from dotenv import load_dotenv
load_dotenv('server.env')
### CONFIG FOR API SETTING ###

SERVER_SCHEME=os.getenv('SERVER_SCHEME')
SERVER_HOST=os.getenv('SERVER_HOST')
SERVER_PORT=os.getenv('SERVER_PORT')

###############################