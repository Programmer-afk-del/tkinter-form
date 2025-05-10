import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def show_specialty_info():
    messagebox.showinfo("Про спеціальність", "Спеціальність: Середня освіта (Математика)\n"
                                              "Це підготовка майбутніх учителів математики для роботи в школі. "
                                              "Студенти вивчають як педагогічні, так і математичні дисципліни.")

def upload_photo():
    # Це демонстраційний блок — в реальному випадку можна додати діалог для вибору фото
    photo_label.config(text="Фото буде тут (демо)")

# Створення головного вікна
root = tk.Tk()
root.title("Анкета")
root.geometry("300x550+500+100")
root.configure(bg="lightblue")

# Прізвище
label1 = tk.Label(root, text="Прізвище:", bg="lightblue")
label1.pack()
edit1 = tk.Entry(root)
edit1.pack()

# Ім’я
label2 = tk.Label(root, text="Ім’я:", bg="lightblue")
label2.pack()
edit2 = tk.Entry(root)
edit2.pack()

# По батькові
label3 = tk.Label(root, text="По батькові:", bg="lightblue")
label3.pack()
edit3 = tk.Entry(root)
edit3.pack()

# Стать: ч / ж
gender_label = tk.Label(root, text="Стать:", bg="lightblue")
gender_label.pack()

checkbutton1 = tk.Checkbutton(root, text="ч", bg="lightblue")
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(root, text="ж", bg="lightblue")
checkbutton2.pack()

# Мітка перед радіокнопками
course_label = tk.Label(root, text="Курс навчання:", bg="lightblue")
course_label.pack()

# Змінна для вибору курсу
course_var = tk.IntVar()
radio1 = tk.Radiobutton(root, text="1", variable=course_var, value=1, bg="lightblue")
radio1.pack()
radio2 = tk.Radiobutton(root, text="2", variable=course_var, value=2, bg="lightblue")
radio2.pack()
radio3 = tk.Radiobutton(root, text="3", variable=course_var, value=3, bg="lightblue")
radio3.pack()
radio4 = tk.Radiobutton(root, text="4", variable=course_var, value=4, bg="lightblue")
radio4.pack()

# Мітка і поле для введення (наприклад, улюблений предмет)
fav_label = tk.Label(root, text="Улюблений предмет:", bg="lightblue")
fav_label.pack()
fav_entry = tk.Entry(root)
fav_entry.pack()

# Кнопка про спеціальність
spec_button = tk.Button(root, text="Про спеціальність", command=show_specialty_info)
spec_button.pack()

# Мітка для фото
photo_label = tk.Label(root, text="", bg="lightblue")
photo_label.pack()

# Кнопка для фото
photo_button = tk.Button(root, text="Фото", command=upload_photo)
photo_button.pack()

# Запуск головного циклу
root.mainloop()