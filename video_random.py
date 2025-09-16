import telebot
import requests

bot = telebot.TeleBot('8229306265:AAH7vsRJNk0CANX9kjaIFob7nhQs2LAJM5c')

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = telebot.types.KeyboardButton("ویدیو🎥")

markup.add(btn1)

@bot.message_handler(commands=['start'])
def s_start(message):
		bot.send_message(message.chat.id, "به ربات ویدیو رندوم خوش آمدید🎉✨", reply_markup=markup)
		
@bot.message_handler(func=lambda message:True)
def video(message):
		user_text = message.text
		if user_text == "ویدیو🎥":
			response = requests.get("https://api-free.ir/api/video/")
			data = response.json()
			cap = data['result']['caption']
			res = data['result']['url']
			bot.send_video(message.chat.id, res, caption=cap)
		else:
			pass
		
print("Bot is running...")

bot.infinity_polling()