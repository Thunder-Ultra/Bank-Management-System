from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from csv import reader

App = QApplication([])
log_in = QMainWindow()

def abs_address(relative_address):
    from os.path import dirname, abspath
    address = abspath(dirname(__file__))
    return address + '/' + relative_address

def submit(user,password):
    with open('credintials.csv') as f:
        db = reader(f)
        for record in db :
            if record[0] == user:
                if record [1] == password:
                    name_status.setText('Logged in successfully ')
                else:
                    print('Username or Password Invalid')

            else:
                print('Username or Password Invalid')

def check_name(new_value):
    valid_characters = 'abcdefghijklmnopqrstuvwxyz'
    for c in new_value:
        if c not in valid_characters:
            name_status.setText('Username invalid')
            break
    else:
        name_status.setText('Username valid')

    

#------------Widgets
name_label = QLabel('User ID :',log_in)
name_entry = QLineEdit(log_in)
name_status=QLabel(log_in)
name_entry.setMaximumWidth(350)

password_label = QLabel('Password :',log_in)
pass_entry = QLineEdit(log_in)
pass_entry.setMaximumWidth(350)

ok = QPushButton('OK',log_in)
reset = QPushButton('Reset',log_in)
abort = QPushButton('Abort',log_in)

#---------Style
log_in.setWindowIcon(QIcon(abs_address('images/start-here.png')))
log_in.setFixedSize(500,200)

name_label.move(50,30)
name_entry.move(200,30)
name_status.setGeometry(200,65,200,20)

name_entry.setFixedWidth(200)
password_label.move(50,100)
pass_entry.move(200,100)
pass_entry.setFixedWidth(200)
abort.move(40,160)
reset.move(150,160)
ok.move(260,160)

#------connections
name_entry.textChanged.connect(check_name)
ok.clicked.connect(submit)
reset.clicked.connect(pass_entry.clear)
reset.clicked.connect(name_entry.clear)
abort.clicked.connect(App.exit)


log_in.show()
App.exec_()
