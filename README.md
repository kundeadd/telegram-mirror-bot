# telegram-mirror-bot

Monitors crypto Telegram channels and copies messages to your own channel.

## What it does

Connects as a Telegram user, listens to messages from selected public channels, and forwards them to a target channel. Supports text and media messages.

## Monitored channels

- CoinDesk, Cointelegraph, Whale Alert
- Lookonchain, Glassnode, CryptoQuant
- Messari, The Block Research, CoinMarketCap
- CoinGecko, DeFi Pulse, and more

## Stack

- Python
- Telethon (Telegram user client)

## Setup

```bash
pip install telethon
python mirror.py
```

First run will ask for phone number and Telegram code.

## Config

Edit `mirror.py`:

```python
SOURCE_CHANNELS = ["@coindesk", "@whale_alert", ...]  # channels to monitor
TARGET_CHANNEL = -1001234567890  # your channel ID
```
