class Methods:
    def imeth(self, x):
        print([self, x])

    # @staticmethod
    def smeth(x):
        print([x])

    # @classmethod
    def cmeth(cls, x):
        print([cls, x])

    # smeth = staticmethod(smeth)
    # cmeth = classmethod(cmeth)

Methods.smeth(7)
