import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from space_farmers_ui import Ui_Form
from get_mission import get


class App(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_mission)
        self.pushButton_2.clicked.connect(self.days)
        self.pushButton_3.clicked.connect(self.res_in_point)
        self.pushButton_4.clicked.connect(self.res_now)
        self.pushButton_5.clicked.connect(self.rect)
        self.pushButton_6.clicked.connect(self.autoklav)
        self.pushButton_7.clicked.connect(self.sh)
        self.s = """"""

    def get_mission(self):
        mis = get()
        self.s += '\n'.join(f'Расстояние:{str(i[0])}\tSH:{str(i[1])}' for i in mis) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def sh(self):
        self.s += '\n'.join(['sh' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def autoklav(self):
        self.s += '\n'.join(['autoklav' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def react(self):
        self.s += '\n'.join(['react' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def res_now(self):
        self.s += '\n'.join(['res_now' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def res_in_point(self):
        self.s += '\n'.join(['res_in_point' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)

    def days(self):
        self.s += '\n'.join(['days' for i in range(5)]) + '\n'
        self.plainTextEdit.setPlainText(self.s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
