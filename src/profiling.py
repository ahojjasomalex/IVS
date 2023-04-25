#!/usr/bin/python
##
# @package src.profiling
# profiling.py is module that calculates standard deviation using src.CalcUtils package
#

from CalcUtils.parser import Parser
import random

#   instantiate Parser class
p = Parser()


def generate_integers(N):
    """!@brief Function generates list of N integers with values <0, 999>
    @param N Number of integers to generate
    @return: List of N random integers
    """
    numbers = []
    random.seed()
    for i in range(N):
        numbers.append(str(int(random.random() * 1000)))
    return numbers


def summarize(numbers: list, op='+'):
    """!@brief The function takes a list of numbers and an operator as input, concatenates them into a string, evaluates
    the string using a parser and returns the result as a string
    @param numbers List of numbers that we want to summarize.
    @param op String that represents the mathematical operation to be performed on the list of numbers, default value is "+",
    can be changed by providing explicit op parameter
    @return String that represents the result of performing the specified operation on the numbers list by parser class
    """
    number_string = ''
    for i in numbers:
        number_string += i + op
    res = str(p.parser.parse(number_string[:-1]))
    return res


def arithmetic_mean(numbers):
    """!@brief The function calculates the arithmetic mean of a list of input numbers
    @param numbers List of input numbers to calculate mean from
    @return Float, arithmetic mean of a list
    """
    res = summarize(numbers)
    N = len(numbers)
    return p.parser.parse(f"{res}/{N}")


def standard_deviation(numbers):
    """!@brief The function calculates the standard deviation of a list of input numbers using the formula for sample standard
    deviation
    @param numbers List of numbers from which to calculate standard deviation
    @return Float, standard deviation of the input numbers
    """
    sum_x_pow_2 = summarize(numbers, op='^2+')
    a_mean = arithmetic_mean(numbers)
    N = len(numbers)
    res = p.parser.parse(f"2√(({sum_x_pow_2} - {N} * {a_mean}^2) / ({N} - 1))")
    return res


if __name__ == "__main__":
    # numbers = generate_integers(1000)
    input_numbers = input("Enter sequence of numbers for standard deviation:")
    input_numbers = input_numbers.split()  # split by whitespaces
    res = standard_deviation(input_numbers)
    print(res)
