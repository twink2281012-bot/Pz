# ПЗ №15, Вариант 12
#Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по
#ремонту бытовой техники. БД должна содержать таблицу Ремонт телевизоров, имеющую
#следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена, Дата
#ремонта, Документ, Мастер, Сумма оплаты.


import sqlite3


DB_NAME = "telemasterskaya.db"


# ──────────────────────────────────────────────
# Инициализация БД
# ──────────────────────────────────────────────

def init_db():
    """Создание таблицы, если не существует."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS remont (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                marka           TEXT    NOT NULL,
                zavod           TEXT    NOT NULL,
                cena            REAL    NOT NULL,
                data_remonta    TEXT    NOT NULL,
                dokument        TEXT    NOT NULL,
                master          TEXT    NOT NULL,
                summa           REAL    NOT NULL
            )
        """)
        conn.commit()


# ──────────────────────────────────────────────
# Ввод данных
# ──────────────────────────────────────────────

def insert_record(marka, zavod, cena, data_remonta, dokument, master, summa):
    """Добавление одной записи."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO remont (marka, zavod, cena, data_remonta, dokument, master, summa) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (marka, zavod, cena, data_remonta, dokument, master, summa),
        )
        conn.commit()


def fill_sample_data():
    """Заполнение 10 тестовых записей."""
    records = [
        ("Samsung UE55", "Samsung Electronics", 45000, "2024-01-10",
         "АКТ-001", "Петров И.И.", 2500),
        ("LG OLED65", "LG Electronics", 78000, "2024-01-15",
         "АКТ-002", "Сидоров А.В.", 3200),
        ("Sony KD-55", "Sony Corporation", 62000, "2024-01-20",
         "АКТ-003", "Петров И.И.", 1800),
        ("Philips 50PUS", "Philips Consumer", 35000, "2024-02-03",
         "АКТ-004", "Козлов Д.С.", 4100),
        ("Hisense 43A", "Hisense Co.", 28000, "2024-02-14",
         "АКТ-005", "Сидоров А.В.", 900),
        ("TCL 55C", "TCL Electronics", 32000, "2024-02-20",
         "АКТ-006", "Петров И.И.", 1500),
        ("Haier 43Smart", "Haier Group", 22000, "2024-03-01",
         "АКТ-007", "Козлов Д.С.", 3700),
        ("Xiaomi Mi TV", "Xiaomi Inc.", 29000, "2024-03-10",
         "АКТ-008", "Сидоров А.В.", 2100),
        ("Skyworth 50G3", "Skyworth Group", 27000, "2024-03-18",
         "АКТ-009", "Петров И.И.", 1200),
        ("BBK 55LED", "BBK Electronics", 20000, "2024-03-25",
         "АКТ-010", "Козлов Д.С.", 800),
    ]
    for rec in records:
        insert_record(*rec)
    print("10 записей успешно добавлены.")


# ──────────────────────────────────────────────
# Вывод всех записей
# ──────────────────────────────────────────────

def print_all():
    """Вывод всей таблицы."""
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("SELECT * FROM remont ORDER BY id").fetchall()
    if not rows:
        print("Таблица пуста.")
        return
    header = f"{'ID':>4} | {'Марка':<18} | {'Завод':<20} | {'Цена':>8} | " \
             f"{'Дата':>12} | {'Документ':>9} | {'Мастер':<15} | {'Сумма':>8}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r[0]:>4} | {r[1]:<18} | {r[2]:<20} | {r[3]:>8.0f} | "
            f"{r[4]:>12} | {r[5]:>9} | {r[6]:<15} | {r[7]:>8.0f}"
        )


# ──────────────────────────────────────────────
# ПОИСК (3 варианта SQL-запроса)
# ──────────────────────────────────────────────

def search_by_master(master_name):
    """Поиск 1: все записи по имени мастера."""
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT * FROM remont WHERE master = ?", (master_name,)
        ).fetchall()
    return rows


def search_by_date_range(date_from, date_to):
    """Поиск 2: записи за период (дата_от — дата_до)."""
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT * FROM remont WHERE data_remonta BETWEEN ? AND ?",
            (date_from, date_to),
        ).fetchall()
    return rows


def search_by_min_summa(min_summa):
    """Поиск 3: записи с суммой оплаты >= min_summa."""
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT * FROM remont WHERE summa >= ? ORDER BY summa DESC",
            (min_summa,),
        ).fetchall()
    return rows


# ──────────────────────────────────────────────
# УДАЛЕНИЕ (3 варианта SQL-запроса)
# ──────────────────────────────────────────────

def delete_by_id(record_id):
    """Удаление 1: по первичному ключу."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM remont WHERE id = ?", (record_id,))
        conn.commit()
    print(f"Запись с ID={record_id} удалена.")


def delete_by_master(master_name):
    """Удаление 2: все записи указанного мастера."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute(
            "DELETE FROM remont WHERE master = ?", (master_name,)
        )
        conn.commit()
    print(f"Удалено записей мастера «{master_name}»: {cur.rowcount}.")


def delete_by_date(date_before):
    """Удаление 3: записи до указанной даты."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute(
            "DELETE FROM remont WHERE data_remonta < ?", (date_before,)
        )
        conn.commit()
    print(f"Удалено записей ранее {date_before}: {cur.rowcount}.")


# ──────────────────────────────────────────────
# РЕДАКТИРОВАНИЕ (3 варианта SQL-запроса)
# ──────────────────────────────────────────────

def update_summa_by_id(record_id, new_summa):
    """Редактирование 1: изменить сумму оплаты по ID."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "UPDATE remont SET summa = ? WHERE id = ?",
            (new_summa, record_id),
        )
        conn.commit()
    print(f"Сумма оплаты записи ID={record_id} изменена на {new_summa}.")


def update_master_by_id(record_id, new_master):
    """Редактирование 2: изменить мастера по ID."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "UPDATE remont SET master = ? WHERE id = ?",
            (new_master, record_id),
        )
        conn.commit()
    print(f"Мастер записи ID={record_id} изменён на «{new_master}».")


def update_cena_for_zavod(zavod, new_cena):
    """Редактирование 3: изменить цену для всех телевизоров указанного завода."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute(
            "UPDATE remont SET cena = ? WHERE zavod = ?",
            (new_cena, zavod),
        )
        conn.commit()
    print(f"Цена для завода «{zavod}» обновлена на {new_cena}. Записей: {cur.rowcount}.")


# ──────────────────────────────────────────────
# Консольное меню
# ──────────────────────────────────────────────

def menu():
    init_db()

    while True:
        print("\n=== ТЕЛЕМАСТЕРСКАЯ ===")
        print("1. Показать все записи")
        print("2. Заполнить 10 тестовых записей")
        print("3. Добавить запись вручную")
        print("4. Поиск")
        print("5. Удаление")
        print("6. Редактирование")
        print("0. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            print_all()

        elif choice == "2":
            fill_sample_data()

        elif choice == "3":
            try:
                marka = input("Марка телевизора: ").strip()
                zavod = input("Завод-изготовитель: ").strip()
                cena = float(input("Цена: "))
                data_r = input("Дата ремонта (ГГГГ-ММ-ДД): ").strip()
                dok = input("Документ: ").strip()
                master = input("Мастер: ").strip()
                summa = float(input("Сумма оплаты: "))
                insert_record(marka, zavod, cena, data_r, dok, master, summa)
                print("Запись добавлена.")
            except ValueError:
                print("Ошибка ввода данных.")

        elif choice == "4":
            print("  4.1 — по мастеру")
            print("  4.2 — по диапазону дат")
            print("  4.3 — по минимальной сумме")
            sub = input("  Выбор: ").strip()
            if sub == "4.1":
                m = input("Имя мастера: ").strip()
                rows = search_by_master(m)
            elif sub == "4.2":
                d1 = input("Дата от (ГГГГ-ММ-ДД): ").strip()
                d2 = input("Дата до (ГГГГ-ММ-ДД): ").strip()
                rows = search_by_date_range(d1, d2)
            elif sub == "4.3":
                try:
                    s = float(input("Минимальная сумма: "))
                    rows = search_by_min_summa(s)
                except ValueError:
                    print("Ошибка.")
                    continue
            else:
                print("Неверный выбор.")
                continue
            if rows:
                for r in rows:
                    print(r)
            else:
                print("Ничего не найдено.")

        elif choice == "5":
            print("  5.1 — по ID")
            print("  5.2 — все записи мастера")
            print("  5.3 — записи ранее даты")
            sub = input("  Выбор: ").strip()
            if sub == "5.1":
                try:
                    delete_by_id(int(input("ID: ")))
                except ValueError:
                    print("Ошибка.")
            elif sub == "5.2":
                delete_by_master(input("Имя мастера: ").strip())
            elif sub == "5.3":
                delete_by_date(input("Дата (ГГГГ-ММ-ДД): ").strip())
            else:
                print("Неверный выбор.")

        elif choice == "6":
            print("  6.1 — изменить сумму оплаты по ID")
            print("  6.2 — изменить мастера по ID")
            print("  6.3 — изменить цену для всех записей завода")
            sub = input("  Выбор: ").strip()
            if sub == "6.1":
                try:
                    update_summa_by_id(
                        int(input("ID: ")),
                        float(input("Новая сумма: ")),
                    )
                except ValueError:
                    print("Ошибка.")
            elif sub == "6.2":
                try:
                    update_master_by_id(
                        int(input("ID: ")),
                        input("Новый мастер: ").strip(),
                    )
                except ValueError:
                    print("Ошибка.")
            elif sub == "6.3":
                try:
                    update_cena_for_zavod(
                        input("Название завода: ").strip(),
                        float(input("Новая цена: ")),
                    )
                except ValueError:
                    print("Ошибка.")
            else:
                print("Неверный выбор.")

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    menu()
