# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IDM_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 340, 371, 202))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.L1_horizontalSlider = QtWidgets.QSlider(self.frame)
        self.L1_horizontalSlider.setMinimum(1)
        self.L1_horizontalSlider.setMaximum(1000)
        self.L1_horizontalSlider.setPageStep(1)
        self.L1_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.L1_horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.L1_horizontalSlider.setObjectName("L1_horizontalSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.L1_horizontalSlider)
        self.L1_label = QtWidgets.QLabel(self.frame)
        self.L1_label.setObjectName("L1_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.L1_label)
        self.L1_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.L1_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.L1_lineEdit.setObjectName("L1_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.L1_lineEdit)
        self.L2_horizontalSlider = QtWidgets.QSlider(self.frame)
        self.L2_horizontalSlider.setMinimum(1)
        self.L2_horizontalSlider.setMaximum(1000)
        self.L2_horizontalSlider.setPageStep(1)
        self.L2_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.L2_horizontalSlider.setObjectName("L2_horizontalSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.L2_horizontalSlider)
        self.L2_label = QtWidgets.QLabel(self.frame)
        self.L2_label.setObjectName("L2_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.L2_label)
        self.L2_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.L2_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.L2_lineEdit.setObjectName("L2_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.L2_lineEdit)
        self.Lambda_horizontalSlider_3 = QtWidgets.QSlider(self.frame)
        self.Lambda_horizontalSlider_3.setMinimum(380)
        self.Lambda_horizontalSlider_3.setMaximum(700)
        self.Lambda_horizontalSlider_3.setPageStep(1)
        self.Lambda_horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.Lambda_horizontalSlider_3.setObjectName("Lambda_horizontalSlider_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Lambda_horizontalSlider_3)
        self.Lambda_label = QtWidgets.QLabel(self.frame)
        self.Lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Lambda_label.setObjectName("Lambda_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Lambda_label)
        self.Lambda_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.Lambda_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.Lambda_lineEdit.setObjectName("Lambda_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Lambda_lineEdit)
        self.IR_label = QtWidgets.QLabel(self.frame)
        self.IR_label.setWordWrap(False)
        self.IR_label.setObjectName("IR_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.IR_label)
        self.IR_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.IR_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.IR_lineEdit.setObjectName("IR_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.IR_lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L1_label.setText(_translate("MainWindow", "             L1"))
        self.L2_label.setText(_translate("MainWindow", "             L2"))
        self.Lambda_label.setText(_translate("MainWindow", "             λ"))
        self.IR_label.setText(_translate("MainWindow", "Índice de refração"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

