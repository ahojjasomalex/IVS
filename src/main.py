#!/usr/bin/env python3
import sys
from GUI.calc import MainWindow, app

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec())
