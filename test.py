import tkinter as tk
from PIL import Image, ImageTk

# Создаем главное окно
root = tk.Tk()
root.geometry("300x300")

# Создаем Frame
frame = tk.Frame(root)
frame.pack(pady=20)

# Загружаем изображение и изменяем его размер до 100x100 пикселей
image_path = "img/speedrecord.png"  # Укажите путь к изображению
image = Image.open(image_path)
image = image.resize((100, 100), Image.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
photo = ImageTk.PhotoImage(image)

# Создаем Label для отображения изображения
label = tk.Label(frame, image=photo)
label.image = photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось сборщиком мусора
label.pack()

root.mainloop()
