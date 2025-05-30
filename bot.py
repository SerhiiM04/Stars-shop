from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7290872299:AAGB0H0QROUqpfL9taDJ1OWW21yX5o-9B-g"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Відкрити магазин", web_app=WebAppInfo(url="https://store-mini-app.vercel.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = "Привіт! Це наш Telegram магазин.\nНатисніть кнопку нижче, щоб почати покупки."
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    print("Бот запущений...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()


---

requirements.txt

python-telegram-bot==13.15


---

Procfile

worker: python bot.py


---
