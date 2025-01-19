# request = {'id': 1, 'url': 'https://proproprogs.org', 'method': 'GET', 'timeout': 1000, 'data': '12.12.2002', }
# json_data = {
#     'id': 2,
#     'access': True,
#     'info': [
#         '01.01.2023',
#         {
#             'login': 'user',
#             'email': 'ramzesp2009@gmil.com'
#         },
#         True,
#         2024
#     ]
# }

primaty_keys = {1, 2, 3, 4}


match primaty_keys:
    case set() as keys if len(keys) == 4:
        print(f"Primaty keys {keys}")
    case _:
        print("wrong request")