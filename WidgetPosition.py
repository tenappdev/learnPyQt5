import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        #create widget and components
        self.label = QLabel('Sawasdee PyQt5', self) #label เป็นตัวแปรที่สร้างขึ้นมาใหม่
        self.label.move(150,50)

        self.buttonExit = QPushButton('Exit',self) #buttonExit เป็นตัวแปรที่สร้างขึ้นมาใหม่
        self.buttonExit.setGeometry(150,130,100,28)

        #initial window
        self.setWindowTitle('Widget Position')
        self.setWindowIcon(QtGui.QIcon('.\images\Arrow.png'))
        self.setGeometry(100,100,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
