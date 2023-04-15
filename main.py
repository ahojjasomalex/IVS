from CalcUtils import parser


def main():
    p = parser.Parser()
    data = '5!'
    res = p.parser.parse(data)
    print(res)


if __name__ == "__main__":
    main()
