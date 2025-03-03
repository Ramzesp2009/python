class Catcher:
    def __getattr__(self, name):
        print('Get: ', name)

    def __setattr__(self, name, value):
        print('Set: ', name, value)


C = Catcher()
C.job
C.pay
C.pay = 99
