'''Module'''

import subprocess
from re import search
from aiogram import Router, F
from aiogram.types import Message

import all_keyboard as kb
from filters.terminal_valid import TerminalValidation
from filters.user_valid import ValidationUser
from filters.valid_getfile import ValidGetDocument
from filters.validation_var_for_keyboard import ValidationVariable, ValidAllVariables
from filters.validation_var_for_keyboard import ValidHotKey
from controller import Control, control_variable
router_linux = Router()


@router_linux.message(ValidationUser(), F.text == "/start")
async def q(message: Message):
    await message.delete()
    await message.answer(text="Привет дорогой пользователь", reply_markup=kb.kb_menu)


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Питание🔋")
async def nutrition(message: Message):
    await message.delete()
    await message.answer(text="Питание", reply_markup=kb.kb_changer)


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Звук🔉")
async def volume(message: Message):
    await message.delete()
    await message.answer(text="Меню звука", reply_markup=kb.kb_volume)


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "+10% к текущей громкости➕")
async def volume_plus(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "10%+"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "-10% к текущей громкости➖")
async def volume_minus(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "10%-"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Максимальная громкость🔊")
async def volume_max(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "100%+"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Минимальная🔈")
async def volume_minimal(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "100%-"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Замутить звук")
async def volume_mute(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "mute"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Размутить звук")
async def volume_unmete(message: Message):
    await message.delete()
    subprocess.call(["amixer", "set", "Master", "unmute"])


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Текущая громкость❔")
async def current_vollume(message: Message):
    await message.delete()
    command = ['amixer', 'sget', 'Master']
    output = subprocess.check_output(command).decode('utf-8')
    match = search(r'\[(\d+)%\]', output)
    if match:
        percentage = match.group(1)
        await message.answer(text=percentage)

    # await message.answer(text=currnet)


@router_linux.message(ValidationUser(), F.text == "Выйти в меню🚪")
async def exit_in_menu(message: Message):
    setattr(control_variable, 'tracking_logic_keyboard', False)
    setattr(control_variable, 'tracking_logic_terminal', False)
    setattr(control_variable, 'hot_keys', False)
    setattr(control_variable, 'get_doc', False)
    await message.answer(
        "Вы полностью вышли из режима клавиатуры и терминала", reply_markup=kb.kb_menu
    )


@router_linux.message(ValidationUser(), F.text == "Клавиатура ввод слов⌨️")
async def keyboard(message: Message):
    await message.delete()

    if hasattr(control_variable, 'tracking_logic_keyboard'):
        setattr(control_variable, 'tracking_logic_keyboard', True)
        await message.answer(text="Клавиатура", reply_markup=kb.kb_exit_menu)
    else:
        await message.answer(text='Такого атрибута нет')


@router_linux.message(ValidationUser(), ValidationVariable())
async def write(message: Message):

    with Control() as cn:
        await cn.keyboard.write_word(message.text)


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == 'Горячие клавиши🔥')
async def launch_hotkey(message: Message):

    await message.delete()
    if hasattr(control_variable, 'hot_keys'):
        setattr(control_variable, 'hot_keys', True)
        await message.answer(text='Горячие клавиши', reply_markup=kb.kb_exit_menu)
    else:
        raise AttributeError


@router_linux.message(ValidationUser(), ValidHotKey())
async def hotkey(message: Message):
    with Control() as cn:
        try:
            await cn.keyboard.press_key(message.text)
        except Exception as e:
            print(f"Error in summon method hot_key,{e}")


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == 'Терминал👨🏽‍💻')
async def term(message: Message):
    await message.delete()
    if hasattr(control_variable, 'tracking_logic_terminal'):
        setattr(control_variable, 'tracking_logic_terminal', True)
    else:
        raise AttributeError
    await message.answer(text='Терминал', reply_markup=kb.kb_exit_menu)


@router_linux.message(ValidationUser(), TerminalValidation())
async def compiling_term(message: Message):
    await message.delete()
    with Control() as cn:
        await cn.terminal.os_pc(message.text, message)


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == 'Получить файл⏬')
async def launch_doc(message: Message):
    await message.delete()
    if hasattr(control_variable, 'get_doc'):
        setattr(control_variable, 'get_doc', True)
    else:
        print("Error in summon method get_doc")
    await message.answer(text='Получение фалов', reply_markup=kb.kb_exit_menu)


@router_linux.message(ValidGetDocument(), ValidationUser())
async def get_document_from_pc(message: Message):
    with Control() as cn:
        await cn.file.get_file(message.text, message)
    await message.delete()


@router_linux.message(ValidationUser(), ValidAllVariables(), F.text == "Фото📷")
async def screenshot(message: Message):
    obj = Control()
    with Control() as cn:
        await cn.screenshot.scren_linux(message)
