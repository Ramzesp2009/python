class Person:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        print('get: ', attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError

    def __setattr__(self, attr, value):
        print('set: ', attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print('del: ', attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]

bob = Person('Bob Smith')
print(bob.name)
bob.name = "Robert Smith"
print(bob.name)
del bob.name
print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
# print(Person.name.__doc__)