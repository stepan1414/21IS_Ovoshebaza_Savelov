from db import init_db
from services import *
from reports import *

def menu():
    print("\n===== ОВОЩЕБАЗА =====")
    print("1. Сотрудники")
    print("2. Склады")
    print("3. Товары")
    print("4. Поставщики")
    print("5. Поставки")
    print("0. Выход")


def employees_menu():
    while True:
        print("\n1.Показать 2.Добавить 3.Изм 4.Удалить 0.Назад")
        c = input("-> ")

        if c == "1":
            show_employees()

        elif c == "2":
            add_employee(input("Имя: "), int(input("Склад ID: ")))

        elif c == "3":
            update_employee(int(input("ID: ")), input("Имя: "), int(input("Склад: ")))

        elif c == "4":
            delete_employee(int(input("ID: ")))

        elif c == "0":
            break


def warehouses_menu():
    while True:
        print("\n1.Показать 2.Добавить 3.Удалить 0.Назад")
        c = input("-> ")

        if c == "1":
            show_warehouses()

        elif c == "2":
            add_warehouse(input("Название: "), input("Город: "))

        elif c == "3":
            delete_warehouse(int(input("ID: ")))

        elif c == "0":
            break


def products_menu():
    while True:
        print("\n1.Показать 2.Добавить 0.Назад")
        c = input("-> ")

        if c == "1":
            show_products()

        elif c == "2":
            add_product(input("Название: "), input("Ед: "))

        elif c == "0":
            break


def suppliers_menu():
    while True:
        print("\n1.Показать 2.Добавить 0.Назад")
        c = input("-> ")

        if c == "1":
            show_suppliers()

        elif c == "2":
            add_supplier(input("Имя: "), input("Тел: "))

        elif c == "0":
            break


def deliveries_menu():
    while True:
        print("\n1.Показать 2.Добавить 0.Назад")
        c = input("-> ")

        if c == "1":
            show_deliveries()

        elif c == "2":
            add_delivery(
                int(input("Товар ID: ")),
                int(input("Поставщик ID: ")),
                int(input("Склад ID: ")),
                int(input("Кол-во: ")),
                input("Дата: ")
            )

        elif c == "0":
            break


def main():
    init_db()

    while True:
        menu()
        c = input("Выбор: ")

        if c == "1":
            employees_menu()
        elif c == "2":
            warehouses_menu()
        elif c == "3":
            products_menu()
        elif c == "4":
            suppliers_menu()
        elif c == "5":
            deliveries_menu()
        elif c == "0":
            break


if __name__ == "__main__":
    main()