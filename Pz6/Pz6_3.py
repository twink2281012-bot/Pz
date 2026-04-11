#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
#A1, а исходное значение K первых элементов будет потеряно). Последние K
#элементов полученного списка положить равными 0.
try:
    N = int(input("Введите размер списка N: "))
    A = []

    print("Введите элементы списка:")
    for i in range(N):
        x = int(input(f"A[{i}] = "))
        A.append(x)

    K = int(input("Введите число K (1 < K < N): "))

    if K <= 1 or K >= N:
        print("Ошибка: K должно быть больше 1 и меньше N")
    else:
        print(f"\nИсходный список: {A}")
        print(f"Сдвиг влево на {K} позиций")

        result = []

        for i in range(K, N):
            result.append(A[i])

        for i in range(K):
            result.append(0)

        print(f"Результат: {result}")

except ValueError:
    print("Ошибка: введено некорректное значение. Ожидалось целое число.")

        if current_diff < min_diff:
            min_diff = current_diff
            best_i = i

    print(f"Лучшая пара: A[{best_i}]={A[best_i]} и A[{best_i + 1}]={A[best_i + 1]}")
    print(f"Их сумма = {A[best_i] + A[best_i + 1]}")
    print(f"Разница с R = {min_diff}")

except ValueError:
    print("Ошибка: введено некорректное значение. Ожидалось целое число.")

except ValueError:
    print("Ошибка: введено некорректное значение. Ожидалось целое число.")
