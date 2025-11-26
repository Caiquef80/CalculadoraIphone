from PyQt5.QtWidgets import QApplication, QDialog
from main import Calculadora
 

if __name__ == "__main__":
    app = QApplication([])
    tela = Calculadora()
    app.exec_()
     