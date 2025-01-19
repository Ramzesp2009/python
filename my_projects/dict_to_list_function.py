def dict_to_list(a_dict):
    lists_tuple = []
    # my solution
    # for k, v in a_dict.items():
    #     if type(v) is int:
    #         v *= 2
    #         a_dict[k] = v
    #
    # for item in a_dict.items():
    #     lists_tuple.append(item)

    for k, v in a_dict.items():
        if type(v) == int:
            v *= 2
        lists_tuple.append((k, v))
    return print(lists_tuple)


my_dict = {'one': 1, 'two': 2, 3: 'three', 'name': 'Pavlo'}

dict_to_list(my_dict)