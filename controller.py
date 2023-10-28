'''Модуль контроллер. Предостовляет простой доступ к модулям проекта'''
import functools
import platform

from modules import (get_file, keyboard_module, module_pycaw,
                     nutrition_module, screenshot_pc, terminal)


@functools.lru_cache
def os_pc():
    '''return name system. Only Windows and Linux'''
    return platform.system()


class Control:
    '''class for controlling functions, and simple access to functions and classes
    methods: error_valid, __enter__, __exit__

    atributes: keyboard, file, pycaw, nutrition, screenshot, terminal

    Instrucions for work with controller:
    refer to an attribute passing an argument via with
    '''

    def error_valid(self):
        '''intercepts errors in functions '''

        def wrapper(func, *args):
            try:
                func(*args)
            except AttributeError as e:
                print(e)
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)

        return wrapper

    def __init__(self):
        self.keyboard = None
        self.file = None
        self.pycaw = None
        self.nutrition = None
        self.screenshot = None
        self.terminal = None

    def __enter__(self):
        '''function for entering context with'''
        self.keyboard = keyboard_module.Keyboard()
        self.file = get_file.Get()
        self.pycaw = module_pycaw.VolumeControl() if os_pc() == 'Windows' else None
        self.nutrition = nutrition_module.Power()
        self.screenshot = screenshot_pc.ScreenshotPC()
        self.terminal = terminal.CompilateTerminal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Not working....'''


class ControlVariable:
    def __init__(self):
        self.tracking_logic_keyboard = False
        self.tracking_logic_terminal = False
        self.hot_keys = False
        self.get_doc = False


control_variable = ControlVariable()
