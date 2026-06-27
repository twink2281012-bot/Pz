# ПЗ №10, Вариант 12, Задача 1
#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Максимальный элемент:
#Среднее арифметическое элементов первой трети:

numbers = [-99, 6, 12, -36, 20, 45, 100, -15, 33, -7, 88, 50]

with open("data_source.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(str(n) for n in numbers))

print("Файл data_source.txt создан.")

with open("data_source.txt", encoding="utf-8") as f:
    data = f.read().split()

nums = [int(x) for x in data]

count = len(nums)
maximum = max(nums)

third = count // 3
first_third = nums[:third]

if first_third:
    avg_first_third = sum(first_third) / len(first_third)
else:
    avg_first_third = 0

with open("data_result.txt", "w", encoding="utf-8") as f:
    f.write("Исходные данные: " + " ".join(str(n) for n in nums) + "\n")
    f.write("Количество элементов: " + str(count) + "\n")
    f.write("Максимальный элемент: " + str(maximum) + "\n")
    f.write(
        "Среднее арифметическое элементов первой трети: "
        + str(round(avg_first_third, 2))
        + "\n"
    )

print("Файл data_result.txt создан.")

with open("data_result.txt", encoding="utf-8") as f:
    print(f.read())
