import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class HorizontalProgressbar(ttk.Progressbar):
    def __init__(self, master, max_value, *args, **kwargs):
        """Прогрес бар: отображает процесс печати,  
        -- max_value: количество символов которое нужно напечатать
        """
        self.padding_top_frame = 10 # Вертикальный отступ от тругих фреймов
        self.progress_var = tk.IntVar(value=0) # Значение прогресса
        
        # Инициализируем прогрессбар с параметрами
        super().__init__(master,orient=tk.HORIZONTAL,maximum=max_value,mode='determinate',variable=self.progress_var,bootstyle="success-striped",*args, **kwargs)
        # Растянуть шкалу на всю длину родителя
        self.pack(pady=(self.padding_top_frame ,0), fill=tk.X)

    # Метод для обновления значения прогресса
    def update_progress(self):
        """Увеличить шкалу на 1"""
        self.progress_var.set(self.progress_var.get()+1)

