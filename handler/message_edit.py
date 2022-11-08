from aiogram import types

async def message_delete(message: types.Message):
    try:
        await message.delete()
    except:
        pass