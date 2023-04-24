#!/usr/bin/python

from CalcUtils.parser import Parser
import random

p = Parser()


def generate_integers(N):
    numbers = []
    random.seed()
    for i in range(N):
        numbers.append(str(int(random.random() * 10000))) #generate N random integers in range 0-10 000
    return numbers


def sumarize(numbers: list, op='+'):

    sumarize = ''
    for i in input_numbers:
        sumarize += i + f"{op}"
    sumarize = sumarize[:-len(op)]

    res = str(p.parser.parse(sumarize))
    return res, len(input_numbers)


def arithmetic_mean(input_numbers):
    sum, N = sumarize(input_numbers)
    return p.parser.parse(f"{sum}/{N}")

def standard_deviation(input_numbers):
    sum_x_pow_2, N = sumarize(input_numbers, op='^2+')
    a_mean = arithmetic_mean(input_numbers)
    print(sum_x_pow_2)
    print(a_mean)
    return p.parser.parse(f"2√(({sum_x_pow_2} - {N} * {a_mean}^2) / ({N} - 1))")

if __name__ == "__main__":
    input_numbers = ""
    # input_numbers = input("Enter sequence of numbers for standard deviation:")
    # input_numbers = input_numbers.split()  # split by whitespaces
    # res = arithmetic_mean(input_numbers)
    # print(res)
    numbers = generate_integers(10)
    print(numbers)
    res = standard_deviation(numbers)
    print(res)