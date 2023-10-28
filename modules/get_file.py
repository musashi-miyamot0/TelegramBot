import os

from aiogram.types import FSInputFile


class Get:

    async def get_file(self, path_to_file: str, message):
        if await self.end_star(path_to_file, message):
            pass
        else:
            file_input = FSInputFile(str(path_to_file))
            await message.answer_document(document=file_input)

    async def end_star(self, message_text: str, message) -> bool:
        if message_text.endswith('*'):
            all_files = os.listdir(message_text[:-1])
            for file in all_files:
                path_to_file = os.path.join(message_text[:-1], file)
                if os.path.isdir(path_to_file):
                    continue
                file = FSInputFile(str(path_to_file))
                await message.answer_document(file)
            return True
        else:
            return False
