#from func import desfazamento, colourization, circunferencia, desenho, franj
#import numpy

#cont=0 #variavel para rotacao de cores
#comprimento=680 # em 10^-6  laser da experiencia esta em 632.8*10^-6
#distancia=10200 #em 10^-7  precisao do parafuso micro = 0.1*10^-6


#print(desfazamento(0.2,.1,1,comprimento))

#print(colourization(comprimento)) #RGB

#tppcomp=circunferencia(comprimento)#defenir circunf do comp de onda
#print(tppcomp)

#section=numpy.tile([1,0],3) #criar vetor alternado de 1 e 0's
#print(section)

# calculo da franja

#franja=franj(1,distancia,comprimento) #determinar n da freanja
#print(numpy.floor(franja))

#teste do desenho
#print(section)
#franja,vectortrue,cont,section = desenho(tppcomp,section,cont, franja, comprimento)

#print(franja,vectortrue,section,cont)

#print(desenho(tppcomp,section,cont, franja,comprimento))

from func import *
from PyQt5 import QtWidgets
from IDM_GUI_QT5 import Ui_MainWindow
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ###INTERFACE CALLBACKS

        #Sliders
        self.ui.L1_horizontalSlider.valueChanged.connect(self.onL1SliderMoveCallBack)
        self.ui.L2_horizontalSlider.valueChanged.connect(self.onL2SliderMoveCallBack)
        self.ui.Lambda_horizontalSlider.valueChanged.connect(self.onLambdaSliderMoveCallBack)

        #Line Edits

        self.ui.L1_lineEdit.editingFinished.connect(self.onL1LineEditChangeCallBack)
        self.ui.L2_lineEdit.editingFinished.connect(self.onL2LineEditChangeCallBack)
        self.ui.Lambda_lineEdit.editingFinished.connect(self.onLambdaLineEditChangeCallBack)

    def onL1SliderMoveCallBack(self):

        self.ui.L1_lineEdit.setText(str(self.ui.L1_horizontalSlider.value()))

    def onL2SliderMoveCallBack(self):

        self.ui.L2_lineEdit.setText(str(self.ui.L2_horizontalSlider.value()))

    def onLambdaSliderMoveCallBack(self):

        self.ui.Lambda_lineEdit.setText(str(self.ui.Lambda_horizontalSlider.value()))

    def onL1LineEditChangeCallBack(self):

        self.ui.L1_horizontalSlider.setValue(int(self.ui.L1_lineEdit.text()[:-3]))

    def onL2LineEditChangeCallBack(self):

        self.ui.L2_horizontalSlider.setValue(int(self.ui.L2_lineEdit.text()[:-3]))

    def onLambdaLineEditChangeCallBack(self):
        self.ui.Lambda_horizontalSlider.setValue(int(self.ui.Lambda_lineEdit.text()[:-3]))

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()