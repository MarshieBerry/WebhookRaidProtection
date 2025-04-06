# Discord Webhook Spam Detection Bot

This is a Discord bot that detects webhook spam in channels, specifically looking for @everyone and @here pings. If a webhook sends multiple spammy pings in a short period (2-3 times in under 10 minutes), the bot will delete the webhook.

## Features

- Detects webhook messages containing @everyone or @here pings.
- Tracks each webhook's ping activity within a 10-minute window (adjustable).
- Deletes the webhook after detecting 2-3 spam pings in less than 10 minutes.
- Sends a message to the channel where the webhook was deleted, indicating the webhook was deleted for spam.

## Requirements

- Python 3.8+
- Discord.py library
- A Discord bot token
