import os
import telebot

# Get bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Taskcash! 🎉\n\n💰 Earn ₹2 per ad, ₹50 per task, ₹15 per referral.\nStart by completing your first task!")

bot.infinity_polling()
