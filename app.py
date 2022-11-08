from aiogram.utils import executor
from import_bot import dp
import logging
from handler import main


logging.basicConfig(level=logging.INFO)


main.reg_handler(dp)

async def on_startup(_):
    pass

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)