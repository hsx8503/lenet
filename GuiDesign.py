# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openCameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openCameraBtn.setGeometry(QtCore.QRect(40, 340, 112, 34))
        self.openCameraBtn.setObjectName("openCameraBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 450, 81, 41))
        self.label.setObjectName("label")
        self.openFolderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderBtn.setGeometry(QtCore.QRect(760, 330, 112, 34))
        self.openFolderBtn.setObjectName("openFolderBtn")
        self.forderImg = QtWidgets.QLabel(self.centralwidget)
        self.forderImg.setGeometry(QtCore.QRect(680, 30, 256, 256))
        self.forderImg.setText("")
        self.forderImg.setObjectName("forderImg")
        self.predict_1Btn = QtWidgets.QPushButton(self.centralwidget)
        self.predict_1Btn.setGeometry(QtCore.QRect(290, 390, 112, 34))
        self.predict_1Btn.setObjectName("predict_1Btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 460, 81, 18))
        self.label_3.setObjectName("label_3")
        self.captureBtn = QtWidgets.QPushButton(self.centralwidget)
        self.captureBtn.setGeometry(QtCore.QRect(290, 330, 112, 34))
        self.captureBtn.setObjectName("captureBtn")
        self.result_capture = QtWidgets.QLabel(self.centralwidget)
        self.result_capture.setGeometry(QtCore.QRect(340, 460, 81, 18))
        self.result_capture.setText("")
        self.result_capture.setObjectName("result_capture")
        self.predict_2Btn = QtWidgets.QPushButton(self.centralwidget)
        self.predict_2Btn.setGeometry(QtCore.QRect(760, 380, 112, 34))
        self.predict_2Btn.setObjectName("predict_2Btn")
        self.result_folder = QtWidgets.QLabel(self.centralwidget)
        self.result_folder.setGeometry(QtCore.QRect(800, 460, 101, 31))
        self.result_folder.setText("")
        self.result_folder.setObjectName("result_folder")
        self.cameraImg = QtWidgets.QLabel(self.centralwidget)
        self.cameraImg.setGeometry(QtCore.QRect(220, 40, 256, 256))
        self.cameraImg.setText("")
        self.cameraImg.setObjectName("cameraImg")
        # 默认设置
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # 槽
        self.captureBtn.clicked.connect(MainWindow.capture) # type: ignore
        self.openFolderBtn.clicked.connect(MainWindow.readImage) # type: ignore
        self.predict_1Btn.clicked.connect(MainWindow.predict_capture) # type: ignore
        self.predict_2Btn.clicked.connect(MainWindow.predict_folder) # type: ignore
        self.openCameraBtn.clicked.connect(MainWindow.openCamera) # type: ignore
        # 默认设置
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openCameraBtn.setText(_translate("MainWindow", "打开摄像头"))
        self.label.setText(_translate("MainWindow", "结果："))
        self.openFolderBtn.setText(_translate("MainWindow", "上传文件"))
        self.predict_1Btn.setText(_translate("MainWindow", "预测"))
        self.label_3.setText(_translate("MainWindow", "结果："))
        self.captureBtn.setText(_translate("MainWindow", "捕获图像"))
        self.predict_2Btn.setText(_translate("MainWindow", "预测"))