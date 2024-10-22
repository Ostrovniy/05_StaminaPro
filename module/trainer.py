import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.text_for_printing = ttk.StringVar(value='тестовый текст для печати')

        self.input = ttk.Label(self, textvariable=self.text_for_printing)
        self.input.pack()

        self.timer = Timer(self)
        self.timer.pack()

        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)
    
    def key_press(self, e):
        # Если строка с текстом пустая, остановить таймер
        if not self.text_for_printing.get():
            self.timer.stop_timer()
            return
        
        # первый символ который нужно напечатать
        first = self.text_for_printing.get()[0]
        # если нажата кнопка совпадает с первым символом значит нажали верно
        if e.char == first:
            self.text_for_printing.set(self.text_for_printing.get()[1:])
            self.timer.start_timer()
