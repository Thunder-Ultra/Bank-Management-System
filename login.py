from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(327, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(30, 30, 54, 17)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(30, 80, 54, 17)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(110, 30, 191, 29)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(110, 80, 191, 29)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(130, 130, 85, 27)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(220, 130, 85, 27)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(0, 0, 327, 25)
        MainWindow.setMenuBar(self.menubar)

        self.actionNewUser = QtWidgets.QAction(MainWindow)
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.addAction(self.actionNewUser)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Log In ")
        self.label.setText("User ID")
        self.label_2.setText("Password")
        self.pushButton.setText("Reset")
        self.pushButton_2.setText("Log In")
        self.menuFile.setTitle("File")
        self.actionNewUser.setText("New User")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
