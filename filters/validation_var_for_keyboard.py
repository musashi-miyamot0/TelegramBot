from aiogram.filters import Filter
from aiogram import types
from controller import control_variable


class ValidationVariable(Filter):
    async def __call__(self, message: types.Message) -> bool:

        return bool(getattr(control_variable, 'tracking_logic_keyboard'))


class ValidHotKey(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return bool(getattr(control_variable, 'hot_keys'))


class ValidAllVariables(Filter):

    async def __call__(self, message: types.Message) -> bool:
        if not (bool(getattr(control_variable, 'tracking_logic_keyboard')) or
                bool(getattr(control_variable, 'tracking_logic_terminal')) or
                bool(getattr(control_variable, 'get_doc'))):
            return True
        else:
            return False
