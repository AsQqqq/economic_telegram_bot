from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard = True)\
    .add(
    KeyboardButton(
        "Высчитывать с НДФЛ"
    )
    )\
    .insert(
    KeyboardButton(
        "Высчитывать без НДФЛ"
    )
    )\
    .add(
    KeyboardButton(
        "Настройки"
    )
    )