"I'm: docstr.__doc__"

def func(args):
    "I'm: docstr.func.__doc__"
    pass

class Spam:
    "I'm: Spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I'm: Spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)
