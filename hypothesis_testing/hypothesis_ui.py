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
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
import sys


class hypothesis_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hypothesis.ui', self)

        # used to validate the inputs to be in int
        self.onlyInt = QIntValidator()
        self.num_of_sample.setValidator(self.onlyInt)
        self.population_mean.setValidator(self.onlyInt)
        self.std_deviation.setValidator(self.onlyInt)
        self.sample_mean.setValidator(self.onlyInt)

        self.compute_button.clicked.connect(self.on_compute_click)
        self.show()
        self.cancel_button.clicked.connect(self.on_cancel_click)

    @pyqtSlot()
    def reset_fields(self):
        self.num_of_sample.setText("")
        self.population_mean.setText("")
        self.sample_mean.setText("")
        self.std_deviation.setText("")
        self.null_hypothesis.setText("")
        self.alternate_hypothesis.setText("")

    @pyqtSlot()
    def on_compute_click(self):
        if self.mean_radio.isChecked():
            num_of_sample = self.num_of_sample.text()
            population_mean = self.population_mean.text()
            std_deviation = self.std_deviation.text()
            sample_mean = self.sample_mean.text()
            null_hypothesis = self.null_hypothesis.text()
            alternate_hypothesis = self.alternate_hypothesis.text()
            print(num_of_sample, population_mean, std_deviation, sample_mean, null_hypothesis, alternate_hypothesis)

        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,)
        if self.propotion_radio.isChecked():
            print(123)
        self.reset_fields()
        hypothesis_ui.close()

    @pyqtSlot()
    def on_cancel_click(self):
        try:
            hypothesis_ui.close()
        except SystemExit:
            print('Closing..!!')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    hypothesis_window = hypothesis_ui()
    hypothesis_window.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing..!!')
