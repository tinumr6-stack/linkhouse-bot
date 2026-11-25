print("Hello, Bot Started!")
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎬 *Link House Movies* ലേക്ക് സ്വാഗതം!\n\nസിനിമകളുടെ വിവരങ്ങൾ, ട്രെയിലർ, റേറ്റിംഗ്, എവിടെ കാണാം എന്നൊക്കെ ഇവിടെ കിട്ടും.\n\n/movie എന്ന് ടൈപ്പ് ചെയ്യൂ.", parse_mode="Markdown")

@bot.message_handler(commands=['movie'])
def movie(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🎬 Lokah - Trailer", url="https://www.youtube.com/results?search_query=Lokah+Chapter+1+Chandra+Trailer"),
        InlineKeyboardButton("🎟️ Lokah - Hotstar", url="https://www.hotstar.com/in")
    )
    markup.add(
        InlineKeyboardButton("🎬 Premalu - Trailer", url="https://www.youtube.com/results?search_query=Premalu+Trailer"),
        InlineKeyboardButton("🎟️ Premalu - Hotstar", url="https://www.hotstar.com/in")
    )
    markup.add(
        InlineKeyboardButton("🎬 Manjummel Boys - Trailer", url="https://www.youtube.com/results?search_query=Manjummel+Boys+Trailer"),
        InlineKeyboardButton("🎟️ Manjummel Boys - Hotstar", url="https://www.hotstar.com/in")
    )
    bot.reply_to(message, "🎬 *Latest Movies*\n\n1.
