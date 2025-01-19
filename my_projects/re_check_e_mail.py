import re

def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_patern = re.compile(email_regexp)
    validation_result = "valid" if email_check_patern.fullmatch(email) else "invalid"
    return (email, validation_result)

# Valid
print(check_email('bs@gmail.com'))
print(check_email('bs@sub.gmail.com'))
print(check_email('bs_@gmail.com'))
print(check_email('bs.@gmail.com'))
# Invalid
print(check_email('bs@gmail.'))
print(check_email('bsgmail.com'))
print(check_email('bs@gmailcom'))
print(check_email('@gmail.com'))