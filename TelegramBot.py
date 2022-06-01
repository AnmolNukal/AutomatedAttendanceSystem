import os
import telebot


bot = telebot.TeleBot('5465773423:AAGWcWlf8yuyvLKd-06ayxBjryGdRLgZDII')

with open('myfile.txt') as f:
    lines = f.read()



@bot.message_handler(commands=['Report'])
def sendAttendance(message):
	bot.reply_to(message, lines)
    

bot.infinity_polling()