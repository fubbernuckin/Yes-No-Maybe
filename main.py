from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import menus.options
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.initMainMenu()
    def initMainMenu(self):
        uic.loadUi('maindev.ui', self)
        self.resetcolors()
        self.mainMenu()
    def mainMenu(self):
        self.show()
        # self.resetcolors()
        #when button is clicked go to different ui
        self.pushButton.clicked.connect(self.goToYes)
        self.pushButton_2.clicked.connect(self.goToMaybe)
        self.pushButton_3.clicked.connect(self.goToNo)
        self.pushButton_4.clicked.connect(self.optionsPage)
    def goToYes(self):
        if(flashEnabled):
            self.flash(1)
        if(doubleClickEnabled):
            self.pushButton.clicked.connect(self.goToYes2)
        else:
            self.gotoYes2()
    
    def gotoYes2(self):
        #say yes
        self.resetcolors()

    def goToNo(self):
        if(flashEnabled):
            self.flash(2)
        if(doubleClickEnabled):
            self.pushButton_2.clicked.connect(self.goToNo2)
        else:
            self.gotoNo2()

    def gotoNo2(self):
        #say no
        self.resetcolors()

    def goToMaybe(self):
        if(flashEnabled):
            self.flash(3)
        if(doubleClickEnabled):
            self.pushButton_3.clicked.connect(self.goToMaybe2)
        else:
            self.gotoMaybe2()

    def gotoMaybe2(self):
        #say maybe
        self.resetcolors()

    def optionsPage(self):
        self.hide()
        self.options = options()
        self.options.show()
        
    def resetcolors(self):
        if(colorBlindEnabled):
            self.pushButton.setStyleSheet(Yes)
            self.pushButton_2.setStyleSheet(colorBlindMaybe)
            self.pushButton_3.setStyleSheet(colorBlindNo)
            # self.pushButton_4.setStyleSheet(colorBlindGrey)
        else:
            self.pushButton.setStyleSheet(Green)
            self.pushButton_2.setStyleSheet(Yellow)
            self.pushButton_3.setStyleSheet(Red)
            # self.pushButton_4.setStyleSheet(Grey)
        self.mainMenu()
    
    def flash(self, buttonNum):
        if(buttonNum == 1):
            self.pushButton.setStyleSheet(flashColor)
        if(buttonNum == 2):
            self.pushButton_2.setStyleSheet(flashColor)
        if(buttonNum == 3):
            self.pushButton_3.setStyleSheet(flashColor)
        if(buttonNum == 4):
            self.pushButton_4.setStyleSheet(flashColor)
        QTimer.singleShot(flashTime, self.resetcolors)


class options(QtWidgets.QMainWindow):
    def __init__(self):
        super(options, self).__init__()
        # uic.loadUi('options.ui', self)
        self.show()
        self.flashBox.setChecked(flashEnabled)
        self.doubleBox.setChecked(doubleClickEnabled)
        self.cbBox.setChecked(colorBlindEnabled)
        self.optionsPage()
    def optionsPage(self):
        self.pushButton.clicked.connect(self.mainMenu)
        self.flashBox.stateChanged.connect(self.somethingChanged)
        self.doubleBox.stateChanged.connect(self.somethingChanged)
        self.cbBox.stateChanged.connect(self.somethingChanged)
    def somethingChanged(self):
        global flashEnabled
        global doubleClickEnabled
        global colorBlindEnabled
        flashEnabled = self.flashBox.isChecked()
        doubleClickEnabled = self.doubleBox.isChecked()
        colorBlindEnabled = self.cbBox.isChecked()
        self.optionsPage()
    def mainMenu(self):
        self.hide()
        self.main = Ui()
        self.main.show()

doubleClickEnabled = False
flashEnabled = False
firstLoad = True
flashTime = 500
ttsEnabled = True
colorBlindEnabled = True
flashColor = "background-color: rgb(255, 255, 255);"
colorBlindNo="background-color: rgb(255, 55, 55);"
colorBlindYes ="background-color: rgb(106, 106, 255);"
colorBlindMaybe="background-color: rgb(255, 255, 28);"
No="background-color: rgb(255, 55, 55);"
Yes="background-color: rgb(10, 190, 10);"
Maybe="background-color: rgb(255, 255, 28);"

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
