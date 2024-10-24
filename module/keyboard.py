import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from config.language_map import get_language_map_by_lancod

keycode_map = {
    '!': '1',
    '"': '2',
    '№': '3',
    ';': '4',
    '%': '5',
    ':': '6',
    '?': '7',
    '*': '8',
    '(': '9',
    ')': '0',
    '_': '-',
    '+': '=',
    '/': '\\',
    ',': '.',
}

Keys_config = {
    'ё':{'id': 1,'line': 1, 'title': 'Ё', 'width': 60, 'font': 'Arial 25', 'keycode': 192},
    '1':{'id': 2,'line': 1, 'title': '1', 'width': 60, 'font': 'Arial 25', 'keycode': 49},
    '2':{'id': 3,'line': 1, 'title': '2', 'width': 60, 'font': 'Arial 25', 'keycode': 50},
    '3':{'id': 4,'line': 1, 'title': '3', 'width': 60, 'font': 'Arial 25', 'keycode': 51},
    '4':{'id': 5,'line': 1, 'title': '4', 'width': 60, 'font': 'Arial 25', 'keycode': 52},
    '5':{'id': 6,'line': 1, 'title': '5', 'width': 60, 'font': 'Arial 25', 'keycode': 53},
    '6':{'id': 7,'line': 1, 'title': '6', 'width': 60, 'font': 'Arial 25', 'keycode': 54},
    '7':{'id': 8,'line': 1, 'title': '7', 'width': 60, 'font': 'Arial 25', 'keycode': 55},
    '8':{'id': 9,'line': 1, 'title': '8', 'width': 60, 'font': 'Arial 25', 'keycode': 56},
    '9':{'id': 10,'line': 1, 'title': '9', 'width': 60, 'font': 'Arial 25', 'keycode': 57},
    '0':{'id': 11,'line': 1, 'title': '0', 'width': 60, 'font': 'Arial 25', 'keycode': 48},
    '-':{'id': 12,'line': 1, 'title': '-', 'width': 60, 'font': 'Arial 25', 'keycode': 189},
    '=':{'id': 13,'line': 1, 'title': '=', 'width': 60, 'font': 'Arial 25', 'keycode': 187},
    'BackSpace':{'id': 14,'line': 1, 'title': 'BackSpace', 'width': 170, 'font': 'Arial 18', 'keycode': 8},

    'Tab':{'id': 15,'line': 2, 'title': 'Tab', 'width': 90, 'font': 'Arial 18', 'keycode': 9},
    'й':{'id': 16,'line': 2, 'title': 'Й', 'width': 60, 'font': 'Arial 25', 'keycode': 81},
    'ц':{'id': 17,'line': 2, 'title': 'Ц', 'width': 60, 'font': 'Arial 25', 'keycode': 87},
    'у':{'id': 18,'line': 2, 'title': 'У', 'width': 60, 'font': 'Arial 25', 'keycode': 69},
    'к':{'id': 19,'line': 2, 'title': 'К', 'width': 60, 'font': 'Arial 25', 'keycode': 82},
    'е':{'id': 20,'line': 2, 'title': 'Е', 'width': 60, 'font': 'Arial 25', 'keycode': 84},
    'н':{'id': 21,'line': 2, 'title': 'Н', 'width': 60, 'font': 'Arial 25', 'keycode': 89},
    'г':{'id': 22,'line': 2, 'title': 'Г', 'width': 60, 'font': 'Arial 25', 'keycode': 85},
    'ш':{'id': 23,'line': 2, 'title': 'Ш', 'width': 60, 'font': 'Arial 25', 'keycode': 73},
    'щ':{'id': 24,'line': 2, 'title': 'Щ', 'width': 60, 'font': 'Arial 25', 'keycode': 79},
    'з':{'id': 25,'line': 2, 'title': 'З', 'width': 60, 'font': 'Arial 25', 'keycode': 80},
    'х':{'id': 26,'line': 2, 'title': 'Х', 'width': 60, 'font': 'Arial 25', 'keycode': 219},
    'ъ':{'id': 27,'line': 2, 'title': 'Ъ', 'width': 60, 'font': 'Arial 25', 'keycode': 221},

    'Caps_Lock':{'id': 28,'line': 3, 'title': 'Caps Lock', 'width': 120, 'font': 'Arial 16', 'keycode': 20},
    'ф':{'id': 29,'line': 3, 'title': 'Ф', 'width': 60, 'font': 'Arial 25', 'keycode': 65},
    'ы':{'id': 29,'line': 3, 'title': 'Ы', 'width': 60, 'font': 'Arial 25', 'keycode': 83},
    'в':{'id': 30,'line': 3, 'title': 'В', 'width': 60, 'font': 'Arial 25', 'keycode': 68},
    'а':{'id': 31,'line': 3, 'title': 'А', 'width': 60, 'font': 'Arial 25', 'keycode': 79},
    'п':{'id': 32,'line': 3, 'title': 'П', 'width': 60, 'font': 'Arial 25', 'keycode': 71},
    'р':{'id': 33,'line': 3, 'title': 'Р', 'width': 60, 'font': 'Arial 25', 'keycode': 72},
    'о':{'id': 34,'line': 3, 'title': 'О', 'width': 60, 'font': 'Arial 25', 'keycode': 74},
    'л':{'id': 35,'line': 3, 'title': 'Л', 'width': 60, 'font': 'Arial 25', 'keycode': 75},
    'д':{'id': 36,'line': 3, 'title': 'Д', 'width': 60, 'font': 'Arial 25', 'keycode': 76},
    'ж':{'id': 37,'line': 3, 'title': 'Ж', 'width': 60, 'font': 'Arial 25', 'keycode': 186},
    'э':{'id': 38,'line': 3, 'title': 'Э', 'width': 60, 'font': 'Arial 25', 'keycode': 222},
    '\\':{'id': 39,'line': 3, 'title': "\\", 'width': 60, 'font': 'Arial 25', 'keycode': 220},

    'Shift_L':{'id': 40,'line': 4, 'title': 'Shift', 'width': 160, 'font': 'Arial 18', 'keycode': 16},
    'я':{'id': 41,'line': 4, 'title': 'Я', 'width': 60, 'font': 'Arial 25', 'keycode': 90},
    'ч':{'id': 42,'line': 4, 'title': 'Ч', 'width': 60, 'font': 'Arial 25', 'keycode': 88},
    'с':{'id': 43,'line': 4, 'title': 'С', 'width': 60, 'font': 'Arial 25', 'keycode': 67},
    'м':{'id': 44,'line': 4, 'title': 'М', 'width': 60, 'font': 'Arial 25', 'keycode': 86},
    'и':{'id': 45,'line': 4, 'title': 'И', 'width': 60, 'font': 'Arial 25', 'keycode': 66},
    'т':{'id': 46,'line': 4, 'title': 'Т', 'width': 60, 'font': 'Arial 25', 'keycode': 78},
    'ь':{'id': 47,'line': 4, 'title': 'Ь', 'width': 60, 'font': 'Arial 25', 'keycode': 77},
    'б':{'id': 48,'line': 4, 'title': 'Б', 'width': 60, 'font': 'Arial 25', 'keycode': 188},
    'ю':{'id': 49,'line': 4, 'title': 'Ю', 'width': 60, 'font': 'Arial 25', 'keycode': 190},
    '.':{'id': 50,'line': 4, 'title': '.', 'width': 60, 'font': 'Arial 25', 'keycode': 191},
    'Shift_R':{'id': 51,'line': 4, 'title': 'Shift', 'width': 190, 'font': 'Arial 18', 'keycode': 16},

    'Control_L':{'id': 52,'line': 5, 'title': 'Ctrl', 'width': 90, 'font': 'Arial 18', 'keycode': 17},
    'Win_L':{'id': 53,'line': 5, 'title': 'Win', 'width': 90, 'font': 'Arial 18', 'keycode': 91},
    'Alt_L':{'id': 54,'line': 5, 'title': 'Alt', 'width': 90, 'font': 'Arial 18', 'keycode': 18},
    ' ':{'id': 55,'line': 5, 'title': 'Пробел', 'width': 335, 'font': 'Arial 18', 'keycode': 32},
    'Alt_R':{'id': 56,'line': 5, 'title': 'Alt', 'width': 90, 'font': 'Arial 18', 'keycode': 18},
    'Fn!':{'id': 57,'line': 5, 'title': 'Fn', 'width': 90, 'font': 'Arial 18', 'keycode': 0},
    'Menu!':{'id': 58,'line': 5, 'title': 'Menu', 'width': 90, 'font': 'Arial 18', 'keycode': 0},
    'Control_R':{'id': 59,'line': 5, 'title': 'Ctrl', 'width': 90, 'font': 'Arial 18', 'keycode': 17},
    
}

# Фрейм для однок кнопки на клавиатуре
class Key(ttk.Frame):
    def __init__(self, master, key, width, font_size, *args, **kwargs):
        super().__init__(master, width=width, height=60, bootstyle="info", *args, **kwargs)

        # Состояние кнопки, активная или нет
        self.status = 'default'

        self.key = ttk.Label(self, text=key, bootstyle="inverse-info", font=f'Arial {font_size}') 
        self.key.pack(side=tk.TOP, expand=True)

        self.pack_propagate(False) # Оключить подстраивания виджета под контент
        self.pack(side=tk.LEFT, padx=2, pady=2)
    
    def active(self):
        """Стиль кнопки когда она активная"""
        if self.status != "active":
            self.configure(bootstyle="warning")
            self.key.configure(bootstyle="inverse-warning")
            self.status = 'active'
            self.update()

    def default(self):
        """Стиль кнопки по умолчанию"""
        if self.status != "default":
            self.configure(bootstyle="info")
            self.key.configure(bootstyle="inverse-info")
            self.status = 'default'
            self.update()


# Фрейм со всеми кнопками на клавиатуре, по строкам
class Keyboard(ttk.Frame):
    def __init__(self, master, first_char, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.all_keys = {} # Словарь со всеми кнопками {'Key': Key()}
        self.keys_config = get_language_map_by_lancod('RU') # Языковая карта клавиатуры
        self.create_and_place() # Добавить каждую клавишу в линию и в текущий фрейм
        self.set_acrive_kay(first_char) # Установить активную кнопку перед началом печати
        

    def set_acrive_kay(self, char):
        """Найти кнопку по символу, активировать ее"""
        # Заглавная буква, с активацией шифт, если символа нету в смиске, но если символ для lower
        if char not in self.all_keys and char.lower() in self.all_keys:
            self.active_kay = self.all_keys[char.lower()] # Получить кнопку
            self.active_kay.active() # Активировать клавишу
            self.all_keys['Shift_L'].active() # Активировать шифт

        # Для маленькой кнопки
        if char in self.all_keys:
            self.active_kay = self.all_keys[char] # Получить кнопку
            self.active_kay.active() # Активировать клавишу
            self.all_keys['Shift_L'].default() # Деактивировать шифт если он активный

        # Для символов, поиск по кей код
        if char not in self.all_keys and char in self.keys_config['autocorrect']:
            self.active_kay = self.all_keys[self.keys_config['autocorrect'][char]]
            self.active_kay.active() # Активировать клавишу
            self.all_keys['Shift_L'].active() # Активировать шифт

    def update_active_kay(self, new_char):
        """Обновить текущюю активную кнопку"""
        # Деактивировать кнопку которая уже активная
        self.active_kay.default()
        # Активировать новую кнопку по символу, если символ передали
        if new_char:
            self.set_acrive_kay(new_char)


    def create_and_place(self):
        """Создаем клавиатуру, и размещаем ее, каждая кнопка в словаре"""
        self.line1 = ttk.Frame(self)
        self.line2 = ttk.Frame(self)
        self.line3 = ttk.Frame(self)
        self.line4 = ttk.Frame(self)
        self.line5 = ttk.Frame(self)

        # Создание клафиш на основе язфкового конфига и отрисовка клавиш по рядам
        for key, value in self.keys_config['keys'].items():
            if value['line'] == 1:
                self.all_keys[key] = Key(self.line1, value['title'], value['width'], value['font'])

            if value['line'] == 2:
                self.all_keys[key] = Key(self.line2, value['title'], value['width'], value['font'])

            if value['line'] == 3:
                self.all_keys[key] = Key(self.line3, value['title'], value['width'], value['font'])

            if value['line'] == 4:
                self.all_keys[key] = Key(self.line4, value['title'], value['width'], value['font'])

            if value['line'] == 5:
                self.all_keys[key] = Key(self.line5, value['title'], value['width'], value['font'])

        self.line1.pack(anchor='w')        
        self.line2.pack(anchor='w')        
        self.line3.pack(anchor='w')        
        self.line4.pack(anchor='w')        
        self.line5.pack(anchor='w')
