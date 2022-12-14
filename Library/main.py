from menu_librarian import menu_librarian, menu, create_databse_if_not_exists
import json
from functions import login, signup, login_menu, signup_menu, start

start()
create_databse_if_not_exists()
# książke mozna wypożyczyć na maksymalnie 14 dni, przedluzenie ksiązki
# polega na odnowieniu 14 dni okresu wypożyczenia
while True:
    menu({
        "Zaloguj sie": (login_menu, (), {}),
        "Zarejestruj sie": (signup_menu, (), {}),
        "Wyjdź": (exit, (1,), {})
    })
