# class Squares:
#     def __init__(self, start, stop):
#         self.value = start - 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value ** 2


def squares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

for i in squares(1, 5):
    print(i, end=':')