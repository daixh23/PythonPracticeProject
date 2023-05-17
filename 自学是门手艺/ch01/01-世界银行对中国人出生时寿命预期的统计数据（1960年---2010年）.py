import matplotlib.pyplot as pyplot
import numpy as numpy

data = numpy.genfromtxt('life-expectancy-china-1960-2016.txt', delimiter=',', names=['x','y'])
da1960 = data[0][1]
da2016 = data[-1][1]
