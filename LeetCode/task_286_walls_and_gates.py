rooms = [[0,  'W',  'G',   0, 0],
         [0,   0,   0,  'W', 0],
         [0,  'W',  0,  'W', 'W'],
         ['G','W',  0,  0, 0],
         [0,   0, 'W', 0, 'W']]
gate = 'G'
empty_room = 0
gate_liste = []
min_size = 0
max_size = len(rooms) - 1
count = 0
for y, room in enumerate(rooms):
    for x, cell in enumerate(room):
        if cell == 'G':
            gate_liste.append([y, x])


def y_up(y):
    y -= 1
    return y

def y_down(y):
    y += 1
    return y

def x_right(x):
    x += 1
    return x

def x_left(x):
    x -= 1
    return x

def search_empty_rooms(rooms):
    empty_rooms_liste = []
    for y, room in enumerate(rooms):
        for x, cell in enumerate(room):
            if rooms[y][x] == count:
                empty_rooms_liste.append([y, x])
    return empty_rooms_liste

while True:
    count += 1
    for y, x in gate_liste:
        if y < max_size:
            if rooms[y_down(y)][x] == empty_room:
                rooms[y_down(y)][x] = count
        if y > min_size:
            if rooms[y_up(y)][x] == empty_room:
                rooms[y_up(y)][x] = count
        if x < max_size:
            if rooms[y][x_right(x)] == empty_room:
                rooms[y][x_right(x)] = count
        if x > min_size:
            if rooms[y][x_left(x)] == empty_room:
                rooms[y][x_left(x)] = count
    gate_liste = search_empty_rooms(rooms)
    if gate_liste:
        continue
    else:
        break


for room in rooms:
    print(room)

# antwort = [[3, 'W', 'G', 1],
#           [2, 2, 1, 'W'],
#           [1, 'W', 2, 'W'],
#           ['G', 'W', 3, 4]]"""