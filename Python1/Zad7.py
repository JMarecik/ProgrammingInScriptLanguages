import re
import cmath

print("Write input data: ")
text = input()
text = re.split('\s+', text)
a, b, c = text
a = int(a)
b = int(b)
c = int(c)
delta = b**2-4*a*c
x1 = (-b-cmath.sqrt(delta))/(2*a)
x2 = (-b+cmath.sqrt(delta))/(2*a)
print("x1 = " + str(x1))
print("x2 = " + str(x2))
