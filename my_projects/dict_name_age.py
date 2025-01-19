dict_age_name = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
def get_age(name):
    print(dict_age_name[name] if name in dict_age_name else "Not found")

get_age(input())