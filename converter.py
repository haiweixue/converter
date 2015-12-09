#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from coder import Convertor
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QFileDialog

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

class Ui_Dialog(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(761, 595)
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit_source = QtGui.QTextEdit(Dialog)
        self.textEdit_source.setObjectName(_fromUtf8("textEdit_source"))
        self.gridLayout.addWidget(self.textEdit_source, 1, 0, 1, 4)
        self.pushButton_loadSourceFile = QtGui.QPushButton(Dialog)
        self.pushButton_loadSourceFile.setObjectName(_fromUtf8("pushButton_loadSourceFile"))
        self.gridLayout.addWidget(self.pushButton_loadSourceFile, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.pushButton_saveSourceFile = QtGui.QPushButton(Dialog)
        self.pushButton_saveSourceFile.setObjectName(_fromUtf8("pushButton_saveSourceFile"))
        self.gridLayout.addWidget(self.pushButton_saveSourceFile, 0, 1, 1, 1)
        self.label_sourceFilePath = QtGui.QLabel(Dialog)
        self.label_sourceFilePath.setObjectName(_fromUtf8("label_sourceFilePath"))
        self.gridLayout.addWidget(self.label_sourceFilePath, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 3, 1, 1)
        self.pushButton_loadDstFile = QtGui.QPushButton(Dialog)
        self.pushButton_loadDstFile.setObjectName(_fromUtf8("pushButton_loadDstFile"))
        self.gridLayout_2.addWidget(self.pushButton_loadDstFile, 2, 0, 1, 1)
        self.pushButton_saveDstFile = QtGui.QPushButton(Dialog)
        self.pushButton_saveDstFile.setObjectName(_fromUtf8("pushButton_saveDstFile"))
        self.gridLayout_2.addWidget(self.pushButton_saveDstFile, 2, 1, 1, 1)
        self.pushButton_exit = QtGui.QPushButton(Dialog)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.gridLayout_2.addWidget(self.pushButton_exit, 2, 4, 1, 1)
        self.textEdit_destination = QtGui.QTextEdit(Dialog)
        self.textEdit_destination.setObjectName(_fromUtf8("textEdit_destination"))
        self.gridLayout_2.addWidget(self.textEdit_destination, 0, 0, 1, 5)
        self.label_destinationFilePath = QtGui.QLabel(Dialog)
        self.label_destinationFilePath.setObjectName(_fromUtf8("label_destinationFilePath"))
        self.gridLayout_2.addWidget(self.label_destinationFilePath, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioButton_base16 = QtGui.QRadioButton(Dialog)
        self.radioButton_base16.setObjectName(_fromUtf8("radioButton_base16"))
        self.gridLayout_3.addWidget(self.radioButton_base16, 4, 1, 1, 1)
        self.pushButton_encode_u = QtGui.QPushButton(Dialog)
        self.pushButton_encode_u.setObjectName(_fromUtf8("pushButton_encode_u"))
        self.gridLayout_3.addWidget(self.pushButton_encode_u, 12, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 9, 2, 1, 1)
        self.radioButton_dec = QtGui.QRadioButton(Dialog)
        self.radioButton_dec.setObjectName(_fromUtf8("radioButton_dec"))
        self.gridLayout_3.addWidget(self.radioButton_dec, 0, 1, 1, 1)
        self.radioButton_url = QtGui.QRadioButton(Dialog)
        self.radioButton_url.setObjectName(_fromUtf8("radioButton_url"))
        self.gridLayout_3.addWidget(self.radioButton_url, 2, 1, 1, 1)
        self.radioButton_md532 = QtGui.QRadioButton(Dialog)
        self.radioButton_md532.setObjectName(_fromUtf8("radioButton_md532"))
        self.gridLayout_3.addWidget(self.radioButton_md532, 5, 1, 1, 1)
        self.radioButton_base64 = QtGui.QRadioButton(Dialog)
        self.radioButton_base64.setObjectName(_fromUtf8("radioButton_base64"))
        self.gridLayout_3.addWidget(self.radioButton_base64, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 9, 1, 1, 1)
        self.radioButton_jsfuck = QtGui.QRadioButton(Dialog)
        self.radioButton_jsfuck.setObjectName(_fromUtf8("radioButton_jsfuck"))
        self.gridLayout_3.addWidget(self.radioButton_jsfuck, 1, 2, 1, 1)
        self.radioButton_html = QtGui.QRadioButton(Dialog)
        self.radioButton_html.setObjectName(_fromUtf8("radioButton_html"))
        self.gridLayout_3.addWidget(self.radioButton_html, 2, 2, 1, 1)
        self.radioButton_hex = QtGui.QRadioButton(Dialog)
        self.radioButton_hex.setObjectName(_fromUtf8("radioButton_hex"))
        self.gridLayout_3.addWidget(self.radioButton_hex, 0, 2, 1, 1)
        self.radioButton_base32 = QtGui.QRadioButton(Dialog)
        self.radioButton_base32.setObjectName(_fromUtf8("radioButton_base32"))
        self.gridLayout_3.addWidget(self.radioButton_base32, 3, 2, 1, 1)
        self.radioButton_md516 = QtGui.QRadioButton(Dialog)
        self.radioButton_md516.setObjectName(_fromUtf8("radioButton_md516"))
        self.gridLayout_3.addWidget(self.radioButton_md516, 5, 2, 1, 1)
        self.radioButton_ascii = QtGui.QRadioButton(Dialog)
        self.radioButton_ascii.setObjectName(_fromUtf8("radioButton_ascii"))
        self.gridLayout_3.addWidget(self.radioButton_ascii, 1, 1, 1, 1)
        self.radioButton_utf7 = QtGui.QRadioButton(Dialog)
        self.radioButton_utf7.setObjectName(_fromUtf8("radioButton_utf7"))
        self.gridLayout_3.addWidget(self.radioButton_utf7, 4, 2, 1, 1)
        self.radioButton_rail_fence = QtGui.QRadioButton(Dialog)
        self.radioButton_rail_fence.setObjectName(_fromUtf8("radioButton_rail_fence"))
        self.gridLayout_3.addWidget(self.radioButton_rail_fence, 6, 2, 1, 1)
        self.radioButton_morse = QtGui.QRadioButton(Dialog)
        self.radioButton_morse.setObjectName(_fromUtf8("radioButton_morse"))
        self.gridLayout_3.addWidget(self.radioButton_morse, 6, 1, 1, 1)
        self.pushButton_encode_d = QtGui.QPushButton(Dialog)
        self.pushButton_encode_d.setObjectName(_fromUtf8("pushButton_encode_d"))
        self.gridLayout_3.addWidget(self.pushButton_encode_d, 11, 1, 1, 1)
        self.pushButton_decode_u = QtGui.QPushButton(Dialog)
        self.pushButton_decode_u.setObjectName(_fromUtf8("pushButton_decode_u"))
        self.gridLayout_3.addWidget(self.pushButton_decode_u, 12, 2, 1, 1)
        self.pushButton_decode_d = QtGui.QPushButton(Dialog)
        self.pushButton_decode_d.setObjectName(_fromUtf8("pushButton_decode_d"))
        self.gridLayout_3.addWidget(self.pushButton_decode_d, 11, 2, 1, 1)
        self.label_notice = QtGui.QLabel(Dialog)
        self.label_notice.setText(_fromUtf8(""))
        self.label_notice.setObjectName(_fromUtf8("label_notice"))
        self.gridLayout_3.addWidget(self.label_notice, 8, 1, 1, 2)
        self.checkBox_auto = QtGui.QCheckBox(Dialog)
        self.checkBox_auto.setObjectName(_fromUtf8("checkBox_auto"))
        self.gridLayout_3.addWidget(self.checkBox_auto, 7, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.label_bottom = QtGui.QLabel(Dialog)
        self.label_bottom.setObjectName(_fromUtf8("label_bottom"))
        self.gridLayout_4.addWidget(self.label_bottom, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_loadSourceFile.setText(_translate("Dialog", "Set File ...", None))
        self.pushButton_saveSourceFile.setText(_translate("Dialog", "Save", None))
        self.label_sourceFilePath.setText(_translate("Dialog", "未选择文件", None))
        self.pushButton_loadDstFile.setText(_translate("Dialog", "Set File ...", None))
        self.pushButton_saveDstFile.setText(_translate("Dialog", "Save", None))
        self.pushButton_exit.setText(_translate("Dialog", "Exit", None))
        self.label_destinationFilePath.setText(_translate("Dialog", "未选择文件", None))
        self.radioButton_base16.setText(_translate("Dialog", "Base16", None))
        self.pushButton_encode_u.setText(_translate("Dialog", "编码↑", None))
        self.radioButton_dec.setText(_translate("Dialog", "Dec", None))
        self.radioButton_url.setText(_translate("Dialog", "URL", None))
        self.radioButton_md532.setText(_translate("Dialog", "MD5-32", None))
        self.radioButton_base64.setText(_translate("Dialog", "Base64", None))
        self.radioButton_jsfuck.setText(_translate("Dialog", "JsFuck", None))
        self.radioButton_html.setText(_translate("Dialog", "HTML", None))
        self.radioButton_hex.setText(_translate("Dialog", "Hex", None))
        self.radioButton_base32.setText(_translate("Dialog", "Base32", None))
        self.radioButton_md516.setText(_translate("Dialog", "MD5-16", None))
        self.radioButton_ascii.setText(_translate("Dialog", "ASCII", None))
        self.radioButton_utf7.setText(_translate("Dialog", "UTF-7", None))
        self.radioButton_rail_fence.setText(_translate("Dialog", "栅栏密码", None))
        self.radioButton_morse.setText(_translate("Dialog", "摩斯密码", None))
        self.pushButton_encode_d.setText(_translate("Dialog", "编码↓", None))
        self.pushButton_decode_u.setText(_translate("Dialog", "解码↑", None))
        self.pushButton_decode_d.setText(_translate("Dialog", "解码↓", None))
        self.checkBox_auto.setText(_translate("Dialog", "自动识别", None))
        self.label_bottom.setText(_translate("Dialog", "Status", None))


        self.radio_buttons = {
            'url'   : self.radioButton_url,
            'utf7'  : self.radioButton_utf7,
            'ascii' : self.radioButton_ascii,
            'base16': self.radioButton_base16,
            'base32': self.radioButton_base32,
            'base64': self.radioButton_base64,
            'hex'   : self.radioButton_hex,
            'dec'   : self.radioButton_dec,
            'html'  : self.radioButton_html,
            'jsfuck': self.radioButton_jsfuck,
            'md516' : self.radioButton_md516,
            'md532' : self.radioButton_md532,
            'morse' : self.radioButton_morse,
            'rail'  : self.radioButton_rail_fence
        }
        self.sourceBuf      = ""
        self.destinationBuf = ""

        # 退出按钮
        self.pushButton_exit.clicked.connect(app.exit)

        # 编辑框内容变化
        self.textEdit_source.textChanged.connect(self.SourceTextboxChanged)
        self.textEdit_destination.textChanged.connect(self.DestinationTextboxChanged)

        # 转换按钮
        self.pushButton_decode_d.clicked.connect(self.DecodingRouter_d)
        self.pushButton_encode_d.clicked.connect(self.EncodingRouter_d)
        self.pushButton_decode_u.clicked.connect(self.DecodingRouter_u)
        self.pushButton_encode_u.clicked.connect(self.EncodingRouter_u)

        # 加载文件按钮
        self.pushButton_loadSourceFile.clicked.connect(self.SetSourceFile)
        self.pushButton_loadDstFile.clicked.connect(self.SetDestinationFile)

        # 保存文件
        self.pushButton_saveSourceFile.clicked.connect(self.SaveSourceFile)

        # 自动识别编码
        self.checkBox_auto.toggled.connect(self.AutoDetectCoding)

        # 特殊编码特殊处理
        self.radioButton_dec.toggled.connect(self.DecButtonStatusChanged)

    def AutoDetectCoding(self):
        if self.checkBox_auto.isChecked():
            for bt in self.radio_buttons:
                self.radio_buttons[bt].setDisabled(True)

        else:
            for bt in self.radio_buttons:
                self.radio_buttons[bt].setDisabled(False)

        self.label_notice.clear()

    def DecButtonStatusChanged(self):
        if self.radioButton_dec.isChecked():
            self.SetLabelText(self.label_notice,"请使用[空白字符]分割数字","Green")
        else:
            self.label_notice.clear()

    def SaveSourceFile(self):
        f = open("/home/haiwei/b.txt", 'wb')
        f.write(self.sourceBuf)
        f.close()

    def SourceTextboxChanged(self):
        self.sourceBuf = self.textEdit_source.toPlainText()


    def DestinationTextboxChanged(self):
        self.destinationBuf = self.textEdit_destination.toPlainText()

    def SetSourceFile(self):
        self.sourceFile = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "/home/",
            "All Files(*.*)")
        try:
            f = open(self.sourceFile)
            self.sourceBuf = f.read()
        except:
            self.SetLabelText(self.label_bottom,"Can not open the file!","Red")
        else:
            self.SetLabelText(self.label_bottom,"Congratulations! No error occurs.","Green")
            self.SetLabelText(self.label_sourceFilePath,self.sourceFile,"Green")
            self.SetTextBox(self.textEdit_source,self.sourceBuf)
        finally:
            f.close()

    def SetDestinationFile(self):
        self.destinationFile = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "/home/",
            "All Files(*.*)")
        try:
            f = open(self.destinationFile)
            self.destinationBuf = f.read()
        except:
            self.SetLabelText(self.label_bottom,"Can not open the file!","Red")
        else:
            self.SetLabelText(self.label_bottom,"Congratulations! No error occurs.","Green")
            self.SetLabelText(self.label_destinationFilePath,self.destinationFile,"Green")
            self.SetTextBox(self.textEdit_destination,self.destinationBuf)
        finally:
            f.close()

    def DecodingRouter_d(self):
        buf = {'src':self.sourceBuf, 'dst':self.destinationBuf}
        self.CodingRouter(
            buf,
            {'src':self.textEdit_source, 'dst':self.textEdit_destination},
            'decode'
        )
        self.sourceBuf      = buf['src']
        self.destinationBuf = buf['dst']


    def DecodingRouter_u(self):
        buf = {'dst':self.sourceBuf, 'src':self.destinationBuf}
        self.CodingRouter(
            buf,
            {'dst':self.textEdit_source, 'src':self.textEdit_destination},
            'decode'
        )
        self.sourceBuf      = buf['dst']
        self.destinationBuf = buf['src']

    def EncodingRouter_d(self):
        buf = {'src':self.sourceBuf, 'dst':self.destinationBuf}
        self.CodingRouter(
            buf,
            {'src':self.textEdit_source, 'dst':self.textEdit_destination},
            'encode'
        )
        self.sourceBuf      = buf['src']
        self.destinationBuf = buf['dst']

    def EncodingRouter_u(self):
        buf = {'dst':self.sourceBuf, 'src':self.destinationBuf}
        self.CodingRouter(
            buf,
            {'dst':self.textEdit_source, 'src':self.textEdit_destination},
            'encode'
        )
        self.sourceBuf      = buf['dst']
        self.destinationBuf = buf['src']

    def SetTextBox(self, textbox, text):
        showLen = 800
        fileLen = len(text)

        self.textEdit_source.textChanged.disconnect(self.SourceTextboxChanged)
        self.textEdit_destination.textChanged.disconnect(self.DestinationTextboxChanged)
        if fileLen > showLen:
            textbox.setHtml(
                text[0:showLen] +
                "...<br><font color=Green><b>"
                "(with other %d characters not displayed)</b></font>" % (fileLen-showLen))
        else:
            textbox.setText(text)
        self.textEdit_source.textChanged.connect(self.SourceTextboxChanged)
        self.textEdit_destination.textChanged.connect(self.DestinationTextboxChanged)


    def SetLabelText(self, label, text, color):
        label.setText(
            QString.fromUtf8("<font color=%s><b>%s</b></font>" %(color,text)))

    def CodingRouter(self, buf, textBox, coding):
        res = ['','']
        for key in self.radio_buttons:
            if self.radio_buttons[key].isChecked():
                if coding is "decode":
                    call_fun = key + Convertor.decode_function_suffix
                else:
                    call_fun = Convertor.encode_function_preffix + key
                try:
                    getattr(Convertor, call_fun)(buf['src'], res)
                except:
                    self.SetLabelText(
                        self.label_bottom,
                        QString.fromUtf8(sys.exc_info()[1].message) + QString.fromAscii(res[1]),
                        'Red')
                else:
                    self.SetLabelText(self.label_bottom,"Congratulations! No error occurs.","Green")
                finally:
                    buf['dst'] = res[0]
                    self.SetTextBox(textBox['dst'],buf['dst'])
                break


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

