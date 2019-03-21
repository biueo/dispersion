# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelock.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

# filename:modelock.py

__author__=('Dengdecai','Gaogan')

# 导入各种python库

import sys
import numpy as np 
from scipy.fftpack import fft,ifft,fftshift,ifftshift
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from SSFM_G import SSFM_G
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from images import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from images import *

def absl(a):
        return np.array([abs(a[t]) for t in np.arange(len(a))])

class Ui_Modelock(object):
    def setupUi(self, Modelock):
        Modelock.setObjectName("Modelock")
        Modelock.resize(800, 600)
        #Modelock.setStyleSheet("background-image: url(beijing.jpg)")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Modelock.sizePolicy().hasHeightForWidth())
        Modelock.setSizePolicy(sizePolicy)
        Modelock.setMinimumSize(QtCore.QSize(800, 600))
        Modelock.setMaximumSize(QtCore.QSize(800, 600))
        self.GraphicsView = QtWidgets.QGraphicsView(Modelock)
        self.GraphicsView.setGeometry(QtCore.QRect(320, 30, 471, 341))
        self.GraphicsView.setStyleSheet("background-color: rgba(255, 255, 255, 51);")
        self.GraphicsView.setObjectName("GraphicsView")
        self.pushButton = QtWidgets.QPushButton(Modelock)
        self.pushButton.setGeometry(QtCore.QRect(215, 400, 101, 71))
        font = QtGui.QFont()
        font.setFamily("STXihei")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 15pt \"STXihei\";\n"
"color: rgb(0, 128, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Modelock)
        self.label.setGeometry(QtCore.QRect(521, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.beijing = QtWidgets.QLabel(Modelock)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.beijing.setText("")
        self.beijing.setPixmap(QtGui.QPixmap(":/beijing.jpg"))
        self.beijing.setObjectName("beijing")
        self.beijing.setWordWrap(False)
        self.beijing.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.beijing.raise_()
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Modelock)
        self.label_2.setGeometry(QtCore.QRect(6, 51, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Modelock)
        self.label_3.setGeometry(QtCore.QRect(45, 10, 158, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(255, 0, 0,0.8);")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Modelock)
        self.line.setGeometry(QtCore.QRect(45, 26, 155, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Modelock)
        self.line_2.setGeometry(QtCore.QRect(45, -1, 155, 16))
        self.line_2.setStyleSheet("color: rgb(0, 0, 128);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.RunInfo = QtWidgets.QTextBrowser(Modelock)
        self.RunInfo.setGeometry(QtCore.QRect(10, 490, 301, 101))
        self.RunInfo.setStyleSheet("background-color: rgba(255, 255, 255, 51);\n"
"color: rgba(255, 0, 0, 200);")
        self.RunInfo.setObjectName("RunInfo")
        self.progressBar = QtWidgets.QProgressBar(Modelock)
        self.progressBar.setGeometry(QtCore.QRect(220, 470, 91, 21))
        self.progressBar.setStyleSheet("background-color: rgba(255, 255, 255, 51);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Modelock)
        self.label_4.setGeometry(QtCore.QRect(12, 465, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.beta2 = QtWidgets.QLineEdit(Modelock)
        self.beta2.setGeometry(QtCore.QRect(109, 88, 71, 19))
        self.beta2.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.beta2.setAlignment(QtCore.Qt.AlignCenter)
        self.beta2.setObjectName("beta2")
        self.label_5 = QtWidgets.QLabel(Modelock)
        self.label_5.setGeometry(QtCore.QRect(10, 88, 101, 16))
        self.label_5.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Modelock)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("54542.jpg"))
        self.label_6.setObjectName("label_6")
        self.L1 = QtWidgets.QLineEdit(Modelock)
        self.L1.setGeometry(QtCore.QRect(30, 158, 41, 19))
        self.L1.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L1.setAlignment(QtCore.Qt.AlignCenter)
        self.L1.setObjectName("L1")
        self.NA = QtWidgets.QLineEdit(Modelock)
        self.NA.setGeometry(QtCore.QRect(120, 228, 41, 19))
        self.NA.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.NA.setAlignment(QtCore.Qt.AlignCenter)
        self.NA.setObjectName("NA")
        self.L_NALM_C = QtWidgets.QLineEdit(Modelock)
        self.L_NALM_C.setGeometry(QtCore.QRect(200, 199, 41, 19))
        self.L_NALM_C.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L_NALM_C.setAlignment(QtCore.Qt.AlignCenter)
        self.L_NALM_C.setObjectName("L_NALM_C")
        self.OutRadio = QtWidgets.QLineEdit(Modelock)
        self.OutRadio.setGeometry(QtCore.QRect(260, 88, 41, 19))
        self.OutRadio.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.OutRadio.setAlignment(QtCore.Qt.AlignCenter)
        self.OutRadio.setObjectName("OutRadio")
        self.core = QtWidgets.QLineEdit(Modelock)
        self.core.setGeometry(QtCore.QRect(80, 258, 61, 19))
        self.core.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.core.setAlignment(QtCore.Qt.AlignCenter)
        self.core.setObjectName("core")
        self.label_7 = QtWidgets.QLabel(Modelock)
        self.label_7.setGeometry(QtCore.QRect(150, 198, 51, 16))
        self.label_7.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Modelock)
        self.label_8.setGeometry(QtCore.QRect(200, 88, 51, 16))
        self.label_8.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Modelock)
        self.label_10.setGeometry(QtCore.QRect(80, 158, 25, 16))
        self.label_10.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Modelock)
        self.label_11.setGeometry(QtCore.QRect(10, 390, 61, 16))
        self.label_11.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Modelock)
        self.label_12.setGeometry(QtCore.QRect(10, 228, 101, 16))
        self.label_12.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Modelock)
        self.label_13.setGeometry(QtCore.QRect(10, 420, 61, 16))
        self.label_13.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Modelock)
        self.label_14.setGeometry(QtCore.QRect(10, 158, 25, 16))
        self.label_14.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Modelock)
        self.label_15.setGeometry(QtCore.QRect(160, 158, 25, 16))
        self.label_15.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Modelock)
        self.label_16.setGeometry(QtCore.QRect(240, 158, 25, 16))
        self.label_16.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_16.setObjectName("label_16")
        self.iter = QtWidgets.QSpinBox(Modelock)
        self.iter.setGeometry(QtCore.QRect(80, 420, 81, 21))
        self.iter.setStyleSheet("background-color: rgba(255, 255, 255, 51);\n"
"color:rgba(255, 255, 255, 204)")
        self.iter.setAlignment(QtCore.Qt.AlignCenter)
        self.iter.setMaximum(10000)
        self.iter.setProperty("value", 30)
        self.iter.setObjectName("iter")
        self.u_time00 = QtWidgets.QComboBox(Modelock)
        self.u_time00.setGeometry(QtCore.QRect(80, 390, 101, 21))
        self.u_time00.setStyleSheet("background-color: rgba(255, 255, 255, 51);\n"
"color: rgba(0, 64, 128, 204);")
        self.u_time00.setObjectName("u_time00")
        self.u_time00.addItem("")
        self.u_time00.addItem("")
        self.L2 = QtWidgets.QLineEdit(Modelock)
        self.L2.setGeometry(QtCore.QRect(100, 158, 41, 19))
        self.L2.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L2.setAlignment(QtCore.Qt.AlignCenter)
        self.L2.setObjectName("L2")
        self.L3 = QtWidgets.QLineEdit(Modelock)
        self.L3.setGeometry(QtCore.QRect(180, 158, 41, 19))
        self.L3.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L3.setAlignment(QtCore.Qt.AlignCenter)
        self.L3.setObjectName("L3")
        self.L4 = QtWidgets.QLineEdit(Modelock)
        self.L4.setGeometry(QtCore.QRect(260, 158, 41, 19))
        self.L4.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L4.setAlignment(QtCore.Qt.AlignCenter)
        self.L4.setObjectName("L4")
        self.label_17 = QtWidgets.QLabel(Modelock)
        self.label_17.setGeometry(QtCore.QRect(10, 258, 61, 16))
        self.label_17.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Modelock)
        self.label_18.setGeometry(QtCore.QRect(10, 288, 61, 16))
        self.label_18.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_18.setObjectName("label_18")
        self.c_ratio = QtWidgets.QLineEdit(Modelock)
        self.c_ratio.setGeometry(QtCore.QRect(80, 288, 61, 19))
        self.c_ratio.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.c_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.c_ratio.setObjectName("c_ratio")
        self.label_19 = QtWidgets.QLabel(Modelock)
        self.label_19.setGeometry(QtCore.QRect(10, 318, 61, 16))
        self.label_19.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_19.setObjectName("label_19")
        self.g = QtWidgets.QLineEdit(Modelock)
        self.g.setGeometry(QtCore.QRect(80, 318, 61, 19))
        self.g.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.g.setAlignment(QtCore.Qt.AlignCenter)
        self.g.setObjectName("g")
        self.label_20 = QtWidgets.QLabel(Modelock)
        self.label_20.setGeometry(QtCore.QRect(10, 198, 51, 16))
        self.label_20.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_20.setObjectName("label_20")
        self.L_NALM_A = QtWidgets.QLineEdit(Modelock)
        self.L_NALM_A.setGeometry(QtCore.QRect(72, 198, 41, 19))
        self.L_NALM_A.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.L_NALM_A.setAlignment(QtCore.Qt.AlignCenter)
        self.L_NALM_A.setObjectName("L_NALM_A")
        self.label_9 = QtWidgets.QLabel(Modelock)
        self.label_9.setGeometry(QtCore.QRect(10, 122, 101, 16))
        self.label_9.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_9.setObjectName("label_9")
        self.label_21 = QtWidgets.QLabel(Modelock)
        self.label_21.setGeometry(QtCore.QRect(204, 122, 41, 20))
        self.label_21.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_21.setObjectName("label_21")
        self.beta3 = QtWidgets.QLineEdit(Modelock)
        self.beta3.setGeometry(QtCore.QRect(109, 122, 71, 19))
        self.beta3.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.beta3.setAlignment(QtCore.Qt.AlignCenter)
        self.beta3.setObjectName("beta3")
        self.loss = QtWidgets.QLineEdit(Modelock)
        self.loss.setGeometry(QtCore.QRect(260, 122, 41, 19))
        self.loss.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.loss.setAlignment(QtCore.Qt.AlignCenter)
        self.loss.setObjectName("loss")
        self.label_22 = QtWidgets.QLabel(Modelock)
        self.label_22.setGeometry(QtCore.QRect(10, 348, 71, 16))
        self.label_22.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_22.setObjectName("label_22")
        self.band = QtWidgets.QLineEdit(Modelock)
        self.band.setGeometry(QtCore.QRect(80, 348, 61, 20))
        self.band.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.band.setAlignment(QtCore.Qt.AlignCenter)
        self.band.setObjectName("band")
        self.label_23 = QtWidgets.QLabel(Modelock)
        self.label_23.setGeometry(QtCore.QRect(6, 4, 33, 33))
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 138);")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/horse.png"))
        self.label_23.setObjectName("label_23")
        self.pushButton_2 = QtWidgets.QPushButton(Modelock)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 384, 91, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_24 = QtWidgets.QLabel(Modelock)
        self.label_24.setGeometry(QtCore.QRect(420, 470, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_3 = QtWidgets.QPushButton(Modelock)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 384, 91, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Modelock)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 415, 91, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Modelock)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 415, 91, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_3 = QtWidgets.QFrame(Modelock)
        self.line_3.setGeometry(QtCore.QRect(320, 440, 471, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_25 = QtWidgets.QLabel(Modelock)
        self.label_25.setGeometry(QtCore.QRect(540, 384, 41, 16))
        self.label_25.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Modelock)
        self.label_26.setGeometry(QtCore.QRect(540, 415, 41, 16))
        self.label_26.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Modelock)
        self.label_27.setGeometry(QtCore.QRect(630, 384, 41, 16))
        self.label_27.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Modelock)
        self.label_28.setGeometry(QtCore.QRect(630, 415, 41, 16))
        self.label_28.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_28.setObjectName("label_28")
        self.Xmin = QtWidgets.QLineEdit(Modelock)
        self.Xmin.setGeometry(QtCore.QRect(580, 384, 41, 19))
        self.Xmin.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.Xmin.setAlignment(QtCore.Qt.AlignCenter)
        self.Xmin.setObjectName("Xmin")
        self.Ymin = QtWidgets.QLineEdit(Modelock)
        self.Ymin.setGeometry(QtCore.QRect(580, 415, 41, 19))
        self.Ymin.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.Ymin.setAlignment(QtCore.Qt.AlignCenter)
        self.Ymin.setObjectName("Ymin")
        self.Ymax = QtWidgets.QLineEdit(Modelock)
        self.Ymax.setGeometry(QtCore.QRect(680, 415, 41, 19))
        self.Ymax.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.Ymax.setAlignment(QtCore.Qt.AlignCenter)
        self.Ymax.setObjectName("Ymax")
        self.Xmax = QtWidgets.QLineEdit(Modelock)
        self.Xmax.setGeometry(QtCore.QRect(680, 384, 41, 19))
        self.Xmax.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.Xmax.setAlignment(QtCore.Qt.AlignCenter)
        self.Xmax.setObjectName("Xmax")
        self.pushButton_6 = QtWidgets.QPushButton(Modelock)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 460, 81, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.T_duration = QtWidgets.QLCDNumber(Modelock)
        self.T_duration.setGeometry(QtCore.QRect(560, 470, 81, 23))
        self.T_duration.setStyleSheet("color: rgb(0, 0, 0);")
        self.T_duration.setDigitCount(6)
        self.T_duration.setProperty("value", 125.11)
        self.T_duration.setObjectName("T_duration")
        self.label_29 = QtWidgets.QLabel(Modelock)
        self.label_29.setGeometry(QtCore.QRect(420, 510, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.F_duration = QtWidgets.QLCDNumber(Modelock)
        self.F_duration.setGeometry(QtCore.QRect(560, 510, 81, 23))
        self.F_duration.setProperty("value", 0.11)
        self.F_duration.setObjectName("F_duration")
        self.label_30 = QtWidgets.QLabel(Modelock)
        self.label_30.setGeometry(QtCore.QRect(420, 550, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.Energy_out = QtWidgets.QLCDNumber(Modelock)
        self.Energy_out.setGeometry(QtCore.QRect(560, 550, 81, 23))
        self.Energy_out.setProperty("value", 0.11)
        self.Energy_out.setObjectName("Energy_out")
        self.label_31 = QtWidgets.QLabel(Modelock)
        self.label_31.setGeometry(QtCore.QRect(670, 470, 111, 111))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap(":/Tsinghua.png"))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(Modelock)
        self.label_32.setGeometry(QtCore.QRect(180, 230, 61, 16))
        self.label_32.setStyleSheet("color: rgba(255, 128, 0,0.8);")
        self.label_32.setObjectName("label_32")
        self.gNALM = QtWidgets.QLineEdit(Modelock)
        self.gNALM.setGeometry(QtCore.QRect(250, 230, 41, 19))
        self.gNALM.setStyleSheet("background-color: rgba(255, 255, 255, 53);\n"
"color: rgba(255, 255, 255, 204);")
        self.gNALM.setAlignment(QtCore.Qt.AlignCenter)
        self.gNALM.setObjectName("gNALM")
        self.label_33 = QtWidgets.QLabel(Modelock)
        self.label_33.setGeometry(QtCore.QRect(150, 250, 171, 151))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/NALM_figure.png"))
        self.label_33.setObjectName("label_33")
        self.pushButton_7 = QtWidgets.QPushButton(Modelock)
        self.pushButton_7.setGeometry(QtCore.QRect(726, 380, 71, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Modelock)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 520, 81, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_34 = QtWidgets.QLabel(Modelock)
        self.label_34.setGeometry(QtCore.QRect(660, 580, 151, 20))
        self.label_34.setObjectName("label_34")
        self.label_6.raise_()
        self.GraphicsView.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.RunInfo.raise_()
        self.label_4.raise_()
        self.beta2.raise_()
        self.label_5.raise_()
        self.progressBar.raise_()
        self.L1.raise_()
        self.NA.raise_()
        self.L_NALM_C.raise_()
        self.OutRadio.raise_()
        self.core.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.iter.raise_()
        self.u_time00.raise_()
        self.L2.raise_()
        self.L3.raise_()
        self.L4.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.c_ratio.raise_()
        self.label_19.raise_()
        self.g.raise_()
        self.label_20.raise_()
        self.L_NALM_A.raise_()
        self.label_9.raise_()
        self.label_21.raise_()
        self.beta3.raise_()
        self.loss.raise_()
        self.label_22.raise_()
        self.band.raise_()
        self.label_23.raise_()
        self.pushButton_2.raise_()
        self.label_24.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.line_3.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.Xmin.raise_()
        self.Ymin.raise_()
        self.Ymax.raise_()
        self.Xmax.raise_()
        self.pushButton_6.raise_()
        self.T_duration.raise_()
        self.label_29.raise_()
        self.F_duration.raise_()
        self.label_30.raise_()
        self.Energy_out.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.gNALM.raise_()
        self.label_33.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_34.raise_()
        

        self.retranslateUi(Modelock)
        self.pushButton.clicked.connect(Modelock.calculate)
        self.pushButton_2.clicked.connect(Modelock.timecircle)
        self.pushButton_3.clicked.connect(Modelock.freqcircle)
        self.pushButton_4.clicked.connect(Modelock.timeout)
        self.pushButton_5.clicked.connect(Modelock.freqout)
        self.pushButton_8.clicked.connect(Modelock.adapt)
        self.pushButton_6.clicked.connect(Modelock.savefig)
        self.pushButton_7.clicked.connect(Modelock.justment)
        self.pushButton.clicked.connect(self.GraphicsView.invalidateScene)
        QtCore.QMetaObject.connectSlotsByName(Modelock)

    def retranslateUi(self, Modelock):
        _translate = QtCore.QCoreApplication.translate
        Modelock.setWindowTitle(_translate("Modelock", "ModeLock"))
        self.pushButton.setText(_translate("Modelock", "计算"))
        self.label.setText(_translate("Modelock", "结果图示"))
        self.label_2.setText(_translate("Modelock", "参数设置:"))
        self.label_3.setText(_translate("Modelock", "8字环形腔锁模仿真"))
        self.label_4.setText(_translate("Modelock", "运行信息:"))
        self.beta2.setWhatsThis(_translate("Modelock", "<html><head/><body><p>二阶色散系数β2</p></body></html>"))
        self.beta2.setText(_translate("Modelock", "0.0246e-24"))
        self.label_5.setText(_translate("Modelock", "<html><head/><body><p>二阶色散系数β<span style=\" vertical-align:sub;\">2</span>：</p></body></html>"))
        self.L1.setText(_translate("Modelock", "1"))
        self.NA.setText(_translate("Modelock", "0.12"))
        self.L_NALM_C.setText(_translate("Modelock", "5.5"))
        self.OutRadio.setText(_translate("Modelock", "0.7"))
        self.core.setText(_translate("Modelock", "6e-6"))
        self.label_7.setText(_translate("Modelock", "<html><head/><body><p>L<span style=\" vertical-align:sub;\">NALM_C</span>：</p></body></html>"))
        self.label_8.setText(_translate("Modelock", "<html><head/><body><p>输出比：</p></body></html>"))
        self.label_10.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-weight:600;\">L</span><span style=\" font-weight:600; vertical-align:sub;\">2</span><span style=\" font-weight:600;\">：</span></p></body></html>"))
        self.label_11.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-size:14pt;\">初始脉冲：</span></p></body></html>"))
        self.label_12.setText(_translate("Modelock", "<html><head/><body><p>光纤数值孔径NA:</p></body></html>"))
        self.label_13.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-size:14pt;\">循环次数：</span></p></body></html>"))
        self.label_14.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-weight:600;\">L</span><span style=\" font-weight:600; vertical-align:sub;\">1</span><span style=\" font-weight:600;\">：</span></p></body></html>"))
        self.label_15.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-weight:600;\">L</span><span style=\" font-weight:600; vertical-align:sub;\">3</span><span style=\" font-weight:600;\">：</span></p></body></html>"))
        self.label_16.setText(_translate("Modelock", "<html><head/><body><p><span style=\" font-weight:600;\">L</span><span style=\" font-weight:600; vertical-align:sub;\">4</span><span style=\" font-weight:600;\">：</span></p></body></html>"))
        self.u_time00.setItemText(0, _translate("Modelock", "高斯脉冲"))
        self.u_time00.setItemText(1, _translate("Modelock", "随机噪声"))
        self.L2.setText(_translate("Modelock", "2"))
        self.L3.setText(_translate("Modelock", "4"))
        self.L4.setText(_translate("Modelock", "4"))
        self.label_17.setText(_translate("Modelock", "<html><head/><body><p>光纤芯径：</p></body></html>"))
        self.label_18.setText(_translate("Modelock", "<html><head/><body><p>输出比例：</p></body></html>"))
        self.c_ratio.setText(_translate("Modelock", "0.5"))
        self.label_19.setText(_translate("Modelock", "<html><head/><body><p>主环增益：</p></body></html>"))
        self.g.setText(_translate("Modelock", "300"))
        self.label_20.setText(_translate("Modelock", "<html><head/><body><p>L<span style=\" vertical-align:sub;\">NALM_A</span>:</p></body></html>"))
        self.L_NALM_A.setText(_translate("Modelock", "4"))
        self.label_9.setText(_translate("Modelock", "<html><head/><body><p>三阶色散系数β<span style=\" vertical-align:sub;\">3</span>：</p></body></html>"))
        self.label_21.setText(_translate("Modelock", "<html><head/><body><p>Loss：</p></body></html>"))
        self.beta3.setText(_translate("Modelock", "0"))
        self.loss.setText(_translate("Modelock", "0.01"))
        self.label_22.setText(_translate("Modelock", "<html><head/><body><p>滤波带宽：</p></body></html>"))
        self.band.setText(_translate("Modelock", "2e-9"))
        self.label_23.setToolTip(_translate("Modelock", "<html><head/><body><p><br/></p></body></html>"))
        self.beijing.setToolTip(_translate("Modelock", "<html><head/><body><p><br/></p></body></html>"))
        self.label_23.setWhatsThis(_translate("Modelock", "<html><head/><body><p>如有问题请联系QQ：8985139</p></body></html>"))
        self.pushButton_2.setText(_translate("Modelock", "时域锁模过程"))
        self.label_24.setText(_translate("Modelock", "最终输出脉宽(fs):"))
        self.pushButton_3.setText(_translate("Modelock", "频域锁模过程"))
        self.pushButton_4.setText(_translate("Modelock", "输出脉冲形状"))
        self.pushButton_5.setText(_translate("Modelock", "输出频谱形状"))
        self.label_25.setText(_translate("Modelock", "<html><head/><body><p>Xmin:</p></body></html>"))
        self.label_26.setText(_translate("Modelock", "<html><head/><body><p>Ymin:</p></body></html>"))
        self.label_27.setText(_translate("Modelock", "<html><head/><body><p>Xmax:</p></body></html>"))
        self.label_28.setText(_translate("Modelock", "<html><head/><body><p>Ymax:</p></body></html>"))
        self.Xmin.setText(_translate("Modelock", "0"))
        self.Ymin.setText(_translate("Modelock", "0"))
        self.Ymax.setText(_translate("Modelock", "0"))
        self.Xmax.setText(_translate("Modelock", "0"))
        self.pushButton_6.setText(_translate("Modelock", "保存图片"))
        self.label_29.setText(_translate("Modelock", "最终输出谱宽(nm):"))
        self.label_30.setText(_translate("Modelock", "最终输出能量(nJ):"))
        self.label_32.setText(_translate("Modelock", "<html><head/><body><p>次环增益：</p></body></html>"))
        self.gNALM.setText(_translate("Modelock", "6.6"))
        self.pushButton_7.setText(_translate("Modelock", "应用"))
        self.pushButton_8.setText(_translate("Modelock", "保存数据"))
        self.label_34.setText(_translate("Modelock", "decaideng@gmail.com"))
class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None, left=0.15,width=0.5,bottom=0.44,height=0.48, dpi=100):
        fig=plt.figure(dpi=100)
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        rect_line1=[left,bottom,width,height]
        plt.axes(rect_line1)
        self.axes=plt.axes(rect_line1)
        
    def timeoutg(self):
        timeout_plot=self.axes.plot(t_signal,abs1_OUT_time[-1])
        plt.xlim(np.min(t_signal),np.max(t_signal))
        plt.ylim(0,np.max(abs1_OUT_time[-1]))
        plt.title(u"输出脉冲时域图", fontproperties='SimHei',fontsize=20)
        plt.xlabel(u"时间/ps", fontproperties='SimHei',fontsize=16)
        plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16)
        plt.grid(True)
        plt.setp(timeout_plot, color='blue', linewidth=2.0)
    def timeoutgset(self,xmin,xmax,ymin,ymax):
        timeout_plot=self.axes.plot(t_signal,abs1_OUT_time[-1])
        plt.xlim(xmin,xmax)
        plt.ylim(ymin,ymax)
        plt.title(u"输出脉冲时域图", fontproperties='SimHei',fontsize=20)
        plt.xlabel(u"时间/ps", fontproperties='SimHei',fontsize=16)
        plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16)
        plt.grid(True)
        plt.setp(timeout_plot, color='blue', linewidth=2.0)

    def freqoutg(self):
        xmajorLocator   = MultipleLocator(20) #将x主刻度标签设置为20的倍数  
        # xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式  
        xminorLocator   = MultipleLocator(10) #将x轴次刻度标签设置为5的倍数 
        ax=self.axes
        freqout_plot=self.axes.plot(c/F_signal*1e9,freqoutdata)
        plt.xlim(970,1090)
        plt.ylim(0,np.max(freqoutdata))
        plt.title(u'输出信号频谱图',fontproperties='SimHei',fontsize=20)
        plt.xlabel(u"波长/nm", fontproperties='SimHei',fontsize=16)
        plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16)
        ax.xaxis.set_major_locator(xmajorLocator) 
        ax.xaxis.set_minor_locator(xminorLocator)  
        ax.xaxis.grid(True, which='major' and 'minor') #x坐标轴的网格使用主刻度  
        ax.yaxis.grid(True, which='major') #y坐标轴的网格使用次刻度  
        plt.grid(True)
        plt.setp(freqout_plot, color='r', linewidth=2.0)
    def freqoutgset(self,xmin,xmax,ymin,ymax):
        xmajorLocator   = MultipleLocator(20) #将x主刻度标签设置为20的倍数  
        # xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式  
        xminorLocator   = MultipleLocator(10) #将x轴次刻度标签设置为5的倍数 
        ax=self.axes
        freqout_plot=self.axes.plot(c/F_signal*1e9,freqoutdata)
        plt.xlim(xmin,xmax)
        plt.ylim(ymin,ymax)
        plt.title(u'输出信号频谱图',fontproperties='SimHei',fontsize=20)
        plt.xlabel(u"波长/nm", fontproperties='SimHei',fontsize=16)
        plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16)
        ax.xaxis.set_major_locator(xmajorLocator) 
        ax.xaxis.set_minor_locator(xminorLocator)  
        ax.xaxis.grid(True, which='major' and 'minor') #x坐标轴的网格使用主刻度  
        ax.yaxis.grid(True, which='major') #y坐标轴的网格使用次刻度  
        plt.grid(True)
        plt.setp(freqout_plot, color='r', linewidth=2.0)


class Figure_Canvas3(FigureCanvas):
    def __init__(self,parent=None, dpi=100):
        fig=plt.figure(dpi=100)
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        self.axes=fig.add_subplot(111,projection='3d')
    def timecircleg(self): 
        for z in np.arange(1,iter,iter//20 ):
                xs=t_signal*1e12
                ys=np.array(abs1_OUT_time[z])
                self.axes.plot(xs,ys,zs=z,zdir='y')
        self.axes.set_ylim(0,iter+1)
        self.axes.set_zlim(0,np.max(abs1_OUT_time))
        plt.title(u'时域锁模过程',fontproperties='SimHei',fontsize=20)
        self.axes.set_xlabel(u'Time(ps)',fontsize=16)
        self.axes.set_ylabel(u'circle-index',fontsize=16)
        self.axes.set_zlabel(u'Amplitude ',fontsize=16)
        plt.grid(True)
    def freqcircleg(self): 
        for z in np.arange(1,iter,iter//20):
                xs=c/F_signal*1e9
                ys=absl(OUT_freq[z][0])
                self.axes.plot(xs,ys,zs=z,zdir='y')
        self.axes.set_ylim(0,iter+1)
        self.axes.set_zlim(0,np.max(abs1_OUT_freq))
        plt.title(u'频域锁模过程',fontproperties='SimHei',fontsize=20)
        self.axes.set_xlabel(u'wavelength(nm)',fontsize=16)
        self.axes.set_ylabel(u'circle-index',fontsize=16)
        self.axes.set_zlabel(u'Amplitude ',fontsize=16)
        plt.grid(True)


class Thread(QtCore.QThread):
    log = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)

    def setItems(self, Rinfo):
        if not self.isRunning():
            self.Rinfo = Rinfo

    def run(self):
        self.log.emit(self.Rinfo)




class mywindow(Ui_Modelock,QtWidgets.QDialog):   
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)
        self.donee=0
        self.fignow=3

    def toLog(self,txt):
        self.RunInfo.append(txt)
    def progressb(self,ivalue):
        self.progressBar.setValue(ivalue)
    #定义槽函数
    def calculate(self):  
        # self.calc=Thread()
        # self.calc.log.connect(self.toLog)
        # self.calc.start()
        global abs1_OUT_time, abs1_OUT_freq, OUT_freq,t_signal,F_signal,c,freqoutdata,timeoutdata,iter
        doneee=0
        n_index=1.45
        h=6.63e-34 
        c=3e8
        tY=1e-3
        beta1=0
        try:
            beta2=float(self.beta2.text())  #
            if beta2>=1e-7:
                self.RunInfo.append('Error：二阶色散系数过大')
                doneee+=1
            if beta2<=0:
                self.RunInfo.append('Error：二阶色散系数不能为负值')
                doneee+=1
        except:
            self.RunInfo.append('Error：二阶色散系数输入有误!')
            doneee+=1
        gama=3e-3
        try:
            NA=float(self.NA.text())
            if NA>=1:
                self.RunInfo.append('Error：数值孔径应过大')
                doneee+=1
            if NA<=0:
                self.RunInfo.append('Error：数值孔径不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：数值孔径NA输入有误!')
                doneee+=1
        try:
            core=float(self.core.text())
            if core>=1e-4:
                self.RunInfo.append('Error：纤芯应输入以m为单位')
                doneee+=1
            if core<=0:
                self.RunInfo.append('Error：纤芯应输入不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：纤芯输入有误!')
                doneee+=1        
        try:
            c_ratio=float(self.c_ratio.text())
            if c_ratio>=1:
                self.RunInfo.append('Error：耦合比应小于1')
                doneee+=1
            if c_ratio<=0:
                self.RunInfo.append('Error：耦合比应大于0')
                doneee+=1
        except:
                self.RunInfo.append('Error：耦合比输入有误!') 
                doneee+=1       
        try:
            L_NALM_C=float(self.L_NALM_C.text())
            if L_NALM_C<=0:
                self.RunInfo.append('Error：L_NALM_C长度应该大于0')
                doneee+=1
        except:
                self.RunInfo.append('Error：L_NALM_C输入有误!') 
                doneee+=1       
        try:
            L_NALM_A=float(self.L_NALM_A.text())
            if L_NALM_A<=0:
                self.RunInfo.append('Error：L_NALM_A长度应该大于0')
                doneee+=1
        except:
                self.RunInfo.append('Error：L_NALM_A输入有误!')
                doneee+=1        
        try:
            OutRadio=float(self.OutRadio.text())
            if OutRadio>=1:
                self.RunInfo.append('Error：输出比过大!')
                doneee+=1
            if OutRadio<=0:
                self.RunInfo.append('Error：你家的输出比小于0呀!bendan')
                doneee+=1

        except:
                self.RunInfo.append('Error：输出比输入有误!')   
                doneee+=1     
        try:
            g=float(self.g.text())
            if g<=0:
                self.RunInfo.append('Error：主环增益不能小于0')
                doneee+=1
        except:
                self.RunInfo.append('Error：增益输入有误!') 
                doneee+=1       
        try:
            L1=float(self.L1.text())
            if L1<=0:
                self.RunInfo.append('Error：L1长度不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：L1输入有误!') 
                doneee+=1       
        try:
            L2=float(self.L2.text())
            if L2<=0:
                self.RunInfo.append('Error：L2长度不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：L2输入有误!')  
                doneee+=1      
        try:
            loss=float(self.loss.text())
            if loss<=0:
                self.RunInfo.append('Error：loss不能为负值')
                doneee+=1
            if loss>=1:
                self.RunInfo.append('Warning：损耗输入过大')
                doneee+=1
        except:
                self.RunInfo.append('Error：loss输入有误!') 
                doneee+=1       
        try:
            L3=float(self.L3.text())  
            if L3<=0:
                self.RunInfo.append('Error：L3长度不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：L3输入有误!') 
                doneee+=1       
        try:
            L4=float(self.L4.text())
            if L4<=0:
                self.RunInfo.append('Error：L4长度不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：L4输入有误!')  
                doneee+=1      
        try:
            band=float(self.band.text())
            if band<=0:
                self.RunInfo.append('Error：滤波器带宽不能为负值')
                doneee+=1
            if band>=1e-7:
                self.RunInfo.append('Error：滤波带宽应输入以m为单位')
                doneee+=1
        except:
                self.RunInfo.append('Error：滤波带宽输入有误!')  
                doneee+=1
        try:
            g_NALM=float(self.gNALM.text()) 
            if g_NALM<=0:
                self.RunInfo.append('Error：次环增益不能为负值')
                doneee+=1
        except:
                self.RunInfo.append('Error：次环增益输入有误!')  
                doneee+=1
        try:
            iter=int(self.iter.text())
            if iter<=20:
                self.RunInfo.append('Error：循环次数输入应该大于20') 
                doneee+=1  
        except:
            self.RunInfo.append('Error：循环次数输入有误!')  
            doneee+=1
        try:
            u_time00=self.u_time00.currentText()
        except:
            self.RunInfo.append('Error：初始脉冲错误')
            doneee+=1
        if doneee!=0:
            return None      
        A=np.pi*(core/2)**2 
        L_NALM=L_NALM_C-L_NALM_A
        #定义初始脉冲和频率
        Tp=300e-15
        Ttotal=100*Tp
        stepT=20e-15
        iteration_T=Ttotal/stepT
        stepF=1/Ttotal
        t_signal=np.linspace(-Ttotal/2,Ttotal/2,iteration_T+1)
        lamda0=1030e-9
        omega0=2*np.pi*c/lamda0
        F_signal=np.r_[(c/lamda0-stepF*iteration_T/2):(c/lamda0+stepF*(iteration_T/2+1)):stepF]
        omega_signal=F_signal*2*np.pi
        Signal_m=1
        C=1
        beta1=0
        n2=4.5e-20
        Amplitude=10

        if u_time00==u"高斯脉冲":
            u_time0=Amplitude*np.exp(-(t_signal/Tp)**(2*Signal_m)/2*(1+C*1j))      #
        if u_time00==u"随机噪声":
            u_time0=Amplitude*np.random.random((int(iteration_T+1)))           #
        u_freq0=fftshift(fft(u_time0))

        la_ase=c/F_signal

        band0=band/(2*np.sqrt(np.log(2)))
        T_BP=np.exp(-(la_ase-lamda0)**2/2/band0**2)
        # 吸收发射谱
        sig_as=(180*np.exp(-(((lamda0*1e9-950)/70)**2)) + \
                        360*np.exp(-(((lamda0*1e9-895)/24)**2)) +\
                        510*np.exp(-(((lamda0*1e9-918)/22)**2)) + \
                        160*np.exp(-(((lamda0*1e9-971)/12)**2)) + \
                        2325*np.exp(-(((lamda0*1e9-975)/4)**2)))*1e-27;
        sig_es=(2325*np.exp(-(((lamda0*1e9-975)/4)**2)) + \
                        160*np.exp(-(((lamda0*1e9-978)/12)**2)) + \
                        340*np.exp(-(((lamda0*1e9-1025)/20)**2)) + \
                        175*np.exp(-(((lamda0*1e9-1050)/60)**2)) + \
                        150*np.exp(-(((lamda0*1e9-1030)/90)**2)))*1e-27;

        Fp=4e12
        gaosim=5

        g0=g*np.exp(-(F_signal-F_signal[int(iteration_T/2-1)])**(2*gaosim)/Fp**(2*gaosim))
        F_gain=F_signal    
        Gamma_s=0.72
        Tau_s=1.5e-3 
        Esat=h*c*A/(lamda0*(sig_as+sig_es))/1.5e-3*Ttotal
        ## 初始信号的强度分布 时域和频域
        OUT_time=[]
        OUT_freq=[]
        abs1_OUT_time=[]
        abs1_OUT_freq=[]
        U_time1=[]
        U_time2=[]
        U_time3=[]
        U_time4=[]
        U_time5=[]
        U_time6=[]
        U_time7=[]


        U_time7.append(u_time0)
        OUT_time.append(u_time0)
        abs1_OUT_time.append(absl(u_time0))
        Peakv_1=max(absl(u_freq0))
        peakv_num1=np.argmax(absl(u_freq0))
        abs1_OUT_freq.append(absl(u_freq0)/Peakv_1)
        i=0
        self.progressBar.setMaximum(iter-1)
        self.progressBar.setValue(i)
        for i in range(iter):
            #非增益光纤传播
            U_time1.append(SSFM_G(U_time7[i],L1,beta2,gama,0,Esat,omega_signal,loss))
            bbbb1=np.sum((absl(U_time1[i])**2)*stepT)
            #经过filter
            U_time2.append(ifft(ifftshift(np.sqrt(T_BP)*fftshift(fft(U_time1[i])))))
            bbbb2=np.sum((absl(U_time2[i])**2)*stepT)
            #非增益光纤传播
            U_time3.append(SSFM_G(U_time2[i],L2,beta2,gama,0,Esat,omega_signal,loss))
            bbbb3=np.sum((absl(U_time3[i])**2)*stepT)
            #在增益光纤里传播
            U_time4.append(SSFM_G(U_time3[i],L3,beta2,gama,g0,Esat,omega_signal,loss))
            bbbb4=np.sum((absl(U_time4[i])**2)*stepT)
            #在非增益光线里传播
            U_time5.append(SSFM_G(U_time4[i],L4,beta2,gama,0,Esat,omega_signal,loss))
            bbbb5=np.sum((absl(U_time5[i])**2)*stepT)
            #经过NALM
            dp=2*np.pi/lamda0*n2/A*(c_ratio*(g_NALM+1)-1)*absl(U_time5[i])**2*L_NALM
            T_NALM=g_NALM*(1-2*c_ratio*(1-c_ratio)*(1+np.cos(dp)))
            U_time6.append(np.sqrt(T_NALM)*U_time5[i])
            bbbb6=np.sum((absl(U_time6[i])**2)*stepT)
            #经过OC
            U_time7.append(U_time6[i]*np.sqrt(1-OutRadio))
            bbbb7=np.sum((absl(U_time7[i])**2)*stepT)
            #输出数据处理
            OUT_time.append((U_time6[i]*np.sqrt(OutRadio))**2)
            OUTPeakU=max(absl(OUT_time[i]))
            OUTPeak_Num=np.argmax(absl(OUT_time[i]))
            bbbb=OUT_time[i]#临时向量
            middle_t=np.where(t_signal==0)
            translat_step=OUTPeak_Num-middle_t
            OUT_time[i]=[bbbb[m] for m in np.mod(np.arange(len(bbbb))+translat_step,len(bbbb))]
            abs1_OUT_time.append(absl(OUT_time[i])[0])
            OUT_freq.append(fftshift(fft(OUT_time[i])))
            OUTPeakv=max(absl(OUT_freq[i]))
            OUTPeakv_Num=np.argmax(absl(OUT_freq[i]))
            abs1_OUT_freq.append(absl(OUT_freq[i])[0])
            self.progressb(i)
        ##数据处理及作图
        U_time_out=U_time6[-1]*np.sqrt(OutRadio)
        U_freq_out=fftshift(fft(U_time_out))

        timeoutdata=abs1_OUT_time[-1]
        freqoutdata=abs1_OUT_freq[-1]


        PeakU=max(timeoutdata**2)
        Peak_Num=np.argmax((abs1_OUT_time[-1])**2)

        half_t1=np.argmin(absl((timeoutdata[0:Peak_Num])**2-[PeakU/2 for i in range(Peak_Num)]))
        half_t2=np.argmin(absl( (timeoutdata[(Peak_Num):len(t_signal)])**2- [PeakU/2 for i in range(len(t_signal)-Peak_Num)] ))
        T_duration=(Peak_Num-half_t1+half_t2)*stepT*1e15

        PeakF=max(freqoutdata**2)
        PeakF_Num=np.argmax((abs1_OUT_freq[-1])**2)
        half_f1=np.argmin(absl( freqoutdata[0:PeakF_Num]**2-[PeakF/2 for i in range(PeakF_Num)] ))
        half_f2=np.argmin(absl( freqoutdata[(PeakF_Num):len(F_signal)]**2-[PeakF/2 for i in range(len(F_signal)-PeakF_Num)]   ))
        F_duration=c/F_signal[half_f1]-c/F_signal[half_f2+PeakF_Num]
        F_duration=F_duration*1e9

        Energy_out=np.sum(absl(U_time_out)**2)*stepT*1e9  #输出脉冲总能量

        self.T_duration.display(T_duration)
        self.F_duration.display(F_duration)
        self.Energy_out.display(Energy_out)

        dr=Figure_Canvas()
        dr.timeoutg()
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        

        self.Xmin.setText(str(np.min(t_signal)))
        self.Ymin.setText(str(0))
        self.Xmax.setText(str(np.max(t_signal)))
        self.Ymax.setText(str('%.4g'%np.max(abs1_OUT_time[-1])))
        self.RunInfo.append('程序运行成功')
        self.fignow=3
        self.donee=1



    def timecircle(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        dr=Figure_Canvas3()
        dr.timecircleg()
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        self.fignow=1        
    def freqcircle(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        dr=Figure_Canvas3()
        dr.freqcircleg()
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show() 
        self.fignow=2
    def timeout(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        dr=Figure_Canvas()
        dr.timeoutg()
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        self.Xmin.setText(str(np.min(t_signal)))
        self.Ymin.setText(str(0))
        self.Xmax.setText(str(np.max(t_signal)))
        self.Ymax.setText(str('%.4g'%np.max(abs1_OUT_time[-1])))
        self.fignow=3
    def freqout(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        dr=Figure_Canvas()
        dr.freqoutg()
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        self.Xmin.setText(str(970))
        self.Ymin.setText(str(0))
        self.Xmax.setText(str(1090))
        self.Ymax.setText(str('%.4g'%np.max(freqoutdata)))
        self.fignow=4
    def timeoutset(self,xmin,xmax,ymin,ymax):
        dr=Figure_Canvas()
        dr.timeoutgset(xmin,xmax,ymin,ymax)
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        self.fignow=3
    def freqoutset(self,xmin,xmax,ymin,ymax):
        dr=Figure_Canvas()
        dr.freqoutgset(xmin,xmax,ymin,ymax)
        graphicscene=QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.GraphicsView.setScene(graphicscene)
        self.GraphicsView.show()
        self.fignow=4 
    def adapt(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        if self.fignow==1:
            TTT=[np.ndarray.tolist(t_signal)]
            for i in range(iter):
                TTT.append(np.ndarray.tolist(abs1_OUT_time[i]))
            for t in range(iter+1):
                if t==0:
                    TTT[t].insert(0,"Time(s)")
                else:
                    TTT[t].insert(0,'circle-index %s' %t)
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"数据保存","时域锁模循环.csv")   #getSaveFileName()函数     “另存为”
                np.savetxt(self.filename[0],TTT,fmt='%18s',delimiter=',')
                self.RunInfo.setText('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.setText('Error:File saved faild!!!')
        if self.fignow==2:
            FFF=[np.ndarray.tolist(c/F_signal)]
            for i in range(iter):
                FFF.append(np.ndarray.tolist(abs1_OUT_freq[i]))
            for t in range(iter+1):
                if t==0:
                    FFF[t].insert(0,"Wavelength(m)")
                else:
                    FFF[t].insert(0,'circle-index %s' %t)

            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"数据保存","频域锁模循环.csv")   #getSaveFileName()函数     “另存为”
                np.savetxt(self.filename[0],FFF,fmt='%18s',delimiter=',')
                self.RunInfo.setText('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.setText('Error:File saved faild!!!')
        if self.fignow==3:
            Tout=[np.ndarray.tolist(t_signal)]
            Tout.append(np.ndarray.tolist(abs1_OUT_time[-1]))
            Tout[0].insert(0,'Time(s)')
            Tout[1].insert(0,'Amplitude')
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"数据保存","时域脉冲输出.csv")   #getSaveFileName()函数     “另存为”
                np.savetxt(self.filename[0],Tout,fmt='%18s',delimiter=',')
                self.RunInfo.setText('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.setText('Error:File saved faild!!!')
        if self.fignow==4:
            Fout=[np.ndarray.tolist(c/F_signal)]
            Fout.append(np.ndarray.tolist(abs1_OUT_freq[-1]))
            Fout[0].insert(0,'Wavelength(m)')
            Fout[1].insert(0,'Amplitude')
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"数据保存","脉冲输出频谱.csv")   #getSaveFileName()函数     “另存为”
                np.savetxt(self.filename[0],Fout,fmt='%18s',delimiter=',')
                self.RunInfo.setText('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.setText('Error:File saved faild!!!')
    def savefig(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        if self.fignow==3:
            xmin=float(self.Xmin.text())
            xmax=float(self.Xmax.text())
            ymin=float(self.Ymin.text())            
            ymax=float(self.Ymax.text())
            plt.plot(t_signal,abs1_OUT_time[-1],'b-', linewidth=2.0)
            plt.xlim(xmin,xmax)
            plt.ylim(ymin,ymax)
            plt.title(u"输出脉冲时域图", fontproperties='SimHei',fontsize=20)
            plt.xlabel(u"时间/ps", fontproperties='SimHei',fontsize=16)
            plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16)
            plt.grid(True)
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"图片保存","时域锁模脉冲.jpg")   #getSaveFileName()函数     “另存为”
                plt.savefig(self.filename[0])
                self.RunInfo.setText('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.setText('Error:File saved faild!!!')
        if self.fignow==4:
            xmin=float(self.Xmin.text())
            xmax=float(self.Xmax.text())
            ymin=float(self.Ymin.text())            
            ymax=float(self.Ymax.text())
            freqout_plot=plt.plot(c/F_signal*1e9,freqoutdata,'r-',linewidth=2)
            plt.xlim(xmin,xmax)
            plt.ylim(ymin,ymax)
            plt.title(u'输出信号频谱图',fontproperties='SimHei',fontsize=20)
            plt.xlabel(u"波长/nm", fontproperties='SimHei',fontsize=16)
            plt.ylabel(u"振幅", fontproperties='SimHei',fontsize=16) 
            plt.grid(True)
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"图片保存","频域锁模脉冲.jpg")   #getSaveFileName()函数     “另存为”
                plt.savefig(self.filename[0])
                self.RunInfo.append('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.append('Error:File saved faild!!!')
        if self.fignow==1:
            fig=plt.figure(dpi=200)
            axes=fig.add_subplot(111,projection='3d')
            for z in np.arange(1,iter,iter//20 ):
                xs=t_signal*1e12
                ys=np.array(abs1_OUT_time[z])
                axes.plot(xs,ys,zs=z,zdir='y')
            axes.set_ylim(0,iter+1)
            axes.set_zlim(0,np.max(abs1_OUT_time))
            plt.title(u'时域锁模过程',fontproperties='SimHei',fontsize=20)
            axes.set_xlabel(u'Time(ps)',fontsize=16)
            axes.set_ylabel(u'circle-index',fontsize=16)
            axes.set_zlabel(u'Amplitude ',fontsize=16)
            plt.grid(True)
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"图片保存","时域锁模过程.jpg")   #getSaveFileName()函数     “另存为”
                plt.savefig(self.filename[0])
                self.RunInfo.append('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.append('Error:File saved faild!!!')
            
        if self.fignow==2:
            fig=plt.figure(dpi=200)
            axes=fig.add_subplot(111,projection='3d')
            for z in np.arange(1,iter,iter//20):
                    xs=c/F_signal*1e9
                    ys=absl(OUT_freq[z][0])
                    axes.plot(xs,ys,zs=z,zdir='y')
            axes.set_ylim(0,iter+1)
            axes.set_zlim(0,np.max(abs1_OUT_freq))
            plt.title(u'频域锁模过程',fontproperties='SimHei',fontsize=20)
            axes.set_xlabel(u'wavelength(nm)',fontsize=16)
            axes.set_ylabel(u'circle-index',fontsize=16)
            axes.set_zlabel(u'Amplitude ',fontsize=16)
            plt.grid(True)
            try:
                fd = QFileDialog()
                self.filename =fd.getSaveFileName(self,"图片保存","频域锁模过程.jpg")   #getSaveFileName()函数     “另存为”
                plt.savefig(self.filename[0])
                self.RunInfo.append('File saved in'+self.filename[0]) 
            except:
                self.RunInfo.append('Error:File saved faild!!!')
    def justment(self):
        if self.donee==0:
            self.RunInfo.append("Error：请先进行计算操作！")
            return None
        doneeee=0
        if self.fignow==3:
            try:
                xmin=float(self.Xmin.text())
                xmax=float(self.Xmax.text())
                ymin=float(self.Ymin.text())            
                ymax=float(self.Ymax.text())
                if xmin>=xmax:
                        self.RunInfo.append('x轴限定范围错误')
                        doneeee+=1
                if xmin>=xmax:
                        self.RunInfo.append('y轴限定范围错误')
                        doneeee+=1
            except:
                self.RunInfo.append('范围限定有误')
            if doneeee==0:   
                self.timeoutset(xmin,xmax,ymin,ymax)
            else:
                return None
        if self.fignow==4:
            try:
                xmin=float(self.Xmin.text())
                xmax=float(self.Xmax.text())
                ymin=float(self.Ymin.text())            
                ymax=float(self.Ymax.text())
                if xmin>=xmax:
                        self.RunInfo.append('x轴限定范围错误')
                        doneeee+=1
                if xmin>=xmax:
                        self.RunInfo.append('y轴限定范围错误')
                        doneeee+=1
            except:
                self.RunInfo.append('范围限定有误')
            if doneeee==0:   
                self.freqoutset(xmin,xmax,ymin,ymax)
            else:
                return None
        if self.fignow==1 or self.fignow==2:
            self.RunInfo.append('三维视图不支持调整，请下载数据自行画图，抱歉！')
            
            
            

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()







app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())

