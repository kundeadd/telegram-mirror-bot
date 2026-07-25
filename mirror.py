from telethon import TelegramClient, events

API_ID = 36496932
API_HASH = "b5d2223b4c8863ff6e21b12751be974d"

SOURCE_CHANNELS = [
    "@coindesk",
    "@cointelegraph",
    "@whale_alert",
    "@lookonchain",
    "@wu_blockchain",
    "@coingecko",
    "@glassnode",
    "@CryptoQuant_Alert",
    "@santimentfeed",
    "@defipulse",
    "@messari",
    "@TheBlockResearch",
    "@CoinMarketCap",
]

TARGET_CHANNEL = -1003994165115

client = TelegramClient("session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        source = await event.get_chat()
        source_name = getattr(source, "title", "Unknown")
        msg = event.message
        prefix = f"[{source_name}]\n\n"
        if msg.media:
            await client.send_message(
                TARGET_CHANNEL,
                message=prefix + (msg.text or ""),
                file=msg.media,
                parse_mode="html"
            )
        else:
            if msg.text:
                await client.send_message(
                    TARGET_CHANNEL,
                    prefix + msg.text,
                    parse_mode="html"
                )
        print(f"Mirrored from {source_name}: {(msg.text or '')[:50]}")
    except Exception as e:
        print(f"Error: {e}")

print("Mirror started. Monitoring 13 channels...")
with client:
    client.run_until_disconnected()
