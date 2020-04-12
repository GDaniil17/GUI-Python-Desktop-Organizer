from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PIL import Image, ImageGrab
from time import sleep, localtime
import pyautogui
import os
import getpass
import time
from datetime import datetime
from easygui import diropenbox, fileopenbox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.listOfExceptions = {'Cleaner.exe', 'cleaner_cash.txt', 'Cleaner.pyw', 'Extensions.txt', 'extensions.txt', 'Cleaner.py'}

        self.cur = getpass.getuser()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(806, 584)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(806, 584))
        MainWindow.setMaximumSize(QtCore.QSize(806, 584))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(129, 10, 31, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.SaveButton = QtWidgets.QPushButton(self.frame)
        self.SaveButton.setGeometry(QtCore.QRect(580, 370, 191, 61))
        
        self.SaveButton.clicked.connect(self.saveButtonFuntion)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")

        self.TextFolder = QtWidgets.QLineEdit(self.frame)
        self.TextFolder.setGeometry(QtCore.QRect(10, 270, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.TextFolder.setFont(font)
        self.TextFolder.setText("")
        self.TextFolder.setObjectName("TextFolder")
        self.TextExtension = QtWidgets.QLineEdit(self.frame)
        self.TextExtension.setGeometry(QtCore.QRect(410, 270, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.TextExtension.setFont(font)
        self.TextExtension.setText("")
        self.TextExtension.setObjectName("TextExtension")
        self.ChooseButton = QtWidgets.QPushButton(self.frame)
        self.ChooseButton.setGeometry(QtCore.QRect(10, 370, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.ChooseButton.setFont(font)
        self.ChooseButton.setCheckable(False)
        self.ChooseButton.setObjectName("ChooseButton")

        self.ChooseButton.clicked.connect(self.ChooseExceptions)

        self.RunButton = QtWidgets.QPushButton(self.frame)
        self.RunButton.setGeometry(QtCore.QRect(580, 460, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.RunButton.setFont(font)
        self.RunButton.setObjectName("RunButton")

        self.RunButton.clicked.connect(self.on_modified)

        self.ClearButton = QtWidgets.QPushButton(self.frame)
        self.ClearButton.setGeometry(QtCore.QRect(580, 270, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName("ClearButton")

        self.ClearButton.clicked.connect(self.clearButtonFunction)

        self.ExtensionsList = QtWidgets.QTableWidget(self.frame)
        self.ExtensionsList.setEnabled(True)
        self.ExtensionsList.setGeometry(QtCore.QRect(10, 10, 781, 251))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.ExtensionsList.setFont(font)
        self.ExtensionsList.setMouseTracking(False)
        self.ExtensionsList.setTabletTracking(False)
        self.ExtensionsList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ExtensionsList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ExtensionsList.setAcceptDrops(True)
        self.ExtensionsList.setAutoFillBackground(False)
        self.ExtensionsList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ExtensionsList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ExtensionsList.setLineWidth(1)
        self.ExtensionsList.setMidLineWidth(0)
        self.ExtensionsList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ExtensionsList.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.ExtensionsList.setProperty("showDropIndicator", True)
        self.ExtensionsList.setDragEnabled(True)
        self.ExtensionsList.setDragDropOverwriteMode(True)
        self.ExtensionsList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.ExtensionsList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.ExtensionsList.setAlternatingRowColors(True)
        self.ExtensionsList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ExtensionsList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.ExtensionsList.setGridStyle(QtCore.Qt.SolidLine)
        self.ExtensionsList.setCornerButtonEnabled(True)
        self.ExtensionsList.setRowCount(0)
        self.ExtensionsList.setObjectName("ExtensionsList")
        self.ExtensionsList.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.ExtensionsList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ExtensionsList.setHorizontalHeaderItem(1, item)
        self.ExtensionsList.horizontalHeader().setVisible(True)
        self.ExtensionsList.horizontalHeader().setCascadingSectionResizes(True)
        
        self.ExtensionsList.setHorizontalHeaderLabels(["Extension", "Folder"])

        self.ExtensionsList.horizontalHeader().setHighlightSections(True)
        self.ExtensionsList.horizontalHeader().setMinimumSectionSize(200)
        self.ExtensionsList.horizontalHeader().setSortIndicatorShown(True)
        self.ExtensionsList.horizontalHeader().setStretchLastSection(True)
        self.ExtensionsList.verticalHeader().setVisible(True)
        self.ExtensionsList.verticalHeader().setCascadingSectionResizes(False)
        self.ExtensionsList.verticalHeader().setStretchLastSection(False)
        self.ChooseDirectoryButton = QtWidgets.QPushButton(self.frame)
        self.ChooseDirectoryButton.setGeometry(QtCore.QRect(10, 460, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.ChooseDirectoryButton.setFont(font)
        self.ChooseDirectoryButton.setCheckable(False)
        self.ChooseDirectoryButton.setObjectName("ChooseDirectoryButton")
        self.ChooseDirectoryButton.setText("Choose directory folder")

        self.ChooseDirectoryButton.clicked.connect(self.ChooseDirectoryFunction)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAdd_or_edit_a_folder_for_certain_extension = QtWidgets.QAction(MainWindow)
        self.actionAdd_or_edit_a_folder_for_certain_extension.setObjectName("actionAdd_or_edit_a_folder_for_certain_extension")


        self.list_for_files = set()
        self.d_files = {}
        self.old = set()

        self.folder_to_track = f'/Users/{self.cur}/Desktop'
        self.folder_destination = f'/Users/{self.cur}/Desktop/{self.cur}'


        ########################################################
        self.extensions_folders = {
        #Uncategorized
            'noname' : f"/Users/{self.cur}/Desktop/{self.cur}/Other/Uncategorized",
        #Audio
            '.aif' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.cda' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.mid' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.midi' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.mp3' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.mpa' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.ogg' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.wav' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.wma' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.wpl' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
            '.m3u' : f"/Users/{self.cur}/Desktop/{self.cur}/Media/Audio",
        #Text
            '.epub' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.cbr' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Comics",
            '.djvu' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.fb2' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.txt' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.doc' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Word",
            '.docx' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Word",
            '.odt ' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.pdf': f"/Users/{self.cur}/Desktop/{self.cur}/Text/PDF",
            '.rtf': f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.tex': f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.wks ': f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.wps': f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
            '.wpd': f"/Users/{self.cur}/Desktop/{self.cur}/Text/TextFiles",
        #Video
            '.3g2': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.3gp': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.avi': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.flv': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.h264': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.m4v': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.mkv': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.mov': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.mp4': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.mpg': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.mpeg': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.rm': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.swf': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.vob': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
            '.wmv': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Video",
        #Images
            '.ai': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.bmp': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.gif': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.ico': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.jpg': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.jpeg': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.png': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.ps': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.psd': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.svg': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.tif': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.tiff': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
            '.CR2': f"/Users/{self.cur}/Desktop/{self.cur}/Media/Images",
        #Internet
            '.asp': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.aspx': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.cer': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.cfm': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.cgi': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.pl': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.css': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.htm': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.js': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.jsp': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.part': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.php': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.rss': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
            '.xhtml': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Internet",
        #Compressed
            '.7z': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.arj': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.deb': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.pkg': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.rar': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.rpm': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.tar.gz': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.z': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
            '.zip': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Compressed",
        #Disc
            '.bin': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Disc",
            '.dmg': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Disc",
            '.iso': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Disc",
            '.toast': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Disc",
            '.vcd': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Disc",
        #Data
            '.csv': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.dat': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.db': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.dbf': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.log': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.mdb': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.sav': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.sql': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.tar': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.xml': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
            '.json': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Database",
        #Executables
            '.apk': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.bat': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.com': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.exe': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.gadget': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.jar': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
            '.wsf': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Executables",
        #Fonts
            '.fnt': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Fonts",
            '.fon': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Fonts",
            '.otf': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Fonts",
            '.ttf': f"/Users/{self.cur}/Desktop/{self.cur}/Other/Fonts",
        #Presentations
            '.key': f"/Users/{self.cur}/Desktop/{self.cur}/Text/Presentations",
            '.odp': f"/Users/{self.cur}/Desktop/{self.cur}/Text/Presentations",
            '.pps': f"/Users/{self.cur}/Desktop/{self.cur}/Text/Presentations",
            '.ppt': f"/Users/{self.cur}/Desktop/{self.cur}/Text/Presentations",
            '.pptx': f"/Users/{self.cur}/Desktop/{self.cur}/Text/Presentations",
        #Programming
            '.c': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/C&C++",
            '.class': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Java",
            '.dart': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Dart",
            '.py': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Python",
            '.sh': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Shell",
            '.swift': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/Swift",
            '.html': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/C&C++",
            '.h': f"/Users/{self.cur}/Desktop/{self.cur}/Programming/C&C++",
        #Spreadsheets
            '.ods' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Excel",
            '.xlr' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Excel",
            '.xls' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Excel",
            '.xlsx' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Microsoft/Excel",
        #System
            '.bak' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.cab' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.cfg' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.cpl' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.self.cur' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.dll' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.dmp' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.drv' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.icns' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.ico' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.ini' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.lnk' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.msi' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.sys' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
            '.tmp' : f"/Users/{self.cur}/Desktop/{self.cur}/Text/Other/System",
        }
        self.setExtensions()
        #self.refresh()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Organizer"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.TextFolder.setPlaceholderText(_translate("MainWindow", "Folder"))
        self.TextExtension.setPlaceholderText(_translate("MainWindow", ".extension"))
        self.ChooseButton.setText(_translate("MainWindow", "Choose files that will be untouched"))
        self.RunButton.setText(_translate("MainWindow", "Run"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.ExtensionsList.setSortingEnabled(True)
        item = self.ExtensionsList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Extension"))
        item = self.ExtensionsList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Folder"))
        self.ChooseDirectoryButton.setText(_translate("MainWindow", "Choose directory folder"))
        self.actionAdd_or_edit_a_folder_for_certain_extension.setText(_translate("MainWindow", "Add or edit a folder for certain extension"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.TextFolder.setPlaceholderText(_translate("MainWindow", "Folder"))
        self.TextExtension.setPlaceholderText(_translate("MainWindow", ".extension"))
        self.ChooseButton.setText(_translate("MainWindow", "Choose files that will be untouched"))
        #self.ForgetButton.setText(_translate("MainWindow", "Forget self.current custom settings"))
        self.RunButton.setText(_translate("MainWindow", "Run"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.actionAdd_or_edit_a_folder_for_certain_extension.setText(_translate("MainWindow", "Add or edit a folder for certain extension"))

    def refresh(self):
        self.ExtensionsList.clear()
        self.ExtensionsList.setHorizontalHeaderLabels(["Extension", "Folder"])
        self.ExtensionsList.setRowCount(len(self.extensions_folders))
        for i, v in enumerate(self.extensions_folders):
            self.ExtensionsList.setItem(i, 0, QtWidgets.QTableWidgetItem(v))
            self.ExtensionsList.setItem(i, 1, QtWidgets.QTableWidgetItem(self.extensions_folders[v]))

    def clearButtonFunction(self):
        self.TextFolder.setText("")
        self.TextExtension.setText("")

    def saveButtonFuntion(self):
        textOfExtension = self.TextExtension.text().replace(" ", "")
        textOfFolder = self.TextFolder.text()
        if len(textOfExtension) > 1 and textOfFolder:
            if textOfExtension[0] != ".":
                textOfExtension = "." + textOfExtension
            self.extensions_folders[textOfExtension] = textOfFolder
            self.refresh()

        f = open(f"/Users/{self.cur}/Desktop/extensions.txt", "w")
        s = ""
        l = len(self.extensions_folders)
        for i, v in enumerate(self.extensions_folders, 1):
            if i == len(self.extensions_folders):
                s += v + " - " + self.extensions_folders[v]
            else:
                    s += v + " - " + self.extensions_folders[v] + ", \n"
        f.write(s)
        f.close()
        self.clearButtonFunction()
        self.refresh()

    def ChooseDirectoryFunction(self):
        self.TextFolder.setText(diropenbox())   

    def ChooseExceptions(self):
        self.listOfExceptions = {'Cleaner.exe', 'cleaner_cash.txt', 'Cleaner.pyw', 'Extensions.txt', 'extensions.txt', 'Cleaner.py'}
        s = set(fileopenbox(multiple = True))
        for i in s:
            t = i.split("\\")
            self.listOfExceptions.add(t[len(t)-1])

        #self.listOfExceptions.update(

    def setExtensions(self):
        if os.path.exists(f"/Users/{self.cur}/Desktop/Extensions.txt"):
            f = open(f"/Users/{self.cur}/Desktop/Extensions.txt", "r")
            s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
            while len(s) != 0:
                    s = dict(map(lambda x: x.split('-'), s.split(',')))
                    for i in s:
                            self.extensions_folders[i] = s[i]
                    s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    
        elif os.path.exists(f"/Users/{self.cur}/Desktop/{self.cur}/Extensions.txt"):
            f = open(f"/Users/{self.cur}/Desktop/{self.cur}/Extensions.txt", "r")
            s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
            while len(s) != 0:
                    s = dict(map(lambda x: x.split('-'), s.split(',')))
                    for i in s:
                            self.extensions_folders[i] = s[i]
                    s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    
        elif os.path.exists(f"/Users/{self.cur}/Desktop/{self.cur}/extensions.txt"):
            f = open(f"/Users/{self.cur}/Desktop/{self.cur}/extensions.txt", "r")
            s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
            while len(s) != 0:
                    s = dict(map(lambda x: x.split('-'), s.split(',')))
                    for i in s:
                            self.extensions_folders[i] = s[i]
                    s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")

        elif os.path.exists(f"/Users/{self.cur}/Desktop/extensions.txt"):
            f = open(f"/Users/{self.cur}/Desktop/extensions.txt", "r")
            s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
            while len(s) != 0:
                    s = dict(map(lambda x: x.split('-'), s.split(',')))
                    for i in s:
                            self.extensions_folders[i] = s[i]
                    s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
        self.refresh()

    def on_modified(self):
            pyautogui.hotkey('win','d')
            sleep(2)
            img = ImageGrab.grab(bbox = None)
            tmp_pic = localtime()
            name_for_pic = f"{tmp_pic[3]}_{tmp_pic[4]}_of_{tmp_pic[2]}_{tmp_pic[1]}_{tmp_pic[0]}.bmp"
            img.save(f"/Users/{self.cur}/Desktop/{self.cur}/" + name_for_pic, "BMP")


            self.old = set()
            for filename in os.listdir(self.folder_to_track):
                i = 1
                if filename not in self.listOfExceptions:
                    try:                      
                        new_name = filename
                        extension = 'noname'
                        try:
                            extension = str(os.path.splitext(self.folder_to_track + '/' + filename)[1])
                            path = self.extensions_folders[extension]
                        except Exception:
                            extension = 'noname'
                        

                        now = datetime.now()
                        year = now.strftime("%Y")
                        #month = now.strftime("%m")

                        self.folder_destination_path = self.extensions_folders[extension]
                        
                        year_exists = False
                        #month_exists = False
                        for folder_name in os.listdir(self.extensions_folders[extension]):
                            if folder_name == year:
                                self.folder_destination_path = self.extensions_folders[extension] + "/" +year
                                year_exists = True
                                #for folder_month in os.listdir(folder_destination_path):
                                #    if month == folder_month:
                                self.folder_destination_path = self.extensions_folders[extension] + "/" + year# + "/" + month
                                        #month_exists = True
                        if not year_exists:
                            os.mkdir(self.extensions_folders[extension] + "/" + year)
                            self.folder_destination_path = self.extensions_folders[extension] + "/" + year
                        #if not month_exists:
                        #    os.mkdir(folder_destination_path + "/" + month)
                        #    folder_destination_path = folder_destination_path + "/" + month


                        file_exists = os.path.isfile(self.folder_destination_path + "/" + new_name)
                        while file_exists:
                            i += 1
                            new_name = os.path.splitext(self.folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(self.folder_to_track + '/' + filename)[1]
                            new_name = new_name.split("/")[4]
                            file_exists = os.path.isfile(self.folder_destination_path + "/" + new_name)
                        src = self.folder_to_track + "/" + filename
                        self.list_for_files.add(new_name)
                        self.d_files[new_name] = self.folder_destination_path + "/" + new_name
                        new_name = self.folder_destination_path + "/" + new_name
                        os.rename(src, new_name)
                        print(f"{filename} successfully added to the directory")
                        f = open(f'C:/Users/{cur}/Desktop/{cur}/List_of_files.txt', "w")
                        #f = open("f'/Users/{cur}/Desktop/{cur}/List_of_directories.txt", "w")
                        t_list = ""
                        for name_list in self.list_for_files:
                            t_list += name_list + " - " + d_files[name_list] + "\n"
                        f.write(t_list)
                        f.close()
                        
                    except Exception:
                        if filename not in self.old:
                            print(filename)
                            #list_for_files += folder_destination_path + " - " + filename + "\n"
                            self.old.add(filename)
            self.old = set()
            if os.path.exists(f"/Users/{self.cur}/Desktop/Extensions.txt"):
                    f = open(f"/Users/{self.cur}/Desktop/Extensions.txt", "r")
                    s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    while len(s) != 0:
                            #print(list(map(lambda x: x.split('-'), s.split(','))))
                            s = dict(map(lambda x: x.split('-'), s.split(',')))
                            for i in s:
                                    self.extensions_folders[i] = s[i]
                            s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                            
            elif os.path.exists(f"/Users/{self.cur}/Desktop/{self.cur}/Extensions.txt"):
                    f = open(f"/Users/{self.cur}/Desktop/{self.cur}/Extensions.txt", "r")
                    s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    while len(s) != 0:
                            s = dict(map(lambda x: x.split('-'), s.split(',')))
                            for i in s:
                                    self.extensions_folders[i] = s[i]
                            s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                            
            elif os.path.exists(f"/Users/{self.cur}/Desktop/{self.cur}/extensions.txt"):
                    f = open(f"/Users/{self.cur}/Desktop/{self.cur}/extensions.txt", "r")
                    s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    while len(s) != 0:
                            s = dict(map(lambda x: x.split('-'), s.split(',')))
                            for i in s:
                                    self.extensions_folders[i] = s[i]
                            s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")

            elif os.path.exists(f"/Users/{self.cur}/Desktop/extensions.txt"):
                    f = open(f"/Users/{self.cur}/Desktop/extensions.txt", "r")
                    s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                    while len(s) != 0:
                            s = dict(map(lambda x: x.split('-'), s.split(',')))
                            for i in s:
                                    self.extensions_folders[i] = s[i]
                            s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                            

            for i in set(self.extensions_folders.values()):
                    if os.path.exists(i):
                            continue
                    else:
                            #print(i)
                            os.makedirs(i)
            try:
                while True:
                    time.sleep(1)
                    on_modified()
            except:
                    try:
                            f = open("f'/Users/{self.cur}/Desktop/{self.cur}/List_of_directories.txt", "w")
                            f.write(self.list_of_files)
                            f.close()
                    except:
                            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


"""
from time import sleep
from PIL import Image, ImageGrab
#import yadisk

#y = yadisk.YaDisk(token="AgAAAAAJTGbeAADLW6TZSbwDw0hXk9OhJAgWZ2g")

if True:#y.check_token():   
    
    
    sleep(2.5)
    img = ImageGrab.grab(bbox = None)
    
    img.save("screen.bmp", "BMP")
    #y.upload("screen.BMP", "/screen.BMP", overwrite = True)

file_exists = os.path.isfile("cleaner_cash.txt")
if file_exists:
        f = open("cleaner_cash.txt", "r")
        r = f.readline()
        if len(r) != 0 and int(r) > 0:
                inp = input("Do you want to run this program again ? \n Y/N \n")
                if "y" in inp.lower():
                        pass
                else:
                        f.close()
                        exit(0)
        f = open("cleaner_cash.txt", "w")
        f.write("1")
else:
        f = open("cleaner_cash.txt", "w")
        f.write("1")
f.close()
"""        

                        


#.files

"""

try:
    while True:
        time.sleep(1)
        on_modified()
except:
        f = open("cleaner_cash.txt", "w")
        f.write("0")
        f.close()
        try:
                f = open("f'/Users/{self.cur}/Desktop/{self.cur}/List_of_directories.txt", "w")
                f.write(list_of_files)
                f.close()
        except:
                pass
"""


#############################################################################################################################

