import os
import datetime

import discord
from discord.ext import commands

import dotenv
dotenv.load_dotenv()


bot = commands.Bot(command_prefix='>', description="This is a PyBot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(f"{numOne} + {numTwo} = {numOne + numTwo}")


@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server stats",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


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
