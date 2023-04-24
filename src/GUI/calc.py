# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import ply
from PyQt6 import QtCore, QtGui, QtWidgets
from parser import Parser
import traceback
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.calc_performed = False
        self.btn_eq = None
        self.btn_fact = None
        self.btn_lparen = None
        self.btn_back = None
        self.btn_min = None
        self.btn_plus = None
        self.btn_umin = None
        self.btn_3 = None
        self.btn_dot = None
        self.btn_0 = None
        self.btn_div = None
        self.btn_2 = None
        self.btn_1 = None
        self.verticalLayout = None
        self.btn_sqrt = None
        self.btn_7 = None
        self.btn_clear = None
        self.btn_pow = None
        self.btn_5 = None
        self.btn_6 = None
        self.btn_4 = None
        self.btn_9 = None
        self.btn_rparen = None
        self.btn_mult = None
        self.btn_8 = None
        self.gridLayout = None
        self.lineEdit = None
        self.centralwidget = None

        self.parser = Parser()
        self.scan_error = False

    ########### AUTOGENERATED DONT TOUCH ###########
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_mult = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        self.btn_mult.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 3, 4, 1, 1)
        self.btn_rparen = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rparen.sizePolicy().hasHeightForWidth())
        self.btn_rparen.setSizePolicy(sizePolicy)
        self.btn_rparen.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_rparen.setFont(font)
        self.btn_rparen.setObjectName("btn_rparen")
        self.gridLayout.addWidget(self.btn_rparen, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 3, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 3, 3, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 3, 2, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pow.sizePolicy().hasHeightForWidth())
        self.btn_pow.setSizePolicy(sizePolicy)
        self.btn_pow.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.gridLayout.addWidget(self.btn_pow, 3, 5, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 1, 5, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 1, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(75, 48))
        font = QtGui.QFont()
        # font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 2, 5, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 4, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 4, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 2, 4, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 5, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 5, 3, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 4, 3, 1, 1)
        self.btn_umin = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_umin.sizePolicy().hasHeightForWidth())
        self.btn_umin.setSizePolicy(sizePolicy)
        self.btn_umin.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_umin.setFont(font)
        self.btn_umin.setObjectName("btn_umin")
        self.gridLayout.addWidget(self.btn_umin, 5, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 5, 4, 1, 1)
        self.btn_min = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        self.btn_min.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_min.setFont(font)
        self.btn_min.setObjectName("btn_min")
        self.gridLayout.addWidget(self.btn_min, 4, 4, 1, 1)
        self.btn_back = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 1, 4, 1, 1)
        self.btn_lparen = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lparen.sizePolicy().hasHeightForWidth())
        self.btn_lparen.setSizePolicy(sizePolicy)
        self.btn_lparen.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_lparen.setFont(font)
        self.btn_lparen.setObjectName("btn_lparen")
        self.gridLayout.addWidget(self.btn_lparen, 1, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy)
        self.btn_fact.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 1, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setMinimumSize(QtCore.QSize(75, 47))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue")
        font.setPointSize(25)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 4, 5, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        ########### END OF AUTOGENERATED STUFF, YOU CAN TOUCH FROM HERE ###########

        #   click events for number buttons
        self.btn_0.clicked.connect(self.click_event_number)
        self.btn_1.clicked.connect(self.click_event_number)
        self.btn_2.clicked.connect(self.click_event_number)
        self.btn_3.clicked.connect(self.click_event_number)
        self.btn_4.clicked.connect(self.click_event_number)
        self.btn_5.clicked.connect(self.click_event_number)
        self.btn_6.clicked.connect(self.click_event_number)
        self.btn_7.clicked.connect(self.click_event_number)
        self.btn_8.clicked.connect(self.click_event_number)
        self.btn_9.clicked.connect(self.click_event_number)

        #   click events for operators
        self.btn_plus.clicked.connect(self.click_event_op)
        self.btn_min.clicked.connect(self.click_event_op)
        self.btn_mult.clicked.connect(self.click_event_op)
        self.btn_div.clicked.connect(self.click_event_op)
        self.btn_pow.clicked.connect(self.click_event_op)
        self.btn_sqrt.clicked.connect(self.click_event_op)
        self.btn_lparen.clicked.connect(self.click_event_op)
        self.btn_rparen.clicked.connect(self.click_event_op)
        self.btn_fact.clicked.connect(self.click_event_op)
        self.btn_dot.clicked.connect(self.click_event_op)
        self.btn_umin.clicked.connect(self.click_event_op)

        #   click events for text formatting
        self.btn_clear.clicked.connect(self.click_event_text_format)
        self.btn_back.clicked.connect(self.click_event_text_format)
        self.btn_eq.clicked.connect(self.click_event_calc)

        #   keyPressEvents
        self.centralwidget.keyPressEvent = self.keyPressEvent

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.btn_lparen.setText(_translate("MainWindow", "("))
        self.btn_rparen.setText(_translate("MainWindow", ")"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_pow.setText(_translate("MainWindow", "^"))
        self.btn_sqrt.setText(_translate("MainWindow", "y√x"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_fact.setText(_translate("MainWindow", "!"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_umin.setText(_translate("MainWindow", "+/-"))
        self.btn_back.setText(_translate("MainWindow", "DEL"))
        self.btn_eq.setText(_translate("MainWindow", "="))

    def click_event_number(self):
        _translate = QtCore.QCoreApplication.translate
        data = self.lineEdit.text()
        if self.scan_error or (data != "" and self.calc_performed):
            data = ''
            self.scan_error = False
            self.calc_performed = False
        btn_val = MainWindow.sender().objectName().strip("btn_")
        self.lineEdit.setText(_translate("MainWindow", data + btn_val))


    def click_event_op(self):
        ops = {
            'plus': '+',
            'min': '-',
            'mult': '*',
            'div': '/',
            'pow': '^',
            'sqrt': '√(',
            'lparen': '(',
            'rparen': ')',
            'dot': '.',
            'fact': '!',
            'umin': ''
        }
        _translate = QtCore.QCoreApplication.translate
        data = self.lineEdit.text()
        btn_name = MainWindow.sender().objectName()
        btn_val = ops[btn_name.split("_")[1]]
        # handle specific operators differently
        #  '√' button
        if btn_name == 'btn_sqrt':
            if data != '' and self.calc_performed:
                self.lineEdit.setText(_translate("MainWindow", '2' + btn_val + data + ")"))
            else:
                self.lineEdit.setText(_translate("MainWindow", data + btn_val))
            if data == '':
                self.lineEdit.setText(_translate("MainWindow", '2' + btn_val + data))
        #  '(' button
        elif btn_name == 'btn_lparen' and self.calc_performed:
            self.lineEdit.setText(_translate("MainWindow", data + "*("))
            self.btn_sqrt.setText(_translate("MainWindow", "y√x"))
        #  '+/-' button
        elif btn_name == 'btn_umin':
            self.btn_sqrt.setText(_translate("MainWindow", "y√x"))
            try:
                if data[0] == '-':
                    # result is negative so flip to positive
                    self.lineEdit.setText(_translate("MainWindow", data[1:]))
                else:
                    # result is positive so add button value
                    self.lineEdit.setText(_translate("MainWindow", '-' + data))
            except IndexError:
                pass
        else:
            self.lineEdit.setText(_translate("MainWindow", data + btn_val))
            self.btn_sqrt.setText(_translate("MainWindow", "y√x"))
        self.calc_performed = False

    def click_event_text_format(self):
        _translate = QtCore.QCoreApplication.translate
        data = self.lineEdit.text()
        btn_val = MainWindow.sender().objectName().split("_")[1]
        if btn_val == 'clear':
            self.lineEdit.setText(_translate("MainWindow", ""))
            self.btn_sqrt.setText(_translate("MainWindow", "y√x"))
            self.calc_performed = False
        if btn_val == 'back':
            self.lineEdit.setText(_translate("MainWindow", data[:-1]))

    def click_event_calc(self):
        _translate = QtCore.QCoreApplication.translate
        if self.scan_error:
            data = ''
        else:
            data = self.lineEdit.text()
        try:
            ans = format_data(self.parser.parser.parse(data))
        except SyntaxError:
            ans = 'Syntax error'
            self.scan_error = True
        except ply.lex.LexError:
            ans = 'Scanning error'
            self.scan_error = True
        except ZeroDivisionError:
            ans = 'Cant divide by 0'
            self.scan_error = True
        except FloatingPointError:
            ans = 'Not an integer'
            self.scan_error = True
        except OverflowError:
            ans = 'Number is too large'
            self.scan_error = True
        self.calc_performed = True
        self.lineEdit.setText(_translate("MainWindow", ans))
        if not self.scan_error:
            self.btn_sqrt.setText(_translate("MainWindow", "2√x"))

    #   calculate when enter/return pressed
    def keyPressEvent(self, event):
        _translate = QtCore.QCoreApplication.translate
        if event.key() in (QtCore.Qt.Key.Key_Enter, QtCore.Qt.Key.Key_Return):
            self.click_event_calc()

def format_data(ans):
    try:
        if ans.is_integer():
            ans = str(int(ans))
        else:
            ans = str(round(ans, 10))
    except AttributeError:
        pass
    return ans


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb, file=sys.stderr)



sys.excepthook = excepthook
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


if __name__ == "__main__":
    pass
    # MainWindow.show()
    # sys.exit(app.exec())