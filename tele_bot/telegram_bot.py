import os

from telegram import Bot, ForceReply, Update, ParseMode, message
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)
from .message_utils import _format_message

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
# retreive the channel_id by adding the bot to channel
# and calling get_updates method on the bot object

bot = Bot(token=TOKEN)


def send_message(message_dict):
    formatted_message = _format_message(message=message_dict)
    bot.send_message(CHANNEL_ID, text=formatted_message, parse_mode=ParseMode.HTML)


# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     update.message.reply_text(
#         "hello, here is your metadata {}".format(update.to_json())
#     )


# updater = Updater(TOKEN)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # on different commands - answer in Telegram
# dispatcher.add_handler(CommandHandler("start", start))
# # Start the Bot
# updater.start_polling()

# # Run the bot until you press Ctrl-C or the process receives SIGINT,
# # SIGTERM or SIGABRT. This should be used most of the time, since
# # start_polling() is non-blocking and will stop the bot gracefully.
# updater.idle()
