# ПЗ №13, Вариант 12
#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

with open("dates.txt", encoding="utf-8") as f:
    text = f.read()

print("=== Содержимое файла dates.txt ===")
print(text)

pattern_dot = re.compile(r"\d{2}\.\d{2}\.\d{4}")

pattern_slash = re.compile(r"\d{2}/\d{2}/\d{4}")

dates_dot = pattern_dot.findall(text)
dates_slash = pattern_slash.findall(text)

print(f"Даты в формате ДД.ММ.ГГГГ ({len(dates_dot)} шт.): {dates_dot}")
print(f"Даты в формате ДД/ММ/ГГГГ ({len(dates_slash)} шт.): {dates_slash}")

february_slash = [d for d in dates_slash if d[3:5] == "02"]

print(f"\nДаты февраля в формате ДД/ММ/ГГГГ: {february_slash}")

with open("dates_february.txt", "w", encoding="utf-8") as f:
    for d in february_slash:
        f.write(d + "\n")

print("Файл dates_february.txt создан.")
