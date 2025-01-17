import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from astro import list_of_signs
from astro import list_of_periods
from astro import get_horoscope

# Главное окно
root = tk.Tk()
root.title("Судьба злодейка") #Назвние приложения
root.geometry("1044x750") #Размеры окна
root.resizable(False, False) #Установка фиксированного размера
# root.iconbitmap(default="favicon.ico") #Иконка

# Загрузка изображения
image = Image.open("bg.png")
photo = ImageTk.PhotoImage(image)

# Создание Label с изображением
label = tk.Label(root, image=photo)
label.image = "astro/bg.png"
label.pack(fill="both", expand=True)

# Создание комбобоксов с прокруткой
comboSign = ttk.Combobox(root, values=list_of_signs, state="readonly")
comboSign.current(0)
comboSign.place(x=140, y=303)
comboSign['height'] = 6

comboPeriod = ttk.Combobox(root, values=list_of_periods, state="readonly")
comboPeriod.current(0)
comboPeriod.place(x=510, y=303)
comboPeriod['height'] = 3

#Кнопка
btn = ttk.Button(text="Получить предсказание")
btn.place(x=750, y=303)

#Окошко для поедсказания

horoscope_label = tk.Text(root)
horoscope_label.config(width=65)
horoscope_label.config(height=15)
horoscope_label.config(state="disabled")
horoscope_label.config(font=("Arial", 15))
horoscope_label.place(relwidth = 0.5, relheight = 0.2, x=350, y=385)

def get_horoscope_click():
    horoscope_label.config(state="normal")
    horoscope_label.delete("1.0", tk.END)
    horoscope_label.insert("1.0", get_horoscope(comboSign.get(), comboPeriod.get()))
    horoscope_label.config(state="disabled")

btn.config(command=get_horoscope_click)
#Запуск
root.mainloop()
