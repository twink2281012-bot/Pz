# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...
# •A (числа A перемножаются N раз)

try:
    A = float(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N (>0): "))

    if N <= 0:
        print("Ошибка: N должно быть больше 0!")
    else:
        result = 1

        count = 1
        while count <= N:
            result = result * A
            count = count + 1

        print(A, "в степени", N, "=", result)

        print("Проверка через **:", A ** N)
except ValueError:
    print("Ошибка")
