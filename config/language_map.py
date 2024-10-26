"""
autocorrect - символ который можно получить при нажатии клавиши вмести с shift, значения это ключ клавиши в key
key - клавиатура, символ клавиши идет как ключ, линия на который находиться клавиша, ее заголовк для отрисовки, ширина для отрисовки, размер и кей код на всякий
"""
# Большая кнопка
width = 85 
font_size = 35 

# Маленькая кнопка
#width = 60 
#font_size = 25 

config_ru = {
    'height': width,
    'font_size': font_size,
    'autocorrect': {'!': '1','"': '2','№': '3',';': '4','%': '5',':': '6','?': '7','*': '8','(': '9',')': '0','_': '-','+': '=','/': '\\',',': '.',},
    'keys': {
        # Первый ряд
        'ё':{'line': 1, 'title': 'Ё', 'width': width, 'font': font_size, 'keycode': 192},
        '1':{'line': 1, 'title': '1', 'width': width, 'font': font_size, 'keycode': 49},
        '2':{'line': 1, 'title': '2', 'width': width, 'font': font_size, 'keycode': 50},
        '3':{'line': 1, 'title': '3', 'width': width, 'font': font_size, 'keycode': 51},
        '4':{'line': 1, 'title': '4', 'width': width, 'font': font_size, 'keycode': 52},
        '5':{'line': 1, 'title': '5', 'width': width, 'font': font_size, 'keycode': 53},
        '6':{'line': 1, 'title': '6', 'width': width, 'font': font_size, 'keycode': 54},
        '7':{'line': 1, 'title': '7', 'width': width, 'font': font_size, 'keycode': 55},
        '8':{'line': 1, 'title': '8', 'width': width, 'font': font_size, 'keycode': 56},
        '9':{'line': 1, 'title': '9', 'width': width, 'font': font_size, 'keycode': 57},
        '0':{'line': 1, 'title': '0', 'width': width, 'font': font_size, 'keycode': 48},
        '-':{'line': 1, 'title': '-', 'width': width, 'font': font_size, 'keycode': 189},
        '=':{'line': 1, 'title': '=', 'width': width, 'font': font_size, 'keycode': 187},
        'BackSpace':{'line': 1, 'title': 'BackSpace', 'width': width*2.2, 'font': int(font_size/1.5), 'keycode': 8},
        # Второй ряд
        'Tab':{'line': 2, 'title': 'Tab', 'width': width*1.5, 'font': int(font_size/1.5), 'keycode': 9},
        'й':{'line': 2, 'title': 'Й', 'width': width, 'font': font_size, 'keycode': 81},
        'ц':{'line': 2, 'title': 'Ц', 'width': width, 'font': font_size, 'keycode': 87},
        'у':{'line': 2, 'title': 'У', 'width': width, 'font': font_size, 'keycode': 69},
        'к':{'line': 2, 'title': 'К', 'width': width, 'font': font_size, 'keycode': 82},
        'е':{'line': 2, 'title': 'Е', 'width': width, 'font': font_size, 'keycode': 84},
        'н':{'line': 2, 'title': 'Н', 'width': width, 'font': font_size, 'keycode': 89},
        'г':{'line': 2, 'title': 'Г', 'width': width, 'font': font_size, 'keycode': 85},
        'ш':{'line': 2, 'title': 'Ш', 'width': width, 'font': font_size, 'keycode': 73},
        'щ':{'line': 2, 'title': 'Щ', 'width': width, 'font': font_size, 'keycode': 79},
        'з':{'line': 2, 'title': 'З', 'width': width, 'font': font_size, 'keycode': 80},
        'х':{'line': 2, 'title': 'Х', 'width': width, 'font': font_size, 'keycode': 219},
        'ъ':{'line': 2, 'title': 'Ъ', 'width': width, 'font': font_size, 'keycode': 221},
        # Третий ряд
        'Caps_Lock':{'line': 3, 'title': 'Caps Lock', 'width': width*2, 'font': int(font_size/1.5), 'keycode': 20},
        'ф':{'line': 3, 'title': 'Ф', 'width': width, 'font': font_size, 'keycode': 65},
        'ы':{'line': 3, 'title': 'Ы', 'width': width, 'font': font_size, 'keycode': 83},
        'в':{'line': 3, 'title': 'В', 'width': width, 'font': font_size, 'keycode': 68},
        'а':{'line': 3, 'title': 'А', 'width': width, 'font': font_size, 'keycode': 79},
        'п':{'line': 3, 'title': 'П', 'width': width, 'font': font_size, 'keycode': 71},
        'р':{'line': 3, 'title': 'Р', 'width': width, 'font': font_size, 'keycode': 72},
        'о':{'line': 3, 'title': 'О', 'width': width, 'font': font_size, 'keycode': 74},
        'л':{'line': 3, 'title': 'Л', 'width': width, 'font': font_size, 'keycode': 75},
        'д':{'line': 3, 'title': 'Д', 'width': width, 'font': font_size, 'keycode': 76},
        'ж':{'line': 3, 'title': 'Ж', 'width': width, 'font': font_size, 'keycode': 186},
        'э':{'line': 3, 'title': 'Э', 'width': width, 'font': font_size, 'keycode': 222},
        '\\':{'line': 3, 'title': "\\", 'width': width, 'font': font_size, 'keycode': 220},
        # Четвертый ряд
        'Shift_L':{'line': 4, 'title': 'Shift', 'width': width*2.8, 'font': int(font_size/1.5), 'keycode': 16},
        'я':{'line': 4, 'title': 'Я', 'width': width, 'font': font_size, 'keycode': 90},
        'ч':{'line': 4, 'title': 'Ч', 'width': width, 'font': font_size, 'keycode': 88},
        'с':{'line': 4, 'title': 'С', 'width': width, 'font': font_size, 'keycode': 67},
        'м':{'line': 4, 'title': 'М', 'width': width, 'font': font_size, 'keycode': 86},
        'и':{'line': 4, 'title': 'И', 'width': width, 'font': font_size, 'keycode': 66},
        'т':{'line': 4, 'title': 'Т', 'width': width, 'font': font_size, 'keycode': 78},
        'ь':{'line': 4, 'title': 'Ь', 'width': width, 'font': font_size, 'keycode': 77},
        'б':{'line': 4, 'title': 'Б', 'width': width, 'font': font_size, 'keycode': 188},
        'ю':{'line': 4, 'title': 'Ю', 'width': width, 'font': font_size, 'keycode': 190},
        '.':{'line': 4, 'title': '.', 'width': width, 'font': font_size, 'keycode': 191},
        'Shift_R':{'line': 4, 'title': 'Shift', 'width': width*2.5, 'font': int(font_size/1.5), 'keycode': 16},
        # Пятый ряд
        'Control_L':{'line': 5, 'title': 'Ctrl', 'width': width*1.6, 'font': int(font_size/1.5), 'keycode': 17},
        'Win_L':{'line': 5, 'title': 'Win', 'width': width*1.3, 'font': int(font_size/1.5), 'keycode': 91},
        'Alt_L':{'line': 5, 'title': 'Alt', 'width': width*1.4, 'font': int(font_size/1.5), 'keycode': 18},
        ' ':{'line': 5, 'title': 'Пробел', 'width': width*5.5, 'font': int(font_size/1.5), 'keycode': 32},
        'Alt_R':{'line': 5, 'title': 'Alt', 'width': width*1.4, 'font': int(font_size/1.5), 'keycode': 18},
        'Fn!':{'line': 5, 'title': 'Fn', 'width': width*1.4, 'font': int(font_size/1.5), 'keycode': 0},
        'Menu!':{'line': 5, 'title': 'Menu', 'width': width*1.3, 'font': int(font_size/1.5), 'keycode': 0},
        'Control_R':{'line': 5, 'title': 'Ctrl', 'width': (width*1.6)-2, 'font': int(font_size/1.5), 'keycode': 17},
    }
}

# Возвращает нужный конфиг по коду языка
def get_language_map_by_lancod(code='RU'):
    # Регистрация конфигов
    data = {
        'RU': config_ru
    }
    return data[code]