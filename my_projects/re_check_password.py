import re

def check_password(key_word):
    length_pattern = re.compile(r"\S{8,}")  # for checking length of password
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, key_word):
        return (False, "No whitespaces allow in the password")

    if not re.fullmatch(length_pattern, key_word):
        return (False, "Password must have at least 8 symbol")

    if not re.fullmatch(lowercase_pattern, key_word):
        return (False, "Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, key_word):
        return (False, "Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, key_word):
        return (False, "Password must have at least one number")

    if not re.fullmatch(special_symbol_pattern, key_word):
        return (False, "Password must have at least one special symbol @%#!&*^")

    return (True, "Password is valid!")


while True:
    keyword = input("Please enter password:    ")
    password_check_result = check_password(keyword)
    if password_check_result[0]:
        print(password_check_result[1])
        break
    print(password_check_result[1])

# The second variant

'''def check_password(key_word):
    massege_for_user = []
    length_pattern = re.compile(r"\S{8,}")  # for checking length of password
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, key_word):
        massege_for_user.append("No whitespaces allow in the password")

    if not re.fullmatch(length_pattern, key_word):
        massege_for_user.append("Password must have at least 8 symbol")

    if not re.fullmatch(lowercase_pattern, key_word):
        massege_for_user.append("Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, key_word):
        massege_for_user.append("Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, key_word):
        massege_for_user.append("Password must have at least one number")

    if not re.fullmatch(special_symbol_pattern, key_word):
        massege_for_user.append("Password must have at least one special symbol @%#!&*^")
    if len(massege_for_user) == 0:
        return ("Password is valid!")
    else:
        return massege_for_user


while True:
    keyword = input("Please enter password:    ")
    password_check_result = check_password(keyword)
    if password_check_result == "Password is valid!":
        print(password_check_result)
        break
    print(password_check_result)'''






