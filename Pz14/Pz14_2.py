# ПЗ №14, Вариант 12 — Задание 2
# GUI-версия задачи из ПЗ №12, вариант 12, задача 2:
# В матрице найти отрицательные элементы,
# сформировать из них новый массив, вывести его размер.

import tkinter as tk
from tkinter import messagebox
import random

ROWS = 4
COLS = 5


def generate():
    """Заполнить матрицу случайными числами."""
    for r in range(ROWS):
        for c in range(COLS):
            val = random.randint(-10, 10)
            cell_vars[r][c].set(str(val))
            # Подсветка отрицательных красным, остальных белым
            color = "#ffcccc" if val < 0 else "white"
            entries[r][c].configure(bg=color)
    result_var.set("Матрица сгенерирована. Нажмите «Найти отрицательные».")


def find_negatives():
    """Прочитать матрицу и найти отрицательные элементы."""
    try:
        matrix = [
            [int(cell_vars[r][c].get()) for c in range(COLS)]
            for r in range(ROWS)
        ]
    except ValueError:
        messagebox.showerror("Ошибка", "Все ячейки должны содержать целые числа.")
        return

    # Подсветка ячеек
    for r in range(ROWS):
        for c in range(COLS):
            color = "#ffcccc" if matrix[r][c] < 0 else "white"
            entries[r][c].configure(bg=color)

    negatives = [el for row in matrix for el in row if el < 0]

    if negatives:
        result_var.set(
            f"Отрицательные элементы: {negatives}\n"
            f"Размер нового массива: {len(negatives)}"
        )
    else:
        result_var.set("Отрицательных элементов не найдено.")


def clear():
    """Очистить все ячейки."""
    for r in range(ROWS):
        for c in range(COLS):
            cell_vars[r][c].set("")
            entries[r][c].configure(bg="white")
    result_var.set("Введите значения и нажмите «Найти отрицательные».")


root = tk.Tk()
root.title("Матрица — отрицательные элементы (ПЗ №12)")
root.resizable(False, False)
root.configure(bg="#ecf0f1")

tk.Label(
    root,
    text="Матрица — поиск отрицательных элементов",
    font=("Arial", 13, "bold"),
    bg="#ecf0f1",
    fg="#2c3e50",
).pack(pady=(15, 4))

tk.Label(
    root,
    text="Задание из ПЗ №12, вариант 12, задача 2",
    font=("Arial", 9),
    bg="#ecf0f1",
    fg="#7f8c8d",
).pack(pady=(0, 10))

# Сетка матрицы
grid_frame = tk.Frame(root, bg="#ecf0f1")
grid_frame.pack(padx=20)

cell_vars = []
entries = []

for r in range(ROWS):
    row_vars = []
    row_entries = []
    for c in range(COLS):
        var = tk.StringVar()
        entry = tk.Entry(
            grid_frame,
            textvariable=var,
            font=("Arial", 12),
            width=5,
            bd=1,
            relief="solid",
            justify="center",
            bg="white",
        )
        entry.grid(row=r, column=c, padx=3, pady=3, ipady=4)
        row_vars.append(var)
        row_entries.append(entry)
    cell_vars.append(row_vars)
    entries.append(row_entries)

# Кнопки
btn_frame = tk.Frame(root, bg="#ecf0f1")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Случайная матрица",
    font=("Arial", 10),
    bg="#6c5ce7",
    fg="white",
    activebackground="#a29bfe",
    bd=0,
    padx=12,
    pady=5,
    cursor="hand2",
    command=generate,
).pack(side="left", padx=5)

tk.Button(
    btn_frame,
    text="Найти отрицательные",
    font=("Arial", 10),
    bg="#00b894",
    fg="white",
    activebackground="#55efc4",
    bd=0,
    padx=12,
    pady=5,
    cursor="hand2",
    command=find_negatives,
).pack(side="left", padx=5)

tk.Button(
    btn_frame,
    text="Очистить",
    font=("Arial", 10),
    bg="#b2bec3",
    fg="white",
    bd=0,
    padx=12,
    pady=5,
    cursor="hand2",
    command=clear,
).pack(side="left", padx=5)

# Результат
result_frame = tk.Frame(root, bg="#dfe6e9", bd=1, relief="solid")
result_frame.pack(padx=20, pady=(5, 20), fill="x")

result_var = tk.StringVar(value="Введите значения и нажмите «Найти отрицательные».")
tk.Label(
    result_frame,
    textvariable=result_var,
    font=("Arial", 10),
    bg="#dfe6e9",
    fg="#2d3436",
    wraplength=360,
    justify="left",
    anchor="w",
).pack(padx=10, pady=8, fill="x")

# Сразу генерируем матрицу при запуске
generate()

root.mainloop()
