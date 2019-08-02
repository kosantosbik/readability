#!/usr/bin/env python3

import readability
import sys
from textract import process
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from window import Ui_MainWindow


def read_file(filename):
    "Opens a file and reads its contents"

    return process(filename).decode('utf-8')

class readUI(QWidget, Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(MainWindow)

        self.selectFileButton.clicked.connect(self.select_file)

    def select_file(self):
        fname = QFileDialog.getOpenFileName(self,
                                            'Open File',
                                            './',
                                            "Text Files (*.doc *docx *.txt *.pdf)")
        filename = fname[0]
        text = read_file(filename)
        measures = readability.getmeasures(text)
        self.kincaid.setText("{0:.2f}".format(measures['readability grades']['Kincaid']))
        self.ari.setText("{0:.2f}".format(measures['readability grades']['ARI']))
        self.coleman.setText("{0:.2f}".format(measures['readability grades']['Coleman-Liau']))
        self.flesh.setText("{0:.2f}".format(measures['readability grades']['FleschReadingEase']))
        self.gunning.setText("{0:.2f}".format(measures['readability grades']['GunningFogIndex']))
        self.lix.setText("{0:.2f}".format(measures['readability grades']['LIX']))
        self.smog.setText("{0:.2f}".format(measures['readability grades']['SMOGIndex']))
        self.rix.setText("{0:.2f}".format(measures['readability grades']['RIX']))
        self.dale.setText("{0:.2f}".format(measures['readability grades']['DaleChallIndex']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = readUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
