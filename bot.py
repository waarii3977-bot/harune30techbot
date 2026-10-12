import os
import telebot
from google import genai

BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
ai_client = genai.Client(api_key=GEMINI_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Baga nagaan dhuftan! Ani Bot AI Gemini dha. Maal siif haa gargaaru?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Dogoggorri uumameera, deebisanii yaalaa.")

if __name__ == "__main__":
    bot.infinity_polling()
