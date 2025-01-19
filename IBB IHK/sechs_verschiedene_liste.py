# erstellen anhand constructor verschiedene liste
integer_list = [i for i in range(1, 11)]
print(integer_list)
print(type(integer_list))

float_list = [i * 1.0 for i in range(1, 11)]
print(float_list)
print(type(float_list))

string_list = ["Some_string"] * 10
print(string_list)
print(type(string_list))

tuple_list = tuple([i for i in range(1, 11)])
print(tuple_list)
print(type(tuple_list))

dictionary_list = {x: x * 5 for x in range(1, 11)}
print(dictionary_list)
print(type(dictionary_list))

# erstellen ein set mange
set_list = {1, 1, 2, 2, 3, 3, 4, 5, 5, 4, 6, 6, 7, 8, 9, 9, 7, 8, 0, 0}
print(set_list)
print(type(set_list))