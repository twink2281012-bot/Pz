# ПЗ №16, Вариант 12
#
# Блок 1, задача 12:
#   Создайте класс «Животное» с атрибутами «имя» и «вид».
#   Напишите метод, который выводит информацию о животном
#   в формате «Имя: имя, Вид: вид».
#
# Блок 2, задача 12:
#   Создайте базовый класс «Транспорт» со свойствами «марка», «модель»
#   и «год выпуска». От этого класса унаследуйте класс «Автомобиль»
#   и добавьте в него свойство «тип кузова».


# ══════════════════════════════════════════════
# Блок 1 — Класс «Животное»
# ══════════════════════════════════════════════

class Zhivotnoe:
    """Класс, описывающий животное."""

    def __init__(self, imya: str, vid: str):
        self.imya = imya
        self.vid = vid

    def info(self) -> str:
        """Вывод информации о животном."""
        return f"Имя: {self.imya}, Вид: {self.vid}"


# Тестовые запуски — Блок 1
print("=== Блок 1: Животное ===")

zhiv1 = Zhivotnoe("Барсик", "Кот")
print(zhiv1.info())

zhiv2 = Zhivotnoe("Шарик", "Собака")
print(zhiv2.info())

zhiv3 = Zhivotnoe("Кеша", "Попугай")
print(zhiv3.info())

zhiv4 = Zhivotnoe("Рыжик", "Хомяк")
print(zhiv4.info())


# ══════════════════════════════════════════════
# Блок 2 — Классы «Транспорт» и «Автомобиль»
# ══════════════════════════════════════════════

class Transport:
    """Базовый класс «Транспорт»."""

    def __init__(self, marka: str, model: str, god_vypuska: int):
        self.marka = marka
        self.model = model
        self.god_vypuska = god_vypuska

    def info(self) -> str:
        """Базовая информация о транспорте."""
        return (
            f"Марка: {self.marka}, "
            f"Модель: {self.model}, "
            f"Год выпуска: {self.god_vypuska}"
        )


class Avtomobil(Transport):
    """Класс «Автомобиль», унаследованный от «Транспорт»."""

    def __init__(self, marka: str, model: str, god_vypuska: int, tip_kuzova: str):
        super().__init__(marka, model, god_vypuska)
        self.tip_kuzova = tip_kuzova

    def info(self) -> str:
        """Полная информация об автомобиле."""
        return super().info() + f", Тип кузова: {self.tip_kuzova}"


# Тестовые запуски — Блок 2
print("\n=== Блок 2: Транспорт / Автомобиль ===")

# Базовый транспорт
t1 = Transport("КАМАЗ", "65115", 2018)
print(t1.info())

# Автомобили
a1 = Avtomobil("Toyota", "Camry", 2021, "Седан")
print(a1.info())

a2 = Avtomobil("Lada", "Granta", 2020, "Лифтбек")
print(a2.info())

a3 = Avtomobil("BMW", "X5", 2023, "Внедорожник")
print(a3.info())

a4 = Avtomobil("Hyundai", "Creta", 2022, "Кроссовер")
print(a4.info())

# Проверка наследования
print(f"\nAvtomobil является наследником Transport: {issubclass(Avtomobil, Transport)}")
print(f"a1 является экземпляром Transport: {isinstance(a1, Transport)}")
