import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from analytics.analytic import Analytic
from PIL import Image, ImageTk


class Block_indicator(ttk.Frame):
    def __init__(self, master, image_path, title, value, prefix, *args, **kwargs):
        """Блок показателя, фотображения картинки и рекорда печати, или кол ошибок или потраченого времени"""
        self.border_size = 2            # Размер обводки бокса
        self.border_color = 'primary'   # Цвет обводки 
        self.main_box_color = 'dark'    # Цвет виджета
        self.title = title              # Заголовок для виджета
        self.value = value              # Значения виджета
        self.prefix = prefix            # Префикс значения, з/мб сим, сек

        super().__init__(master, width=350, height=110+self.border_size*2, bootstyle=self.border_color, *args, **kwargs)

        # Основной контейнер, где будет фото, текст и значения, внутренние отступы служат обводкой
        self.main_box = ttk.Frame(self, bootstyle=self.main_box_color)
        self.main_box.pack(expand=True, fill=tk.BOTH, padx=self.border_size, pady=self.border_size)

        # Загружаем изображение и изменяем его размер до 100x100 пикселей
        self.image = Image.open(image_path).convert("RGBA")
        #self.image = self.image.resize((100, 100), Image.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Создаем Label для отображения изображения
        label = ttk.Label(self.main_box, image=self.photo, bootstyle=f"inverse-{self.main_box_color}")
        label.image = self.photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось сборщиком мусора
        label.pack(side=tk.LEFT, padx=5)

        # Заголовк блока (Рекорт скорости, Напечатано символов и прочее)
        self.title_lable = ttk.Label(self.main_box, text=self.title, font=f'Arial 16 bold', bootstyle=f"inverse-{self.main_box_color}")
        self.title_lable.pack(fill=tk.X, pady=(5, 0))

        # Значения
        self.speed_lable = ttk.Label(self.main_box, text=f'{self.value} {self.prefix}', font=f'Arial 38 bold', bootstyle=f"inverse-{self.main_box_color}")
        self.speed_lable.pack(fill=tk.X, expand=True)

        self.pack_propagate(False) # Оключить подстраивания виджета под контент

class AnaliticFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        """ Деш борд, создает и оборажает Block_indicator в два ряда """
        super().__init__(master, bootstyle="default", *args, **kwargs)

        self.analitic_data = self.analytic = Analytic('RU')
        self.analitic_data_en = self.analytic = Analytic('EN')

        # Показатели аналитик для языка ru
        self.record = self.analitic_data.gl_get_print_speed_record()
        self.quantity_true = self.analitic_data.gl_get_quantity_true()
        self.quantity_false = self.analitic_data.gl_get_quantity_false()
        self.minutes_spent = self.analitic_data.gl_get_minutes_spent()

        # Показатели аналитик для языка En
        self.record_en = self.analitic_data_en.gl_get_print_speed_record()
        self.quantity_true_en = self.analitic_data_en.gl_get_quantity_true()
        self.quantity_false_en = self.analitic_data_en.gl_get_quantity_false()
        self.minutes_spent_en = self.analitic_data_en.gl_get_minutes_spent()

        # Первый блок, для языка ru-----------------------------------------------------------------------------------------------------------------------------------------------------
        self.title_ru = ttk.Label(self, text='Показатели для ru', font='Arial 36 bold')
        self.title_ru.pack(fill=tk.X)

        self.line_ru = ttk.Frame(self)
        self.line_ru.pack(fill=tk.X)

        # https://www.flaticon.com/ru/packs/mental-health-18094876
        self.box_record_ru = Block_indicator(self.line_ru, image_path='img/speedrecord.png', title='Скорость печати', value=self.record, prefix='з/м')
        self.box_record_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_true_ru = Block_indicator(self.line_ru, image_path='img/char_true.png', title='Символов напеча...', value=self.quantity_true, prefix='')
        self.box_quantity_true_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_false_ru = Block_indicator(self.line_ru, image_path='img/char_false.png', title='Ошибок...', value=self.quantity_false, prefix='')
        self.box_quantity_false_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_minutes_spent_ru = Block_indicator(self.line_ru, image_path='img/time.png', title='Всего минут', value=self.minutes_spent, prefix='')
        self.box_minutes_spent_ru.pack(side=tk.LEFT, padx=5, pady=5)

        # Второй блок для языка En-----------------------------------------------------------------------------------------------------------------------------------------------------
        self.title_en = ttk.Label(self, text='Показатели для En', font='Arial 36 bold')
        self.title_en.pack(fill=tk.X, pady=(30, 0))

        self.line_en = ttk.Frame(self)
        self.line_en.pack(fill=tk.X)

        self.box_record_en = Block_indicator(self.line_en, image_path='img/speedrecord.png', title='Скорость печати', value=self.record_en, prefix='з/м')
        self.box_record_en.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_true_en = Block_indicator(self.line_en, image_path='img/char_true.png', title='Символов напеча...', value=self.quantity_true_en, prefix='')
        self.box_quantity_true_en.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_false_en = Block_indicator(self.line_en, image_path='img/char_false.png', title='Ошибок...', value=self.quantity_false_en, prefix='')
        self.box_quantity_false_en.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_minutes_spent_en = Block_indicator(self.line_en, image_path='img/time.png', title='Всего минут', value=self.minutes_spent_en, prefix='')
        self.box_minutes_spent_en.pack(side=tk.LEFT, padx=5, pady=5)
        # -----------------------------------------------------------------------------------------------------------------------------------------------------

        self.pack(expand=True, fill=tk.BOTH, padx=50)