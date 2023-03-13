import math


class Operations:
    def __init__(self):
        self.ops = ['+', '-', '*', '/', '^', 'root', '!']
        self.callstack = []  # number stack

    def clear(self):
        self.__init__()

    def push_stack(self, n):
        if n in self.ops:
            self.callstack.append(n)
        elif isinstance(n, int) or isinstance(n, float):
            self.callstack.append(n)
        else:
            raise ValueError(f"{n} is not a digit")

    def pop_stack(self):
        return self.callstack.pop()

    def expression_calc(self):
        #  prefix notation

        op = self.pop_stack()  # operator
        b = self.pop_stack()
        a = self.pop_stack()

        try:
            if op == '!':
                self.callstack.append(math.factorial(a))
            if op == '+':
                self.callstack.append(a + b)
            if op == '-':
                self.callstack.append(a - b)
            if op == '*':
                self.callstack.append(a * b)
            if op == '/':
                self.callstack.append(a / b)
            if op == '^':
                self.callstack.append(a ** b)
            if op == 'sqrt':
                self.callstack.append(b ** (1 / a))

        except IndexError:
            return 1

    def calc(self):
        while len(self.callstack) > 1:  # call stack not empty
            self.expression_calc()

    def push_vars(self, a, b):
        self.push_stack(a)
        self.push_stack(b)

    def add(self, a, b):
        self.push_vars(a, b)
        self.push_stack('+')

    def sub(self, a, b):
        self.push_vars(a, b)
        self.push_stack('-')

    def tim(self, a, b):
        self.push_vars(a, b)
        self.push_stack('*')

    def div(self, a, b):
        self.push_vars(a, b)
        self.push_stack('/')

    def exp(self, a, b):
        self.push_vars(a, b)
        self.push_stack('^')

    def root(self, a, b):
        self.push_vars(a, b)
        self.push_stack('root')

    def fact(self, a, b):
        self.push_vars(a, b)
        self.push_stack('!')
