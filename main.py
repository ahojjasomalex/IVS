import sys

import ply.lex

from CalcUtils import parser


def main():
    p = parser.Parser()
    try:
        while True:
            data = str(input())
            try:
                res = p.parser.parse(data)

                if res is None:
                    continue
                if res.is_integer():
                    res = int(res)
                else:
                    res = round(res, 10)

                print(res)

            except SyntaxError as e:
                print(e, file=sys.stderr)
            except ply.lex.LexError as e:
                print(e, file=sys.stderr)

    except KeyboardInterrupt:
        sys.exit("Program stopped by CTRL+C")


if __name__ == "__main__":
    main()
