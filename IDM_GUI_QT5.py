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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 5, 1, 1)
        self.Wave_graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wave_graphicsView.sizePolicy().hasHeightForWidth())
        self.Wave_graphicsView.setSizePolicy(sizePolicy)
        self.Wave_graphicsView.setMinimumSize(QtCore.QSize(163, 133))
        self.Wave_graphicsView.setMaximumSize(QtCore.QSize(163, 133))
        self.Wave_graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Wave_graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Wave_graphicsView.setObjectName("Wave_graphicsView")
        self.gridLayout.addWidget(self.Wave_graphicsView, 2, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.Scheme_graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Scheme_graphicsView.sizePolicy().hasHeightForWidth())
        self.Scheme_graphicsView.setSizePolicy(sizePolicy)
        self.Scheme_graphicsView.setMinimumSize(QtCore.QSize(500, 312))
        self.Scheme_graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scheme_graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scheme_graphicsView.setObjectName("Scheme_graphicsView")
        self.gridLayout.addWidget(self.Scheme_graphicsView, 1, 3, 3, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.Franjas_graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.Franjas_graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Franjas_graphicsView.sizePolicy().hasHeightForWidth())
        self.Franjas_graphicsView.setSizePolicy(sizePolicy)
        self.Franjas_graphicsView.setMinimumSize(QtCore.QSize(202, 202))
        self.Franjas_graphicsView.setMaximumSize(QtCore.QSize(202, 202))
        self.Franjas_graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        self.Franjas_graphicsView.setBaseSize(QtCore.QSize(0, 0))
        self.Franjas_graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Franjas_graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Franjas_graphicsView.setObjectName("Franjas_graphicsView")
        self.gridLayout.addWidget(self.Franjas_graphicsView, 6, 4, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.L1_horizontalSlider = QtWidgets.QSlider(self.frame)
        self.L1_horizontalSlider.setMinimum(0)
        self.L1_horizontalSlider.setMaximum(150)
        self.L1_horizontalSlider.setSingleStep(1)
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
        self.L1_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.L1_lineEdit.setObjectName("L1_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.L1_lineEdit)
        self.L2_horizontalSlider = QtWidgets.QSlider(self.frame)
        self.L2_horizontalSlider.setMinimum(0)
        self.L2_horizontalSlider.setMaximum(150)
        self.L2_horizontalSlider.setPageStep(1)
        self.L2_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.L2_horizontalSlider.setObjectName("L2_horizontalSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.L2_horizontalSlider)
        self.L2_label = QtWidgets.QLabel(self.frame)
        self.L2_label.setObjectName("L2_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.L2_label)
        self.L2_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.L2_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.L2_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.L2_lineEdit.setObjectName("L2_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.L2_lineEdit)
        self.Lambda_horizontalSlider = QtWidgets.QSlider(self.frame)
        self.Lambda_horizontalSlider.setMinimum(380)
        self.Lambda_horizontalSlider.setMaximum(750)
        self.Lambda_horizontalSlider.setPageStep(1)
        self.Lambda_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Lambda_horizontalSlider.setObjectName("Lambda_horizontalSlider")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Lambda_horizontalSlider)
        self.Lambda_label = QtWidgets.QLabel(self.frame)
        self.Lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Lambda_label.setObjectName("Lambda_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Lambda_label)
        self.Lambda_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.Lambda_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.Lambda_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Lambda_lineEdit.setObjectName("Lambda_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Lambda_lineEdit)
        self.IR_label = QtWidgets.QLabel(self.frame)
        self.IR_label.setWordWrap(False)
        self.IR_label.setObjectName("IR_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.IR_label)
        self.IR_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.IR_lineEdit.setMaximumSize(QtCore.QSize(64, 16777215))
        self.IR_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.IR_lineEdit.setObjectName("IR_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.IR_lineEdit)
        self.gridLayout.addWidget(self.frame, 6, 0, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.titleLabel.setFont(font)
        self.titleLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleLabel.setTextFormat(QtCore.Qt.RichText)
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 2)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador do Interferômetro de Michelson"))
        self.L1_label.setText(_translate("MainWindow", "             L1"))
        self.L1_lineEdit.setInputMask(_translate("MainWindow", "D000 μm"))
        self.L1_lineEdit.setText(_translate("MainWindow", "1 μm"))
        self.L2_label.setText(_translate("MainWindow", "             L2"))
        self.L2_lineEdit.setInputMask(_translate("MainWindow", "D000 μm"))
        self.L2_lineEdit.setText(_translate("MainWindow", "1 μm"))
        self.Lambda_label.setText(_translate("MainWindow", "             λ"))
        self.Lambda_lineEdit.setInputMask(_translate("MainWindow", "D99 \\nm"))
        self.Lambda_lineEdit.setText(_translate("MainWindow", "380 nm"))
        self.IR_label.setText(_translate("MainWindow", "Índice de refração"))
        self.IR_lineEdit.setInputMask(_translate("MainWindow", "0D.00"))
        self.IR_lineEdit.setText(_translate("MainWindow", "1.0"))
        self.titleLabel.setText(_translate("MainWindow", "Interferômetro de Michelson"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

