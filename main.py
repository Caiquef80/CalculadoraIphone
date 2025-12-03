from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import soma, sub , div ,mult, porc
class Calculadora(QMainWindow):
    
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      loadUi("interface.ui", self)
      self.show()
      self.num1 = 0
      self.num2 = 0
      self.selectedOperation = None
      self.setOperationList = {
         "+": soma,
         "-": sub,
         "/": div,
         "x": mult,
         "%": porc
      }

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
      self.btn_multiplicacao.clicked.connect(lambda: self.setOperation("x"))
      self.btn_subtracao.clicked.connect(lambda: self.setOperation("-"))
      self.btn_soma.clicked.connect(lambda: self.setOperation("+"))
      self.btn_divisao.clicked.connect(lambda: self.setOperation("/"))
      self.btn_porcentagem.clicked.connect(lambda: self.setOperation("%"))
      self.btn_float.clicked.connect(self.addComma)
      self.limpar.clicked.connect(self.cleanDisplay)
      self.btn_igual.clicked.connect(self.showResult)
      self.btn_comparativo.clicked.connect(self.invert)

   def addComma(self):
      ultimo = self.display.text()
      if(ultimo.count(",") > 0):
         resultado = ultimo
      else:
         resultado = ultimo + ","
      self.display.setText(resultado)



   def addNumber(self, numero):
      self.limpar.setText("<-")
      variavel =  self.display.text()
      if variavel == "0":
         resultado = str(numero)
      else:
         resultado = variavel + str(numero)
      self.display.setText(resultado)
    
   def cleanDisplay(self):
      if self.limpar.text() == "AC":
         self.display.setText("0")
         self.display_2.setText("0")
         self.num2 = 0
      else:
         ultimo = self.display.text()[:-1]
         if len(ultimo) == 0:              
            ultimo = "0"
            self.limpar.setText("AC")
         self.display.setText(ultimo)

           
   def invert(self):
      numero = int(self.display.text())
      numero = str(numero * -1)
      self.display.setText(numero)
      
   def percent(self):
      perc = self.getNumberDisplay(self.display)
      result = porc(self.num1, perc)
      self.setNumberDisplay(result)

    
   def setOperation(self , operation):
      self.selectedOperation = operation
      self.num1 = self.getNumberDisplay(self.display)
      self.num2 = 0
      result = self.display.text()
      self.display_2.setText(result)
      self.display.setText("0")
        

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
      if self.num2 == 0:          
         self.num2 = self.getNumberDisplay(self.display)
         
      num1 = self.num1
      num2 = self.num2
      operation = self.setOperationList.get(self.selectedOperation)
      
      result = operation(num1 , num2)
      self.num1 = result
      self.setNumberDisplay(result)
      self.setCalcDisplay(num1 , num2 , self.selectedOperation)
      self.limpar.setText("AC")