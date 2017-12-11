import numpy
from random import randint

elements_number = 8
x = []
a1 = []
b1 = []

for i in range(elements_number):
    for k in range(elements_number):
        x.append(randint(0, 99))
    a1.append(x.copy())
    x.clear()

for i in range(elements_number):
    for k in range(elements_number):
        x.append(randint(0, 99))
    b1.append(x.copy())
    x.clear()

a = numpy.array(a1)
b = numpy.array(b1)

print(a * b)
