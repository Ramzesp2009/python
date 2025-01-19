# def open_file():
#     try:
#         datei = open("./dateien/test.txt", 'r')
#         inhalt = datei.read()
#         datei.close()
#
#     except FileNotFoundError as e:
#         print('FileNotFoundError', e)
#     else:
#         print(inhalt)
#
#
# open_file()


def open_file():
    try:
        with open("./test.txt", "w+") as datei:
            datei.write("The first comment")
            inhalt = datei.read()
            print(inhalt)

    except FileNotFoundError:
        print("ERROR")
    else:
        print("Everything was read")


open_file()
