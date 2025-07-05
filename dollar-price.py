import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests

bot = telebot.TeleBot("Token bot")

@bot.message_handler(commands=['start'])
def start(message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	button = KeyboardButton("قیمت دلار")
	markup.add(button)
	bot.reply_to(message, "قیمت ارز های دیجیتالی", reply_markup=markup)
	
@bot.message_handler(func=lambda message: message.text == "قیمت دلار")
def get_dollar_price(message):
	try:
		respnse = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
		data = respnse.json()
		usd_irr = data['usd']['irr']
		bot.reply_to(message, f"قیمت دلار {usd_irr:.2f} تومان")
	except:
		bot.reply_to(message, "خطایی پیش آمد لطفا بعدا امتهان کنید")


print('بات فعال شد')
bot.polling()