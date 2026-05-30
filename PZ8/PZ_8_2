print("\n--- ЗАДАЧА 2: Словарь англо-русских слов ---")

eng_rus_dict = {
    'apple': 'яблоко',
    'car': 'машина',
    'house': 'дом',
    'cat': 'кошка',
    'dog': 'собака',
    'sun': 'солнце',
    'moon': 'луна',
    'star': 'звезда',
    'water': 'вода',
    'fire': 'огонь'
}

print("Словарь англо-русских слов (10 слов):")
print("-" * 40)
for english, russian in eng_rus_dict.items():
    print(f"  {english} -> {russian}")

print("-" * 40)
print(f"Всего слов в словаре: {len(eng_rus_dict)}")

def translate(word):
    word = word.lower()
    if word in eng_rus_dict:
        return f"Перевод слова '{word}': {eng_rus_dict[word]}"
    else:
        return f"Слово '{word}' не найдено в словаре"

print("\nПроверка перевода:")
print(translate("cat"))
print(translate("sun"))
print(translate("elephant"))

print("\n" + "=" * 60)
print("КОНЕЦ РАБОТЫ")
print("=" * 60)
