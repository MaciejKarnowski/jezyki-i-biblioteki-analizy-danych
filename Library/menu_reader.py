from menu import menu
from menu_librarian import menu_browse
from datetime import date, timedelta


def menu_reader():
    return menu({
        "Wypożycz": (borrow, (), {}),
        "Prolonguj": (prolong, (), {}),
        "Zarezerwuj": (reserve, (), {}),
        "Przeglądaj katalog": (menu_browse, (), {}),
        "Wyjdź": (exit, (1,), {})
    })


def borrow():
    book = input("Tytuł książki: ")
    z = 0
    to_replace_with = []
    with open("ksiazki.txt", 'r', encoding="windows-1250") as file:
        data = file.readlines()
    for i in range(len(data)):
        spec_line = data[i].split(sep=';')
        if spec_line[0] == book:
            if spec_line[3].replace("\n", "") != str(0):
                print("Book currently on rent, try to reserve")
                while True:
                    menu_reader()
            spec_line[2] = str(date.today() + timedelta(days=14))
            to_replace_with = spec_line
            z = i

    data[z] = ";".join(to_replace_with)
    if to_replace_with:
        with open("ksiazki.txt", 'w', encoding="windows-1250") as file:
            file.writelines(data)
    else:
        print("książki nie ma w bibliotece")


def prolong():
    book = input("Tytuł książki: ")
    z = 0
    to_replace_with = []
    with open("ksiazki.txt", 'r', encoding="windows-1250") as file:
        data = file.readlines()
    for i in range(len(data)):
        spec_line = data[i].split(sep=';')
        if spec_line[0] == book:
            if spec_line[3].replace("\n", "") != str(0):
                print("book already reserved, better luck next time")
                while True:
                    menu_reader()
            spec_line[2] = str(date.today() + timedelta(days=14)) + "\n"
            to_replace_with = spec_line
            z = i

    data[z] = ";".join(to_replace_with)
    if to_replace_with:
        with open("ksiazki.txt", 'w', encoding="windows-1250") as file:
            file.writelines(data)
    else:
        print("książki nie ma w bibliotece")


def reserve():
    book = input("Tytuł książki: ")
    z = 0
    to_replace_with = []
    with open("ksiazki.txt", 'r', encoding="windows-1250") as file:
        data = file.readlines()
    for i in range(len(data)):
        spec_line = data[i].split(sep=';')
        if spec_line[0] == book:
            if spec_line[3].replace("\n", "") != str(0):
                print("book already reserved, better luck next time")
                while True:
                    menu_reader()
            elif spec_line[2] == str(0):
                print("book is avaiable to rent now")
                while True:
                    menu_reader()
            spec_line[3] = "reserved\n"
            to_replace_with = spec_line
            z = i

    data[z] = ";".join(to_replace_with)
    if to_replace_with:
        with open("ksiazki.txt", 'w', encoding="windows-1250") as file:
            file.writelines(data)
    else:
        print("książki nie ma w bibliotece")
