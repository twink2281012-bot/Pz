# ПЗ №10, Вариант 12, Задача 2
#2. Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно вставив после каждой строки строку из символов
#«*».

import string

with open("text18-12.txt", encoding="utf-16-le") as f:
    content = f.read()

print("=== Содержимое файла text18-12.txt ===")
print(content)

space_count = sum(1 for ch in content if ch == " " or ch == "\t")
print(f"Количество пробельных символов: {space_count}")

lines = content.splitlines()

with open("text18-12_result.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
        f.write("*" * len(line) + "\n")

print("\nФайл text18-12_result.txt создан. Содержимое:")
with open("text18-12_result.txt", encoding="utf-8") as f:
    print(f.read())
