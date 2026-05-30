#1. Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65, 
#'history': 75}.
print("\n--- ЗАДАЧА 1: Поиск ключа с минимальным значением ---")

sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
print("Исходный словарь:", sample_dict)

# Находим ключ с минимальным значением
min_key = min(sample_dict, key=sample_dict.get)
min_value = sample_dict[min_key]

print(f"Ключ с минимальным значением: '{min_key}' = {min_value}")

# Альтернативный способ
print("\nПоиск минимального значения:")
for key, value in sample_dict.items():
    if value == min_value:
        print(f"  Минимум: {key} = {value}")

print("\n" + "-" * 40)
