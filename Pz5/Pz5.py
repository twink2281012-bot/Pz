# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.

def find_sum():
    try:
        n = 60
        total = 0

        for i in range(1, n + 1):
            total = total + i

        return total
    except Exception as e:
        print(f"Произошла ошибка в функции find_sum: {e}")
        return 0

try:
    result = find_sum()
    print("Сумма чисел от 1 до 60 равна:", result)
except Exception as e:
    print(f"Произошла ошибка при выполнении программы: {e}")
