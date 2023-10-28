from aiogram.filters import Filter
from aiogram.types import Message
import platform
from controller import control_variable


class ValidGetDocument(Filter):
    def __init__(self) -> None:
        self.var_get_file = None

    @staticmethod
    async def operating_system():
        return str(platform.system())

    async def __call__(self, message: Message):
        result = await self.operating_system()
        if result == 'Linux':
            self.var_get_file = getattr(control_variable, 'get_doc')
            return bool(self.var_get_file)
        elif result == 'Windows':
            self.var_get_file = getattr(control_variable, 'get_doc')
            return bool(self.var_get_file)
