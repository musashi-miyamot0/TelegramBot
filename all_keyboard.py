from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Определение меню с кнопками
menu = [
        [
            KeyboardButton(text="Питание🔋"),
            KeyboardButton(text="Звук🔉"),
        ],
        [
            KeyboardButton(text="Терминал👨🏽‍💻"),
            KeyboardButton(text="Клавиатура ввод слов⌨️"),
            KeyboardButton(text="Фото📷"),
        ],
    [
        KeyboardButton(text='Горячие клавиши🔥'),
        KeyboardButton(text='Получить файл⏬')
    ]
    ]
# Определение меню с кнопками для контроля питания
changer = [
        [KeyboardButton(text="Выключить❌"), KeyboardButton(text="Перезагрузка🔄")],
        [
            KeyboardButton(text="Спящий режим💤"),
        ],
        [
            KeyboardButton(text="Выйти в меню🚪"),
        ],
    ]

# Определение меню с кнопками для управления громкостью
volume = [
        [
            KeyboardButton(text="+10% к текущей громкости➕"),
            KeyboardButton(text="-10% к текущей громкости➖"),
        ],
        [
            KeyboardButton(text="Максимальная громкость🔊"),
            KeyboardButton(text="Минимальная🔈"),
        ],
    [KeyboardButton(text="Замутить звук"),
     KeyboardButton(text="Размутить звук")],
    [KeyboardButton(text="Выйти в меню🚪"), KeyboardButton(text='Текущая громкость❔')],
    ]

keyboard = [
        [KeyboardButton(text="F"), KeyboardButton(text="M"), KeyboardButton(text="C")],
        [
            KeyboardButton(text="Space"),
            KeyboardButton(text="⬆️"),
            KeyboardButton(text="enter"),
        ],
        [KeyboardButton(text="⬅️"), KeyboardButton(text="⬇️"), KeyboardButton(text="➡️")],
    ]
exit_menu_one_but = [[KeyboardButton(text='Выйти в меню🚪')]]

# Создание ReplyKeyboardMarkup с заданными кнопками и параметрами
kb_exit_menu = ReplyKeyboardMarkup(keyboard=exit_menu_one_but, resize_keyboard=True)
kb_menu = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True)
kb_changer = ReplyKeyboardMarkup(keyboard=changer, resize_keyboard=True)
kb_volume = ReplyKeyboardMarkup(keyboard=volume, resize_keyboard=True)
kb_keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
