#1. Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65, 
#'history': 75}.
print("\n--- ЗАДАЧА 1: Поиск ключа с минимальным значением ---")

sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
print("Исходный словарь:", sample_dict)

min_key = min(sample_dict, key=sample_dict.get)
min_value = sample_dict[min_key]

print(f"Ключ с минимальным значением: '{min_key}' = {min_value}")

print("\n" + "-" * 40)
