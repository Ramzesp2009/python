try:
    with open('../my_file.txt', encoding='utf-8') as file:
        s = file.readlines()
        # int(s)
        print(s)
    # file = open('my_file.txt', encoding='utf-8')
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("It's impossible the file to open")
except:
    print("Error by working with the file")
finally:
    print(file.closed)