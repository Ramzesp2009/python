# def connect_db(connect: dict) -> str:
#     match connect:
#         case {'server': host, 'login': login, 'password': psw, 'port': port}:
#             pass
#         case {'server': host, 'login': login, 'password': psw}:
#             port = 22
#         case _:
#             return "error connction"
#
#     return f"connection: {host}@{login}.{psw}:{port}"
#
# request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234', 'port': 8000}
#
# result = connect_db(request)
# print(result)

book_1 = ('Romazan', 'Python', 2022)
book_2 = ['Romazan', 'Python 2', 2022, 199.99]
book_3 = {'author': 'Romazan', 'title': 'Deeplearning with Python', 'year': 2024}
book_4 = {'author': 'Romazan', 'title': 'Python part 2', 'price': 249.99, 'year': 2024}

def book_to_tuple(data: dict | tuple | list, min_year=1800, max_year=2025) -> tuple | None:
    price = None
    match data:
        case author, title, year:
            pass
        case author, title, year, price, *_:
            pass
        case {'author': author, 'title': title, 'year': year, 'price': price}:
            pass
        case {'author': author, 'title': title, 'year': year}:
            pass
        case _: # wildcard
            return None

    if not (min_year < year < max_year):
        return None

    return author, title, year, price


res = book_to_tuple(book_1)
print('case 1', res)
res = book_to_tuple(book_2)
print('case 2', res)
res = book_to_tuple(book_3)
print('case 3', res)
res = book_to_tuple(book_4)
print('case 4', res)




