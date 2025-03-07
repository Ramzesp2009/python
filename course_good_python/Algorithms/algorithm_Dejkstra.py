import math


def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i


def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin


D = (
    (0, 3, 1, 3, 0, 0),
    (3, 0, 4, 0, 0, 0),
    (1, 4, 0, 0, 7, 5),
    (3, 0, 0, 0, 0, 2),
    (0, 0, 7, 0, 0, 4),
    (0, 0, 5, 2, 4, 0),
)

N = len(D)              # кількість вершин
T = [math.inf]*N        # останній рядок таблички

v = 0                   # початкова вершина
S = {v}                 # множина відвіданих вершин
T[v] = 0                # вартість початкової вершини

while v != -1:                      # поки не відвідаємо всі вершини
    for j in get_link_v(v, D):      # перебираємо всі сусідні вершини
        if j not in S:              # якщо вершина не відвідана
            w = T[v] + D[v][j]
            if w < T[j]:
                T[j] = w

    v = arg_min(T, S)               # вибираємо найближчу вершину
    if v > 0:                       # якщо відвідаємо вершину
        S.add(v)                    # додаємо відвідану вершину

print(T)

