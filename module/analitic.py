import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from analytics.analytic import Analytic
from PIL import Image, ImageTk

#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib.pyplot as plt

class Block_indicator(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.border_size = 2
        super().__init__(master, width=320, height=100+self.border_size*2, bootstyle="warning", *args, **kwargs)

        self.main_box = ttk.Frame(self, bootstyle="info") # dark
        self.main_box.pack(expand=True, fill=tk.BOTH, padx=self.border_size, pady=self.border_size)

        # Загружаем изображение и изменяем его размер до 100x100 пикселей
        self.image = Image.open("img/speedrecord.png").convert("RGBA")
        self.image = self.image.resize((100, 100), Image.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
        self.photo = ImageTk.PhotoImage(self.image)

        # Создаем Label для отображения изображения
        label = tk.Label(self.main_box, image=self.photo)
        label.image = self.photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось сборщиком мусора
        label.pack(side=tk.LEFT)

        

        self.pack_propagate(False) # Оключить подстраивания виджета под контент

class AnaliticFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        """  """
        super().__init__(master, bootstyle="default", *args, **kwargs)

        

        Block_indicator(self).pack(pady=10)

        self.pack(expand=True, fill=tk.BOTH)

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


