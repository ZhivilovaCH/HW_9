from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot('6020503123:AAEYLt200RgWIOTwNrCc5G_Ehw4XsaREDbA')
dp = Dispatcher(bot, storage=MemoryStorage())
