user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23,
}

def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

# print(user_info(user_profile['name'], user_profile['comments_qty']))
# print(user_info(name=user_profile['name'], comments_qty=user_profile['comments_qty']))

print(user_info(**user_profile))

# name, com = user_profile

# print(name)
# print(com)

user_data = ['Bogdan', 23]

def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(user_info(name=user_data[0], comments_qty=user_data[1]))

print(user_info(*user_data))

my_name, my_qty = user_data
print(my_name, my_qty)

my_list_auto = [
    {'marke': 'Volvo', 'model': 'V40'},
    {'marke': 'Audi', 'model': 'Q7'},
    {'marke': 'Porsche', 'model': '911'}
]

one_list, two_list, three_list = my_list_auto

def unpacking_function(marke, model):
    return f"I like {marke} model {model}"

print(unpacking_function(**one_list))
print(unpacking_function(**two_list))
print(unpacking_function(**three_list))