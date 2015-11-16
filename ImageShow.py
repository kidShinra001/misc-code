__author__ = 'Jonathan'

from scipy import misc
import numpy

face = misc.imread('CRUK logo50.jpg')
print(face.shape)
numpy.savetxt('foo.csv', face, delimiter=' ', newline = '\r\n', fmt='%03.0d')

