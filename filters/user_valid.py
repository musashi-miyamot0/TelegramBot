'''Aiogram.filters importet class Filter'''
import os

from aiogram import types
from aiogram.filters import Filter
from dotenv import load_dotenv


class ValidationUser(Filter):
    '''Class ValidationUser check in id in env file with id user telegram'''
    async def __call__(self, message: types.Message):
        try:
            load_dotenv()
        except Exception as error:
            print(f'Что то пошло не так при загрузке переменных окружения: {str(error)}')
        id_inp = message.from_user.id
        id_us_env = int(os.getenv('USER_ID'))
        return id_inp == id_us_env
