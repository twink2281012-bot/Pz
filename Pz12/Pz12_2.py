# ПЗ №12, Вариант 12, Задача 2
#В матрице найти отрицательные элементы, сформировать из них новый массив.
#Вывести размер полученного массива.

import random


def generate_matrix(rows, cols, low=-10, high=10):
    """Генерация матрицы случайных целых чисел."""
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """Вывод матрицы на экран."""
    for row in matrix:
        print(" ".join(f"{el:4}" for el in row))


rows = 4
cols = 5

matrix = generate_matrix(rows, cols)

print("Исходная матрица:")
print_matrix(matrix)
print()

negative_elements = [el for row in matrix for el in row if el < 0]

print(f"Отрицательные элементы: {negative_elements}")
print(f"Размер нового массива: {len(negative_elements)}")
