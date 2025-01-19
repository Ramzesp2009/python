# Funktion rechnung des Steuers


def steuer(x):
#  return gehalt * 0.22 if gehalt > 2500 else gehalt * 0.18
    if x > 2500:
        sum_of_steuer = x * 0.22
    else:
        sum_of_steuer = x * 0.18
    return sum_of_steuer

# Klasse steuer


# def class_steuer(gehalt):
#     if gehalt > 2500:
#         procent = 22
#     else:
#         procent = 18
#     return procent

# Program rechnung des Steuers


gehalt = int(input("Bitte geben Sie Ihre Gehalt ein: "))
print(f"Gehalt ist {gehalt} dann Steuer wird {class_steuer(gehalt)}% also {steuer(gehalt)}Euro")