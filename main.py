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
        self.sceneFranjas = QtWidgets.QGraphicsScene()

        self.sceneFranjas.setSceneRect(0, 0, 200, 200)


        self.ui.Franjas_graphicsView.setScene(self.sceneFranjas)

        self.secao = numpy.tile([1, 0], 5)
        self.v = 1
        self.ka=[0,0,25,50,75,100,125,150,175]

        self.line1=self.ui.L1_horizontalSlider.value()
        self.line2=self.ui.L2_horizontalSlider.value()
        self.lamb=self.ui.Lambda_horizontalSlider.value()

        # self.fran=franj(1,self.line1,self.line2,self.lamb)
        # print(self.lamb,self.line1,self.fran)
        print(numpy.absolute(-1))
        for i in range (0,9,1):
            if i==0:
                self.circ = QtWidgets.QGraphicsEllipseItem(0,0,200,200)
            else:
                self.circ = QtWidgets.QGraphicsEllipseItem((self.ka[i]/2)+(0/10),(self.ka[i]/2)+(0/10),200-self.ka[i]-(0/5),200-self.ka[i]-(0/5))  # (pos x,pos y,largura,altura)
            if int(self.secao[i]) == 0:

                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.red))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))

            self.sceneFranjas.addItem(self.circ)


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
        self.line1=self.ui.L1_horizontalSlider.value()
        self.fran = franj(1,self.line1, self.line2, self.lamb)
        print(self.fran)
        self.onUpdateFranjas()



    def onL2SliderMoveCallBack(self):
        self.ui.L2_lineEdit.setText(str(self.ui.L2_horizontalSlider.value()))
        self.line2=self.ui.L2_horizontalSlider.value()
        self.fran = franj(1,self.line1, self.line2, self.lamb)
        self.onUpdateFranjas()



    def onLambdaSliderMoveCallBack(self):
        self.ui.Lambda_lineEdit.setText(str(self.ui.Lambda_horizontalSlider.value()))
        self.lamb=self.ui.Lambda_horizontalSlider.value()
        self.fran = franj(1,self.line1, self.line2, self.lamb)
        self.onUpdateFranjas()

    def onL1LineEditChangeCallBack(self):

        self.ui.L1_horizontalSlider.setValue(int(self.ui.L1_lineEdit.text()[:-3]))
        self.line1 =int(self.ui.L1_lineEdit.text()[:-3])
        self.fran = franj(1, self.line1, self.line2, self.lamb)
        print(self.fran)
        self.onUpdateFranjas()

    def onL2LineEditChangeCallBack(self):

        self.ui.L2_horizontalSlider.setValue(int(self.ui.L2_lineEdit.text()[:-3]))
        self.line2=int(self.ui.L2_lineEdit.text()[:-3])
        self.fran = franj(1,self.line1, self.line2, self.lamb)
        self.onUpdateFranjas()

    def onLambdaLineEditChangeCallBack(self):
        self.ui.Lambda_horizontalSlider.setValue(int(self.ui.Lambda_lineEdit.text()[:-3]))
        self.lamb=int(self.ui.Lambda_lineEdit.text()[:-3])
        self.fran = franj(1,self.line1, self.line2, self.lamb)
        self.onUpdateFranjas()

    def onUpdateFranjas(self):

        self.sceneFranjas.clear()

        # print(self.secao[0], self.v)

        if numpy.floor(self.fran) >= self.v:
            self.secao = numpy.roll(self.secao, int(numpy.floor(self.fran)- self.v))  # caso sim ele da switch de cor branco pa preto
            self.v = numpy.floor(self.fran)

        if numpy.floor(self.fran) < self.v:  # verifica se o numero de franjas diminuiu
            self.secao = numpy.roll(self.secao, -1)
            self.v = numpy.floor(self.fran)

        print(self.fran, self.secao, self.secao[0])

        for i in range(0, 9, 1):
            if i == 0: #define o limite exterior das circunferencias
                self.circ = QtWidgets.QGraphicsEllipseItem(0, 0, 200, 200)
            else:
                self.circ = QtWidgets.QGraphicsEllipseItem((self.ka[i]/2) + (12.5*(self.fran-numpy.floor(self.fran))), (self.ka[i]/2) + (12.5*(self.fran-numpy.floor(self.fran))),
                                                           200 - self.ka[i] - (25*(self.fran-numpy.floor(self.fran))),
                                                           200 - self.ka[i] - (25*(self.fran-numpy.floor(self.fran)))) # (pos x,pos y,largura,altura)
            if int(self.secao[i]) == 0: #como secao da rotate permite alteracao de cores
                #print(colourization(self.ui.Lambda_horizontalSlider.value())) retorna os valores de rgb
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.red))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))

            self.sceneFranjas.addItem(self.circ)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()