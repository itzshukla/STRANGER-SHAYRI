from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from shayari import shayari_list
from jokes import jokes_list
from songs import songs_lyrics
from love import love_shayari
from dialogues import dialogue_list
import random
import os

def format_message(content: str, category: str) -> str:
    return f"🌟 *{category}*: {content} 🌟"

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

    formatted_messages = [format_message(message, "Shayari") for message in selected_messages]
    for formatted_message in formatted_messages:
        update.message.reply_text(formatted_message, parse_mode=ParseMode.MARKDOWN)

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

    formatted_jokes = [format_message(joke, "Joke") for joke in selected_jokes]
    for formatted_joke in formatted_jokes:
        update.message.reply_text(formatted_joke, parse_mode=ParseMode.MARKDOWN)

def gana(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please provide a song name with the command. For example, `/gana song1`.")
        return

    song_name = args[0].lower()
    song_lyrics = songs_lyrics.get(song_name, "Lyrics not available for this song.")
    formatted_song = format_message(song_lyrics, "Song")
    update.message.reply_text(formatted_song, parse_mode=ParseMode.MARKDOWN)

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

    formatted_love_shayari = [format_message(message, "Love Shayari") for message in selected_messages]
    for formatted_message in formatted_love_shayari:
        update.message.reply_text(formatted_message, parse_mode=ParseMode.MARKDOWN)

def dialogue(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text("Please use the command in the format `/dialogue` or `/dialogues`.")
        return

    num_dialogues = 1
    try:
        num_dialogues = int(args[0])
    except ValueError:
        update.message.reply_text("Please enter a valid number.")

    total_dialogues = len(dialogue_list)
    if num_dialogues >= total_dialogues:
        selected_dialogues = dialogue_list * (num_dialogues // total_dialogues) + random.sample(dialogue_list, num_dialogues % total_dialogues)
    else:
        selected_dialogues = random.sample(dialogue_list, num_dialogues)

    formatted_dialogues = [format_message(dialogue, "Dialogue") for dialogue in selected_dialogues]
    for formatted_dialogue in formatted_dialogues:
        update.message.reply_text(formatted_dialogue, parse_mode=ParseMode.MARKDOWN)

def sstop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🛑 Spamming process stopped. Type /sspam for Shayari, /joke for jokes, /gana for song lyrics, /mspam for love Shayari, /dialogue for dialogues. 🛑", parse_mode=ParseMode.MARKDOWN)

def main() -> None:
    updater = Updater(os.environ.get("BOT_TOKEN"))  # BOT_TOKEN is set in the Heroku Config Vars

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("sspam", sspam, pass_args=True))
    dp.add_handler(CommandHandler("joke", joke, pass_args=True))
    dp.add_handler(CommandHandler("gana", gana, pass_args=True))
    dp.add_handler(CommandHandler("mspam", mspam, pass_args=True))
    dp.add_handler(CommandHandler("dialogue", dialogue, pass_args=True))
    dp.add_handler(CommandHandler("dialogues", dialogue, pass_args=True))
    dp.add_handler(CommandHandler("sstop", sstop))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
