import json
from menu_reader import menu_reader
from menu_librarian import menu_librarian
from menu import menu
import os


def start():
    base = {
        "user": [{"maciek": "maciek1"}],
        "admin": [{"admin": "admin"}]
    }
    if not os.path.isfile("login.json") or os.stat("login.json").st_size == 0:
        with open("login.json", "w") as outfile:
            json.dump(base, outfile,
                      indent=4)


def login(file, user_type):
    attempts = 3
    with open(file) as lf:
        data = json.load(lf)[user_type][0]
        login = input("Enter login: ")
        while login not in data:
            login = input("login not in database, try again or press q to quit:\n")
            if login == 'q':
                exit()
        while True:
            password = input("Enter password: ")
            if password == 'q':
                break
            elif data[login] != password and attempts != 0:
                print(f"wrong password \nremaining attempts: {attempts}")
                attempts -= 1
            elif data[login] == password:
                print(f"Welcome {login}")
                if user_type == "admin":
                    while True:
                        menu_librarian()
                else:
                    while True:
                        menu_reader()
            else:
                print("login failed")
                break


def signup(file, user_type):
    with open(file, 'r+') as f:
        data = json.load(f)
        login = input("Enter login: ")
        while login in data[user_type][0] or login == 'q':
            login = input("Login already exists\nEnter login: ")
            if login == 'q':
                exit()
        while True:
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
            if password == confirm_password and password != 'q':
                data[user_type][0].update({login: password})
                f.seek(0)
                return json.dump(data, f, indent=4)
            elif password == 'q' or confirm_password == 'q':
                exit()
            else:
                print("passwords don't match, try again")


def login_menu():
    return menu({
        "Czytlenik": (login, (["login.json", "user"]), {}),
        "Bibliotekarz": (login, (["login.json", "admin"]), {}),
        "Wyjdź": (exit, (1,), {})
    })


def signup_menu():
    return menu({
        "Czytlenik": (signup, (["login.json", "user"]), {}),
        "Bibliotekarz": (signup, (["login.json", "admin"]), {}),
        "Wyjdź": (exit, (1,), {})
    })


def foo():
    pass
