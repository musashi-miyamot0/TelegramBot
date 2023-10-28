from aiogram.filters import Filter
from aiogram.types import Message

from controller import control_variable


# Filter for validation user id


class TerminalValidation(Filter):
    async def __call__(self, message: Message):
        return bool(getattr(control_variable, 'tracking_logic_terminal'))
