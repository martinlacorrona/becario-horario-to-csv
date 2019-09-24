import sys
import timetable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QFormLayout,
        QLabel, QLineEdit, QPushButton, QFileDialog)

class Window(QWidget):
    passwordLabel2 = "Text"

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createFormGroupBox(), 0, 0)
        self.setLayout(grid)

        self.setWindowTitle("Becaria Timetable")
        self.resize(400, 300)

    def createFormGroupBox(self):
        formGroupBox = QGroupBox("Information")
        layout = QFormLayout()
        passwordLabel = QLineEdit()
        passwordLabel2 = passwordLabel
        passwordLabel.setEchoMode(QLineEdit.Password)
        usernameLabel = QLineEdit()
        isForNextWeekLabel = QCheckBox()
        layout.addRow(QLabel("Username:"), usernameLabel)
        layout.addRow(QLabel("Password:"), passwordLabel)
        layout.addRow(QLabel("IsForNextWeek:"), isForNextWeekLabel)
        button = QPushButton("Genereate")
        button.clicked.connect(self.button_pressed)
        layout.addRow(QLabel(), button)
        formGroupBox.setLayout(layout)
        return formGroupBox

    # def saveFileDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         print(fileName)

    def button_pressed(self):
        #print(formGroupBox.passwordLabel)
        #saveFileDialog()
        timetable.main("test.csv", "tatin", "tatin", False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())