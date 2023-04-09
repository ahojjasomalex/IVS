from ivs_math import Operations
from lexer import Lexer


def main():
    l = Lexer()

    data = ''' -5/5+6+(9+7*2)-5!*3`27'''
    l.fill(data)
    l.print_tokens()
    print(l.get_token_types())
    print(l.get_token_values())

    data = '6+6'
    l.fill(data)
    print('')
    l.print_tokens()
    print(l.get_token_types())
    print(l.get_token_values())

    l.clear()

    l.fill(data)
    print('')
    l.print_tokens()
    print(l.get_token_types())
    print(l.get_token_values())


if __name__ == "__main__":
    main()
