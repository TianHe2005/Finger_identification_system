# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(286, 353)
        Widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(170, 80, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 80, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(10, 120, 251, 211))
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 40, 111, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 40, 12))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 180, 141, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(29, 71, 191, 91))
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(Widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 120, 271, 221))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(49, 71, 171, 91))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 30, 61, 18))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 200, 56, 18))
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.widget.raise_()

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "注册"))
        self.pushButton_2.setText(_translate("Widget", "登录"))
        self.pushButton_3.setText(_translate("Widget", "录入指纹"))
        self.label.setText(_translate("Widget", "用户名"))
        self.pushButton_4.setText(_translate("Widget", "注册"))
        self.label_3.setText(_translate("Widget", "指纹图片"))
        self.label_2.setText(_translate("Widget", "TextLabel"))
        self.pushButton_5.setText(_translate("Widget", "选择指纹"))
        self.pushButton_6.setText(_translate("Widget", "登录"))
