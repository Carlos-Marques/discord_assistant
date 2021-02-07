import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='elegiggle ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="Name?", help="Tells you your name")
async def your_name(ctx):
    response = "YEFF!"
    await ctx.send(response)

bot.run(TOKEN)
