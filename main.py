import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
import PySide6.QtCore

import os
DOUBLE_CLICK_TIMER = 1500
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.mainmenu()
    def mainmenu(self):
        loader = QUiLoader()
        self.ui = loader.load('test.ui')
        self.ui.show()
        #button clicked show yes
        self.ui.pushButton.clicked.connect(self.yes)
        self.ui.pushButton_2.clicked.connect(self.no)
        self.ui.pushButton_3.clicked.connect(self.questionMark)
        self.ui.pushButton_4.clicked.connect(self.altMenu)
    def yes(self):
        self.ui.pushButton.clicked.connect(self.yesAlt)
        self.ui.pushButton_2.clicked.connect(self.no)
        self.ui.pushButton_3.clicked.connect(self.questionMark)
        self.ui.pushButton_4.clicked.connect(self.altMenu)
       #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(DOUBLE_CLICK_TIMER, self.mainmenu)
    def no(self):
        self.ui.pushButton.clicked.connect(self.yes)
        self.ui.pushButton_2.clicked.connect(self.noAlt)
        self.ui.pushButton_3.clicked.connect(self.questionMark)
        self.ui.pushButton_4.clicked.connect(self.altMenu)
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(DOUBLE_CLICK_TIMER, self.mainmenu)
    def questionMark(self):
        self.ui.pushButton.clicked.connect(self.yes)
        self.ui.pushButton_2.clicked.connect(self.no)
        self.ui.pushButton_3.clicked.connect(self.questionMarkAlt)
        self.ui.pushButton_4.clicked.connect(self.altMenu)
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(DOUBLE_CLICK_TIMER, self.mainmenu)
    def altMenu(self):
        self.ui.pushButton.clicked.connect(self.yes)
        self.ui.pushButton_2.clicked.connect(self.no)
        self.ui.pushButton_3.clicked.connect(self.questionMark)
        self.ui.pushButton_4.clicked.connect(self.altaltMenu)
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(DOUBLE_CLICK_TIMER, self.mainmenu)
    def yesAlt(self):
        loader = QUiLoader()
        self.ui = loader.load('yes.ui')
        self.ui.show()
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile("yes.mp3"))
        effect.setVolume(0.25)
        effect.play()
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(3000, self.mainmenu)
    def noAlt(self):
        loader = QUiLoader()
        self.ui = loader.load('no.ui')
        self.ui.show()
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(3000, self.mainmenu)
    def questionMarkAlt(self):
        loader = QUiLoader()
        self.ui = loader.load('question.ui')
        self.ui.show()
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(3000, self.mainmenu)
    def altaltMenu(self):
        loader = QUiLoader()
        self.ui = loader.load('altMenu.ui')
        self.ui.show()
        #go back to main window after 3 seconds
        PySide6.QtCore.QTimer.singleShot(3000, self.mainmenu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())