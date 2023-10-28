import subprocess
import functools
from platform import system

class CompilateTerminal:
    @functools.lru_cache(maxsize=100)
    async def linux_terminal(self, message_text, mes_obj):
        try:
            res = subprocess.run(message_text, text=True, capture_output=True, shell=True)
            if res.stdout is not None:
                await mes_obj.answer(text=res.stdout)
        except Exception as e:
            print(f'Ошибка в модуле терминала: {e}')

    @functools.lru_cache(maxsize=100)
    async def windows_terminal(self, message_text, mes_obj):
        command = 'powershell.exe ' + message_text
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stdout:
                await mes_obj.answer(text=stdout.decode('cp1251'))  # Используем кодировку cp1251
            if stderr:
                await mes_obj.answer(text=stderr.decode('cp1251'))  # Используем кодировку cp1251
        except Exception as e:
            print(f'Ошибка в модуле терминала: {e}')

    @functools.lru_cache(maxsize=100)
    async def os_pc(self, message_text: str, message_obj):
        model = system()
        if model == 'Linux':
            await self.linux_terminal(message_text, message_obj)
        elif model == 'Windows':
            await self.windows_terminal(message_text, message_obj)
        else:
            return 'Unsupported OS'
