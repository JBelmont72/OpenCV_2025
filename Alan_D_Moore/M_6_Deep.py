'''

'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the QTextEdit widget
        self.text_edit = qtw.QTextEdit()
        self.text_edit.setReadOnly(False)  # Allow editing

        # Create a vertical layout
        layout = qtw.QVBoxLayout()
        layout.addWidget(self.text_edit)

        myButton=qtw.QPushButton('Push Me')
        myButton.setGeometry(200,200,50,50)
        myButton.setCheckable(True)
        myButton.clicked.connect(self.butClick)  # Connect button click event to butClick() method of MainWindow class object (self).
        layout.addWidget(myButton)
    
        
        
        # Create a central widget and apply the layout
        central_widget = qtw.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create a 'File' menu
        file_menu = menu_bar.addMenu('File')

        # Add actions to the 'File' menu
        file_menu.addAction('Open', self.open_file)
        file_menu.addAction('Save', self.save_file)
        file_menu.addSeparator()
        file_menu.addAction('Quit', self.close)

        # Create a status bar
        self.statusBar().showMessage('Welcome to my editor', 2000)

        # Create a button (optional - removed unnecessary geometry)
        self.my_button = qtw.QPushButton('Push Me')
        self.my_button.clicked.connect(self.butClick)  # Connect button click

    def butClick(self):
        print('You pressed the button!')

    def open_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Open File", "", "*.txt")
        if filename:
            try:
                with open(filename, 'r') as handle:
                    text = handle.read()
                self.text_edit.clear()
                self.text_edit.insertPlainText(text)
                self.statusBar().showMessage(f'Opened: {filename}')
            except Exception as e:
                self.statusBar().showMessage(f"Error opening file: {e}")

    def save_file(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", "", "*.txt")
        if filename:
            try:
                text = self.text_edit.toPlainText()
                with open(filename, 'w') as handle:
                    handle.write(text)
                self.statusBar().showMessage(f'Saved to {filename}')
            except Exception as e:
                self.statusBar().showMessage(f"Error saving file: {e}")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())