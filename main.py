import sys

import ply.lex

from CalcUtils import parser


def main():
    p = parser.Parser()
    try:
        while True:
            data = input()
            try:
                ans = p.parser.parse(data)

                if ans is None:
                    continue
                if ans.is_integer():
                    ans = str(int(ans))
                else:
                    ans = str(round(ans, 10))

                print(ans)

            except SyntaxError as e:
                print(e, file=sys.stderr)
            except ZeroDivisionError as e:
                print(e, file=sys.stderr)
            except ply.lex.LexError as e:
                print(e, file=sys.stderr)

    except KeyboardInterrupt:
        sys.exit("Program stopped by CTRL+C")


if __name__ == "__main__":
    main()
