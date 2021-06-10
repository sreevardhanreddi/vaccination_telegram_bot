# Telegram bot to notify vaccination slots

---

## Run 

```
# add your .env variables, refer environment variables section
docker-compose up -d

```

---

## Environment variables

```
PINCODES of the area you want to get notified about, which are semi-colon separated
TELEGRAM_TOKEN token of the bot you can get this by requesting @BotFather
CHANNEL_ID Channel Id is to which the bot should broadcast the messages to (the bot needs to have admin access to the channel)

```