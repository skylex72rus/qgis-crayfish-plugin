# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crayfish_animation_dialog_widget.ui'
#
# Created: Thu May  7 15:06:54 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CrayfishAnimationDialog(object):
    def setupUi(self, CrayfishAnimationDialog):
        CrayfishAnimationDialog.setObjectName(_fromUtf8("CrayfishAnimationDialog"))
        CrayfishAnimationDialog.resize(455, 376)
        self.verticalLayout_6 = QtGui.QVBoxLayout(CrayfishAnimationDialog)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(CrayfishAnimationDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinWidth = QtGui.QSpinBox(self.tab)
        self.spinWidth.setMinimum(16)
        self.spinWidth.setMaximum(9999)
        self.spinWidth.setProperty("value", 1920)
        self.spinWidth.setObjectName(_fromUtf8("spinWidth"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinWidth)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinHeight = QtGui.QSpinBox(self.tab)
        self.spinHeight.setMinimum(16)
        self.spinHeight.setMaximum(9999)
        self.spinHeight.setProperty("value", 1080)
        self.spinHeight.setObjectName(_fromUtf8("spinHeight"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinHeight)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.cboStart = QtGui.QComboBox(self.tab)
        self.cboStart.setObjectName(_fromUtf8("cboStart"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboStart)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.cboEnd = QtGui.QComboBox(self.tab)
        self.cboEnd.setObjectName(_fromUtf8("cboEnd"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cboEnd)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.spinSpeed = QtGui.QSpinBox(self.tab)
        self.spinSpeed.setMinimum(1)
        self.spinSpeed.setMaximum(60)
        self.spinSpeed.setProperty("value", 5)
        self.spinSpeed.setObjectName(_fromUtf8("spinSpeed"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinSpeed)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.editOutput = QtGui.QLineEdit(self.tab)
        self.editOutput.setObjectName(_fromUtf8("editOutput"))
        self.horizontalLayout.addWidget(self.editOutput)
        self.btnBrowseOutput = QtGui.QToolButton(self.tab)
        self.btnBrowseOutput.setObjectName(_fromUtf8("btnBrowseOutput"))
        self.horizontalLayout.addWidget(self.btnBrowseOutput)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.radLayoutDefault = QtGui.QRadioButton(self.tab_2)
        self.radLayoutDefault.setChecked(True)
        self.radLayoutDefault.setObjectName(_fromUtf8("radLayoutDefault"))
        self.verticalLayout_5.addWidget(self.radLayoutDefault)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 397, 175))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupTitle = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupTitle.setCheckable(True)
        self.groupTitle.setChecked(False)
        self.groupTitle.setObjectName(_fromUtf8("groupTitle"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupTitle)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widgetTitleProps = AnimationLayoutItemProps(self.groupTitle)
        self.widgetTitleProps.setObjectName(_fromUtf8("widgetTitleProps"))
        self.verticalLayout.addWidget(self.widgetTitleProps)
        self.verticalLayout_4.addWidget(self.groupTitle)
        self.groupTime = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupTime.setCheckable(True)
        self.groupTime.setObjectName(_fromUtf8("groupTime"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupTime)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widgetTimeProps = AnimationLayoutItemProps(self.groupTime)
        self.widgetTimeProps.setObjectName(_fromUtf8("widgetTimeProps"))
        self.verticalLayout_2.addWidget(self.widgetTimeProps)
        self.verticalLayout_4.addWidget(self.groupTime)
        self.groupLegend = QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupLegend.setCheckable(True)
        self.groupLegend.setChecked(False)
        self.groupLegend.setObjectName(_fromUtf8("groupLegend"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupLegend)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widgetLegendProps = AnimationLayoutItemProps(self.groupLegend)
        self.widgetLegendProps.setObjectName(_fromUtf8("widgetLegendProps"))
        self.verticalLayout_3.addWidget(self.widgetLegendProps)
        self.verticalLayout_4.addWidget(self.groupLegend)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.radLayoutCustom = QtGui.QRadioButton(self.tab_2)
        self.radLayoutCustom.setObjectName(_fromUtf8("radLayoutCustom"))
        self.verticalLayout_5.addWidget(self.radLayoutCustom)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnBrowseTemplate = QtGui.QToolButton(self.tab_2)
        self.btnBrowseTemplate.setObjectName(_fromUtf8("btnBrowseTemplate"))
        self.gridLayout_2.addWidget(self.btnBrowseTemplate, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.editTemplate = QtGui.QLineEdit(self.tab_2)
        self.editTemplate.setObjectName(_fromUtf8("editTemplate"))
        self.gridLayout_2.addWidget(self.editTemplate, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 2, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.tab_3)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.radQualBest = QtGui.QRadioButton(self.tab_3)
        self.radQualBest.setChecked(False)
        self.radQualBest.setObjectName(_fromUtf8("radQualBest"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.radQualBest)
        self.radQualHigh = QtGui.QRadioButton(self.tab_3)
        self.radQualHigh.setChecked(True)
        self.radQualHigh.setObjectName(_fromUtf8("radQualHigh"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.radQualHigh)
        self.radQualLow = QtGui.QRadioButton(self.tab_3)
        self.radQualLow.setObjectName(_fromUtf8("radQualLow"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.radQualLow)
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBrowseFfmpegPath = QtGui.QToolButton(self.groupBox)
        self.btnBrowseFfmpegPath.setObjectName(_fromUtf8("btnBrowseFfmpegPath"))
        self.gridLayout.addWidget(self.btnBrowseFfmpegPath, 3, 2, 1, 1)
        self.editFfmpegPath = QtGui.QLineEdit(self.groupBox)
        self.editFfmpegPath.setObjectName(_fromUtf8("editFfmpegPath"))
        self.gridLayout.addWidget(self.editFfmpegPath, 3, 1, 1, 1)
        self.radFfmpegCustom = QtGui.QRadioButton(self.groupBox)
        self.radFfmpegCustom.setObjectName(_fromUtf8("radFfmpegCustom"))
        self.gridLayout.addWidget(self.radFfmpegCustom, 3, 0, 1, 1)
        self.radFfmpegSystem = QtGui.QRadioButton(self.groupBox)
        self.radFfmpegSystem.setChecked(True)
        self.radFfmpegSystem.setObjectName(_fromUtf8("radFfmpegSystem"))
        self.gridLayout.addWidget(self.radFfmpegSystem, 2, 0, 1, 4)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 3)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 500, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtGui.QFormLayout.FieldRole, spacerItem2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.progress = QtGui.QProgressBar(CrayfishAnimationDialog)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.horizontalLayout_4.addWidget(self.progress)
        self.buttonBox = QtGui.QDialogButtonBox(CrayfishAnimationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CrayfishAnimationDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CrayfishAnimationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CrayfishAnimationDialog)

    def retranslateUi(self, CrayfishAnimationDialog):
        CrayfishAnimationDialog.setWindowTitle(_translate("CrayfishAnimationDialog", "Export Animation", None))
        self.label_2.setText(_translate("CrayfishAnimationDialog", "Width", None))
        self.spinWidth.setSuffix(_translate("CrayfishAnimationDialog", " px", None))
        self.label_3.setText(_translate("CrayfishAnimationDialog", "Height", None))
        self.spinHeight.setSuffix(_translate("CrayfishAnimationDialog", " px", None))
        self.label_6.setText(_translate("CrayfishAnimationDialog", "Start Time", None))
        self.label_7.setText(_translate("CrayfishAnimationDialog", "End Time", None))
        self.label_8.setText(_translate("CrayfishAnimationDialog", "Speed", None))
        self.spinSpeed.setSuffix(_translate("CrayfishAnimationDialog", " fps", None))
        self.label.setText(_translate("CrayfishAnimationDialog", "Output", None))
        self.btnBrowseOutput.setText(_translate("CrayfishAnimationDialog", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CrayfishAnimationDialog", "General", None))
        self.radLayoutDefault.setText(_translate("CrayfishAnimationDialog", "Default layout", None))
        self.groupTitle.setTitle(_translate("CrayfishAnimationDialog", "Title", None))
        self.groupTime.setTitle(_translate("CrayfishAnimationDialog", "Time", None))
        self.groupLegend.setTitle(_translate("CrayfishAnimationDialog", "Legend", None))
        self.radLayoutCustom.setText(_translate("CrayfishAnimationDialog", "Custom layout (.qpt)", None))
        self.btnBrowseTemplate.setText(_translate("CrayfishAnimationDialog", "...", None))
        self.label_5.setText(_translate("CrayfishAnimationDialog", "Template", None))
        self.label_10.setText(_translate("CrayfishAnimationDialog", "(Note: label with ID \'time\' will display output time)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CrayfishAnimationDialog", "Layout", None))
        self.label_4.setText(_translate("CrayfishAnimationDialog", "Quality", None))
        self.radQualBest.setText(_translate("CrayfishAnimationDialog", "Best (lossless)", None))
        self.radQualHigh.setText(_translate("CrayfishAnimationDialog", "High", None))
        self.radQualLow.setText(_translate("CrayfishAnimationDialog", "Low", None))
        self.btnBrowseFfmpegPath.setText(_translate("CrayfishAnimationDialog", "...", None))
        self.radFfmpegCustom.setText(_translate("CrayfishAnimationDialog", "custom", None))
        self.radFfmpegSystem.setText(_translate("CrayfishAnimationDialog", "default from system path", None))
        self.label_9.setText(_translate("CrayfishAnimationDialog", "Video encoding utility (FFmpeg) to use:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("CrayfishAnimationDialog", "Video", None))

from qgis.gui import QgsCollapsibleGroupBox
from crayfish_animation_layout_item_props import AnimationLayoutItemProps
