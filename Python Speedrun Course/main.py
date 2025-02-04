class One:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Two:
    def __init__(self, hand, foot):
        self.hand = hand
        self.foot = foot

class Three(One, Two):
    def __init__(self, name, age, hand, foot, something, jet):
        One.__init__(self, name, age)
        Two.__init__(self, hand, foot)
        self.something = something
        self.jet = jet

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nHand: {self.hand}\nFoot: {self.foot}\nSomething: {self.something}\nJet: {self.jet}'


wtf = Three(name='Bob', age=22, hand=2, foot=2, something=True, jet=False)
print(wtf)
