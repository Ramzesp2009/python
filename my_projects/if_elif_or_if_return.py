def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "One parameter not add"

    if a >= b:
        return f"{a} more or equal {b}"

    return f"{a} less {b}"


# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         info = "One parameter not add"
#
#     elif a >= b:
#         info = f"{a} more or equal {b}"
#
#     else:
#         info = f"{a} less {b}"
#
#     return info


print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))