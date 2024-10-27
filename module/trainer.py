import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer
from module.keyboard import Keyboard
from module.progressbar import HorizontalProgressbar
from module.input import Input
from sounds._sound import Sound

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, lesson_data, *args, **kwargs):
        super().__init__(master, bootstyle="default", *args, **kwargs)

        self.lesson = lesson_data                   # Урок который будет проходить {title: '', ....}
        self.title = self.lesson['title']           # Название урока
        self.language = self.lesson['language']     # Языковая раскладка урока
        self.text = self.lesson['text']             # Текст для печати
        self.len_chars = len(self.text)             # Количесвто символов для печати

        self.text_for_printing = ttk.StringVar(value=self.text)     # Текст который нужно печатать
        self.text_done = ttk.StringVar(value='')                    # Текст который уже напечатали
        self.print_speed = ttk.StringVar(value='Рекорт: ')          # Скорость печати текста

        self.sound_success = Sound(path_sound="sounds/click-button.wav")
        self.sound_error = Sound(path_sound="sounds/click-button-error.wav")

        # -------------------------------------------------------------------------------------------------
        self.box = ttk.Frame(self)
        self.box.pack(fill=tk.X, pady=(10,0))

        self.title_lable = ttk.Label(self.box, text=f'Урок: {self.title}', anchor='w', font=f'Arial 14 bold')
        self.title_lable.pack(side=tk.LEFT, anchor='w')

        self.record = ttk.Label(self.box, anchor='e', font=f'Arial 14', textvariable=self.print_speed)
        self.record.pack(side=tk.LEFT, anchor='e', expand=True, padx=(0, 10))

        self.timer = Timer(self.box)
        self.timer.pack(side=tk.LEFT, anchor='e')
        # -------------------------------------------------------------------------------------------------

        self.input = Input(self, self.text_for_printing, self.text_done)            # Текст для печати и напечатанный текст
        self.progres_bar = HorizontalProgressbar(self,len(self.text))               # Шкала выполнения, насколько текст уже напечатан
        self.kayboard = Keyboard(self, self.get_first_char(), self.language)        # Клавиатура, передаем первый символл для подсветки его перед началом печати

        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)
        self.bind("<KeyRelease>", self.on_key_release)

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
            self.sound_success.start_play(e.keysym) # Музыка упешного нажатия кнопки
            self.timer.start_timer() # Запустить таймер, если он еще не запуще
            self.progres_bar.update_progress() #Обновить прогрес бар +1

            # Завершение ввода, когда ввели последний символ
            if self.is_last_char():
                self.timer.stop_timer() # Остановить таймер в конце
                self.kayboard.end() # Отключить клавиатуру в конце
                self.input.end() # Покрасить граниуц в зеленый
                self.print_speed.set(f"Скорсоть: {int((self.len_chars/self.timer.time)*60)}")

            self.updata_text_done() # Обновить текст который уже напечатан
            self.update_text_for_printing() # Удалить первый введенным символ, обновляем строку ввода
            self.kayboard.update_active_kay(self.get_first_char()) # Обновить кнопку для подсветки, первый символ подсветить
        else:
            self.sound_error.start_play(e.keysym) # Музыка не успешного нажатия кнопки

    def on_key_release(self, e):
        """Обработка события когда кнопку отпустили"""
        Sound.clear_event_list(e.keysym) # Очистить список мобытий музыки, если кнопка отпущена ее можно запустить повторно
