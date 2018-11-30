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
from PyQt5 import QtWidgets, QtGui, QtCore
from IDM_GUI_QT5 import Ui_MainWindow
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        font = QtGui.QFont('White Rabbit')
        font.setPointSize(120)
        brush1= QtGui.QBrush()
        pen1 = QtGui.QPen()
        # rect=.QtWidgets.QRec
        # Since the UI is a QGraphicsView, I create a Scene
        # so it has something to show
        self.scene = QtWidgets.QGraphicsScene()
        # self.extcrect= QtWidgets.QGraphicsRectItem(20,10,300,200)
        # self.extcrect.setBrush()
        self.scene.setSceneRect(0, 0, 200, 200)
        # self.dot1 = QtWidgets.QGraphicsTextItem(':')
        # self.dot1.setFont(font)
        # self.dot1.setPos(140, 0)
        # self.scene.addItem(self.dot1)
        self.circ1 = QtWidgets.QGraphicsEllipseItem(0, 0, 200, 200)  # posx e posy sao o canto superior esquerdo
        # self.circ3.setPen(QtGui.QPen(QtCore.Qt.red, 25))
        self.circ1.setBrush(QtGui.QBrush(QtCore.Qt.red))
        self.scene.addItem(self.circ1)

        self.circ2= QtWidgets.QGraphicsEllipseItem(25,25,150,150) #posx e posy sao o canto superior esquerdo
        self.circ2.setBrush(QtGui.QBrush(QtCore.Qt.white))
        self.scene.addItem(self.circ2)

        self.circ3= QtWidgets.QGraphicsEllipseItem(50,50,100,100) #(pos x,pos y,largura,altura)
        self.circ3.setBrush(QtGui.QBrush(QtCore.Qt.red))
        self.scene.addItem(self.circ3)

        self.circ4= QtWidgets.QGraphicsEllipseItem(75,75,50,50) #(pos x,pos y,largura,altura)
        self.circ4.setBrush(QtGui.QBrush(QtCore.Qt.white))
        self.scene.addItem(self.circ4)
        self.ui.Franjas_graphicsView.setScene(self.scene)

        # self.brush=QBrs

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
        # self.exactRect = QtWidgets.QGraphicsRectItem(20, 10, 300, 200)
        # self.ui.Franjas_graphicsView.setSceneRect(self.exactRect)
        self.ui.Franjas_graphicsView.setScene(self.scene)
        #self.scene.addLine(5)
        #self.ui.Franjas_graphicsView.items(1)



    def onL2SliderMoveCallBack(self):

        self.ui.L2_lineEdit.setText(str(self.ui.L2_horizontalSlider.value()))
        kk=self.ui.L2_horizontalSlider.value()
        self.scene.clear()
        ka=[50,100,150,200]
        # self.circ4 = QtWidgets.QGraphicsEllipseItem(kk/10, kk/10, 200-(kk/5), 200-(kk/5))  # (pos x,pos y,largura,altura)
        # self.circ4.setBrush(QtGui.QBrush(QtCore.Qt.white))
        # self.scene.addItem(self.circ4)
        # self.circ5 = QtWidgets.QGraphicsEllipseItem(25+(kk/10), 25+(kk/10), 150-(kk/5), 150-(kk/5))  # (pos x,pos y,largura,altura)
        # self.circ5.setBrush(QtGui.QBrush(QtCore.Qt.red))
        # self.scene.addItem(self.circ5)
        for i in range(0,200,50):
            self.circ = QtWidgets.QGraphicsEllipseItem((i/2)+(kk/10),(i/2)+(kk/10), 200-i-(kk/5), 200-i-(kk/5))  # (pos x,pos y,largura,altura)
            if (i%100)==0:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.red))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))
            self.scene.addItem(self.circ)



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