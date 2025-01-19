import secrets, string

print(string.ascii_letters)
print()
print(string.ascii_lowercase)
print()
print(string.ascii_uppercase)
print()
print(string.digits)
print()
print(string.punctuation)
all_chars = string.ascii_letters + string.digits + string.punctuation
password = [''.join(secrets.choice(all_chars) for i in range(15))]
print(password)
