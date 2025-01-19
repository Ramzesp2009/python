from class_person import Person

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self._name = name

    def get_name(self):
        return self._name

student = Student('Pavlo')
print(student.get_name())