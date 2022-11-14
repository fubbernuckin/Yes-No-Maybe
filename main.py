from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.mainMenu()
    def mainMenu(self):
        uic.loadUi('test.ui', self)
        self.show()
        #when button is clicked go to different ui
        self.pushButton.clicked.connect(self.goToYes)
        self.pushButton_2.clicked.connect(self.goToNo)
        self.pushButton_3.clicked.connect(self.goToMaybe)
        self.pushButton_4.clicked.connect(self.goToOther)
    def goToYes(self):
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        QTimer.singleShot(1000, self.resetcolors)
    def goToNo(self):
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        QTimer.singleShot(1000, self.resetcolors)
    def goToMaybe(self):
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        QTimer.singleShot(1000, self.resetcolors)
    def goToOther(self):
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        QTimer.singleShot(1000, self.resetcolors)
    def resetcolors(self):
        self.pushButton.setStyleSheet("background-color: rgb(106, 106, 255);")
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 55, 55);")
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 28);")
        self.pushButton_4.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.mainMenu


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedHeight(800)
window.setFixedWidth(450)
app.exec_()
