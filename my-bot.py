import telebot

bot = telebot.TeleBot("tokan bot")

@bot.message_handler(commands=['start'])
def send_welcom(message):
	bot.reply_to(message, "سلام استارت")

@bot.message_handler(func=lambda message: message.text == "سلام"  or message.text == "hello")
def reply_hello(message):
	bot.reply_to(message, "سلام مهدی")
	
@bot.message_handler(func=lambda message: message.text == "خوبی")
def hello(message):
	bot.reply_to(message, "اره گوگولی مگولی تو چطوری")
	
print("در حال اجرا ...")
bot.polling()