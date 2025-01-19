from get_all_users import get_all_users
from save_user import save_user
from update_user import update_user
from delete_user import delete_user


def main_menu():
    while True:
        print("\nHauptmenu:")
        print("1: Mitglieder liste lesen")
        print("2: Mitglieder hinzufugen")
        print("3: Mitglieder bearbeiten")
        print("4: Mitglieder entfernen")
        print("5: Beenden")

        choice = input("Wahle eine Option: ")

        if choice == "1":
            users = get_all_users()
            print_users(users)
        elif choice == "2":
            users = get_all_users()
            save_user(users)
        elif choice == "3":
            users = get_all_users()
            update_user(users)
        elif choice == "4":
            users = get_all_users()
            delete_user(users)
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungultige Eingabe, Bitte erneut versuchen.")


def print_users(users):
    if not users:
        print("Keine Mitglieder gefunden.")
    else:
        for user in users:
            print(f"Name: {user['name']}, Alter: {user['alter']}, "
                  f"Email: {user['email']}, Hobby: {user['hobby']}")


if __name__ == '__main__':
    main_menu()
