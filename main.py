from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence

class Calculadora(QMainWindow):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("interface.ui", self)
        self.show()
        # QShortcut(QKeySequence("0") , self).activated.connect(lambda: self.addNumber(0))
        self.btn1.clicked.connect(lambda: self.addNumber(1))
        self.btn2.clicked.connect(lambda: self.addNumber(2))
        self.btn3.clicked.connect(lambda: self.addNumber(3))
        self.btn4.clicked.connect(lambda: self.addNumber(4))
        self.btn5.clicked.connect(lambda: self.addNumber(5))
        self.btn6.clicked.connect(lambda: self.addNumber(6))
        self.btn7.clicked.connect(lambda: self.addNumber(7))
        self.btn8.clicked.connect(lambda: self.addNumber(8))
        self.btn9.clicked.connect(lambda: self.addNumber(9))
        self.btn0.clicked.connect(lambda: self.addNumber(0))
        self.limpar.clicked.connect(lambda:self.cleanDisplay("AC"))

    def addNumber(self, numero):
       variavel =  self.display.text()
       if variavel == "0":
           variavel = self.display.setText(str(numero))
       else:
        
        self.display.setText(variavel + str(numero))
        print(numero)
    
    def cleanDisplay(self , clean):
        return self.display.setText("0")