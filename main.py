import ctypes
import sys

import numpy as np
import pyqtgraph
from PyQt5 import QtWidgets, QtGui, QtCore

from IDM_GUI_QT5 import Ui_MainWindow
from func import *

#show icon on windows task bar

myappid = 'interferometrodemichelson' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Since the UI is a QGraphicsView, I create a Scene
        # so it has something to show
        self.firstRun = True
        self.sceneFranjas = QtWidgets.QGraphicsScene()
        self.sceneScheme = QtWidgets.QGraphicsScene()

        self.sceneFranjas.setSceneRect(0, 0, 200, 200)
        self.sceneScheme.setSceneRect(0, 0, 500, 312)

        self.ui.Franjas_graphicsView.setScene(self.sceneFranjas)
        self.ui.Scheme_graphicsView.setScene(self.sceneScheme)

        self.schemaPixmap = QtGui.QPixmap('gui\scheme\esquema_idm.png')
        self.onUpdateColors()

        self.secao = np.tile([1, 0], 5)
        self.v = 1
        self.ka=[0,0,25,50,75,100,125,150,175]

        self.onUpdateVars()

        #print("xx",self.lamb,self.line1,self.fran)

        self.onUpdateColors()
        self.onUpdateGraphics()


        ###INTERFACE CALLBACKS

        #Sliders
        self.ui.L1_horizontalSlider.valueChanged.connect(self.onL1SliderMoveCallBack)
        self.ui.L2_horizontalSlider.valueChanged.connect(self.onL2SliderMoveCallBack)
        self.ui.Lambda_horizontalSlider.valueChanged.connect(self.onLambdaSliderMoveCallBack)

        #Line Edits

        self.ui.L1_lineEdit.editingFinished.connect(self.onL1LineEditChangeCallBack)
        self.ui.L2_lineEdit.editingFinished.connect(self.onL2LineEditChangeCallBack)
        self.ui.Lambda_lineEdit.editingFinished.connect(self.onLambdaLineEditChangeCallBack)
        self.ui.L1_lineEdit.setText("  " + str(self.ui.L1_horizontalSlider.value() * 0.01))
        self.ui.L2_lineEdit.setText("  " + str(self.ui.L2_horizontalSlider.value() * 0.01))
        #Spin Box
        self.ui.IR_doubleSpinBox.valueChanged.connect(self.onIRSpinBoxChangeCallBack)


        self.firstRun = False


    def onUpdateColors(self):

        self.r, self.g, self.b, self.a = colourization(int(self.ui.Lambda_horizontalSlider.value()))
        #print(self.r*255, self.g*255, self.b*255, self.a*255)
        self.colorQT = QtGui.QColor(self.r*255, self.g*255, self.b*255, self.a*255)

    def onL1SliderMoveCallBack(self):
        if(self.ui.L1_horizontalSlider.value()<1000):

            self.ui.L1_lineEdit.setText("  "+str(self.ui.L1_horizontalSlider.value()*0.01))
        elif (self.ui.L1_horizontalSlider.value() < 10000):
            self.ui.L1_lineEdit.setText(" " + str(self.ui.L1_horizontalSlider.value() * 0.01))
        else:
            self.ui.L1_lineEdit.setText(str(self.ui.L1_horizontalSlider.value() * 0.01))
        self.onUpdateVars()

        self.onUpdateGraphics()



    def onL2SliderMoveCallBack(self):

        if(self.ui.L2_horizontalSlider.value()<1000):

            self.ui.L2_lineEdit.setText("  "+str(self.ui.L2_horizontalSlider.value()*0.01))

        elif (self.ui.L2_horizontalSlider.value() < 10000):

            self.ui.L2_lineEdit.setText(" " + str(self.ui.L2_horizontalSlider.value() * 0.01))
        else:
            self.ui.L2_lineEdit.setText(str(self.ui.L2_horizontalSlider.value()*0.01))

        self.onUpdateVars()

        self.onUpdateGraphics()


    def onLambdaSliderMoveCallBack(self):

        self.ui.Lambda_lineEdit.setText(str(self.ui.Lambda_horizontalSlider.value()))

        self.onUpdateVars()

        self.onUpdateColors()
        self.onUpdateGraphics()

    def onL1LineEditChangeCallBack(self):

        self.ui.L1_horizontalSlider.setValue(float(self.ui.L1_lineEdit.text()[:-3])*100)

        self.onUpdateVars()

        self.onUpdateGraphics()

    def onL2LineEditChangeCallBack(self):
        self.onUpdateVars()
        self.ui.L2_horizontalSlider.setValue(float(self.ui.L2_lineEdit.text()[:-3])*100)
        self.line2=float(self.ui.L2_lineEdit.text()[:-3])*100
        self.fran = franj(self.ir,self.line1, self.line2, self.lamb)
        self.onUpdateGraphics()

    def onLambdaLineEditChangeCallBack(self):

        self.ui.Lambda_horizontalSlider.setValue(int(self.ui.Lambda_lineEdit.text()[:-3]))

        self.onUpdateVars()

        self.onUpdateGraphics()

    def onIRSpinBoxChangeCallBack(self):

        self.onUpdateVars()
        self.onUpdateGraphics()

    def onUpdateFranjas(self):

        self.sceneFranjas.clear()

        if np.floor(self.fran) >= self.v:
            self.secao = np.roll(self.secao, int(np.floor(self.fran)- self.v))  # caso sim ele da switch de cor branco pa preto
            self.v = np.floor(self.fran)

        if np.floor(self.fran) < self.v:  # verifica se o numero de franjas diminuiu
            self.secao = np.roll(self.secao, -1)
            self.v = np.floor(self.fran)

        #print(self.fran, self.secao, self.secao[0])

        for i in range(0, 9, 1):
            if i == 0: #define o limite exterior das circunferencias
                self.circ = QtWidgets.QGraphicsEllipseItem(0, 0, 200, 200)
            else:
                self.circ = QtWidgets.QGraphicsEllipseItem((self.ka[i]/2) + (12.5*(self.fran-np.floor(self.fran))), (self.ka[i]/2) + (12.5*(self.fran-np.floor(self.fran))),
                                                           200 - self.ka[i] - (25*(self.fran-np.floor(self.fran))),
                                                           200 - self.ka[i] - (25*(self.fran-np.floor(self.fran)))) # (pos x,pos y,largura,altura)
            if int(self.secao[i]) == 0: #como secao da rotate permite alteracao de cores
                #print(colourization(self.ui.Lambda_horizontalSlider.value())) retorna os valores de rgb
                self.circ.setBrush(QtGui.QBrush(self.colorQT))
            else:
                self.circ.setBrush(QtGui.QBrush(QtCore.Qt.white))

            self.sceneFranjas.addItem(self.circ)


    def onUpdateScheme(self):
            self.sceneScheme.clear()
            self.sceneScheme.addPixmap(self.schemaPixmap)

            self.onUpdateVars()

            self.mirrorL2 = QtWidgets.QGraphicsRectItem(470+0.1*self.line2, 131, 5, 70)
            self.mirrorL2.setBrush(QtGui.QBrush(QtCore.Qt.black))
            self.mirrorL1 = QtWidgets.QGraphicsRectItem(205,21-0.1*self.line1, 70, 5)
            self.mirrorL1.setBrush(QtGui.QBrush(QtCore.Qt.black))

            self.sceneScheme.addLine(QtCore.QLineF(99, 155, 240, 155), self.colorQT) #line from lazer to middle
            self.sceneScheme.addLine(QtCore.QLineF(250, 166, 250, 236), self.colorQT)  # line from middle to lense L1
            self.sceneScheme.addLine(QtCore.QLineF(248, 169, 250, 236), self.colorQT)#line from middle to lense L2
            self.sceneScheme.addLine(QtCore.QLineF(239, 155, 240, 21-0.1*self.line1), self.colorQT)  # line from middle to L1
            self.sceneScheme.addLine(QtCore.QLineF(245, 149, 240, 21-0.1*self.line1), self.colorQT)  # line from L1 to middle
            self.sceneScheme.addLine(QtCore.QLineF(470+0.1*self.line2, 166, 258, 160), self.colorQT)  # line from middle to L2
            self.sceneScheme.addLine(QtCore.QLineF(470+0.1*self.line2, 166, 250, 167), self.colorQT)  # line from L2 to middle
            self.sceneScheme.addLine(QtCore.QLineF(250, 250, 250, 299), self.colorQT) #lense to observer
            self.sceneScheme.addItem(self.mirrorL1)# Espelho L1
            self.sceneScheme.addItem(self.mirrorL2) #Espelho L2

    def onUpdateWave(self):
        if not self.firstRun:
            self.ui.Wave_graphicsView.removeItem(self.Wave1)
            self.ui.Wave_graphicsView.removeItem(self.Wave2)

        x = np.linspace(0, 100/(self.freq), 10001)
        y1 = np.sin(x * self.freq)
        y2 = np.sin(x*self.freq + desfazamento(self.line1, self.line2, self.ir, self.lamb))

        self.Wave1 = pyqtgraph.PlotDataItem(x, y1, pen=self.colorQT, symbol=None)
        self.Wave2 = pyqtgraph.PlotDataItem(x, y2, pen=self.colorQT, symbol=None)




        self.ui.Wave_graphicsView.addItem(self.Wave1, labels={'left': '', 'bottom': 'Desfasamento'})  ## setting pen=None disables line drawing
        self.ui.Wave_graphicsView.addItem(self.Wave2)  ## setting pen=None disables line drawing


    def onUpdateGraphics(self):

        self.onUpdateScheme()
        self.onUpdateFranjas()
        self.onUpdateWave()


    def onUpdateVars(self):
        self.line1 = self.ui.L1_horizontalSlider.value()*0.01
        self.line2 = self.ui.L2_horizontalSlider.value()*0.01
        self.lamb = self.ui.Lambda_horizontalSlider.value()
        self.freq = LengthToFreq(int(self.ui.Lambda_horizontalSlider.value()))
        self.ir = float(self.ui.IR_doubleSpinBox.value())
        self.fran=franj(self.ir,self.line1,self.line2,self.lamb)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    app_icon = QtGui.QIcon()
    app_icon.addFile('gui/icons/icon_IDM_16x16.png', QtCore.QSize(16, 16))
    app_icon.addFile('gui/icons/icon_IDM_24x24.png', QtCore.QSize(24, 24))
    app_icon.addFile('gui/icons/icon_IDM_32x32.png', QtCore.QSize(32, 32))
    app_icon.addFile('gui/icons/icon_IDM_48x48.png', QtCore.QSize(48, 48))
    app_icon.addFile('gui/icons/icon_IDM_256x256.png', QtCore.QSize(256, 256))
    application.setWindowIcon(app_icon)
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()