class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    # @classmethod
    def printNumInstances(cls):
        print(f"Number of instaces created: {cls.numInstances},{cls}")
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass

if __name__ == '__main__':
    x = Sub()
    y = Spam()
    x.printNumInstances()
    Sub.printNumInstances()
    y.printNumInstances()