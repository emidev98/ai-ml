userNumber = int(input("Chose a number : "))
square = 0

while square**2 < userNumber:
    square += 1

if square**2 == userNumber:
    print(f"The square of {userNumber} is {square}")
else:
    print(f"{userNumber} does not have a fix square")
