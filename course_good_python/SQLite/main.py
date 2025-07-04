import sqlite3 as sq


cars = [
    ('Audi', 52642),
    ('Mersedes', 51127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('BMW', 32134),
]

with sq.connect("saper.db") as con:
    cur = con.cursor()

    # cur.execute("""DROP TABLE IF EXISTS users""")

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        )""")

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    

