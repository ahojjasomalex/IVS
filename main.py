import sys

import ply.lex

from CalcUtils import parser
import PySimpleGUI as sg

layout = [[sg.Txt('' * 10)],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18),
                   text_color='black', key='input')],
          [sg.Txt('' * 10)],
          [sg.ReadFormButton('c'), sg.ReadFormButton('«'), sg.ReadFormButton('^'), sg.ReadFormButton('`')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
          ]

form = sg.FlexForm('CALCULATOR', default_button_element_size=(5, 2),
                   auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)


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
            except ply.lex.LexError as e:
                print(e, file=sys.stderr)

    except KeyboardInterrupt:
        sys.exit("Program stopped by CTRL+C")


if __name__ == "__main__":
    main()
