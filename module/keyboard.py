import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from config.language_map import get_language_map_by_lancod

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
    def __init__(self, master, first_char,  *args, **kwargs):

        self.padding = 5 # Внутренний отступ клавиатуры, который добавлет бортики
        self.bgstyle = "dark" # Бекграут заливка, для клавиатуры и каждой строки

        super().__init__(master, bootstyle=self.bgstyle, *args, **kwargs)

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

    def end(self):
        """Метод который запускаеться когда выкючаеться клавиатура"""
        self.all_keys['Shift_L'].default()

    def create_and_place(self):
        """Создаем клавиатуру, и размещаем ее, каждая кнопка в словаре"""
        # Каждая строка имеет совй БД, что бы совпадал с БД Всей клавиатуры
        self.line1 = ttk.Frame(self, bootstyle=self.bgstyle)
        self.line2 = ttk.Frame(self, bootstyle=self.bgstyle)
        self.line3 = ttk.Frame(self, bootstyle=self.bgstyle)
        self.line4 = ttk.Frame(self, bootstyle=self.bgstyle)
        self.line5 = ttk.Frame(self, bootstyle=self.bgstyle)

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

        # Каждую строку прижать к левой стороне, и отступить по 5 по бокам
        # Первая и последняя строка отступает по 5 пикселе сверху и снизу
        self.line1.pack(anchor='w', padx=self.padding, pady=(self.padding, 0))        
        self.line2.pack(anchor='w', padx=self.padding)        
        self.line3.pack(anchor='w', padx=self.padding)        
        self.line4.pack(anchor='w', padx=self.padding)        
        self.line5.pack(anchor='w', padx=self.padding, pady=(0, self.padding))
