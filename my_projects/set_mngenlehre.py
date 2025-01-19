st = {8, 15, "x"}
su = {4, "x", "abc", 15}
print("Type st:", type(st))
print("st:", st)
print("Type su:", type(su))
print("su:", su)

print("Vereinigungsmenge:", st | su)
print("Schnittmenge:", st & su)
print("Differenzmenge st - su:", st - su)
print("Differenzmenge su - st:", su - st)
print("Summetrische Differenzmenge:", st ^ su)