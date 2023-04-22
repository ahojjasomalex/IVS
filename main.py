import sys

import ply.lex

from CalcUtils import parser
from GUI.calc import Ui_MainWindow
from PyQt6 import QtWidgets


def format_data(ans):
    if ans.is_integer():
        ans = str(int(ans))
    else:
        ans = str(round(ans, 10))
    return ans


def main():
    p = parser.Parser()
    try:
        while True:
            data = input()
            try:
                ans = format_data(p.parser.parse(data))

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
    # main()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
