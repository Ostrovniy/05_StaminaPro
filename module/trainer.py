import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer
from module.keyboard import Keyboard

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        text = 'джэ\\яЭ/ЬБЮ,'

        self.text_for_printing = ttk.StringVar(value=text)
        self.input = ttk.Label(self, textvariable=self.text_for_printing, font='Arial 40')
        self.input.pack()

        self.timer = Timer(self)
        self.timer.pack()
        
        # Создаем клавиатуру и активируем первый символ для ввода
        self.kayboard = Keyboard(self, first_char=self.get_first_char())
        self.kayboard.pack()

        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)

    def get_first_char(self):
        """Певый символ строки или false если символов не осталось"""
        if self.text_for_printing.get():
            return self.text_for_printing.get()[0]
        return False

    # Главный обработчик события
    def key_press(self, e):
        # Если строка пустая, остановить обработку события
        if not self.text_for_printing.get():
            self.timer.stop_timer()
            return
        
        # если нажата кнопка совпадает с первым символом значит нажали верно
        first_char = self.get_first_char()

        if e.char == first_char:
            # Запустить таймер, если он еще не
            self.timer.start_timer()
            
            # При последнем введенном верном символе, остановка таймер и клавы
            if len(self.text_for_printing.get()) == 1:
                self.kayboard.end() # Отключить клавиатуру в конце
                self.timer.stop_timer() # Остановить таймер в конце

            # Удалить первый введенным символ, обновляем строку ввода
            self.text_for_printing.set(self.text_for_printing.get()[1:])
            # Обновить кнопку для подсветки, первый символ подсветить
            self.kayboard.update_active_kay(self.get_first_char())
            
