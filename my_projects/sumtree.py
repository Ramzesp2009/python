tree = [1, [2, [3, 4], 5], 6, [7, 8]]
def sumtree(L):
    tot = 0
    for x in L:
        print(f"print L {L}")
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

# s = sumtree(tree)
# print(s)


def sumtree_2(L):
    tot = 0
    items = list(L)
    while items:
        print(items)
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

# s = sumtree_2(tree)
# print(s)

def sumtree_3(L):
    tot = 0
    items = list(L)
    while items:
        print(items)
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot

s = sumtree_3(tree)
print(s)