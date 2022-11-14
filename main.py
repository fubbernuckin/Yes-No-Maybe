from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('test.ui', self)
        self.show()
        #when button is clicked go to different ui
        self.pushButton.clicked.connect(self.goToYes)
        self.pushButton_2.clicked.connect(self.goToNo)
        self.pushButton_3.clicked.connect(self.goToMaybe)
        self.pushButton_4.clicked.connect(self.goToOther)
    def goToYes(self):
        self.hide()
        uic.loadUi('yes.ui', self)
        self.show()
    def goToNo(self):
        self.hide()
        uic.loadUi('no.ui', self)
        self.show()
    def goToMaybe(self):
        self.hide()
        uic.loadUi('question.ui', self)
        self.show()
    def goToOther(self):
        self.hide()
        uic.loadUi('altMenu.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedHeight(800)
window.setFixedWidth(450)
app.exec_()
