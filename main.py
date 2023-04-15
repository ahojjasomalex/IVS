import sys
from CalcUtils import parser


def main():
    p = parser.Parser()
    try:
        while True:
            data = str(input())
            try:
                res = p.parser.parse(data)

                if res.is_integer():
                    res = int(res)
                else:
                    res = round(res, 10)

                print(res)

            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        sys.exit("Program stopped by CTRL+C")


if __name__ == "__main__":
    main()
