from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import soma
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
        self.btn_float.clicked.connect(self.addComma)
        self.limpar.clicked.connect(lambda:self.cleanDisplay("AC"))
        self.btn_igual.clicked.connect(self.showResult)

    def addComma(self):
       ultimo = self.display.text()
       if(ultimo.count(",") > 0):
          resultado = ultimo
       else:
        resultado = ultimo + ","
       
       self.display.setText(resultado)



    def addNumber(self, numero):
       variavel =  self.display.text()
       if variavel == "0":
           variavel = self.display.setText(str(numero))
       else:
        
        self.display.setText(variavel + str(numero))
        print(numero)
    
    def cleanDisplay(self , clean):
        return self.display.setText("0")
    
    def showResult(self):
       num1 = self.display.text()
       num2 = 2
       if ("," in num1):  
           num1 = num1.replace(",",".")
           num1 = float(num1)
       else: 
            num1 = int(num1)
       result = soma(num1 , num2)
       print(f'Numero: {result}')
       print(f"Tipo:",  type(result))