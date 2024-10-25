import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# Фрейм для однок кнопки на клавиатуре
class Input(ttk.Frame):
    def __init__(self, master, text, textdone, *args, **kwargs):
        self.height = 100 # (1) Высота фрейма в пикселяд 

        super().__init__(master, bootstyle="primary", height=self.height, *args, **kwargs) #

        self.columnconfigure((0, 1), weight=1, uniform='a') # Две колокнпи делят 50 на 50 екран
        self.rowconfigure(0, weight=1, uniform='a') # Одна строка занимает всю высоту екрана
        self.grid_propagate(False) # Отключаем авто размер фрейм

        # Левая часть, текст который уже напечатан
        self.done_text = ttk.Label(self, font=f'Arial 50', textvariable=textdone, anchor='e', bootstyle="secondary")
        self.done_text.grid(row=0, column=0, sticky='nwse', padx=5, pady=5)

        # Правая часть, текст который нужно напечатать
        self.input_text = ttk.Label(self, font=f'Arial 50', textvariable=text, anchor='w')
        self.input_text.grid(row=0, column=1, sticky='nwse', padx=(0,5), pady=5)

        # (2) Поле ввода растянуть на всю доступную ширину
        self.pack(fill=tk.X, pady=10)
    
    def end(self):
        """Сцена цвета обводки на зеленый, успешное завершение ввода"""
        self.configure(bootstyle="success")
