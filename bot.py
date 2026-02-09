import os
import discord
from discord.ext import commands, tasks
from datetime import time
import pytz

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1434557633725202533

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    good_morning.start()
    hydrate.start()

# 🌟 11:11 AM – Good morning stars
@tasks.loop(time=time(hour=11, minute=11, tzinfo=pytz.timezone("Asia/Kolkata")))
async def good_morning():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone ✨⭐ Good morning stars ⭐✨")

# 💧 3:33 PM – Hydration reminder
@tasks.loop(time=time(hour=15, minute=33, tzinfo=pytz.timezone("Asia/Kolkata")))
async def hydrate():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone 💧✨ Stay hydrated guys ✨💧")

bot.run(TOKEN)
