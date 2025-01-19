
def filter_list(lists, i):
    returned_list = []
    # my solution
    # for val in lists:
    #     if type(val) is type(i):
    #         returned_list.append(val)

    for val in lists:
        if type(val) == i:
            returned_list.append(val)

    # it isn't recommended, because bool is subclass of int
    # for val in lists:
    #     if isinstance(val, i):
    #         returned_list.append(val)
    return returned_list

# print(filter_list([35, True, 'abc', 10], True))
# print(filter_list([35, True, 'abc', 10], 5))
# print(filter_list([35, True, 'abc', 10], 'abc'))

print(filter_list([35, True, 'abc', 10], bool))
print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))


