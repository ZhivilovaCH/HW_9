from handlers import dp
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

ChatAdminId = 1440002651
bookings = "1. Ваше имя 2. Телефон"

class list_of_bookings(StatesGroup):
    client_name = State()
    client_phone = State()

async def start_bot(_):
    print('Бот запущен')


if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)


# from telegram import Bot
# from telegram import Update
# from telegram.ext import Updater
# from telegram.ext import CallbackContext
# from telegram.ext import MessageHandler
# from telegram.ext import CommandHandler
# from telegram.ext import ConversationHandler
# from telegram.ext import Filters
#
# def main():
#     updater = Updater(
#         token=6225291688:'6225291688:AAG25OFtKjRgtNczHqPHmq5Dy1-CHkpkLmQ'),
#         use_context = True,
#     )