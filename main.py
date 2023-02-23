import discord
import os
#from dotenv import load_dotenv
# load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_messsage(message):
    if message.author == client.user:
        return

    if message.content.startswith('$a'):
        await message.channel.send('HELLO PEEPS!')
# client.run(ODMyODM5ODE3NzU4NTA3MDY5.YHpohQ.Fw2gZeYF4PkR_a9tAwtfyfMsTUA)
client.run(os.environ['.env'])
