# pyuic5 name.ui -o name.py

import sys
from main_window import *


def check_styles_by_windows() -> list:
    styles = [x for x in QtWidgets.QStyleFactory.keys()]
    print("Styles:", styles)
    return styles


def main():
    app = QtWidgets.QApplication(sys.argv)
    style = check_styles_by_windows()
    app.setStyle(style[2])
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
