from random import randint

elements_number = 50

x = []
for i in range(elements_number):
    x.append(randint(0, 999))

print("Before sorting:")
print(x)
y = x.copy()
x.sort()

for i in range(elements_number):
    for k in range(elements_number - i - 1):
        if y[k] > y[k+1]:
            t = y[k]
            y[k] = y[k + 1]
            y[k + 1] = t

print("After sorting:")
print(y)

''' Checking sort algorithm '''
flag = True
for i in range(elements_number):
    if x[i] != y[i]:
        flag = False
        break

if flag:
    print("OK!")
else:
    print("Error!")
