from telebot import types

register_callbacks = {
    'OK': 'REGISTER_ACCEPTED',
    'NO': 'REGISTER_DENY'
}

register_keyboards = types.InlineKeyboardMarkup()
register_keyboards.row(types.InlineKeyboardButton(text='Все верно',
                                                  callback_data=register_callbacks.get('OK')))
register_keyboards.row(types.InlineKeyboardButton(text='Нет. Есть ошибка...',
                                                  callback_data=register_callbacks.get('NO')))
