'''

'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg


# class MainWindow(qtw.QMainWindow):
#     def __init__(self, title):
#         super().__init__()
    
#         self.setWindowTitle(title)
#         self.setGeometry(100, 100, 800, 600)
        
#         ## create a textEdit Widget
#         self.textEdit=qtw.QTextEdit()
#         self.textEdit.setReadOnly(False)
        
#         ## create a vertical layout
#         # layout = qtw.QWidget()
#         # layout.setLayout(qtw.QVBoxLayout())
#         ## or
#         layout=qtw.QVBoxLayout()
#         ## add textEdit to layout
#         layout.addWidget(self.textEdit)
        
#         ## create a centralWidget and apply the layout
#         central_widget=qtw.QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

        # # Create a QTextEdit widget
        # self.text_edit = qtw.QTextEdit()
        # self.text_edit.setReadOnly(False)  # Allow editing

        # # Create a vertical layout
        # layout = qtw.QVBoxLayout()
        # layout.addWidget(self.text_edit)

        # myButton = qtw.QPushButton('Push Me')
        # myButton.setCheckable(True)
        # myButton.clicked.connect(self.butClick)  # Connect button click event to butClick() method of MainWindow class object (self).
        # layout.addWidget(myButton)

        # # Create a central widget and apply the layout
        # central_widget = qtw.QWidget()
        # central_widget.setLayout(layout)
        # self.setCentralWidget(central_widget)

    # def butClick(self):
    #     print('You pressed the button!')
    
    
#         self.show()
    
    
    
# if __name__ == '__main__':
#     app =qtw.QApplication(sys.argv)
#     window=MainWindow('another window by me')
#     sys.exit(app.exec_())
    
    
    
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):
    def __init__(self, title):
        super().__init__()
    
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 800, 600)
        layout = qtw.QVBoxLayout()
        ## create a textEdit Widget
        textEdit=qtw.QTextEdit()
        textEdit.setReadOnly(False)
        ## add textEdit to layout
        layout.addWidget(textEdit)
        h_layout=qtw.QHBoxLayout()
        # creae a label
        Label=qtw.QLabel('this is a label')
        Label.setText('This is a label')
        Label.setAlignment(qtc.Qt.AlignLeft)
        Label.setStyleSheet('color:blue; font-size: 20px;')
        # add Label and lineEdit to h_layout
        h_layout.addWidget(Label)
        h_layout.addStretch()
        h_layout.addWidget(qtw.QLabel('this is a label2'))
        
        
        h_layout.addStretch()
        # add h_layout to layout
        # layout.addLayout(h_layout)
        # create a lineEdit
        lineEdit=qtw.QLineEdit()
        lineEdit.setPlaceholderText('Enter text here')
        lineEdit.setText('This is a lineEdit')
        h_layout.addWidget(lineEdit)
        
        ## create a centralWidget and apply the layout
        centralWidget=qtw.QWidget()
        # centralWidget.setLayout(layout)
        centralWidget.setLayout(h_layout)
        self.setCentralWidget(centralWidget)
        
        
        self.show()
        
        
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w=MainWindow('This is my Window!')
    sys.exit(app.exec_())
    