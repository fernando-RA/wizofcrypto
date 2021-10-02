# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Build Lean SaaS!'
        f'Check out the Getting Started Category for more info!'
        f'Hop in on the conversation in the Incubator Category!'
        f'Reach out in the #help channel if you need anything.'
        f'Have fun!'
    )

client.run(TOKEN)
