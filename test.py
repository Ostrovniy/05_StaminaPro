import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

root = tk.Tk()

# Создаем изображение и указываем фон как прозрачный
img = Image.new('RGBA', (200, 60), (255, 255, 255, 0))  
draw = ImageDraw.Draw(img)

# Загружаем шрифты разных размеров
large_font = ImageFont.truetype("arial.ttf", 38)  # Основной размер
small_font = ImageFont.truetype("arial.ttf", 18)  # Размер для текста "з/м"

# Рисуем текст на изображении
draw.text((10, 10), "250", font=large_font, fill="black")  # Число с большим шрифтом
draw.text((110, 30), "з/м", font=small_font, fill="black")  # Текст с маленьким шрифтом

# Преобразуем изображение для Tkinter
img_tk = ImageTk.PhotoImage(img)

# Создаем и размещаем Label с изображением
label = tk.Label(root, image=img_tk, bg="white")
label.pack()

root.mainloop()
