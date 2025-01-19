first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard", "husband's sister": "Isabelle"}
# new_family = first_family | second_family
# new_family = first_family.update(second_family)
# print(new_family)
print(first_family | second_family)