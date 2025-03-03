t = "mimika"
p = [0] * len(t)
j = 0
i = 1
while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        j += 1
        i += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = j - 1

print(p)
