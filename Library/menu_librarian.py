from menu import menu
import os
import json
import csv


def menu_librarian():
    return menu({
        "Przyjmij zwrot książki": (accept_return, (), {}),
        "Dodaj książkę": (add_book, (), {}),
        "Usuń książkę": (delete_book, (), {}),
        "Dodaj czytelnika": (add_user, (), {}),
        "Przeglądaj katalog": (menu_browse, (), {}),
        "Wyjdź": (exit, (1,), {})
    })


def create_databse_if_not_exists():
    ksiazki = ["Moby Dick", "Herman Melville", "0", "0"]
    if not os.path.isfile("ksiazki.txt") or os.stat("ksiazki.txt").st_size == 0:
        with open("ksiazki.txt", 'r') as out:
            out.write(";".join(ksiazki))


def accept_return():
    book = input("Tytuł książki: ")
    z = 0
    to_replace_with = []
    with open("ksiazki.txt", 'r', encoding="windows-1250") as file:
        data = file.readlines()
    for i in range(len(data)):
        spec_line = data[i].split(sep=';')
        if spec_line[0] == book:
            spec_line[2] = '0'
            to_replace_with = spec_line
            z = i
    data[z] = ";".join(to_replace_with)
    if to_replace_with:
        with open("ksiazki.txt", 'w', encoding="windows-1250") as file:
            file.writelines(data)


def add_book():
    book = input("Wpisz nazwe książki: ")
    author = input("Wpisz autora książki: ")
    ksiazka = [book, author, "0", "0"]
    with open("ksiazki.txt", 'a', encoding="windows-1250") as out:
        out.write("\n")
        out.write(";".join(ksiazka))
    pass


def delete_book():
    book = input("Tytuł książki: ")
    z = 0
    to_replace_with = []
    with open("ksiazki.txt", 'r', encoding="windows-1250") as file:
        data = file.readlines()
    for i in range(len(data)):
        spec_line = data[i].split(sep=';')
        if spec_line[0] == book:
            spec_line[2] = '0'
            to_replace_with = spec_line
            z = i
    data[z] = ''
    if to_replace_with:
        with open("ksiazki.txt", 'w', encoding="windows-1250") as file:
            file.writelines(data)


def add_user():
    with open("login.json", 'r+') as f:
        data = json.load(f)
        login = input("Enter login: ")
        while login in data["user"][0] or login == 'q':
            login = input("Login already exists\nEnter login: ")
            if login == 'q':
                exit()
        while True:
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
            if password == confirm_password and password != 'q':
                data["user"][0].update({login: password})
                print(data)
                f.seek(0)
                return json.dump(data, f, indent=4)
            elif password == 'q' or confirm_password == 'q':
                exit()
            else:
                print("passwords don't match, try again")


def menu_browse():
    menu({
        "tytuł": (browse_cat, ([1]), {}),
        "autor": (browse_cat, ([2]), {}),
        "słowo klucz": (browse_cat, ([3]), {}),
        "cały katalog": (browse_cat, ([4]), {}),
        "Wyjdź": (exit, (1,), {})
    })


def browse_cat(n):
    if n == 1:
        klucz = input("wpisz tytuł po jakim chcesz wyszukać: ")
        with open("ksiazki.txt") as file:
            data = [column for column in csv.reader(file, delimiter=';')]
            file.seek(0)
            title = [column[0] for column in csv.reader(file, delimiter=';')]
            for i in range(len(data)):
                if klucz in title[i]:
                    print(data[i])
    if n == 2:
        klucz = input("wpisz autora po jakim chcesz wyszukać: ")
        with open("ksiazki.txt") as file:
            data = [column for column in csv.reader(file, delimiter=';')]
            file.seek(0)
            author = [column[1] for column in csv.reader(file, delimiter=';')]
            for i in range(len(data)):
                if klucz in author[i]:
                    print(data[i])
    if n == 3:
        klucz = input("wpisz słowo klucz po jakim chcesz wyszukać: ")
        print(klucz)
        with open("ksiazki.txt") as file:
            data = [column for column in csv.reader(file, delimiter=';')]
            file.seek(0)
            title = [column[0] for column in csv.reader(file, delimiter=';')]
            file.seek(0)
            author = [column[1] for column in csv.reader(file, delimiter=';')]
            for i in range(len(data)):
                if klucz in author[i] or klucz in title[i]:
                    print(data[i])
    if n == 4:
        with open("ksiazki.txt") as file:
            data = [column for column in csv.reader(file, delimiter=';')]
            for i in range(len(data)):
                print(data[i])
