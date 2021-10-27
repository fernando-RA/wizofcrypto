import os


from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

from src.telegram.bot import send_random_message
from src.discord.bot import client

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# TABLE OF CONTENTS
# - CRON JOBS
# - DISCORD BOT LISTENERS
# - TELERGAM BOT LISTENERS
# - TWITTER BOT LISTENERS

# CRON JOBS
sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=7, minute=30)
def scheduled_job():
    send_random_message()


sched.start()


# DISCORD BOT LISTENERS

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

# TELEGRAM BOT LISTENERS

# TWITTER BOT LISTENERS
