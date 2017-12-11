
cipher = "snake"

while True:
    text = input("Write password: ")
    if text == cipher:
        print("Password is correct!")
        break
    else:
        print("Password is incorrect!")
