from aiogram import types

async def message_delete(message: types.Message):
    try:
        await message.delete()
    except:
        print("Error delete message")