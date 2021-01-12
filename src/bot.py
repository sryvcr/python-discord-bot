import os

import discord
from discord.ext import commands

import dotenv
dotenv.load_dotenv()


bot = commands.Bot(command_prefix='>', description="This is a PyBot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# Events
@bot.event
async def on_ready():
    print('PyBot is ready')


@bot.listen()
async def on_message(message: str):
    if message.content.startswith(">"):
        print(f"message content: {message.content}")

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_APP_SECRET_CLIENT"))
