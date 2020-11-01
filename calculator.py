def division(a, b):
    outcome = a / b
    return outcome


def multiplication(a, b):
    outcome = a * b
    return outcome


def addition(a, b):
    outcome = a + b
    return outcome


def subtraction(a, b):
    outcome = a - b
    return outcome


def exit_program():
    print("Program was terminated")
    quit()

action = "+"

while action.upper() in('+' , '-' , '*' , '/' , 'X'):

    action = input("Choose action. Type: '+' , '-' , '*' , '/' or 'X' if you want to quit: ")
    if action.upper() == "X":
        exit_program()
    num1 = ""
    num2 = ""

    while type(num1) != float:
        try:
            num1 = input("Type first number: ")
            if num1.upper() == "X":
                exit_program()
            num1 = float(num1)
        except ValueError:
            print("It was not a number.")
    while type(num2) != float:
        try:
            num2 = input("Type second number: ")
            if num2.upper() == "X":
                exit_program()
            num2 = float(num2)
        except ValueError:
            print("error:it was not a number")

    if action == '+':
        result = addition(num1, num2)
        print("The result of {operation} of {num1} and {num2} is {result}".format(operation='addition', num1=num1, num2=num2, result=result))
    elif action == '-':
        result = subtraction(num1, num2)
        print("The result of {operation} of {num1} and {num2} is {result}".format(operation='subtraction', num1=num1, num2=num2, result=result))
    elif action == '*':
        result = multiplication(num1, num2)
        print("The result of {operation} of {num1} and {num2} is {result}".format(operation='multiplication', num1=num1, num2=num2, result=result))
    elif action == '/':
        result = division(num1, num2)
        print("The result of {operation} of {num1} and {num2} is {result}".format(operation='division', num1=num1, num2=num2, result=result))
    else:
        print("You did not specified mathematical operation correctly. Start again.")

print("Program was terminated")
