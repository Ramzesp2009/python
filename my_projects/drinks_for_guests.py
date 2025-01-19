def create_greeting(friend_name, favorite_drink):
    print(f"Hello {friend_name}, I hope you are having a wonderful day! Would you like a glass of {favorite_drink}?")

name_input = input().title()
drink_input = input().title()

create_greeting(name_input, drink_input)

# name, drink = input().capitalize(), input().capitalize
# print(f"Hello {name}, I hope you are having a wonderful day! Would you like a glass of {drink}?")