file = open('../my_file.txt', encoding='utf-8')

# print(file.read(4))
# file.seek(0)
# print(file.read(4))
# pos = file.tell()
# print(pos)
# print(file.readline(), end='')
# print(file.readline(), end='')

for line in file:
    print(line, end='')

# s = file.readlines()
# print(s)

file.close()