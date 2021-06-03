import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.default())
token = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print("Online")
    await bot.change_presence(activity = discord.Streaming(name = "Lofi", url = "https://www.youtube.com/watch?v=5qap5aO4i9A")) #status = discord.Status.(dnd)(online)(idle)etc...


@bot.command()
async def ping(ctx):
    await ctx.send(f"**Latency:** {round(bot.latency*1000)}ms")





bot.run(token)


