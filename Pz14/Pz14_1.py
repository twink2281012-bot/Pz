# ПЗ №14, Вариант 12 


import tkinter as tk
from tkinter import messagebox


def register():
    username = username_var.get().strip()
    email = email_var.get().strip()
    password = password_var.get()
    confirm = confirm_var.get()

    if not username or not email or not password or not confirm:
        messagebox.showwarning("Внимание", "Заполните все поля!")
        return
    if "@" not in email or "." not in email:
        messagebox.showerror("Ошибка", "Некорректный email!")
        return
    if password != confirm:
        messagebox.showerror("Ошибка", "Пароли не совпадают!")
        return

    messagebox.showinfo("Успех", f"Пользователь «{username}» успешно зарегистрирован!")
    username_var.set("")
    email_var.set("")
    password_var.set("")
    confirm_var.set("")


root = tk.Tk()
root.title("Registration Form")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(
    root,
    text="Create Account",
    font=("Arial", 16, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50",
).pack(pady=(20, 4))

tk.Label(
    root,
    text="Please fill in the fields below",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#7f8c8d",
).pack(pady=(0, 14))

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(padx=35, pady=5)

username_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()
confirm_var = tk.StringVar()

fields = [
    ("Username", username_var, False),
    ("Email", email_var, False),
    ("Password", password_var, True),
    ("Confirm Password", confirm_var, True),
]

for label_text, var, is_password in fields:
    tk.Label(
        frame,
        text=label_text,
        font=("Arial", 10),
        bg="#f0f4f8",
        fg="#2c3e50",
        anchor="w",
    ).pack(fill="x", pady=(8, 0))
    show_char = "*" if is_password else ""
    tk.Entry(
        frame,
        textvariable=var,
        show=show_char,
        font=("Arial", 11),
        width=28,
        bd=1,
        relief="solid",
    ).pack(ipady=4)

tk.Button(
    root,
    text="Register",
    font=("Arial", 11, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=7,
    cursor="hand2",
    command=register,
).pack(pady=15)

tk.Label(
    root,
    text="Already have an account? Log in",
    font=("Arial", 9),
    bg="#f0f4f8",
    fg="#3498db",
    cursor="hand2",
).pack(pady=(0, 20))

root.mainloop()
