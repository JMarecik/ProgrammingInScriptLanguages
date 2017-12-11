import re

words = {'i ': 'oraz ', 'oraz ': 'i ', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}

file1 = open('exampleText.txt').read()
for k, v in words.items():
    file1 = re.sub(k, v, file1)

file2 = open('exampleText3.txt', 'w').write(file1)

