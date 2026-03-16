# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
try:
    number = int(input("Введите двузначное число: "))

    tens = number // 10

    units = number % 10

    new_number = units * 10 + tens

    print("Число после перестановки цифр:", new_number)
except ValueError:
    print("Ошибка")
