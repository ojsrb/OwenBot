import os
import random
import discord
from discord import Intents
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

currentVersion = "1.0.2"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()

client = commands.Bot(command_prefix='/', intents=intents)

whitelist = [1131962772587020298, 800898653820551168]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name='ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}")
    ephemeral = True

@client.tree.command(name='insult')
async def insult(interaction: discord.Interaction, user: discord.User):
    insults = [" is a big meanie!",
               " is terrible",
               " is not cool",
               " is very bad",
               " is stupid",
               " is not funny",
               " is smelly"
               ]
    if user.id == 800898653820551168:
        await interaction.response.send_message("You cannot insult my papa!", ephemeral=True)
    else:
        await interaction.response.send_message("Sending insults...", ephemeral=True)
        await interaction.channel.send(f"{user.name}{random.choice(insults)}")

@client.tree.command(name='praise')
async def insult(interaction: discord.Interaction, user: discord.User):
    praises = [" is very kind!",
               " is awesome!",
               " is my favorite member.",
               " is mega cool :)",
               " should be president.",
               " is the GOAT",
               " is the most amazing person in the world",
               " is very cool",
               " is utterly amazing"
               ]

    await interaction.response.send_message(f"{user}{random.choice(praises)}")

@client.tree.command(name='papa')
async def papa(interaction: discord.Interaction):
    if interaction.user.id in whitelist:
        await interaction.response.send_message("You are my papa!")
    else:
        await interaction.response.send_message("You are not my papa! o.n. is my papa!")

@client.tree.command(name='say')
async def say(interaction: discord.Interaction, message: str):
    if interaction.user.id in whitelist:
        await interaction.response.send_message("sending message...", ephemeral=True)
        await interaction.channel.send(message)

    else:
        await interaction.response.send_message("You cant do that!", ephemeral=True)

@client.tree.command(name='dice')
async def dice(interaction: discord.Interaction, sides: int):
    await interaction.response.send_message(f"{random.randint(1, sides)}")

@client.tree.command(name='family')
async def family(interaction: discord.Interaction):
    await interaction.response.send_message("My papa is o.n., my big bro is Goober")

@client.tree.command(name='id')
async def id(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"{user.name}:{user.id}")

@client.tree.command(name='version')
async def version(interaction: discord.Interaction):
    global currentVersion
    await interaction.response.send_message(f"My version is currently: {currentVersion}")
client.run(TOKEN)
