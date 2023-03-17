from create_bot import dp
from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

ChatAdminId = 1440002651
bookings = "1. Ваше имя 2. Телефон"

class list_of_bookings(StatesGroup):
    client_name = State()
    client_phone = State()

@dp.message_handler(commands=['start', 'начать'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, доброго дня!'
                         f' Продолжая регистрацию вы соглашаетесь на обработку персональных данных напишите "cогласен"')

@dp.message_handler(commands=['согласен', 'Согласен'])
async def booking_name(message: Message):
    await message.answer(text=f'Укажите имя гостя')
    # await list_of_bookings.client_name.set()
