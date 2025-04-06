import discord
from discord.ext import commands
from collections import defaultdict
import asyncio
import datetime
intents = discord.Intents.default()
intents.message_content = True  
intents.guilds = True
intents.webhooks = True
bot = commands.Bot(command_prefix="!", intents=intents)
webhook_ping_count = defaultdict(list)
@bot.event
async def on_message(message):
    if message.webhook_id and ("@everyone" in message.content or "@here" in message.content):
        now = datetime.datetime.utcnow()
        webhook_id = message.webhook_id
        webhook_ping_count[webhook_id] = [
            t for t in webhook_ping_count[webhook_id] if (now - t).total_seconds() < 600
        ]
        webhook_ping_count[webhook_id].append(now)

        if len(webhook_ping_count[webhook_id]) >= 3: 
            try:
                webhooks = await message.channel.webhooks()
                for webhook in webhooks:
                    if webhook.id == webhook_id:
                        await webhook.delete()
                        print(f"Deleted webhook {webhook.name} ({webhook.id}) for spam pings.")
                        await message.channel.send(f"Webhook was deleted for spam pings")
                        break
            except Exception as e:
                print(f"Error deleting webhook: {e}")
    await bot.process_commands(message)
bot.run("bot_token")
