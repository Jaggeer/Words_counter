from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(713, 471)
        Form.setMinimumSize(QSize(713, 471))
        font = QFont()
        font.setFamilies([u"Cuprum"])
        font.setBold(False)
        Form.setFont(font)
        Form.setStyleSheet(u"QWidget {\n"
"    font-family: 'Cuprum';\n"
"    font-weight: 400;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font)
        self.tab.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_3 = QScrollArea(self.groupBox_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 443, 364))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_5.addWidget(self.scrollArea_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.verticalSpacer = QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(u" font-family: 'Cuprum';\n"
"    font-weight: 400;\n"
"	font-size: 14px;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 178, 296))
        self.scrollAreaWidgetContents.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.groupBox_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 443, 364))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0443\u0440\u0441\u043e\u0432\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u0437\u041b\u041f\u0431-\u0418\u0421\u0438\u0422-20-1", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0430\u043f\u043e\u043a \u0438 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0430\u043f\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u0438\u0437 \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438:", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043f\u0443\u0442\u044c", None))
        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0424\u0430\u0439\u043b\u044b \u0438 \u043f\u0430\u043f\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0445 \u0441\u043b\u043e\u0432", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0418\u043d\u0434\u0435\u043a\u0441 \u0438 \u043f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

