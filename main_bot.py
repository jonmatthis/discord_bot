# main_bot.py
import os

import discord
from dotenv import load_dotenv

from custom_client import CustomClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = CustomClient()
client.run(TOKEN)
