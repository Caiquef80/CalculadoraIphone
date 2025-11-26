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
        self.btn_multiplicacao.clicked.connect(self.setOperation)
        self.btn_subtracao.clicked.connect(self.setOperation)
        self.btn_soma.clicked.connect(self.setOperation)
        self.btn_divisao.clicked.connect(self.setOperation)
        self.btn_float.clicked.connect(self.addComma)
        self.limpar.clicked.connect(self.cleanDisplay)
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
    
    def cleanDisplay(self):
        self.display.setText("0")
    
    def setOperation(self):
       result = self.display.text()
       self.display_2.setText(result)
       self.cleanDisplay()

    def getNumberDisplay(self, display):
        num = display.text()
        if ("," in num):  
           num = num.replace(",",".")
           num = float(num)
        else: 
            num = int(num)
        return num
    def setNumberDisplay(self, number):
       number = str(number)
       number = number.replace("." , ",")
       self.display.setText(number)

    def setCalcDisplay(self, num1 , num2, operation):
       num1 = str(num1).replace("." , ",")
       num2 = str(num2).replace("." , ",")
       result = f"{num1} {operation} {num2}"
       self.display_2.setText(result)

    def showResult(self):
       num1 = self.getNumberDisplay(self.display)
       num2 = self.getNumberDisplay(self.display_2)
       result = soma(num1 , num2)
       self.setNumberDisplay(result)
       self.setCalcDisplay(num1 , num2 , "+")