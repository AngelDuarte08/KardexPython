import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox,
                             QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)

class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.starUI()
        
    def starUI(self):
        self.setGeometry(100,100, 350, 250)
        self.setWindowTitle("KardexUPPE")
        self.generateForm()
        self.show()

    #Generate the graphic interface
    def generateForm(self):
        self.ifLogged = False

        lUser = QLabel(self)
        lUser.setText("Usuario: ")
        lUser.setFont(QFont('Arial',10))
        lUser.move(20,54)

        self.leUser = QLineEdit(self)
        self.leUser.resize(250, 24)
        self.leUser.move(90,50)

        lPassword = QLabel(self)
        lPassword.setText("Password: ")
        lPassword.setFont(QFont('Arial',10))
        lPassword.move(20,86)

        self.lPassword = QLineEdit(self)
        self.lPassword.resize(250, 24)
        self.lPassword.move(90,82) 
        self.lPassword.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        
        self.checkViewPassword = QCheckBox(self)
        self.checkViewPassword.setText("Ver Constraseña")
        self.checkViewPassword.move(90,110)

        bLogin = QPushButton(self)
        bLogin.setText("Login")
        bLogin.resize(320, 34)
        bLogin.move(20,140)

    