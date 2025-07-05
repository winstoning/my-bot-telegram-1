import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import random

bot = telebot.TeleBot("Token bot")


soal = [
'بهترین زبان برنامه نویسی چیست؟',
'نظر شما در باره این ربات چیست؟',
'آیا ابوالفضل خر است / با بله جواب دهید'
]


@bot.message_handler(commands=['start'])
def start(message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	button = KeyboardButton('نظر سنجی')
	markup.add(button)
	bot.reply_to(message, 'لطفا داخل نظر سنجی شرکت کنید با دکمه زیر✓✓✓', reply_markup=markup)
	
@bot.message_handler(func=lambda message: message.text == "نظر سنجی")
def nazar(message):
	random_soal = random.choice(soal)
	bot.reply_to(message, random_soal)
	bot.register_next_step_handler(message, save_answer)
def save_answer(message):
	answer = message.text
	bot.reply_to(message, f"جواب شما :  {message.text} ")
	
	#ذخیره جواب کاربر در فایل txt
	with open('bot.txt', 'a' , encoding='utf-8') as file:
		file.write(f"کاربر :  {message.from_user.id}: {answer}\n ")

bot.polling()