from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import os

shayari_list = [
    "Dil ko behlaye, aankhon ko rulaye, yeh ishq nahi toh phir aur kya kahain?",
    "Tere ishq mein khud ko bhula diya, tere pyaar mein kuch khaas hai.",
    "Raat bhar teri yaadon mein khoya, dil se dil juda na ho paya.",
    "Mohabbat mein teri deewana ho gaya, tere ishq mein khud ko bhula diya.",
    "Dil se tera khayal na jaye, tere bina jeena mushkil ho jaye.",
    "Tere pyaar mein dard bhara hai, par tujhse juda ho jaana bhi impossible hai.",
    "Tere ishq mein dooba, teri yaadon mein khoya, main hoon tere bina adhoora.",
]

def sspam(update: Update, context: CallbackContext) -> None:
    random_shayari = random.choice(shayari_list)
    update.message.reply_text(random_shayari)

def main() -> None:
    updater = Updater(os.environ.get("BOT_TOKEN"))  # BOT_TOKEN is set in the Heroku Config Vars

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("sspam", sspam))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
