filename = "exampleData"

file = open(filename, 'w')
file.write("Hello world!")
file.close()

file = open(filename, 'r')
print("Text from file: " + file.read())
file.close()
