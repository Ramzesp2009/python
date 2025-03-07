import math

def get_path(p, end, start):
    path = [end]
    while end != start:
        end = P[end][start]
        path.append(end)
    return path

V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]]

n = len(V)

P = [[v for v in range(n)] for u in range(n)]

# Floyd's algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

start = 1
end = 4

print(get_path(P, end, start))