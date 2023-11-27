from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from shayari import shayari_list
from jokes import jokes_list
from songs import songs_lyrics
from love import love_shayari
import random
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
   
        "\nUse /help to see all available commands."
    )

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available commands:\n"
        "/sspam <number> - Get random Shayari.\n"
        "/joke <number> - Get random jokes.\n"
        "/songs <song_name> - Get lyrics for a specific song.\n"
        "/mspam <number> - Spam love Shayari or proposal type Shayari.\n"
        "/alive - Check if the bot is alive and working.\n"
        "/help - Display this help message."
    )
    update.message.reply_text(help_text)

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
        update.message.reply_text("Please use the command in the format `/joke <number>`.")
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

def songs(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please provide a song name with the command. For example, `/songs song1`.")
        return

    song_name = args[0].lower()
    song_lyrics = songs_lyrics.get(song_name, "Lyrics not available for this song.")
    update.message.reply_text(song_lyrics)

def mspam(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please use the command in the format `/mspam <number>`.")
        return

    try:
        num_messages = int(args[0])
    except ValueError:
        update.message.reply_text("Please enter a valid number.")
        return

    if num_messages <= 0:
        update.message.reply_text("Please enter a positive number.")
        return

    total_messages = len(love_shayari)
    if num_messages >= total_messages:
        selected_messages = love_shayari * (num_messages // total_messages) + random.sample(love_shayari, num_messages % total_messages)
    else:
        selected_messages = random.sample(love_shayari, num_messages)

    for message in selected_messages:
        update.message.reply_text(message)

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Message delivery canceled. Type /sspam for Shayari, /joke for jokes, /songs for song lyrics, /mspam for love Shayari.")

def alive(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("BOT IS ALIVE AND WORKING LIKE LION 🦁. AAKHIR BETA BHI TOH SHIVANSH KA HU AUR STRANGER KA BHAI🙂", parse_mode=ParseMode.MARKDOWN)

def main() -> None:
    updater = Updater(os.environ.get("BOT_TOKEN"))  # BOT_TOKEN is set in the Heroku Config Vars

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("sspam", sspam, pass_args=True))
    dp.add_handler(CommandHandler("joke", joke, pass_args=True))
    dp.add_handler(CommandHandler("songs", songs, pass_args=True))
    dp.add_handler(CommandHandler("mspam", mspam, pass_args=True))
    dp.add_handler(CommandHandler("cancel", cancel))
    dp.add_handler(CommandHandler("alive", alive))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
