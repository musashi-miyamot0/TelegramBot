from aiogram import Router, F
from aiogram.types import Message


from controller import control_variable, Control
from filters.user_valid import ValidationUser
from filters.valid_getfile import ValidGetDocument
from filters.validation_var_for_keyboard import ValidationVariable, ValidAllVariables
from modules.screenshot_pc import ScreenshotPC
import all_keyboard as kb
from filters.validation_var_for_keyboard import ValidHotKey
from filters.terminal_valid import TerminalValidation
router_windows = Router()


@router_windows.message(ValidationUser(), F.text == "/start")
async def command_start(message: Message):
    """
    Start command handler.
    """
    await message.delete()
    await message.answer(text="Привет дорогой пользователь", reply_markup=kb.kb_menu)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Питание🔋")
async def pitanie(message: Message):
    """
    Power menu handler.
    """
    await message.delete()
    await message.answer(text="Питание", reply_markup=kb.kb_changer)

# Off your PC


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Выключить❌")
async def off(message: Message):
    """
    Turn off PC handler.
    """
    with Control() as c:
        c.nutrition.off()

# Reboot your PC


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Перезагрузка🔄")
async def reboot(message: Message):
    """
    Reboot PC handler.
    """
    with Control() as c:
        c.nutrition.reboot()

# Activate sleep mode on your PC


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Спящий режим💤")
async def sleep(message: Message):
    """
    Sleep mode handler.
    """

    with Control() as c:
        c.nutrition.sleep_mode()

# Return volume keyboard


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Звук🔉")
async def volume(message: Message):
    """
    Volume menu handler.
    """
    await message.delete()
    await message.answer(text="Меню звука", reply_markup=kb.kb_volume)

# Create screenshot and send to chat


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Фото📷")
async def nutrition(message: Message):
    """
    Screenshot handler.
    """
    await message.delete()
    obj = ScreenshotPC()
    await obj.scren_windows(message)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "+10% к текущей громкости➕")
async def volume_plus(message: Message):
    """
    Volume increase handler.
    """

    with Control() as c:
        c.pycaw.minus_and_plus(increase=True)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "-10% к текущей громкости➖")
async def volume_minus(message: Message):
    """
    Volume decrease handler.
    """
    with Control() as c:
        c.pycaw.minus_and_plus(increase=False)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Максимальная громкость🔊")
async def volume_max(message: Message):
    """
    Max volume handler.
    """
    with Control() as c:
        c.pycaw.maximum_and_minimum(1.0)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Минимальная🔈")
async def volume_minimum(message: Message):
    """
    Min volume handler.
    """
    with Control() as c:
        c.pycaw.maximum_and_minimum(0.0)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Замутить звук")
async def volume_mute(message: Message):
    """
    Mute volume handler.
    """
    await message.delete()
    with Control() as c:
        c.pycaw.mute(True)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Размутить звук")
async def volume_unmete(message: Message):
    """
    Unmute volume handler.
    """
    await message.delete()
    with Control() as c:
        c.pycaw.mute(False)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == "Текущая громкость❔")
async def current_vollume(message: Message):
    """
    Current volume handler.
    """
    await message.delete()
    with Control() as c:
        result = c.pycaw.current_volume_message()
    await message.answer(text=f"Текущая громкость: {result}")


@router_windows.message(ValidationUser(), F.text == "Выйти в меню🚪")
async def exit_menu(message: Message):
    """
    Exit menu handler.
    """
    setattr(control_variable, 'tracking_logic_keyboard', False)
    setattr(control_variable, 'tracking_logic_terminal', False)
    setattr(control_variable, 'hot_keys', False)
    setattr(control_variable, 'get_doc', False)
    await message.answer(text='Вы вышли в меню', reply_markup=kb.kb_menu)


@router_windows.message(ValidationUser(), F.text == "Клавиатура ввод слов⌨️")
async def keyboard(message: Message) -> None:
    """
    Keyboard input menu handler.
    """
    await message.delete()
    await message.answer(text='Клавиатура', reply_markup=kb.kb_exit_menu)
    setattr(control_variable, 'tracking_logic_keyboard', True)


@router_windows.message(ValidationUser(), ValidationVariable())
async def key_write(message: Message):
    """
    Keyboard input handler.
    """
    await message.delete()
    with Control() as cn:
        await cn.keyboard.write_word(message.text)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == 'Получить файл⏬')
async def launch_doc(message: Message):
    """
    Launch document handler.
    """
    await message.delete()
    if hasattr(control_variable, 'get_doc'):
        setattr(control_variable, 'get_doc', True)
    else:
        print("Error in summon method get_doc")
    await message.answer(text='Получение фалов', reply_markup=kb.kb_exit_menu)


@router_windows.message(ValidGetDocument(), ValidationUser())
async def get_document_from_pc(message: Message):
    """
    Get document from PC handler.
    """
    with Control() as cn:
        await cn.file.get_file(message.text, message)
    await message.delete()


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == 'Терминал👨🏽‍💻')
async def terminal(message: Message):

    if hasattr(control_variable, 'tracking_logic_terminal'):
        setattr(control_variable, 'tracking_logic_terminal', True)
        await message.answer(text='Терминал', reply_markup=kb.kb_exit_menu)
    else:
        await message.answer(text='Такой переменой нет')


@router_windows.message(TerminalValidation(), ValidationUser())
async def terminal_validation(message: Message):
    with Control() as cn:
        await cn.terminal.os_pc(message.text, message)


@router_windows.message(ValidationUser(), ValidAllVariables(), F.text == 'Горячие клавиши🔥')
async def hot_key(message: Message):
    '''
    handler for hot key
    '''
    await message.delete()
    if hasattr(control_variable, 'hot_keys'):
        setattr(control_variable, 'hot_keys', True)
        await message.answer(text='Горячие клавиши', reply_markup=kb.kb_exit_menu)
    else:
        raise AttributeError


@router_windows.message(ValidationUser(), ValidHotKey())
async def hotkey(message: Message):
    '''
    handler for hot key
    '''
    await message.delete()
    with Control() as cn:
        try:
            await cn.keyboard.hotkey_input(message.text.split(' '))

        except Exception as e:

            print(f"Error in summon method hot_key,{e}")


@router_windows.message()
async def f_but(message: Message):
    """
    Function button handler.
    """
    await message.delete()
