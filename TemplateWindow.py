import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
 
#class Window(QWidget):
#class Window(QMainWindow):
class Window(QDialog):
    #constructor 
    def __init__(self):
        super().__init__()
         
        #create widget and components here

        #initial window
        self.setWindowTitle('Template Window')
        #self.setWindowIcon(QtGui.QIcon('.\images\Arrows.png'))
        self.setGeometry(100,100,400,200)
        self.show()

#main start
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Macintosh')
    window = Window()
    sys.exit(app.exec())
