# pyplot_2

from matplotlib import pyplot
import numpy

days = numpy.arange(0, 21)
other_site, real_python = days, days ** 2


pyplot.plot(days, other_site)
pyplot.plot(days, real_python)
pyplot.xticks([0, 5, 10, 15, 20])
pyplot.xlabel("Days of Readig")
pyplot.ylabel("Amount of Python Learned")
pyplot.title("Python Learned Reading Real Python vs Other Site")
pyplot.legend(["Other Site", "Real Python"])
pyplot.show()
