import math
from operator import neg


class Complex(object):

    def __init__(self, re, im):
        '''Creates Complex Number'''
        self.re = re
        self.im = im

    def __str__(self):
        '''Returns complex number as a string'''
        return '(%s, %s)' % (self.re, self.im)

    def __add__(self, rhs):
        '''Adds complex numbers'''
        return Complex(self.re + rhs.re, self.im + rhs.im)

    def __mul__(self, rhs):
        '''Multiplication complex numbers'''
        return Complex(self.re * rhs.re - self.im * rhs.im,
                       self.im * rhs.re + self.re * rhs.im)

    def __sub__(self, rhs):
        '''Adds complex numbers'''
        return Complex(self.re - rhs.re, self.im - rhs.im)

    def __abs__(self):
        '''Absolute values complex number'''
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def __neg__(self):
        '''Negation complex number'''
        return Complex(-self.re, -self.im)

    def __eq__(self, rhs):
        '''Equality complex numbers'''
        return self.re == rhs.re and self.im == rhs.im

'''Testing'''
# x = Complex(0, 1)
# y = Complex(2, 2)
# print(x + y)
# print(y - x)
# print(y * x)
# print(abs(x))
# print(x == y)
# print(neg(x))
