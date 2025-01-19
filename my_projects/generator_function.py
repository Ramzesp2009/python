from sys import getsizeof

my_scores = {
    1: 'aaa',
    2: 'bbb',
    3: 'ccc'
}
score = {k: v.upper() for k, v in my_scores.items()}
print(score)


list_str = ['aaa', 'bbbb', 'ccccc']
my_new_list = [word for word in list_str if len(word) > 3]
print(my_new_list)

test_tuple = (1, 2, 3, 4)
new_tuple = (i for i in test_tuple)
print(list(new_tuple), tuple(new_tuple))
print()

nums = (3, 5, 67)
square = (num * num for num in nums)
print(list(square))
