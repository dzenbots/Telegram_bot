import telebot
from telebot.types import Message

from keyboards import register_keyboards, register_callbacks
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
                         text=f'Привет, {user.name}!')
        bot.send_message(chat_id=user.telegram_id,
                         text='Вот что я умею:')
    else:
        if user.reg_status == reg_statuses.get('first'):
            bot.send_message(chat_id=user.telegram_id,
                             text=f'Привет! Я умный бот')
            bot.send_message(chat_id=user.telegram_id,
                             text='Давай знакомиться!')
            bot.send_message(chat_id=user.telegram_id,
                             text='Как тебя зовут?')


@bot.message_handler(content_types=['text'])
def get_text_message(message: Message):
    user_id = message.chat.id
    user = User.get(telegram_id=user_id)
    if user.reg_status == reg_statuses.get('complete'):
        pass
    if user.reg_status == reg_statuses.get('first'):
        bot.send_message(chat_id=user.telegram_id,
                         text='Давай проверим:')
        bot.send_message(chat_id=user.telegram_id,
                         text=f'Твой никнейм в телеграме: {message.from_user.username}')
        bot.send_message(chat_id=user.telegram_id,
                         text=f'И ты утверждаешь, что тебя зовут {message.text}')
        bot.send_message(chat_id=user.telegram_id,
                         text='Все верно?', reply_markup=register_keyboards)
        User.update(name=message.text).where(User.telegram_id == user_id).execute()


@bot.callback_query_handler(func=lambda call: call.data == register_callbacks.get('OK'))
def complete_register(call):
    user_id = call.message.chat.id
    user = User.get(telegram_id=user_id)
    user.update(reg_status=reg_statuses.get('complete')).execute()
    bot.send_message(chat_id=user.telegram_id,
                     text='Вот и познакомились. Смотри что я умею!')


@bot.callback_query_handler(func=lambda call: call.data == register_callbacks.get('NO'))
def restart_register(call):
    user_id = call.message.chat.id
    user = User.get(telegram_id=user_id)
    user.update(name='')
    bot.send_message(chat_id=user.telegram_id,
                     text='Как тебя зовут?')


if __name__ == '__main__':
    init_db()
    bot.polling(none_stop=True)
