import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# Таймер со всеми методами
class Timer(ttk.Label):
    def __init__(self, master, *args, **kwargs):
        self.time = 0 # Количество секунд
        self.running = False # Статус работы таймера
        self.timer_display = ttk.StringVar(value="00:00")

        super().__init__(master, font=("Arial", 14), textvariable=self.timer_display, *args, **kwargs)

    def start_timer(self):
        """Запуск таймера, если он еще не запущен"""
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        """Остановка таймера"""
        self.running = False

    def update_timer(self):
        """Обновление таймера каждые 1000 мс"""
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            self.timer_display.set(f"{minutes:02}:{seconds:02}")
            # Обновляем таймер каждую секунду
            self.after(1000, self.update_timer)