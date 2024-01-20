import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import calculadora


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("untitled.ui", self) #NOME DO ARQUIVO .ui para ser convertido dinamicamente

        self.somar.clicked.connect(self.clickhandlersoma)
        self.subtrair.clicked.connect(self.clickhandlersubtrai)
        self.multiplicar.clicked.connect(self.clickhandlermultiplica)
        self.dividir.clicked.connect(self.clickhandlerdivide)
        
    def clickhandlersoma(self):
        try:
            a = float(self.entrada1.text())
            b = float(self.entrada2.text())
            result= calculadora.somar(a,b)
            self.resultado.setText(f'{result:.2f}')
        except ValueError:
            self.resultado.setText("VALOR INCORRETO DIGITE NUMEROS INTEIROS OU REAIS")

    def clickhandlersubtrai(self):
        try:
            a = float(self.entrada1.text())
            b = float(self.entrada2.text())
            result= calculadora.subtrair(a,b)
            self.resultado.setText(f'{result:.2f}')
        except ValueError:
            self.resultado.setText("VALOR INCORRETO DIGITE NUMEROS INTEIROS OU REAIS")

    def clickhandlermultiplica(self):
        try:
            a = float(self.entrada1.text())
            b = float(self.entrada2.text())
            result= calculadora.multiplicar(a,b)
            self.resultado.setText(f'{result:.2f}')
        except ValueError:
            self.resultado.setText("VALOR INCORRETO DIGITE NUMEROS INTEIROS OU REAIS")

    def clickhandlerdivide(self):
        try:
            a = float(self.entrada1.text())
            b = float(self.entrada2.text())
            result= calculadora.dividir(a,b)
            self.resultado.setText(f'{result:.2f}')
        except:
            self.resultado.setText("VALOR INCORRETO DIGITE NUMEROS INTEIROS OU REAIS\n2º NUMERO DEVE SER DIFERENTE DE 0")

    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()