#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_man():
    """
    Запросить данные о товаре.
    """

    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    dateString = input("Дата: ")

    # Создать словарь.
    return {
        'name': name,
        'zodiac': zodiac,
        'dateString': dateString,
    }


def display_names(mans):
    """
    Отобразить список людей.
    """
    print(mans)
    # Проверить, что список людей не пуст.
    if mans:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Знак зодиака",
                "Дата"
            )
        )
        print(line)
        # Вывести данные о всех людях.
        for idx, man in enumerate(mans, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    man.get('name', ''),
                    man.get('zodiac', ''),
                    man.get('dateString', '')
                )
            )
        print(line)

    else:
        print("Список людей пуст.")


def main():
    """
    Главная функция программы.
    """

    # Список людей.
    mans = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            man = get_man()

            # Добавить словарь в список.
            mans.append(man)
            # Отсортировать список в случае необходимости.
            if len(mans) > 1:
                mans.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Отобразить всех людей.
            display_names(mans)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
