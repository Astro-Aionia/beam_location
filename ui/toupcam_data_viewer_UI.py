# Form implementation generated from reading ui file 'toupcam_data_viewer_UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_toupcam_data_viewer(object):
    def setupUi(self, toupcam_data_viewer):
        toupcam_data_viewer.setObjectName("toupcam_data_viewer")
        toupcam_data_viewer.resize(500, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toupcam_data_viewer.sizePolicy().hasHeightForWidth())
        toupcam_data_viewer.setSizePolicy(sizePolicy)
        toupcam_data_viewer.setMinimumSize(QtCore.QSize(0, 0))
        toupcam_data_viewer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(toupcam_data_viewer)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(parent=toupcam_data_viewer)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=toupcam_data_viewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(480, 360))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(toupcam_data_viewer)
        QtCore.QMetaObject.connectSlotsByName(toupcam_data_viewer)

    def retranslateUi(self, toupcam_data_viewer):
        _translate = QtCore.QCoreApplication.translate
        toupcam_data_viewer.setWindowTitle(_translate("toupcam_data_viewer", "toupcam_data viewer"))
        self.label_1.setText(_translate("toupcam_data_viewer", "Latest Photo"))
