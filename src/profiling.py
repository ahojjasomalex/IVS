#!/usr/bin/python
from CalcUtils.parser import Parser
import random

p = Parser()

def generate_integers(N):
    """
    This function generates a list of N random integers between 0 and 999.

    @param N The parameter N is an integer that represents the number of integers to be generated.

    @return The function `generate_integers(N)` returns a list of `N` randomly generated integers between 0 and 999
    (inclusive) as strings.
    """
    numbers = []
    random.seed()
    for i in range(N):
        numbers.append(str(int(random.random() * 1000)))
    return numbers


def summarize(numbers: list, op='+'):
    """
    The function takes a list of numbers and an operator as input, concatenates them into a string, evaluates the string
    using a parser, and returns the result as a string.

    @param numbers The "numbers" parameter is a list of numbers that we want to summarize.
    @param op The "op" parameter is a string that represents the mathematical operation to be performed on the list of
    numbers. The default value is "+", which means that the function will perform addition on the list of numbers. However,
    the user can also specify other operations such as "-", "*", "/", etc.

    @return a string that represents the result of performing the specified operation (default is addition) on the numbers
    in the input list. The string is obtained by concatenating the numbers in the list with the specified operator, and then
    parsing the resulting string using the `parser` module.
    """
    number_string = ''
    for i in numbers:
        number_string += i + op
    res = str(p.parser.parse(number_string[:-1]))
    return res


def arithmetic_mean(input_numbers):
    """! The function calculates the arithmetic mean of a list of input numbers.

    @param input_numbers The input_numbers parameter is a list of numbers for which we want to calculate the arithmetic
    mean.

    @return The function `arithmetic_mean` is returning the arithmetic mean of the input numbers. It first calculates the
    sum of the input numbers using the `summarize` function (which is not defined in the code snippet provided), then
    divides the sum by the number of input numbers to get the mean. The mean is returned as a `float` value.
    """
    res = summarize(input_numbers)
    N = len(input_numbers)
    return p.parser.parse(f"{res}/{N}")


def standard_deviation(input_numbers):
    """! The function calculates the standard deviation of a list of input numbers using the formula for sample standard
    deviation.

    @param input_numbers The input_numbers parameter is a list of numbers for which we want to calculate the standard
    deviation.
    @return The function `standard_deviation` returns the calculated standard deviation of the input numbers
    """
    sum_x_pow_2 = summarize(input_numbers, op='^2+')
    a_mean = arithmetic_mean(input_numbers)
    N = len(input_numbers)
    res = p.parser.parse(f"2√(({sum_x_pow_2} - {N} * {a_mean}^2) / ({N} - 1))")
    return res


if __name__ == "__main__":
    # numbers = generate_integers(1000)
    input_numbers = input("Enter sequence of numbers for standard deviation:")
    input_numbers = input_numbers.split()  # split by whitespaces
    res = standard_deviation(input_numbers)
    print(res)