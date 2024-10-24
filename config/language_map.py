"""
autocorrect - символ который можно получить при нажатии клавиши вмести с shift, значения это ключ клавиши в key
key - клавиатура, символ клавиши идет как ключ, линия на который находиться клавиша, ее заголовк для отрисовки, ширина для отрисовки, размер и кей код на всякий
"""

config_ru = {
    'autocorrect': {'!': '1','"': '2','№': '3',';': '4','%': '5',':': '6','?': '7','*': '8','(': '9',')': '0','_': '-','+': '=','/': '\\',',': '.',},
    'keys': {
        # Первый ряд
        'ё':{'line': 1, 'title': 'Ё', 'width': 60, 'font': '25', 'keycode': 192},
        '1':{'line': 1, 'title': '1', 'width': 60, 'font': '25', 'keycode': 49},
        '2':{'line': 1, 'title': '2', 'width': 60, 'font': '25', 'keycode': 50},
        '3':{'line': 1, 'title': '3', 'width': 60, 'font': '25', 'keycode': 51},
        '4':{'line': 1, 'title': '4', 'width': 60, 'font': '25', 'keycode': 52},
        '5':{'line': 1, 'title': '5', 'width': 60, 'font': '25', 'keycode': 53},
        '6':{'line': 1, 'title': '6', 'width': 60, 'font': '25', 'keycode': 54},
        '7':{'line': 1, 'title': '7', 'width': 60, 'font': '25', 'keycode': 55},
        '8':{'line': 1, 'title': '8', 'width': 60, 'font': '25', 'keycode': 56},
        '9':{'line': 1, 'title': '9', 'width': 60, 'font': '25', 'keycode': 57},
        '0':{'line': 1, 'title': '0', 'width': 60, 'font': '25', 'keycode': 48},
        '-':{'line': 1, 'title': '-', 'width': 60, 'font': '25', 'keycode': 189},
        '=':{'line': 1, 'title': '=', 'width': 60, 'font': '25', 'keycode': 187},
        'BackSpace':{'line': 1, 'title': 'BackSpace', 'width': 170, 'font': '18', 'keycode': 8},
        # Второй ряд
        'Tab':{'line': 2, 'title': 'Tab', 'width': 90, 'font': '18', 'keycode': 9},
        'й':{'line': 2, 'title': 'Й', 'width': 60, 'font': '25', 'keycode': 81},
        'ц':{'line': 2, 'title': 'Ц', 'width': 60, 'font': '25', 'keycode': 87},
        'у':{'line': 2, 'title': 'У', 'width': 60, 'font': '25', 'keycode': 69},
        'к':{'line': 2, 'title': 'К', 'width': 60, 'font': '25', 'keycode': 82},
        'е':{'line': 2, 'title': 'Е', 'width': 60, 'font': '25', 'keycode': 84},
        'н':{'line': 2, 'title': 'Н', 'width': 60, 'font': '25', 'keycode': 89},
        'г':{'line': 2, 'title': 'Г', 'width': 60, 'font': '25', 'keycode': 85},
        'ш':{'line': 2, 'title': 'Ш', 'width': 60, 'font': '25', 'keycode': 73},
        'щ':{'line': 2, 'title': 'Щ', 'width': 60, 'font': '25', 'keycode': 79},
        'з':{'line': 2, 'title': 'З', 'width': 60, 'font': '25', 'keycode': 80},
        'х':{'line': 2, 'title': 'Х', 'width': 60, 'font': '25', 'keycode': 219},
        'ъ':{'line': 2, 'title': 'Ъ', 'width': 60, 'font': '25', 'keycode': 221},
        # Третий ряд
        'Caps_Lock':{'line': 3, 'title': 'Caps Lock', 'width': 120, 'font': '16', 'keycode': 20},
        'ф':{'line': 3, 'title': 'Ф', 'width': 60, 'font': '25', 'keycode': 65},
        'ы':{'line': 3, 'title': 'Ы', 'width': 60, 'font': '25', 'keycode': 83},
        'в':{'line': 3, 'title': 'В', 'width': 60, 'font': '25', 'keycode': 68},
        'а':{'line': 3, 'title': 'А', 'width': 60, 'font': '25', 'keycode': 79},
        'п':{'line': 3, 'title': 'П', 'width': 60, 'font': '25', 'keycode': 71},
        'р':{'line': 3, 'title': 'Р', 'width': 60, 'font': '25', 'keycode': 72},
        'о':{'line': 3, 'title': 'О', 'width': 60, 'font': '25', 'keycode': 74},
        'л':{'line': 3, 'title': 'Л', 'width': 60, 'font': '25', 'keycode': 75},
        'д':{'line': 3, 'title': 'Д', 'width': 60, 'font': '25', 'keycode': 76},
        'ж':{'line': 3, 'title': 'Ж', 'width': 60, 'font': '25', 'keycode': 186},
        'э':{'line': 3, 'title': 'Э', 'width': 60, 'font': '25', 'keycode': 222},
        '\\':{'line': 3, 'title': "\\", 'width': 60, 'font': '25', 'keycode': 220},
        # Четвертый ряд
        'Shift_L':{'line': 4, 'title': 'Shift', 'width': 160, 'font': '18', 'keycode': 16},
        'я':{'line': 4, 'title': 'Я', 'width': 60, 'font': '25', 'keycode': 90},
        'ч':{'line': 4, 'title': 'Ч', 'width': 60, 'font': '25', 'keycode': 88},
        'с':{'line': 4, 'title': 'С', 'width': 60, 'font': '25', 'keycode': 67},
        'м':{'line': 4, 'title': 'М', 'width': 60, 'font': '25', 'keycode': 86},
        'и':{'line': 4, 'title': 'И', 'width': 60, 'font': '25', 'keycode': 66},
        'т':{'line': 4, 'title': 'Т', 'width': 60, 'font': '25', 'keycode': 78},
        'ь':{'line': 4, 'title': 'Ь', 'width': 60, 'font': '25', 'keycode': 77},
        'б':{'line': 4, 'title': 'Б', 'width': 60, 'font': '25', 'keycode': 188},
        'ю':{'line': 4, 'title': 'Ю', 'width': 60, 'font': '25', 'keycode': 190},
        '.':{'line': 4, 'title': '.', 'width': 60, 'font': '25', 'keycode': 191},
        'Shift_R':{'line': 4, 'title': 'Shift', 'width': 190, 'font': '18', 'keycode': 16},
        # Пятый ряд
        'Control_L':{'line': 5, 'title': 'Ctrl', 'width': 90, 'font': '18', 'keycode': 17},
        'Win_L':{'line': 5, 'title': 'Win', 'width': 90, 'font': '18', 'keycode': 91},
        'Alt_L':{'line': 5, 'title': 'Alt', 'width': 90, 'font': '18', 'keycode': 18},
        ' ':{'line': 5, 'title': 'Пробел', 'width': 335, 'font': '18', 'keycode': 32},
        'Alt_R':{'line': 5, 'title': 'Alt', 'width': 90, 'font': '18', 'keycode': 18},
        'Fn!':{'line': 5, 'title': 'Fn', 'width': 90, 'font': '18', 'keycode': 0},
        'Menu!':{'line': 5, 'title': 'Menu', 'width': 90, 'font': '18', 'keycode': 0},
        'Control_R':{'line': 5, 'title': 'Ctrl', 'width': 90, 'font': '18', 'keycode': 17},
    }
}

# Возвращает нужный конфиг по коду языка
def get_language_map_by_lancod(code='RU'):
    # Регистрация конфигов
    data = {
        'RU': config_ru
    }
    return data[code]