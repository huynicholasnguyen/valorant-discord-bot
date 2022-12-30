import os
import discord
from dotenv import load_dotenv

load_dotenv()

d_token = os.getenv('discord_token')
client = discord.Client()



