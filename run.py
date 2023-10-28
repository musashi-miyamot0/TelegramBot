
'''Module launch bot'''
import asyncio
from platform import system
from os import getenv
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


class Run:
    '''class launch bot'''

    def __init__(self):
        '''init variable '''
        load_dotenv()
        self.bot = Bot(token=getenv("TOKEN"))
        self.dp = Dispatcher()

    async def on_startup(self, _):
        print("Бот запущен успешно")

    def validation(self, os_sys):
        if os_sys == "Linux":
            from handlers.handlers_for_linux import router_linux
            self.dp.include_router(router_linux)
            print(f"Операционная система: {os_sys}")
        else:
            from handlers.handlers_for_windows import router_windows
            self.dp.include_router(router_windows)
            print(f"Операционная система: {os_sys}")

    async def main(self):
        os_name = system()
        await self.on_startup(None)
        self.validation(os_name)
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    asyncio.run(Run().main())
