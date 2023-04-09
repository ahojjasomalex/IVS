from ivs_math import Operations
from lexer import Lexer


def main():
    data = ''' -5/5+6+(9+7*2)-5!*3`27'''
    l = Lexer()
    l.fill(data)
    l.print_tokens()
    tokens = l.get_tokens()
    print(tokens)


if __name__ == "__main__":
    main()
