# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options.ui'
#
# Created: Mon Dec 12 19:00:36 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName(_fromUtf8("Options"))
        Options.setWindowModality(QtCore.Qt.ApplicationModal)
        Options.resize(279, 239)
        Options.setWindowTitle(_("Linkchecker options"))
        self.verticalLayout = QtGui.QVBoxLayout(Options)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gui_options = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gui_options.sizePolicy().hasHeightForWidth())
        self.gui_options.setSizePolicy(sizePolicy)
        self.gui_options.setToolTip(_fromUtf8(""))
        self.gui_options.setObjectName(_fromUtf8("gui_options"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gui_options)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_8 = QtGui.QLabel(self.gui_options)
        self.label_8.setMinimumSize(QtCore.QSize(240, 0))
        self.label_8.setText(_("The most common check options are configurable. They override any configuration file settings."))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.frame = QtGui.QFrame(self.gui_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setHorizontalSpacing(4)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.label.setText(_("Recursive depth"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.recursionlevel = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recursionlevel.sizePolicy().hasHeightForWidth())
        self.recursionlevel.setSizePolicy(sizePolicy)
        self.recursionlevel.setMinimumSize(QtCore.QSize(0, 25))
        self.recursionlevel.setToolTip(_("Check recursively all links up to given depth. A negative depth will enable infinite recursion."))
        self.recursionlevel.setMinimum(-1)
        self.recursionlevel.setMaximum(100)
        self.recursionlevel.setProperty("value", -1)
        self.recursionlevel.setObjectName(_fromUtf8("recursionlevel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.recursionlevel)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.label_2.setText(_("Verbose output"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verbose = QtGui.QCheckBox(self.frame)
        self.verbose.setEnabled(True)
        self.verbose.setToolTip(_("Log all checked URLs once. Default is to log only errors and warnings."))
        self.verbose.setText(_fromUtf8(""))
        self.verbose.setObjectName(_fromUtf8("verbose"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.verbose)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setText(_("Debug"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.debug = QtGui.QCheckBox(self.frame)
        self.debug.setText(_fromUtf8(""))
        self.debug.setObjectName(_fromUtf8("debug"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.debug)
        self.warningregex = QtGui.QLineEdit(self.frame)
        self.warningregex.setObjectName(_fromUtf8("warningregex"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.warningregex)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setText(_("Warning regex"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_3.addWidget(self.frame)
        self.widget = QtGui.QWidget(self.gui_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setText(_("Close"))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_3.addWidget(self.widget)
        self.tabWidget.addTab(self.gui_options, _fromUtf8(""))
        self.config_options = QtGui.QWidget()
        self.config_options.setToolTip(_fromUtf8(""))
        self.config_options.setObjectName(_fromUtf8("config_options"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.config_options)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_9 = QtGui.QLabel(self.config_options)
        self.label_9.setText(_("The user configuration file holds advanced options and can be edited with an integrated text editor."))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_5.addWidget(self.label_9)
        self.frame_2 = QtGui.QFrame(self.config_options)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.user_config_label = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_config_label.sizePolicy().hasHeightForWidth())
        self.user_config_label.setSizePolicy(sizePolicy)
        self.user_config_label.setToolTip(_("Overrides system wide configuration file settings."))
        self.user_config_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.user_config_label.setLineWidth(0)
        self.user_config_label.setText(_("/home/user/.linkchecker/linkcheckerrc"))
        self.user_config_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_config_label.setWordWrap(True)
        self.user_config_label.setMargin(0)
        self.user_config_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.user_config_label.setObjectName(_fromUtf8("user_config_label"))
        self.verticalLayout_4.addWidget(self.user_config_label)
        self.user_config_button = QtGui.QPushButton(self.frame_2)
        self.user_config_button.setEnabled(False)
        self.user_config_button.setToolTip(_fromUtf8(""))
        self.user_config_button.setText(_("Edit"))
        self.user_config_button.setObjectName(_fromUtf8("user_config_button"))
        self.verticalLayout_4.addWidget(self.user_config_button)
        self.verticalLayout_5.addWidget(self.frame_2)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.tabWidget.addTab(self.config_options, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Options)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gui_options), _("GUI options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_options), _("Configuration file"))

