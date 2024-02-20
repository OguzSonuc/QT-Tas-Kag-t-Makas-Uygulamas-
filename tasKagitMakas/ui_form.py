# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_anaPencere(object):
    def setupUi(self, anaPencere):
        if not anaPencere.objectName():
            anaPencere.setObjectName(u"anaPencere")
        anaPencere.resize(329, 275)
        anaPencere.setWindowTitle(u"TA\u015e KA\u011eIT MAKAS")
        self.horizontalLayout = QHBoxLayout(anaPencere)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(anaPencere)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sayac = QLabel(self.groupBox)
        self.sayac.setObjectName(u"sayac")

        self.verticalLayout_2.addWidget(self.sayac)

        self.radioMakas = QRadioButton(self.groupBox)
        self.radioMakas.setObjectName(u"radioMakas")

        self.verticalLayout_2.addWidget(self.radioMakas)

        self.radioTas = QRadioButton(self.groupBox)
        self.radioTas.setObjectName(u"radioTas")

        self.verticalLayout_2.addWidget(self.radioTas)

        self.radioKagit = QRadioButton(self.groupBox)
        self.radioKagit.setObjectName(u"radioKagit")

        self.verticalLayout_2.addWidget(self.radioKagit)

        self.label_1 = QLabel(self.groupBox)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_2.addWidget(self.label_1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(anaPencere)

        QMetaObject.connectSlotsByName(anaPencere)
    # setupUi

    def retranslateUi(self, anaPencere):
        self.groupBox.setTitle(QCoreApplication.translate("anaPencere", u"GroupBox", None))
        self.sayac.setText(QCoreApplication.translate("anaPencere", u"SAYA\u00c7 = 0", None))
        self.radioMakas.setText(QCoreApplication.translate("anaPencere", u"Makas", None))
        self.radioTas.setText(QCoreApplication.translate("anaPencere", u"Ta\u015f", None))
        self.radioKagit.setText(QCoreApplication.translate("anaPencere", u"Ka\u011f\u0131t", None))
        self.label_1.setText(QCoreApplication.translate("anaPencere", u"PC SE\u00c7\u0130M\u0130 :", None))
        self.label_2.setText(QCoreApplication.translate("anaPencere", u"DURUM : ", None))
        self.label_3.setText(QCoreApplication.translate("anaPencere", u"S\u0130Z:                     B\u0130LG\u0130SAYAR:", None))
        pass
    # retranslateUi

