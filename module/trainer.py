import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer
from module.keyboard import Keyboard
from module.progressbar import HorizontalProgressbar
from module.input import Input

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, bootstyle="danger", *args, **kwargs)

        text = 'годы горы груз гиря шаг шарм шрам штык'
        self.len_chars = len(text)

        self.text_for_printing = ttk.StringVar(value=text) # Текст который нужно печатать
        self.text_done = ttk.StringVar(value='') # Текст который уже напечатали

        # -------------------------------------------------------------------------------------------------
        self.box = ttk.Frame(self)
        self.box.pack(fill=tk.X, pady=(10,0))

        self.title = ttk.Label(self.box, text='Урок: печачать жр-зн', anchor='w', font=f'Arial 14 bold')
        self.title.pack(side=tk.LEFT, anchor='w')

        self.record = ttk.Label(self.box, text='Рекорт: 220 з/м', anchor='e', font=f'Arial 14')
        self.record.pack(side=tk.LEFT, anchor='e', expand=True, padx=(0, 10))

        self.timer = Timer(self.box)
        self.timer.pack(side=tk.LEFT, anchor='e')
        # -------------------------------------------------------------------------------------------------

        self.input = Input(self, self.text_for_printing, self.text_done)    # Текст для печати и напечатанный текст
        self.progres_bar = HorizontalProgressbar(self,len(text))            # Шкала выполнения, насколько текст уже напечатан
        self.kayboard = Keyboard(self, self.get_first_char())               # Клавиатура, передаем первый символл для подсветки его перед началом печати

        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)

    def get_first_char(self):
        """ Певый символ строки или false если символов не осталось """
        if self.text_for_printing.get():
            return self.text_for_printing.get()[0]
        return False
    
    def is_last_char(self):
        """ Вводимый символ явзяеться последним символовм ? """
        return len(self.text_for_printing.get()) == 1
    
    def is_no_char(self):
        """ True если символов для печати не осталось """
        return not self.text_for_printing.get()
    
    def updata_text_done(self):
        """ Обновить текст который уже напечатан, переменная хранит максимум 12 символов
        Для корректного отображения в поле ввода, размер фрейма и шрифта влияет на колич
        ество символов которые можно отобразить """
        if len(self.text_done.get()) >= 12:
            self.text_done.set(self.text_done.get()[1:] + self.get_first_char())
        else:
            self.text_done.set(self.text_done.get() + self.text_for_printing.get()[0])

    def update_text_for_printing(self):
        """ Удалить первый символ текста для печати, обновления текста воода """
        self.text_for_printing.set(self.text_for_printing.get()[1:])
        
    def key_press(self, e):
        """ Обработка события нажатия на клавиатуру """
        # Все символы напечатаны
        if self.is_no_char():
            self.timer.stop_timer()
            return
        
        # Напечатали ожыдаемый символ
        if e.char == self.get_first_char():
            self.timer.start_timer() # Запустить таймер, если он еще не запуще
            self.progres_bar.update_progress() #Обновить прогрес бар +1

            # Завершение ввода, когда ввели последний символ
            if self.is_last_char():
                self.timer.stop_timer() # Остановить таймер в конце
                self.kayboard.end() # Отключить клавиатуру в конце
                self.input.end() # Покрасить граниуц в зеленый
                print(f'Скорость печати: {(self.len_chars/self.timer.time)*60}')

            self.updata_text_done() # Обновить текст который уже напечатан
            self.update_text_for_printing() # Удалить первый введенным символ, обновляем строку ввода
            self.kayboard.update_active_kay(self.get_first_char()) # Обновить кнопку для подсветки, первый символ подсветить
            
