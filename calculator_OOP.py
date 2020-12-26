class UserInput:

    def __init__(self):
        self._value = None
        self._action = None
        self._numbers = []
        self._run = False

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, symbol):
        self._action = symbol

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, empty_list):
        self._numbers = empty_list

    @property
    def run(self):
        return self._run

    @run.setter
    def run(self, true_or_false):
        self._run = true_or_false

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value == 'x':
            CalcFunc.exit_program()
        if value == '=':
            self._run = True
        elif value not in ['+', '-', '*', '/', 'c', None]:
            try:
                value = float(value)
                self._numbers.append(value)
            except ValueError:
                print("Wrong input data")
        else:
            self._action = value
        self._value = value


class CalcFunc:

    @staticmethod
    def exit_program() -> object:
        print("Program closed")
        return quit()

    @classmethod
    def addition(cls, numbers):
        total = numbers[0]
        for number in numbers[1:]:
            total += number
        return total

    @classmethod
    def subtraction(cls, numbers):
        total = numbers[0]
        for number in numbers[1:]:
            total -= number
        return total

    @classmethod
    def multiplication(cls, numbers):
        total = 1
        for number in numbers:
            total *= number
        return total

    @classmethod
    def division(cls, numbers):
        total = numbers[0]
        try:
            for number in numbers[1:]:
                total /= number
            return total
        except ZeroDivisionError:
            print("You can't divide by zero!")


class Calculator:

    def __init__(self, terminal_input: UserInput):
        self._terminal_input = terminal_input

    def choose_calc_func(self):
        if self._terminal_input.action == '+':
            return CalcFunc.addition(self._terminal_input.numbers)
        elif self._terminal_input.action == '-':
            return CalcFunc.subtraction(self._terminal_input.numbers)
        elif self._terminal_input.action == '*':
            return CalcFunc.multiplication(self._terminal_input.numbers)
        elif self._terminal_input.action == '/':
            return CalcFunc.division(self._terminal_input.numbers)

    def clear_variables(self):
        self._terminal_input.value = None
        self._terminal_input.action = None
        del self._terminal_input.numbers[:-1]
        self._terminal_input.run = False

    def clear_all(self):
        self.clear_variables()
        self._terminal_input.numbers = []


ui = UserInput()
my_calculator = Calculator(ui)
print("Use calculator by writing to the terminal commends: '+', '-', '*', '/', 'c', '=' or numbers.")

while ui.value != 'x':
    ui.value = input("Get input: ")
    if ui.run:
        print("Result: ", my_calculator.choose_calc_func())
        ui.numbers.append(my_calculator.choose_calc_func())
        my_calculator.clear_variables()
    if ui.value == 'c':
        my_calculator.clear_all()
