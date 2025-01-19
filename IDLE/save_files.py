# save file

from matplotlib import pyplot
import numpy

xs = numpy.arange(1, 6)
tops = numpy.arange(2, 12, 2)

pyplot.bar(xs, tops)
pyplot.savefig("C://Python/IDLE")
pyplot.show()
