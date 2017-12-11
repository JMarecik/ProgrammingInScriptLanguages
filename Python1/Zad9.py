import re

file1 = open('exampleText.txt').read()

file1 = re.sub('I(?i) ', "", file1)
file1 = re.sub('S(?i)ie ', "", file1)
file1 = re.sub('O(?i)raz ', "", file1)
file1 = re.sub('N(?i)igdy', "", file1)
file1 = re.sub('D(?i)laczego', "", file1)
file2 = open('exampleText2.txt', 'w').write(file1)
