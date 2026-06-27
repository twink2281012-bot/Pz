# ПЗ №12, Вариант 12, Задача 1
#В матрице найти сумму и произведение элементов столбца N (N задать с
#клавиатуры)

import random


def generate_matrix(rows, cols, low=-10, high=10):
    """Генерация матрицы случайных целых чисел."""
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """Вывод матрицы на экран."""
    for row in matrix:
        print(" ".join(f"{el:4}" for el in row))


def column_sum(matrix, n):
    """Сумма элементов столбца n."""
    return sum(row[n] for row in matrix)


def column_product(matrix, n):
    """Произведение элементов столбца n."""
    result = 1
    for row in matrix:
        result *= row[n]
    return result


rows = 4
cols = 5

matrix = generate_matrix(rows, cols)

print("Исходная матрица:")
print_matrix(matrix)
print()

while True:
    try:
        n = int(input(f"Введите номер столбца (0 — {cols - 1}): "))
        if 0 <= n < cols:
            break
        print(f"Номер столбца должен быть от 0 до {cols - 1}.")
    except ValueError:
        print("Введите целое число.")

col_elements = [matrix[i][n] for i in range(rows)]
print(f"\nЭлементы столбца {n}: {col_elements}")
print(f"Сумма элементов столбца {n}: {column_sum(matrix, n)}")
print(f"Произведение элементов столбца {n}: {column_product(matrix, n)}")
