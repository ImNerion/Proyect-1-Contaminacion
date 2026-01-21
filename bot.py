import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

datos_contaminacion = [
    "Una botella de plástico puede tardar más de 400 años en degradarse.",
    "Cada año llegan al océano más de 8 millones de toneladas de plástico.",
    "El aire contaminado causa millones de muertes prematuras al año.",
    "Solo el 9% del plástico producido en el mundo se recicla.",
    "Una pila común puede contaminar hasta 600.000 litros de agua.",
    "El transporte es una de las principales fuentes de contaminación del aire."
]

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def comandos(ctx):
    await ctx.send('!principal_info, !hello, !info_rapida, !howhelp')

@bot.command()
async def hello(ctx):
    with open('Proyects Lesson 2/images/botimage.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Hola, soy un bot {bot.user}! Estoy para ayudarte con uno de los problemas mas importantes en la tierra actualmente, La contaminacion. Si quieres mas informacion, utiliza el comando "!comandos"' )

@bot.command()
async def principal_info(ctx):
    await ctx.send('La contaminación es el impacto de sustancias químicas (ya sean solidas, liquidas o gaseosas) o de formas de energía (como la radiacion, el calor, la luz o el sonido) que alteran el estado de la naturaleza o impactan en la salud humana con graves consecuencias a medio y largo plazo. Si quieres mas informacion, utiliza el comando "!comandos"')

@bot.command()
async def howhelp(ctx):
    await ctx.send('Para ayudar a reducir la contaminación en 2026, puedes adoptar acciones clave centradas en la sostenibilidad y el consumo responsable, Tales como Reducir y Reutilizar Separación en Origen, Compostaje, ETC. Si quieres mas informacion, utiliza el comando "!comandos"')

@bot.command()
async def info_rapida(ctx):
    dato = random.choice(datos_contaminacion)
    await ctx.send(f"Dato ambiental: {dato}")

bot.run('')