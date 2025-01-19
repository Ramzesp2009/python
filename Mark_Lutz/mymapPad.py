def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


def mymapPad_2(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


S1, S2 = 'abc', 'xyz123'
print(mymapPad_2(S1, S2))
print(mymapPad_2(S1, S2, pad=99))