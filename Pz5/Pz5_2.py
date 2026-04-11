# Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
# значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить правый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftRight3(A, B, C):
    try:
        print(f"    Вызвана функция ShiftRight3 с числами: A={A}, B={B}, C={C}")

        temp = C

        C = B
        B = A
        A = temp

        print(f"    После сдвига: A={A}, B={B}, C={C}")
        print()

        return A, B, C
    except Exception as e:
        print(f"    Ошибка в функции ShiftRight3: {e}")
        print()
        return A, B, C

try:
    print("Программа для правого циклического сдвига трех чисел")
    print("-" * 50)

    print("Введите первый набор чисел (A1, B1, C1):")
    try:
        A1 = float(input("A1 = "))
        B1 = float(input("B1 = "))
        C1 = float(input("C1 = "))
    except ValueError as e:
        print(f"Ошибка ввода для первого набора: {e}")
        print("Будут использованы значения по умолчанию (0, 0, 0)")
        A1, B1, C1 = 0.0, 0.0, 0.0

    print("\nВведите второй набор чисел (A2, B2, C2):")
    try:
        A2 = float(input("A2 = "))
        B2 = float(input("B2 = "))
        C2 = float(input("C2 = "))
    except ValueError as e:
        print(f"Ошибка ввода для второго набора: {e}")
        print("Будут использованы значения по умолчанию (0, 0, 0)")
        A2, B2, C2 = 0.0, 0.0, 0.0

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)

    print("Первый набор чисел:")
    print(f"Исходные: A1={A1}, B1={B1}, C1={C1}")
    A1_new, B1_new, C1_new = ShiftRight3(A1, B1, C1)
    print(f"Результат: A1={A1_new}, B1={B1_new}, C1={C1_new}")

    print()

    print("Второй набор чисел:")
    print(f"Исходные: A2={A2}, B2={B2}, C2={C2}")
    A2_new, B2_new, C2_new = ShiftRight3(A2, B2, C2)
    print(f"Результат: A2={A2_new}, B2={B2_new}, C2={C2_new}")

except Exception as e:
    print(f"\nНепредвиденная ошибка в программе: {e}")
