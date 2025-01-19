zahl_list = [1, 2, 3, 4, 5]
zweite_list = zahl_list.copy()
print(zahl_list)
print(zweite_list)
zweite_list.append(6)
print(zahl_list)
print(zweite_list)
print(zahl_list.count(1))
new_list = [1, 1, 1, 1]
zahl_list.extend(new_list)
print(zahl_list)
print(zahl_list.count(1))
print(zweite_list)
