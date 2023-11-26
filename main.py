from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from shayari import shayari_list
from jokes import jokes_list
import random
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Use the /sspam command for Shayari and /joke command for jokes. Type /cancel to stop receiving messages.")

def sspam(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please use the command in the format `/sspam <number>`.")
        return

    try:
        num_messages = int(args[0])
    except ValueError:
        update.message.reply_text("Please enter a valid number.")
        return

    if num_messages <= 0:
        update.message.reply_text("Please enter a positive number.")
        return

    total_messages = len(shayari_list)
    if num_messages >= total_messages:
        selected_messages = shayari_list * (num_messages // total_messages) + random.sample(shayari_list, num_messages % total_messages)
    else:
        selected_messages = random.sample(shayari_list, num_messages)

    for message in selected_messages:
        update.message.reply_text(message)

def joke(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please use the command in the format `/joke`.")
        return

    num_jokes = 1
    try:
        num_jokes = int(args[0])
    except ValueError:
        update.message.reply_text("Please enter a valid number.")

    total_jokes = len(jokes_list)
    if num_jokes >= total_jokes:
        selected_jokes = jokes_list * (num_jokes // total_jokes) + random.sample(jokes_list, num_jokes % total_jokes)
    else:
        selected_jokes = random.sample(jokes_list, num_jokes)

    for joke in selected_jokes:
        update.message.reply_text(joke)

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Message delivery canceled. Type /sspam for Shayari and /joke for jokes.")

def alive(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("BOT IS ALIVE AND WORKING LIKE LION 🦁. AAKHIR BETA BHI TOH XYTRA KA HU AUR AMAN KA BHAI🙂", parse_mode=ParseMode.MARKDOWN)

def main() -> None:
    updater = Updater(os.environ.get("BOT_TOKEN"))  # BOT_TOKEN is set in the Heroku Config Vars

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sspam", sspam, pass_args=True))
    dp.add_handler(CommandHandler("joke", joke, pass_args=True))
    dp.add_handler(CommandHandler("jokes", joke, pass_args=True))  # Alias for /joke
    dp.add_handler(CommandHandler("cancel", cancel))
    dp.add_handler(CommandHandler("alive", alive))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
