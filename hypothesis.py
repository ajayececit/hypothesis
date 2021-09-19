# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hypothesispZofVA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtWidgets import *
from PyQt5 import uic


class hypothesis_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hypothesis.ui', self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    hypothesis_window = hypothesis_ui()
    hypothesis_window.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing..!!')
