from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from shayari import shayari_list
import random
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Use the /sspam command to get Shayari. Type /cancel to stop receiving Shayari.")

def sspam(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please use the command in the format `/sspam <number>`.")
        return

    try:
        num_shayari = int(args[0])
    except ValueError:
        update.message.reply_text("Please enter a valid number.")
        return

    if num_shayari <= 0:
        update.message.reply_text("Please enter a positive number.")
        return

    total_shayari = len(shayari_list)
    if num_shayari >= total_shayari:
        selected_shayari = shayari_list * (num_shayari // total_shayari) + random.sample(shayari_list, num_shayari % total_shayari)
    else:
        selected_shayari = random.sample(shayari_list, num_shayari)

    for shayari in selected_shayari:
        update.message.reply_text(shayari)

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Shayari delivery canceled. Type /sspam to get more Shayari.")

def alive(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("BOT IS ALIVE AND WORKING LIKE LION 🦁. AAKHIR BETA BHI TOH XYTRA KA HU AUR AMAN KA BHAI🙂", parse_mode=ParseMode.MARKDOWN)

def main() -> None:
    updater = Updater(os.environ.get("BOT_TOKEN"))  # BOT_TOKEN is set in the Heroku Config Vars

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sspam", sspam, pass_args=True))
    dp.add_handler(CommandHandler("cancel", cancel))
    dp.add_handler(CommandHandler("alive", alive))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
