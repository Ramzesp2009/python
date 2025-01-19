st = "Hallo"
print(st, type(st))

by = b"Hallo"
print(by, type(by))

by = bytes("hallo", "UTF-8")
print(by, type(by))

by = b'Hallo'
st = by.decode()
print(st, type(st))