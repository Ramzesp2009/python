from valedate_descriptors1 import CardHolder

def loadclass():
    import sys, importlib
    modulename = sys.argv[1]
    module = importlib.import_module(modulename)
    print('[Using: %s]' % module.CardHolder)
    return module.CardHolder

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
    CardHolder = loadclass()
    bob = CardHolder('1234-5678', 'Bob Smith', 45, '123 Main st.')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob)
    sue = CardHolder('9876-5432', 'Sue Jones', 42, '987 Main st.')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")
    try:
        sue.acct = '1234567'
    except:
        print("Bad acct fpr Sue")