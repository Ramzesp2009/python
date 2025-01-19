def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x

seq = list(range(10))
p1 = permute2(seq)
print(next(p1))
print(next(p1))
print(next(p1))