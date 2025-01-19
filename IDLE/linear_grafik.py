# new grafic linear

from matplotlib import pyplot
from numpy import random


# centers = numpy.arange(1, 6)
# tops = numpy.arange(2, 12, 2)

# fruits = {
#    "apples": 10,
#    "oranges": 16,
#    "bananas": 9,
#    "pears": 4,
# }

pyplot.hist(random.randn(10000), 20)

# pyplot.bar(fruits.keys(), fruits.values())
pyplot.show()
