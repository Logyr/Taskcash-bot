import telebot

# 🔐 YOUR REAL BOT TOKEN (only use directly like this for testing!)
BOT_TOKEN = '7765274319:AAGczfO2u2Fo9l5OybygxZ75o5GOazhoAO8'

# Create bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Taskcash! 🎉\n\n💰 Earn ₹2 per ad, ₹50 per task, ₹15 per referral.\nStart by completing your first task!")

# Keep bot running
bot.infinity_polling()
