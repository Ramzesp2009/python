# Задаємо початкові дані
rooms = [
    [99, 'W', 0, 99],
    [99, 99, 99, 'W'],
    [99, 'W', 99, 'W'],
    [0, 'W', 99, 99]
]
empty_room = 99
gate = 0
empty_room_liste = []
one_liste = []


# Функція для оновлення кімнати
def update_room(y, x, value):
    # Перевірка чи можна змінити кімнату (тільки якщо значення клітини == empty_room)
    if 0 <= y < len(rooms) and 0 <= x < len(rooms[0]) and rooms[y][x] == empty_room:
        rooms[y][x] = value


# Збираємо локації воріт (0)
for y, room in enumerate(rooms):
    for x, cell in enumerate(room):
        if cell == gate:
            one_liste.append([y, x])

updated_positions = []
count = 0
# Функція для обробки воріт
while True:
    count += 1

    if one_liste:
        for y, x in one_liste:
            # Перевірка навколишніх клітин і оновлення
            if y < 3 and rooms[y + 1][x] == empty_room:  # Перевірка клітинки знизу
                update_room(y + 1, x, count)
                updated_positions.append([y + 1, x])
            if y > 0 and rooms[y - 1][x] == empty_room:  # Перевірка клітинки зверху
                update_room(y - 1, x, count)
                updated_positions.append([y - 1, x])
            if x < 3 and rooms[y][x + 1] == empty_room:  # Перевірка клітинки справа
                update_room(y, x + 1, count)
                updated_positions.append([y, x + 1])
            if x > 0 and rooms[y][x - 1] == empty_room:  # Перевірка клітинки зліва
                update_room(y, x - 1, count)
                updated_positions.append([y, x - 1])
        one_liste = updated_positions
        updated_positions.clear()
    else:
        break
    # for y, room in enumerate(rooms):
    #     for x, cell in enumerate(room):
    #         if cell == empty_room:
    #             one_liste.append([y, x])

for room in rooms:
    print(room)  # Перевірка результату
