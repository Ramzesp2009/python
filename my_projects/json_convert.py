import json

# json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'
#
# sneakers = json.loads(json_str)
#
# json_from_dict = json.dumps(sneakers, indent=1)
#
# print(json_from_dict)
# print(type(json_from_dict))

my_dictionary = {
    'a': 1,
    'b': (1, 2, 3),
    3: 'abc',
    'bool': (True, False, True),
    'None': None
}
json_dict = json.dumps(my_dictionary, indent=2)
print(json_dict)
print(type(json_dict))
converted_json = json.loads(json_dict)
print(converted_json)