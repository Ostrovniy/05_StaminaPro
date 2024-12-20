import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.timer import Timer
from module.keyboard import Keyboard
from module.progressbar import HorizontalProgressbar
from module.input import Input
from sounds._sound import SoundPygame
from analytics.analytic import Analytic

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, lesson_data, *args, **kwargs):
        """Фрейм для прохождения урока, обработка нажяти на клавиатуру и обработка напечатаного текста"""
        
        super().__init__(master, bootstyle="default", *args, **kwargs)
        self.status = 'старт'                       # Статус печати, {старт, пауза, конец}
        self.lesson = lesson_data                   # Урок который будет проходить {title: '', ....}
        self.title = self.lesson['title']           # Название урока
        self.language = self.lesson['language']     # Языковая раскладка урока
        self.text = self.lesson['text']             # Текст для печати
        self.len_chars = len(self.text)             # Количесвто символов для печати
        self.analytic = Analytic(self.language)     # Класс уплаврения аналитикой

        self.text_for_printing = ttk.StringVar(value=self.text)     # Текст который нужно печатать
        self.text_done = ttk.StringVar(value='')                    # Текст который уже напечатали
        self.print_speed = ttk.StringVar(value=f'Рекорт: {self.analytic.gl_get_print_speed_record()}') # Текущий рекортд скорости печати

        self.sound_success = SoundPygame(path_sound="sounds/click-button.wav")      # Музыка для успешного нажатия
        self.sound_error = SoundPygame(path_sound="sounds/click-button-error.wav")  # Музыка для неуспешного нажатия

        # Первая строка, Заголовк урока, текущий рекорт и Таймер ------------------------------------------
        self.box = ttk.Frame(self)
        self.box.pack(fill=tk.X, pady=(10,0))

        # Название урока
        self.title_lable = ttk.Label(self.box, text=f'Урок: {self.title}', anchor='w', font=f'Arial 14 bold')
        self.title_lable.pack(side=tk.LEFT, anchor='w')

        # Текущий рекор по скорости печати
        self.record = ttk.Label(self.box, anchor='e', font=f'Arial 14', textvariable=self.print_speed)
        self.record.pack(side=tk.LEFT, anchor='e', expand=True, padx=(0, 10))

        # Таймер
        self.timer = Timer(self.box)
        self.timer.pack(side=tk.LEFT, anchor='e')

        # (2-5) строка (Поле ввода, Прогрес бар, Клавиатура, Текст подсказка ------------------------------

        self.input = Input(self, self.text_for_printing, self.text_done)            # Текст для печати и напечатанный текст
        self.progres_bar = HorizontalProgressbar(self, self.len_chars)              # Шкала выполнения, насколько текст уже напечатан
        self.kayboard = Keyboard(self, self.get_first_char(), self.language)        # Клавиатура, передаем первый символл для подсветки его перед началом печати

        # Текстовая метка, для надати на паузу, пишет информацию в каком состояни находиться програма
        text_info = 'Введите корректный первый символ и таймер запуститься'
        self.lable_info_var = ttk.StringVar(value=text_info)
        self.lable_info = ttk.Label(self, textvariable=self.lable_info_var)
        self.lable_info.pack()

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
    
    def updata_text_done(self):
        """ Обновить текст который уже напечатан, переменная хранит максимум 12 символов
        Для корректного отображения в поле ввода, размер фрейма и шрифта влияет на колич
        ество символов которые можно отобразить """
        if len(self.text_done.get()) >= 18:
            self.text_done.set(self.text_done.get()[1:] + self.get_first_char())
        else:
            self.text_done.set(self.text_done.get() + self.text_for_printing.get()[0])

    def update_text_for_printing(self):
        """ Удалить первый символ текста для печати, обновления текста воода """
        self.text_for_printing.set(self.text_for_printing.get()[1:])
        
    def key_press(self, e):
        """ Обработка события нажатия на клавиатуру """

        # (1) Обработка ситуации, когда печать закончена и нажатия на обрабатываються
        if self.status == 'конец':
            return
        
        # (2) Переключатель паузы, включить и выключить
        if e.keysym == 'Escape':
            if self.status == 'старт':
                self.lable_info_var.set('Нажмите Esc что бы продолжыть печать')
                self.status = 'пауза'
                self.timer.stop_timer() # Остановка времени
                self.input.set_pausa_style()
                self.progres_bar.set_pausa_style()
                print('Пауза установлена')
                return
            if self.status == 'пауза':
                self.status = 'старт'
                self.timer.start_timer()  # Продолжаем таймер
                self.input.set_default_style()
                self.progres_bar.set_default_style()
                self.lable_info_var.set('Нажмите Esc что бы поставить паузу')
                print('Продолжаем, установлне старт')
                return
            
        # (3) Если пауза, то ничего дальше не делать ихнорируем ввод данных
        if self.status == 'пауза':
            return

        # (4) Напечатали ожыдаемый символ
        if e.char == self.get_first_char():
            self.analytic.gl_increment_quantity_true()              # Увеличить кол верных символов на 1
            self.sound_success.start_play(e.keysym)                 # Музыка упешного нажатия кнопки
            self.timer.start_timer()                                # Запустить таймер, если он еще не запуще
            self.progres_bar.update_progress()                      # Обновить прогрес бар +1

            # (7) Завершение ввода, когда ввели последний символ
            if self.is_last_char():
                self.status = 'конец'
                self.timer.stop_timer()                             # Остановить таймер в конце
                self.kayboard.end()                                 # Отключить клавиатуру в конце
                self.lable_info_var.set('Финиш !!!')                # Обновить текст под клавиатурой
                timePr = self.timer.time                            # Время печати в секундах
                speed = int((self.len_chars/timePr)*60)             # Расчитать скорость печати, 140 знаков в минуту
                self.analytic.gl_set_max_speed_record(speed)        # Обновить рекорд если он побит
                self.analytic.gl_increment_minutes_spent(timePr)    # Добавить потреченое время на печать
                self.analytic.save_data()                           # Сохранить данные в БД json по аналитике
                self.input.end(speed)

            # (6) Стандартная обработка введеного верно символа
            else:
                self.updata_text_done()                                 # Обновить текст который уже напечатан
                self.update_text_for_printing()                         # Удалить первый введенным символ, обновляем строку ввода
                self.kayboard.update_active_kay(self.get_first_char())  # Обновить кнопку для подсветки, если она есть

        # (5) Напечатали не верный символ
        else:
            self.analytic.gl_increment_quantity_false()             # Увеличить кол ошибок на 1
            self.sound_error.start_play(e.keysym)                   # Музыка не успешного нажатия кнопки

    def on_key_release(self, e):
        """Обработка события когда кнопку отпустили и нужно очистить
        список событий что бы запустить можно было повторно звук"""
        SoundPygame.clear_event_list(e.keysym)                      
