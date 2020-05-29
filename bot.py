import telebot
from telebot.types import Message

from models import init_db, User
from settings import BOT_TOKEN, BOT_PROXY

from telebot import apihelper

from statuses import reg_statuses

apihelper.proxy = {'https': BOT_PROXY}

bot = telebot.TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    user_id = message.chat.id
    if User.select().where(User.telegram_id == user_id).count() == 0:
        User.create(name='',
                    telegram_id=user_id,
                    reg_status=reg_statuses.get('first'))
    user = User.get(telegram_id=user_id)
    if user.reg_status == reg_statuses.get('complete'):
        bot.send_message(chat_id=user.telegram_id,
                         text=f'Привет, {user.name}!'
                              f'Вот что я умею:')
    else:
        if user.reg_status == reg_statuses.get('first'):
            bot.send_message(chat_id=user.telegram_id,
                             text=f'Привет! Я умный бот. \\nДавай знакомиться!\\n'
                                  f'Как тебя зовут?')


if __name__ == '__main__':
    init_db()
    bot.polling(none_stop=True)
