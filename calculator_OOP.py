class Calc:
    def __init__(self, action):
        self.a = 0
        self.b = 0
        self.action = action
        self.symbol = " "

    def get_num_a(self):
        a = float(input("Give num a: "))
        self.a = a
        print(self.a)
        return self.a

    def get_num_b(self):
        b = float(input("Give num b: "))
        self.b = b
        print(self.b)
        return self.b

    def addition(self):
        total = self.a + self.b
        print(total)
        return total

    def subtraction(self):
        total = self.a - self.b
        print(total)
        return total

    def multiplication(self):
        total = self.a * self.b
        print(total)
        return total

    def division(self):
        total = self.a / self.b
        print(total)
        return total

    def clear(self):
        self.a = 0
        self.b = 0
        self.symbol = " "
        print("All cleared")

    def exit_program(self):
        print("Program closed")
        quit()

    def decision(self):
        if self.action == 'a':
            return Calc.get_num_a(self)
        elif self.action == 'b':
            return Calc.get_num_b(self)
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
            print("You need to specify two numbers.")


app = Calc(' ')

while app.action != 'x':
    app.action = str(input('Type "a" to input num a, "b" to input num b, "+" to add, "-" to subtract, "*" to multiply, "/" to divide, "c" to clear content, "x" to exit. :'))
    app.decision()