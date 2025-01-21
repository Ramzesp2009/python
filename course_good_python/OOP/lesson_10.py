from string import ascii_letters


class Person:
    S_UKR = "абвгдеэжзіийклмнопрстуфхчцюяї"
    S_UKR_UPPER = S_UKR.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)


        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise  TypeError("The name musst be a string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Invalid recording format")

        letters = ascii_letters + cls.S_UKR + cls.S_UKR_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError("The name must be more than one letter")
            if len(s.strip(letters)) != 0:
                raise TypeError("In the name avoid using only letters")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 128:
            raise TypeError("The age must be an integer and in range 14-128")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("The weight must be a floating number and more than 20kg")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("The number passport must be a string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
            raise TypeError("The number of pass must to have a format XXXX XXXXXX")

        for p in s:
            if not p.isdigit():
                raise TypeError("The seria and number of pass must be numbers")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


p = Person("Ромазан Павло Григорович", 40, '1234 567890', 92.5)
p.old = 44
p.passport = '1233 122122'
p.weight = 95.5
print(p.__dict__)