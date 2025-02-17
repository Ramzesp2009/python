class Methods:
    def imeth(self, x):
        print([self, x])

    # @staticmethod
    def smeth(x):
        print([x])

    # @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

# Methods.smeth(7)
obj = Methods()
print(obj.name)
