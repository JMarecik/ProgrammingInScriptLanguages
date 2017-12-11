import numpy
from random import randint

elements_number = int(input("Give matrix size: "))
x = []
a1 = []

for i in range(elements_number):
    for k in range(elements_number):
        x.append(randint(0, 9))
    a1.append(x.copy())
    x.clear()

a = numpy.array(a1)

print(numpy.linalg.det(a))
