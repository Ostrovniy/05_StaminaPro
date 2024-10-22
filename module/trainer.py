import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.text_for_printing = ttk.StringVar(value='Тестовый текст для печати')

        self.input = ttk.Label(self, textvariable=self.text_for_printing)
        self.input.pack()

        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)
    
    def key_press(self, e):
        print('нажатия на кнопку')