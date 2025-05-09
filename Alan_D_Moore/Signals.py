'''


'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton
import time

class MainWindow(QMainWindow):
    def __init__(self,):
        
        super().__init__()
        self.setWindowTitle('Sam\'s Window')
        button=QPushButton('Press Me')
        button.setCheckable(True)
        button.clicked.connect(self.press_me)
        
        self.setCentralWidget(button)
    def press_me(self):
        print(' Sam pressed me')
app= QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()    