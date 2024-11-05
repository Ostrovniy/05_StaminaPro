import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class Input(ttk.Frame):
    def __init__(self, master, text, textdone, *args, **kwargs):
        """ Фрейм, поле ввода текста, отображает текущий текс для воода и уже введенный текст """
        self.padding_top_frame = 10 # Отступ всего врейма сверху
        self.padding = 5 # Размер рамки, та что цветная
        self.height = 100 # (1) Высота фрейма в пикселяд
        self.forn_size = 50 # Размер шрифта
        self.text = text
        self.textdone = textdone
        
        super().__init__(master, bootstyle="primary", height=self.height, *args, **kwargs) 

        # Настройка сетки, 2 колокни и 1 ряд
        self.columnconfigure((0, 1), weight=1, uniform='a') # Две колокнпи делят 50 на 50 екран
        self.rowconfigure(0, weight=1, uniform='a') # Одна строка занимает всю высоту екрана
        self.grid_propagate(False) # Отключаем авто размер фрейм

        # Левая часть, Текст который уже напечатан, выровнять по правок стороне
        self.done_text = ttk.Label(self, font=f'Arial {self.forn_size}', textvariable=textdone, anchor='e', bootstyle="secondary")
        self.done_text.grid(row=0, column=0, sticky='nwse', padx=self.padding, pady=self.padding)

        # Правая часть, Текст который еще предстоит напечатать, выровнять по левой стороне
        self.input_text = ttk.Label(self, font=f'Arial {self.forn_size}', textvariable=text, anchor='w')
        self.input_text.grid(row=0, column=1, sticky='nwse', padx=(0,self.padding), pady=self.padding)

        # (2) Поле ввода растянуть на всю доступную ширину
        self.pack(fill=tk.X, pady=(self.padding_top_frame, 0))

    def end(self, speed):
        """Смена цвета обводки на зеленый, успешное завершение ввода"""
        self.configure(bootstyle="success")
        self.textdone.set('Скорость:')
        self.text.set(f'{speed} з/м')

    def set_pausa_style(self):
        """Смена цвета обводки на жолтый, когда установлена пауза"""
        self.configure(bootstyle="warning")

    def set_default_style(self):
        """Смена цвета обводки на обычный, когда пауза отключена"""
        self.configure(bootstyle="primary")
