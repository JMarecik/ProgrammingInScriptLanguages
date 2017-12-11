import re

print("Podaj imie, nazwisko, rok urodzenia: ")
text = input()
text = re.split('\s+', text)
print("Imie: " + text[0])
print("Nazwisko: " + text[1])
print("Data urodzenia: " + text[2])