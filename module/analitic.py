import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from analytics.analytic import Analytic
from PIL import Image, ImageTk

#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib.pyplot as plt

class Block_indicator(ttk.Frame):
    def __init__(self, master, image_path, title, value, prefix, *args, **kwargs):
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

        self.title_lable = ttk.Label(self.main_box, text=self.title, font=f'Arial 16 bold', bootstyle=f"inverse-{self.main_box_color}")
        self.title_lable.pack(fill=tk.X, pady=(5, 0))

        self.speed_lable = ttk.Label(self.main_box, text=f'{self.value} {self.prefix}', font=f'Arial 38 bold', bootstyle=f"inverse-{self.main_box_color}")
        self.speed_lable.pack(fill=tk.X, expand=True)

        

        self.pack_propagate(False) # Оключить подстраивания виджета под контент

class AnaliticFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        """  """
        super().__init__(master, bootstyle="default", *args, **kwargs)

        self.analitic_data = self.analytic = Analytic('RU')

        self.record = self.analitic_data.gl_get_print_speed_record()
        self.quantity_true = self.analitic_data.gl_get_quantity_true()
        self.quantity_false = self.analitic_data.gl_get_quantity_false()
        self.minutes_spent = self.analitic_data.gl_get_minutes_spent()

        self.title_ru = ttk.Label(self, text='Показатели для ru', font='Arial 36 bold')
        self.title_ru.pack(fill=tk.X)

        self.line_ru = ttk.Frame(self)
        self.line_ru.pack(fill=tk.X)

        self.box_record_ru = Block_indicator(self.line_ru, image_path='img/speedrecord.png', title='Скорость печати', value=self.record, prefix='з/м')
        self.box_record_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_true_ru = Block_indicator(self.line_ru, image_path='img/speedrecord.png', title='Символов напеча...', value=self.quantity_true, prefix='')
        self.box_quantity_true_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_quantity_false_ru = Block_indicator(self.line_ru, image_path='img/speedrecord.png', title='Ошибок...', value=self.quantity_false, prefix='')
        self.box_quantity_false_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.box_minutes_spent_ru = Block_indicator(self.line_ru, image_path='img/speedrecord.png', title='Всего минут', value=self.minutes_spent, prefix='')
        self.box_minutes_spent_ru.pack(side=tk.LEFT, padx=5, pady=5)

        self.pack(expand=True, fill=tk.BOTH, padx=50)

        #self.analitic_data = self.analytic = Analytic('RU')
        #self.record = self.analitic_data.gl_get_print_speed_record()

        #ttk.Label(self, text='Отображения аналитических показателей').pack()
        #ttk.Label(self, text=f'Рекорт: {self.record}').pack()
        #self.pack()

        #sales_data = {
            #"Product A": 100,
            #"Product B": 200,
            #"Product C": 600,
            #"Product D": 400,
            #"Product E": 500
        #}

        #plt.rcParams["axes.prop_cycle"] = plt.cycler(
            #color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])
        
        #fig1, ax1 = plt.subplots()
        #ax1.bar(sales_data.keys(), sales_data.values())
        #ax1.set_title("Sales by Product")
        #ax1.set_xlabel("Product")
        #ax1.set_ylabel("Sales")

        #canvas1 = FigureCanvasTkAgg(fig1, self)
        #canvas1.draw()
        #canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)
        #canvas1.get_tk_widget().pack()

        # Создаем обработчик закрытия окна
        #master.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        pass
        # Завершаем процессы matplotlib и закрываем окно
        #plt.close('all')  # Закрываем все фигуры matplotlib
        #self.master.destroy()  # Закрываем окно Tkinter


