import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer
from module.keyboard import Keyboard
from module.input import Input

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        text = 'годы горы груз гиря шаг шарм шрам штык'

        self.text_for_printing = ttk.StringVar(value=text) # Текст который нужно печатать
        self.text_done = ttk.StringVar(value='') # Текст который уже напечатали

        # -------------------------------------------------------------------------------------------------
        self.box = ttk.Frame(self)
        self.box.pack(fill=tk.X, pady=(10,0))

        self.title = ttk.Label(self.box, text='Урок: печачать жр-зн', anchor='w', font=f'Arial 14 bold')
        self.title.pack(side=tk.LEFT, anchor='w')

        self.record = ttk.Label(self.box, text='Рекорд: 220 з/м', anchor='e', font=f'Arial 14')
        self.record.pack(side=tk.LEFT, anchor='e', expand=True, padx=(0, 10))

        self.timer = Timer(self.box)
        self.timer.pack(side=tk.LEFT, anchor='e')
        # -------------------------------------------------------------------------------------------------

        self.input = Input(self, text=self.text_for_printing, textdone=self.text_done)

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
                self.input.end() # Покрасить граниуц в зеленый

            # Обновить переменную напечатанного текста
            if len(self.text_done.get()) >= 12:
                self.text_done.set(self.text_done.get()[1:]+first_char)
            else:
                self.text_done.set(self.text_done.get()+self.text_for_printing.get()[0])

            # Удалить первый введенным символ, обновляем строку ввода
            self.text_for_printing.set(self.text_for_printing.get()[1:])
            # Обновить кнопку для подсветки, первый символ подсветить
            self.kayboard.update_active_kay(self.get_first_char())
            
