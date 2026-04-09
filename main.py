from os import getenv
from dotenv import load_dotenv
from interactions import Client, Intents
import commands

# inits
load_dotenv()
token = getenv("bot_token")
bot = Client(intents=Intents.ALL)
commands.init(bot)

# start a bot
print("bot started!")
bot.start(token)