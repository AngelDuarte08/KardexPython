import sys
from Views.Login import Login
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
login = Login()
login.starUI()
sys.exit(app.exec())
