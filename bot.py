from settings import BOT_TOKEN, BOT_PROXY
from telebot import TeleBot, apihelper

apihelper.proxy = {'https': BOT_PROXY}

bot = TeleBot(token=BOT_TOKEN)


if __name__ == '__main__':
    bot.polling(none_stop=True)