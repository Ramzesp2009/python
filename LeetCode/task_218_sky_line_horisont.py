# buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
buildings = [[2, 9, 11], [3, 10, 13], [5, 12, 12], [12, 20, 13], [19, 24, 8]]
# створюємо пустий словник для кожної координати х і у
buildings_dict = {}
# тимчасовий список
temp_list = []
answer = []
# створюємо список списків
for building in buildings:
    x1 = building[0]
    x2 = building[1]
    y = building[2]
    for x in range(building[0], building[1]+1):
        new_list = [x, y]
        temp_list.append(new_list)
# print(temp_list)

# створюємо словник де кожному х відповідає кількість вершин на горизонті
for x, y in temp_list:
    if x not in buildings_dict:
        buildings_dict[x] = set()
    buildings_dict[x].add(y)


for i in range(buildings[0][0], buildings[-1][1]):
    if i not in buildings_dict:
        buildings_dict[i] = {0}

# print(buildings_dict)
output_list = []
for i in range(buildings[0][0], buildings[-1][1]+1):
    temp_x = i
    temp_y = max(buildings_dict.get(i))
    temp_list = [temp_x, temp_y]
    output_list.append(temp_list)
    # print(buildings_dict.get(i))  # so I get values
    # print(max(buildings_dict.get(i)))  # so I get maximal values from set(i)
# print(output_list)  # I get list with koordinate each x : y
answer.append([output_list[0][0], 0])
answer.append([output_list[0][0], output_list[0][1]])
# print(len(output_list))
for i in range(1, len(output_list)):
    if output_list[i][1] > output_list[i-1][1]:
        x = output_list[i][0]
        y = output_list[i-1][1]
        xy = [x, y]
        answer.append(xy)
        answer.append([output_list[i][0], output_list[i][1]])
    elif output_list[i][1] < output_list[i-1][1]:
        x = output_list[i-1][0]
        y = output_list[i-1][1]
        xy = [x, y]
        answer.append(xy)
        answer.append([output_list[i-1][0], output_list[i][1]])
    elif output_list[i][1] == output_list[i-1][1]:
        continue
# else:
#     answer.append([output_list[-1][0], 0])
answer.append([output_list[-1][0], output_list[-1][1]])
answer.append([output_list[-1][0], 0])

print(answer)