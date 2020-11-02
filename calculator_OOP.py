class Calc:
    def __init__(self):
        self.numbers = []
        self.action = " "
        self.symbol = " "

    def get_number(self):
        number = float(input("Give number: "))
        self.numbers.append(number)
        print(self.numbers)
        return self.numbers

    def addition(self):
        temp = 0
        for n in self.numbers:
            temp += n
        print(temp)
        self.numbers = []
        self.numbers.append(temp)
        return temp

    def subtraction(self):
        temp = 0
        for n in self.numbers:
            temp -= n
        print(temp)
        self.numbers = []
        self.numbers.append(temp)
        return temp

    def multiplication(self):
        temp = 1
        for n in self.numbers:
            temp *= n
        print(temp)
        self.numbers = []
        self.numbers.append(temp)
        return temp

    def division(self):
        temp = 0
        for n in self.numbers:
            temp /= n
        print(temp)
        self.numbers = []
        self.numbers.append(temp)
        return temp

    def clear(self):
        self.numbers = []
        self.symbol = " "
        print("All cleared")

    def exit_program(self):
        print("Program closed")
        quit()

    def decision(self):
        if self.action == 'n':
            return Calc.get_number(self)
        elif self.action == 'c':
            return Calc.clear(self)
        elif self.action == 'x':
            return Calc.exit_program(self)
        elif self.action == '=':
            return Calc.do_math(self)
        else:
            self.symbol = self.action

    def do_math(self):
        if self.symbol == '+':
            return Calc.addition(self)
        elif self.symbol == '-':
            return Calc.subtraction(self)
        elif self.symbol == '*':
            return Calc.multiplication(self)
        elif self.symbol == '/':
            return Calc.division(self)
        else:
            print("Invalid form of expression")


app = Calc()

while app.action != 'x':
    app.action = str(input('Type "n" to input number, "+" to add, "-" to subtract, "*" to multiply, "/" to divide, "=" to calculate, "c" to clear content, "x" to exit. :'))
    app.decision()
