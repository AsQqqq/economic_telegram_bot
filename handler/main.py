#====import=bot====
from import_bot import admins_id, dp, bot, scheduler
#==================

#основные импорты
from aiogram import types
from datetime import timedelta, datetime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import main_menu_kb, ndfl_false_kb, ndfl_true_kb, not_keyboard, setting_inline_kb, setting_keyboard, editNdfl_keyboard
from handler.message_edit import message_delete

#процент НДФЛ 
percent_ndfl = 0.13

#===================start=======================

#стартовый хандлер, запускается с команды /start
async def start_command(message: types.Message):
    #удаление последнего сообщения пользователя
    await message.delete()
    #выводим сообщение пользователю вместе с клавиатурой
    await message.answer("Привет!", reply_markup = main_menu_kb)

#только для админа, запускается текстом test
async def test_persent(message: types.Message):
    #проверяем пишет админ или пользователь
    if admins_id == message.from_user.id:
        #если админ то удаляем его сообщение
        await message.delete()
        #делаем из числа процент
        NDFL = percent_ndfl*100
        #выводим процет НДФЛ
        msg = await message.answer(f"Процент НДФЛ: {NDFL}")

        #создаем переменную с секундами
        date_30s = datetime.now() + timedelta(seconds=30)
        #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
        scheduler.add_job(message_delete, "date", run_date=date_30s, kwargs={"message":msg})
    else:
        #если пишет пользователь то даем понять что он просто написал сообщение, проигнорив его
        pass

#хандлер для меню настроек
async def setting_bot(message: types.Message):
    #удаление сообщения пользователя
    await message.delete()
    global global_setting_menu
    #запуск инлайн клавиатуры и вывод текста
    global_setting_menu_msg = await message.answer("Выбери пункт для настройки или помощи", reply_markup=setting_keyboard)
    #таймер
    date_25s = datetime.now() + timedelta(seconds=25)
    #удаление сообщения по таймеру
    scheduler.add_job(message_delete, "date", run_date=date_25s, kwargs={"message":global_setting_menu_msg})

#вот так выглядит запуск от инлайн клавиатуры
@dp.callback_query_handler(text='persent_ndfl')
#это хандлер запускающий этот стейт
async def print_persent_ndfl(call: types.CallbackQuery):
    #удаление предыдущего сообщения
    await call.message.delete()
    #делаем из числа процент
    NDFL = percent_ndfl*100
    #выводим процет НДФЛ
    msg = await call.message.answer(f"Текущий процент НДФЛ: {NDFL}%", reply_markup=editNdfl_keyboard)
    #создаем переменную с секундами
    date_30s = datetime.now() + timedelta(seconds=30)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_30s, kwargs={"message":msg})

#вот так выглядит запуск от инлайн клавиатуры
@dp.callback_query_handler(text='help_commands')
#это хандлер запускающий этот стейт
async def help_command_inline(call: types.CallbackQuery):
    #удаление предыдущего сообщения
    await call.message.delete()
    #выводим текст
    msg = await call.message.answer("Все команды:\n/last - Последний результат!\n/connect - Связаться с разработчиком\n\nЭто меню можно вызвать командой /help!")
    #создаем переменную с секундами
    date_15s = datetime.now() + timedelta(seconds=15)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_15s, kwargs={"message":msg})

#это хандлер запускающий этот стейт
async def help_command(message: types.Message):
    #удаление предыдущего сообщения
    await message.delete()
    #выводим текст
    msg = await message.answer("Все команды:\n/last - Последний результат!\n/connect - Связаться с разработчиком\n\nЭто меню можно вызвать в меню настроек")
    #создаем переменную с секундами
    date_15s = datetime.now() + timedelta(seconds=15)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_15s, kwargs={"message":msg})

msg_text = None

#это хандлер запускающий этот стейт
async def last_command(message: types.Message):
    #удаление предыдущего сообщения
    await message.delete()
    
    if not msg_text == None:
        #выводим текст
        msg = await message.answer(f"Ваша последняя операция:\n{msg_text}")
    else:
        msg = await message.answer("Вы еще не выполняли операций")
    #создаем переменную с секундами
    date_15s = datetime.now() + timedelta(seconds=15)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_15s, kwargs={"message":msg})

#это хандлер запускающий этот стейт
async def connect_command(message: types.Message):
    #удаление предыдущего сообщения
    await message.delete()
    #выводим текст
    msg = await message.answer("Разработчик бота - https://github.com/AsQqqq")
    #создаем переменную с секундами
    date_15s = datetime.now() + timedelta(seconds=15)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_15s, kwargs={"message":msg})

#хандлер для удаления лишних сообщений
async def no_message(message:types.Message):
    #удаление сообщения
    await message.delete()
    #ввывод текста
    msg = await message.answer('Не понятное слово... введи /start или /help')
    #таймер и удаление сообщений бота
    date_10s = datetime.now() + timedelta(seconds=10)
    scheduler.add_job(message_delete, "date", run_date=date_10s, kwargs={"message": msg})

#===================setting=====================

#это создание библеотеки стейтов. Тут идет запись в оперативную память сервера
class state_setting_ndfl(StatesGroup):
    #название стейта и его модуль(... = State())
    ndfl_setting_state = State()

#вот так выглядит запуск от инлайн клавиатуры
@dp.callback_query_handler(text='edit_ndfl')
#это хандлер запускающий этот стейт
async def edit_persent_ndfl(call: types.CallbackQuery):
    #удаление предыдущего сообщения
    await call.message.delete()
    #обьявление глобальной переменной
    global msg_id_setting_bot_id
    #вывод текста с переменной и плюс клавиатура с отменением стейта
    msg_id_setting_bot = await call.message.answer('Напиши новый процент НДФЛ(к примеру 13 или 5 и тп)', reply_markup=not_keyboard)
    #из переменной вытягиваем только ее айди для будущих манипуляций
    msg_id_setting_bot_id = msg_id_setting_bot.message_id
    #запускаем стейт и ждем следующих действий в next хандлерах
    await state_setting_ndfl.ndfl_setting_state.set()

#проверка на string в int(из строки в цифру)
#так как клавиатура в 65 строке у нас инлайн, то мы тут ее ловим и добовляемся в стейт через функцию state = ..., а лямбда проверяет int или str
@dp.message_handler(lambda message: not message.text.isdigit(), state = state_setting_ndfl.ndfl_setting_state)
async def drive_exp_invalid(message: types.Message):
    #удаление последнего сообщения пользователя
    await message.delete()
    #тут мы редактируем ту глобальную переменную, точнее получаем айди и по нему редактируем сообщение прошлое. Ну и вызываем клавиатуру отмены, так как при исправлении
    #она удалиться
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_setting_bot_id, text=("Введите цифрами"), reply_markup=not_keyboard)

#конец стейта, его завершение и вывод полученных данных
async def setting_ndfl_state(message: types.Message, state: FSMContext):
    #удаление последнего сообщения пользователя
    await message.delete()
    #обьявление глобальной переменной
    global percent_ndfl
    #закрепляем в стейт результат пользователя
    async with state.proxy() as data:
        data['ndfl_setting_state'] = message.text
    #получаем данные из стейта
    data = await state.get_data()
    #полученные данные мы форматируем и выбираем что нам именно нужно
    percent_new = int(data.get("ndfl_setting_state"))
    #проводим деление на 100 для получения числа, а не процента
    percent = percent_new/100
    #изменяем переменную в самом начале кода(14 строчка)
    percent_ndfl = percent
    #редактируем сообщение и выводим ризультат
    msg = await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_setting_bot_id, text=(f'Ваш новый процент: {percent_new}%'))
    #создаем переменную с секундами
    date_20s = datetime.now() + timedelta(seconds=20)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message":msg})
    #отключаем стейт
    await state.finish()

#===================true========================

"""
    всё что было сказано выше обьясняет большую часть сделанную ниже. То что будет и вправду новое, я подпишу и разжую
"""

#было прописано выше
class deduction_from_personal_income_tax(StatesGroup):
    rate_per_hour = State()
    hours_worked = State()

#запуск стейта
async def ndfl_true_handler(message: types.Message):
    global msg_id_true_bot_id
    await message.delete()
    msg_id_true_bot = await message.answer('Ставка в час', reply_markup=not_keyboard)
    msg_id_true_bot_id = msg_id_true_bot.message_id
    await deduction_from_personal_income_tax.rate_per_hour.set()

#проверка на string в int(из строки в цифру)
@dp.message_handler(lambda message: not message.text.isdigit(), state = deduction_from_personal_income_tax.rate_per_hour)
async def drive_exp_invalid(message: types.Message):
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_true_bot_id, text=("Введите цифрами"), reply_markup=not_keyboard)

#ловим ставку
async def bet_hour(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['rate_per_hour'] = message.text
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_true_bot_id, text=('Сколько часов ты отработал?'), reply_markup=not_keyboard)
    await deduction_from_personal_income_tax.next()

#проверка на string в int(из строки в цифру)
@dp.message_handler(lambda message: not message.text.isdigit(), state = deduction_from_personal_income_tax.hours_worked)
async def drive_exp_invalid(message: types.Message):
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_true_bot_id, text=("Введите цифрами"), reply_markup=not_keyboard)

#конец стейта, его завершение и вывод полученных данных
async def hour_work(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['hours_worked'] = message.text
    data = await state.get_data()
    #получаем нужные нам данные из стейта
    rate_per_hour_per = int(data.get("rate_per_hour"))
    hours_worked_per = int(data.get("hours_worked"))
    #делаем вычесление
    #обработка вывода
    number_of_days_worked = float(hours_worked_per/24)
    variable_one = float((rate_per_hour_per*hours_worked_per)-((rate_per_hour_per*hours_worked_per)*percent_ndfl))
    if hours_worked_per > 24:
        round_works_other_days = str(round(number_of_days_worked))
        round_works = str(round_works_other_days) + " дней" + f"({str(round(hours_worked_per))} часов)"
    else:
        round_works_other_hour = str(round(hours_worked_per))
        round_works = round_works_other_hour + " часов"
    persent_ndfl_nice = percent_ndfl*100
    #выводим пользователю
    msg = await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_true_bot_id, text=(f'Ваша заработная плата за {round_works}:\n{variable_one} рублей,\nпри условии что {round(float(rate_per_hour_per))} рублей в час и коммисией {persent_ndfl_nice}%'))
    #создаем переменную с секундами
    date_20s = datetime.now() + timedelta(seconds=20)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message":msg})
    
    global msg_text
    msg_text = msg.text

    #завершение стейта
    await state.finish()

#===================false=======================

"""
    всё что было сказано выше обьясняет большую часть сделанную ниже. То что будет и вправду новое, я подпишу и разжую
"""

#было прописано выше
class deduction_from_personal_income_tax_false(StatesGroup):
    rate_per_hour = State()
    hours_worked = State()

#запуск стейта
async def ndfl_false_handler(message: types.Message):
    global msg_id_false_bot_id
    await message.delete()
    msg_id_false_bot = await message.answer('Ставка в час', reply_markup=not_keyboard)
    msg_id_false_bot_id = msg_id_false_bot.message_id
    await deduction_from_personal_income_tax_false.rate_per_hour.set()

#проверка на string в int(из строки в цифру)
@dp.message_handler(lambda message: not message.text.isdigit(), state = deduction_from_personal_income_tax_false.rate_per_hour)
async def drive_exp_invalid(message: types.Message):
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_false_bot_id, text=("Введите цифрами"), reply_markup=not_keyboard)

#ловим ставку
async def bet_hour_false(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['rate_per_hour'] = message.text
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_false_bot_id, text=('Сколько часов ты отработал?'), reply_markup=not_keyboard)
    await deduction_from_personal_income_tax_false.next()

#проверка на string в int(из строки в цифру
@dp.message_handler(lambda message: not message.text.isdigit(), state = deduction_from_personal_income_tax_false.hours_worked)
async def drive_exp_invalid(message: types.Message):
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_false_bot_id, text=("Введите цифрами"), reply_markup=not_keyboard)

#конец стейта, его завершение и вывод полученных данных
async def hour_work_false(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        data['hours_worked'] = message.text
    data = await state.get_data()


    rate_per_hour_per = int(data.get("rate_per_hour"))
    hours_worked_per = int(data.get("hours_worked"))
    variable_one = float(rate_per_hour_per*hours_worked_per)


    #await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_false_bot_id, text=(f'{variable_one}'))

    #обработка вывода
    number_of_days_worked = float(hours_worked_per/24)
    if hours_worked_per > 24:
        round_works_other_days = str(round(number_of_days_worked))
        round_works = str(round_works_other_days) + " дней" + f"({str(round(hours_worked_per))} часов)"
    else:
        round_works_other_hour = str(round(hours_worked_per))
        round_works = round_works_other_hour + " часов"
    #выводим пользователю
    msg = await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id_false_bot_id, text=(f'Ваша заработная плата за {round_works}:\n{variable_one} рублей,\nпри условии что {round(float(rate_per_hour_per))} рублей в час'))
    #создаем переменную с секундами
    date_20s = datetime.now() + timedelta(seconds=20)
    #через scheduler выполняем выше сказанные секунды и после удаляем сообщение по айди
    scheduler.add_job(message_delete, "date", run_date=date_20s, kwargs={"message":msg})

    global msg_text
    msg_text = msg.text

    await state.finish()

#===================stop=state==================

#хандлер для отмены стейтов
@dp.callback_query_handler(text='stop_state', state='*')
async def not_state(call: types.CallbackQuery, state: FSMContext):
    #удаление сообщния стейта
    await call.message.delete()
    #попадаем в выключаемый стейт
    current_state = await state.get_state()
    #если стейт равен None то возращаем
    if current_state is None:
        return
    #пишем сообщение об отмене
    msg = await call.message.answer('❌ дейстивие отменено')
    #запускаем таймер и удаляем сообщение бота
    date_15s = datetime.now() + timedelta(seconds=15)
    scheduler.add_job(message_delete, "date", run_date=date_15s, kwargs={"message":msg})
    #закрываем стейт
    await state.finish()

#====================reg=handler================

#регистратор
def reg_handler(dp):
    #Запуск команды /start
    dp.register_message_handler(start_command, commands='start')
    #Запуск команды /help
    dp.register_message_handler(help_command, commands='help')
    #Запуск команды /help
    dp.register_message_handler(last_command, commands='last')
    #Запуск команды /help
    dp.register_message_handler(connect_command, commands='connect')
    #Запуск высчитывания с ндфл
    dp.register_message_handler(ndfl_true_handler, text='Высчитывать с НДФЛ', state=None)
    #Запуск высчитывания без ндфл
    dp.register_message_handler(ndfl_false_handler, text='Высчитывать без НДФЛ', state=None)
    #тест для админа
    dp.register_message_handler(test_persent, text='test')
    #настройки бота
    dp.register_message_handler(setting_bot, text='Настройки')
    #логи для стейтов с ндфл
    dp.register_message_handler(bet_hour, state=deduction_from_personal_income_tax.rate_per_hour)
    dp.register_message_handler(hour_work, state=deduction_from_personal_income_tax.hours_worked)
    #логи для стейтов без ндфл
    dp.register_message_handler(bet_hour_false, state=deduction_from_personal_income_tax_false.rate_per_hour)
    dp.register_message_handler(hour_work_false, state=deduction_from_personal_income_tax_false.hours_worked)
    #логи для стейтов настройки
    dp.register_message_handler(setting_ndfl_state, state=state_setting_ndfl.ndfl_setting_state)
    #ловля лишних сообщений
    dp.register_message_handler(no_message)