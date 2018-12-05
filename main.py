import numpy
from func import *
from PyQt5 import QtWidgets, QtGui, QtCore
from IDM_GUI_QT5 import Ui_MainWindow
import sys, numpy



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Since the UI is a QGraphicsView, I create a Scene
        # so it has something to show
        self.scene = QtWidgets.QGraphicsScene()
        self.sceneScheme = QtWidgets.QGraphicsScene()

        self.scene.setSceneRect(0, 0, 200, 200)
        self.sceneScheme.setSceneRect(0, 0, 500, 312)

        self.ui.Franjas_graphicsView.setScene(self.scene)
        self.ui.Scheme_graphicsView.setScene(self.sceneScheme)

        self.schemaPixmap = QtGui.QPixmap('esquema_idm.png')
        self.onUpdateColors()

        self.secao = numpy.tile([1, 0], 5)
        self.v = 1
        self.ka=[0,0,25,50,75,100,125,150,175]

        self.onUpdateGraphics()

        for i in range (0,9,1):
            if i==0:
                self.circ = QtWidgets.QGraphicsEllipseItem(0,0,200,200)
            else:
                self.circ = QtWidgets.QGraphicsEllipseItem((self.ka[i]/2)+(0/10),(self.ka[i]/2)+(0/10),200-self.ka[i]-(0/5),200-self.ka[i]-(0/5))  # (pos x,pos y,largura,altura)
            if int(self.secao[i]) == 0:

                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.red))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))

            self.scene.addItem(self.circ)


        ###INTERFACE CALLBACKS

        #Sliders
        self.ui.L1_horizontalSlider.valueChanged.connect(self.onL1SliderMoveCallBack)
        self.ui.L2_horizontalSlider.valueChanged.connect(self.onL2SliderMoveCallBack)
        self.ui.Lambda_horizontalSlider.valueChanged.connect(self.onLambdaSliderMoveCallBack)

        #Line Edits

        self.ui.L1_lineEdit.editingFinished.connect(self.onL1LineEditChangeCallBack)
        self.ui.L2_lineEdit.editingFinished.connect(self.onL2LineEditChangeCallBack)
        self.ui.Lambda_lineEdit.editingFinished.connect(self.onLambdaLineEditChangeCallBack)

    def onUpdateColors(self):

        self.r, self.g, self.b, self.a = colourization(int(self.ui.Lambda_horizontalSlider.value()))
        print(self.r*255, self.g*255, self.b*255, self.a*255)
        self.colorQT = QtGui.QColor(self.r*255, self.g*255, self.b*255, self.a*255)

    def onL1SliderMoveCallBack(self):

        self.ui.L1_lineEdit.setText(str(self.ui.L1_horizontalSlider.value()))

        self.ui.Franjas_graphicsView.setScene(self.scene)
        self.onUpdateGraphics()



    def onL2SliderMoveCallBack(self):


        self.ui.L2_lineEdit.setText(str(self.ui.L2_horizontalSlider.value()))
        self.loopback(self.ui.L2_horizontalSlider.value())
        self.onUpdateGraphics()


    def onLambdaSliderMoveCallBack(self):

        self.ui.Lambda_lineEdit.setText(str(self.ui.Lambda_horizontalSlider.value()))
        self.onUpdateColors()
        self.onUpdateGraphics()

    def onL1LineEditChangeCallBack(self):

        self.ui.L1_horizontalSlider.setValue(int(self.ui.L1_lineEdit.text()[:-3]))

    def onL2LineEditChangeCallBack(self):

        self.ui.L2_horizontalSlider.setValue(int(self.ui.L2_lineEdit.text()[:-3]))

    def onLambdaLineEditChangeCallBack(self):
        self.ui.Lambda_horizontalSlider.setValue(int(self.ui.Lambda_lineEdit.text()[:-3]))

    def loopback(self, kdis):
        self.scene.clear()
        val = numpy.floor(kdis / 125)
        print(self.secao[0], self.v)

        if val >= self.v:
            self.secao = numpy.roll(self.secao, int(val - self.v))  # caso sim ele da switch de cor branco pa preto
            self.v = val

        if val < self.v:  # verifica se o numero de franjas diminuiu
            self.secao = numpy.roll(self.secao, -1)
            self.v = val

        print(kdis, val) #state check para ver se ta tudo ok
        kk = kdis - ((self.v) * 125)
        print(kk, self.secao, self.secao[0])

        for i in range(0, 9, 1):
            if i == 0: #define o limite exterior das circunferencias
                self.circ = QtWidgets.QGraphicsEllipseItem(0, 0, 200, 200)
            else:
                self.circ = QtWidgets.QGraphicsEllipseItem((self.ka[i] / 2) + (kk / 10), (self.ka[i] / 2) + (kk / 10),
                                                           200 - self.ka[i] - (kk / 5),
                                                           200 - self.ka[i] - (kk / 5))  # (pos x,pos y,largura,altura)
            if int(self.secao[i]) == 0: #como secao da rotate permite alteracao de cores

                #print(colourization(self.ui.Lambda_horizontalSlider.value())) retorna os valores de rgb
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.red))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))

            self.scene.addItem(self.circ)

    def onUpdateScheme(self):
            self.sceneScheme.clear()
            self.sceneScheme.addPixmap(self.schemaPixmap)

            self.mirrorL2 = QtWidgets.QGraphicsRectItem(470+0.1*int(self.ui.L2_horizontalSlider.value()), 131, 5, 70)
            self.mirrorL2.setBrush(QtGui.QBrush(QtCore.Qt.black))
            self.mirrorL1 = QtWidgets.QGraphicsRectItem(205,21-0.1*int(self.ui.L1_horizontalSlider.value()), 70, 5)
            self.mirrorL1.setBrush(QtGui.QBrush(QtCore.Qt.black))

            self.sceneScheme.addLine(QtCore.QLineF(99, 155, 240, 155), self.colorQT) #line from lazer to middle
            self.sceneScheme.addLine(QtCore.QLineF(250, 166, 250, 236), self.colorQT)  # line from middle to lense L1
            self.sceneScheme.addLine(QtCore.QLineF(248, 169, 250, 236), self.colorQT)#line from middle to lense L2
            self.sceneScheme.addLine(QtCore.QLineF(239, 155, 240, 21-0.1*int(self.ui.L1_horizontalSlider.value())), self.colorQT)  # line from middle to L1
            self.sceneScheme.addLine(QtCore.QLineF(245, 149, 240, 21-0.1*int(self.ui.L1_horizontalSlider.value())), self.colorQT)  # line from L1 to middle
            self.sceneScheme.addLine(QtCore.QLineF(470+0.1*int(self.ui.L2_horizontalSlider.value()), 166, 258, 160), self.colorQT)  # line from middle to L2
            self.sceneScheme.addLine(QtCore.QLineF(470+0.1*int(self.ui.L2_horizontalSlider.value()), 166, 250, 167), self.colorQT)  # line from L2 to middle
            self.sceneScheme.addLine(QtCore.QLineF(250, 250, 250, 299), self.colorQT) #lense to observer
            self.sceneScheme.addItem(self.mirrorL1)# Espelho L1
            self.sceneScheme.addItem(self.mirrorL2) #Espelho L2

    def onUpdateGraphics(self):

        self.onUpdateScheme()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()