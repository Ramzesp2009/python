import string, secrets

li = []
for i in range(5):
    li.append(secrets.randbelow(50) + 1)
print("Zehnmal wurfeln:", li)

tx = ""
for i in range(10):
    tx += secrets.choice(string.ascii_lowercase)
print("Text mit zehn zufalligen kleinen Bucgstaben:", tx)
