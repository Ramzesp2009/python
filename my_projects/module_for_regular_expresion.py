import re

my_string = "My name is Pablo."
other_string = "My name is Pablo. Pablo is a student."
my_patern = re.compile(r'P...o.$')
res = re.search(r'P...o\.$', my_string)
print(res)
print(res.span())
print(res.start())
print(res.end())
print(my_patern)
print(my_patern.search(my_string))
my_patern = re.compile(r'^My.*\.$')
print(my_patern)
print(my_patern.search(my_string))
my_patern_2 = re.compile(r'P...o')
print(my_patern_2)
print(my_patern_2.findall(other_string))
