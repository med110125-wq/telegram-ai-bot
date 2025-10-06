import telebot
import requests
from googletrans import Translator

BOT_TOKEN = "8370835011:AAGuVCtF2U6F6is6MBJGnKL9G7RzvrXg5u0"

bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()

def get_ai_response(message):
    try:
        url = "https://api.monkedev.com/fun/chat"
        params = {"msg": message, "uid": "user1"}
        response = requests.get(url, params=params)
        data = response.json()
        return data["response"]
    except:
        return "حصل خطأ بسيط، جرب تاني 🙏"

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text
    detected = translator.detect(text).lang
    ai_reply = get_ai_response(text)

    if detected == "ar":
        translated_reply = translator.translate(ai_reply, dest="ar").text
    else:
        translated_reply = ai_reply

    bot.reply_to(message, translated_reply)

print("🤖 البوت شغال دلوقتي...")
bot.infinity_polling()
