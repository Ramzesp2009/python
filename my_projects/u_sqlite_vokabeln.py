import os, sys, sqlite3, random

random.seed()


def menu():
    while True:
        try:
            menu = int(input("Ihre Auswahl: 0 (= Ende), 1 (= Alle), "
                             "2 (= Lernen), 3 (= Test):"))
        except:
            continue
        if menu == 0:
            break
        elif menu == 1:
            anzeige_liste(lists)
        elif menu == 2:
            lernen(lists)
        elif menu == 3:
            prufen(lists)
        else:
            print("Falsche Wahl.")


def zeigen():
    lists = []
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM vokabeln"
    cursor.execute(sql)
    for dsatz in cursor:
        lists.append([dsatz[0], dsatz[1], dsatz[2]])
    connection.close()
    return lists


def anzeige_liste(lists):
    for i in lists:
        print(i[0], "/", i[1], "/", i[2])


def data_base():
    lists = [[1, "Bedingung", "condition"],
          [2, "suchen", "to look for"],
          [3, "Werbeanzeige", "advertisement"],
          [4, "abkürzen", "to abbreviate"],
          [5, "nützlich", "useful"],
          [6, "Wirkung", "effect"],
          [7, "beraten", "to advise"],
          [8, "übersetzen", "to translate"],
          [9, "einfach", "easy"],
          [10, "ankündigen", "to announce"]]
    connection = sqlite3.connect("lernen.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE vokabeln(id INTEGER PRIMARY KEY, deutsch TEXT, english TEXT)"
    for list in lists:
        sql = "INSERT INTO vokabeln VALUES(" + str(list[0]) + ", '" + list[1] + "', '" + list[2] + "')"
        cursor.execute(sql)
        connection.commit()
    connection.close()
    return lists


def lernen(lists):
    z = random.choice(lists)
    print(z[1], "/", z[2])


def prufen(lists):
    while(lists):
        x = random.randint(0, len(lists)-1)
        answer = input(f"Bitte ubersetzen {lists[x][1]} ==> ")
        if answer == lists[x][2]:
            print("Richtig, Vokabel wird aus dem Test genommen")
            del lists[x]
        else:
            print("Leider falsch, richtig ware:", lists[x][2])
    print("Test erfolgreich beendet")


if not os.path.exists("lernen.db"):
    lists = data_base()
else:
    lists = zeigen()


menu()
