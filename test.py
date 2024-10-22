import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# Главный фрейм для тренажера
class Trainer(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        

        # Переменная для отображаемого текста
        self.text_for_printing = ttk.StringVar(value='Тестовый текст для печати')
        self.input = ttk.Label(self, textvariable=self.text_for_printing)
        self.input.pack(pady=10)

        # Таймер переменные
        self.time = 0
        self.running = False
        self.timer_display = ttk.StringVar(value="00:00:00")

        # Поле для отображения таймера
        self.timer_label = ttk.Label(self, textvariable=self.timer_display, font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # Кнопки для запуска и остановки таймера
        self.start_button = ttk.Button(self, text="Старт", command=self.start_timer)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(self, text="Стоп", command=self.stop_timer)
        self.stop_button.pack(side="right", padx=5)

        # Привязка события нажатия клавиш
        self.focus_set()  # Устанавливаем фокус на фрейм
        self.bind('<KeyPress>', self.key_press)

    def key_press(self, e):
        """Обработка нажатия клавиш"""
        first = self.text_for_printing.get()[0]
        if e.char == first:
            self.text_for_printing.set(self.text_for_printing.get()[1:])

    def start_timer(self):
        """Запуск таймера"""
        if not self.running:
            self.running = True
            self.update_timer()
            self.focus_set()  # Устанавливаем фокус на фрейм

    def stop_timer(self):
        """Остановка таймера"""
        self.running = False

    def update_timer(self):
        """Обновление таймера каждые 1000 мс"""
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_display.set(f"{hours:02}:{minutes:02}:{seconds:02}")
            # Обновляем таймер каждую секунду
            self.after(1000, self.update_timer)

# Создание окна
root = ttk.Window(themename="darkly")
root.geometry('1400x600')
trainer = Trainer(root)
trainer.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()
