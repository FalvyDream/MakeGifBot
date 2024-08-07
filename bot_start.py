import asyncio
from aiogram import Bot, Dispatcher
import logging

from handlers import router
from config_reader import config

# Создание бота и диспатчера
bot = Bot(config.token.get_secret_value())
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())