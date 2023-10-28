"""This module for integration keyboard to your PC """
from pyautogui import press, hotkey
import pyperclip


def error_valid(func):
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка в модуле клавиатуры:{e}")
    return wrapper


class Keyboard:
    @staticmethod
    @error_valid
    async def write_word(user_message: str) -> None:
        pyperclip.copy(user_message)
        hotkey('Ctrl', 'v')

    @staticmethod
    @error_valid
    async def press_key(user_message: str) -> None:
        press(user_message)

    @staticmethod
    @error_valid
    async def hotkey_input(user_message: str) -> None:
        hotkey(user_message)
