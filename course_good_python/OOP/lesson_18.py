# __getitem__(self, item, __setitem__(self, key, value), __delitem__(self, key)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            return "Wrong index"

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or value < 0:
            print("ERROR")
        elif key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            print("ERROR")

        del self.marks[key]


s1 = Student("Mark", [5, 4, 5, 4, 5])
del s1[1]
print(s1.marks)
# print(s1[2])