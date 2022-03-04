numberOne = int(input("Vnesi prvo število: "))
numberTwo = int(input("Vnesi drugo število: "))
operation = input("Izberi (+, -, *, /): ")

if operation == "+":
    print(numberOne + numberTwo)
elif operation == "-":
    print(numberOne - numberTwo)
elif operation == "*":
    print(numberOne * numberTwo)
elif operation == "/":
    print(numberOne / numberTwo)
else:
    print("Nisi izbral pravilne matematične operacije")
