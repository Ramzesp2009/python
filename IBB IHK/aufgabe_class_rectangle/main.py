from class_Rectangle import Ractangle
from class_point_3d import Point3D
from class_bank_account import BankAccount
from class_flache import Flache

rectangle_1 = Ractangle(10, 15)
rectangle_2 = Ractangle(10, 15)

print(rectangle_1 == rectangle_2)

point_1 = Point3D(1, 2, 3)
point_2 = Point3D(2, 1, 4)
print(point_1.__eq__(point_2))
print(point_2.__abs__())

bankaccount_1 = BankAccount(3500)
bankaccount_2 = BankAccount(4500)
print(bankaccount_1 > bankaccount_2)
print(bankaccount_1 + bankaccount_2)

flache = Flache(4, 5)
print(flache * 5)
print(repr(flache))