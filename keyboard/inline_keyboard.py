from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ndfl_true_kb = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Ввести значения', callback_data='ndfl_true'))

ndfl_false_kb = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Ввести значения', callback_data='ndfl_false'))

setting_inline_kb = InlineKeyboardMarkup()\
    .add(InlineKeyboardButton('Настройки НДФЛ', callback_data='ndfl_setting'))

not_keyboard = InlineKeyboardMarkup(resize_keyboard = True)\
    .add(
    InlineKeyboardButton(
        "Отменить", callback_data='stop_state'
    )
    ) 