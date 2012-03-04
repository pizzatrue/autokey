#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from phrasepage.ui on Sun Mar  4 11:39:40 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PhrasePage(object):
    def setupUi(self, PhrasePage):
        PhrasePage.setObjectName(_fromUtf8("PhrasePage"))
        PhrasePage.resize(540, 421)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PhrasePage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.urlLabel = KUrlLabel(PhrasePage)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName(_fromUtf8("urlLabel"))
        self.verticalLayout_2.addWidget(self.urlLabel)
        self.phraseText = KTextEdit(PhrasePage)
        self.phraseText.setTabChangesFocus(True)
        self.phraseText.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.phraseText.setAcceptRichText(False)
        self.phraseText.setObjectName(_fromUtf8("phraseText"))
        self.verticalLayout_2.addWidget(self.phraseText)
        self.settingsGroupBox = QtGui.QGroupBox(PhrasePage)
        self.settingsGroupBox.setObjectName(_fromUtf8("settingsGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.promptCheckbox = QtGui.QCheckBox(self.settingsGroupBox)
        self.promptCheckbox.setObjectName(_fromUtf8("promptCheckbox"))
        self.verticalLayout.addWidget(self.promptCheckbox)
        self.showInTrayCheckbox = QtGui.QCheckBox(self.settingsGroupBox)
        self.showInTrayCheckbox.setObjectName(_fromUtf8("showInTrayCheckbox"))
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.settingsGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.sendModeCombo = QtGui.QComboBox(self.settingsGroupBox)
        self.sendModeCombo.setObjectName(_fromUtf8("sendModeCombo"))
        self.horizontalLayout_2.addWidget(self.sendModeCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kseparator = KSeparator(self.settingsGroupBox)
        self.kseparator.setObjectName(_fromUtf8("kseparator"))
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupBox)
        self.settingsWidget.setObjectName(_fromUtf8("settingsWidget"))
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)

        self.retranslateUi(PhrasePage)
        QtCore.QMetaObject.connectSlotsByName(PhrasePage)

    def retranslateUi(self, PhrasePage):
        PhrasePage.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.urlLabel.setTipText(kdecore.i18n(_fromUtf8("Open the phrase in the default text editor")))
        self.settingsGroupBox.setTitle(kdecore.i18n(_fromUtf8("Phrase Settings")))
        self.promptCheckbox.setText(kdecore.i18n(_fromUtf8("Always prompt before pasting this phrase")))
        self.showInTrayCheckbox.setText(kdecore.i18n(_fromUtf8("Show in notification icon menu")))
        self.label.setText(kdecore.i18n(_fromUtf8("Paste using")))

from PyKDE4.kdeui import KUrlLabel, KSeparator, KTextEdit
from configwindow import SettingsWidget
