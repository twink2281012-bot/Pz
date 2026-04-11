# Дано число R и список размера N. Найти два соседних элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
# их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной)

try:
    N = int(input("Введите размер списка N: "))
    A = []

    print("Введите элементы списка:")
    for i in range(N):
        x = int(input(f"A[{i}] = "))
        A.append(x)

    R = int(input("Введите число R: "))

    print("\nИсходный список:", A)
    print("Число R =", R)

    min_diff = float('inf')
    best_i = 0

    for i in range(N - 1):
        current_sum = A[i] + A[i + 1]
        current_diff = abs(current_sum - R)

        if current_diff < min_diff:
            min_diff = current_diff
            best_i = i

    print(f"Лучшая пара: A[{best_i}]={A[best_i]} и A[{best_i + 1}]={A[best_i + 1]}")
    print(f"Их сумма = {A[best_i] + A[best_i + 1]}")
    print(f"Разница с R = {min_diff}")

except ValueError:
    print("Ошибка: введено некорректное значение. Ожидалось целое число.")
