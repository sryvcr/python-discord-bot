import os
import re
import datetime
import requests
from urllib import parse, request

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
    embed.add_field(name="Server ID:", value=f"{ctx.guild.id}")
    embed.add_field(name="Server owner:", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region:", value=f"{ctx.guild.region}")
    embed.add_field(name="Server created at:", value=f"{ctx.guild.created_at}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search: str):
    """
        this function does a search in youtube and return to discord the first 10 result
    """
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen(
        f'http://www.youtube.com/results?{query_string}')
    search_results = re.findall(
        r'/watch\?v=(.{11})', html_content.read().decode())
    for i in range(10):
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[i])


@bot.command()
async def pokedex(ctx, *, search_by: str or int):
    """
        this function return to discord a pokedex result
    """
    pokemon_res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{search_by}').json()
    pokemon_species_res = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{search_by}').json()
    abilities = list(map(lambda x: x['ability']['name'], pokemon_res['abilities']))
    description = pokemon_species_res['flavor_text_entries'][0]['flavor_text']
    types = list(map(lambda x: x['type']['name'], pokemon_res['types']))
    stats = list(map(lambda x: x['stat']['name'] + ": " + str(x['base_stat']), pokemon_res['stats']))
    embed = discord.Embed(title=f"Pokedex", description="Pokemon info", color=discord.Color.dark_green())
    embed.add_field(name="Pokedex ID:", value=f"{pokemon_res['id']}")
    embed.add_field(name="Name:", value=f"{pokemon_res['name']}")
    embed.add_field(name="Types:", value=f"{', '.join(types)}")
    embed.add_field(name="Description:", value=f"{description}")
    embed.add_field(name="Abilities:", value=f"{', '.join(abilities)}")
    embed.add_field(name="Stats:", value=f"{', '.join(stats)}")
    embed.add_field(name="Color:", value=f"{pokemon_species_res['color']['name']}")
    embed.add_field(name="Height:", value=f"{pokemon_res['height']}")
    embed.add_field(name="Weight:", value=f"{pokemon_res['weight']}")
    embed.add_field(name="Base experience:", value=f"{pokemon_res['base_experience']}")
    embed.add_field(name="Capture rate:", value=f"{pokemon_species_res['capture_rate']}")
    embed.add_field(name="Habitat:", value=f"{'undefined' if pokemon_species_res['habitat'] == None else pokemon_species_res['habitat']['name']}")
    embed.set_thumbnail(url=f"{pokemon_res['sprites']['front_default']}")
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
