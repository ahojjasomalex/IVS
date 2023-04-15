from CalcUtils import parser


def main():
    p = parser.Parser()
    data = '(-(1+2)^3+5!)*2'
    res = p.parser.parse(data)
    print(res)


if __name__ == "__main__":
    main()
