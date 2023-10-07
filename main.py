import discord
from discord.ext import commands
from tokenimm import *
import os, random
import requests
import string

intents = discord.Intents.default()
intents.message_content = True
dosya = tokenem()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]


@bot.command("duck")
async def duck(ctx):
    """duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır."""
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def sifre(ctx):
    all_characters = [
        string.digits,
        string.punctuation,
        string.ascii_lowercase,
        string.ascii_uppercase,
    ]
    sifre = ""
    for j in range(4):
        for i in range(2):
            sifre += all_characters[i][random.randint(0, 9)]
        sifre = list(sifre)
        random.shuffle(sifre)
        ana_sifre = ""
        ana_sifre = ana_sifre.join(sifre)
    await ctx.send(ana_sifre)


bot.run(dosya)
