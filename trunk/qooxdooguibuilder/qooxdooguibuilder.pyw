# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class DragLabel(QtGui.QLabel):


    def __init__(self, text, parent=None):

        QtGui.QLabel.__init__(self, QtCore.QString("Text"), parent)


    def mousePressEvent(self, event):
        plainText = self.text()

        mimeData = QtCore.QMimeData()
        mimeData.setText(plainText)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - child.pos())

        dropAction = drag.start(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)

        if dropAction == QtCore.Qt.MoveAction:
            self.close()
            self.update()



class DrawArea(QtGui.QWidget):


    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)

        self.setAcceptDrops(True)
        self.setBackgroundRole(QtGui.QPalette.Light)
        self.setGeometry(self.x(), self.y(), self.width() * 2, self.height() * 6)


    def dragEnterEvent(self, event):

        if event.mimeData().hasFormat("application/x-dnditemdata"):
            if event.source() == self:
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()


    def dropEvent(self, event):
        
        if event.mimeData().hasFormat("application/x-dnditemdata"):
            itemData = event.mimeData().data("application/x-dnditemdata")
            dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.ReadOnly)

            pixmap = QtGui.QPixmap()
            offset = QtCore.QPoint()
            dataStream >> pixmap >> offset

            newIcon = QtGui.QLabel(self)
            newIcon.setPixmap(pixmap)
            newIcon.move(event.pos() - offset)
            newIcon.show()

            if event.source() == self:
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()


    def mousePressEvent(self, event):
        
        child = self.childAt(event.pos())
        if not child:
            return

        pixmap = child.pixmap()
        child.close()

        itemData = QtCore.QByteArray()
        dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
        dataStream << pixmap << QtCore.QPoint(event.pos() - child.pos())

        mimeData = QtCore.QMimeData()
        mimeData.setData("application/x-dnditemdata", itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - child.pos())

        if drag.start(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            child.close()
        else:
            child.show()
            child.setPixmap(pixmap)



class PropertiesDockWidget(QtGui.QDockWidget):


    def __init__(self, parent = None):

        QtGui.QDockWidget.__init__(self, "Properties", parent)

        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.setFeatures(QtGui.QDockWidget.DockWidgetClosable | QtGui.QDockWidget.DockWidgetMovable)
        self.setFixedWidth(273)
        self.setMinimumHeight(219)


    def closeEvent(self, event):

        main_window.propertiesAction.setChecked(False)



class PropertiesWidget(QtGui.QTableWidget):


    def __init__(self, parent = None):

        QtGui.QTableWidget.__init__(self, parent)

        self.setAlternatingRowColors(True)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(QtCore.QStringList(["Property", "Value"]))

        self.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.verticalHeader().hide()


    def load(self, filePath):

        return



class ControlsDockWidget(QtGui.QDockWidget):


    def __init__(self, parent = None):

        QtGui.QDockWidget.__init__(self, "Controls", parent)

        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.setFeatures(QtGui.QDockWidget.DockWidgetClosable | QtGui.QDockWidget.DockWidgetMovable)
        self.setFixedWidth(273)


    def closeEvent(self, event):

        main_window.controlsAction.setChecked(False)



class ControlsWidget(QtGui.QWidget):


    def __init__(self, parent = None):

        QtGui.QListWidget.__init__(self, parent)

        self.setGeometry(self.x(), self.y(), 254, 360)

        itemButton = QtGui.QLabel(self)
        itemButton.setPixmap(QtGui.QPixmap("controls/Button.png"))
        itemButton.move(2, 2)

        itemCheckBox = QtGui.QLabel(self)
        itemCheckBox.setPixmap(QtGui.QPixmap("controls/CheckBox.png"))
        itemCheckBox.move(2, 23)

        itemComboBox = QtGui.QLabel(self)
        itemComboBox.setPixmap(QtGui.QPixmap("controls/ComboBox.png"))
        itemComboBox.move(2, 44)

        itemGroupBox = QtGui.QLabel(self)
        itemGroupBox.setPixmap(QtGui.QPixmap("controls/GroupBox.png"))
        itemGroupBox.move(2, 65)

        itemIframe = QtGui.QLabel(self)
        itemIframe.setPixmap(QtGui.QPixmap("controls/Iframe.png"))
        itemIframe.move(2, 86)

        itemLabel = QtGui.QLabel(self)
        itemLabel.setPixmap(QtGui.QPixmap("controls/Label.png"))
        itemLabel.move(2, 107)

        itemList = QtGui.QLabel(self)
        itemList.setPixmap(QtGui.QPixmap("controls/List.png"))
        itemList.move(2, 128)

        itemMenuBar = QtGui.QLabel(self)
        itemMenuBar.setPixmap(QtGui.QPixmap("controls/MenuBar.png"))
        itemMenuBar.move(2, 149)

        itemPasswordField = QtGui.QLabel(self)
        itemPasswordField.setPixmap(QtGui.QPixmap("controls/PasswordField.png"))
        itemPasswordField.move(2, 170)

        itemRadioButton = QtGui.QLabel(self)
        itemRadioButton.setPixmap(QtGui.QPixmap("controls/RadioButton.png"))
        itemRadioButton.move(2, 191)

        itemSpinner = QtGui.QLabel(self)
        itemSpinner.setPixmap(QtGui.QPixmap("controls/Spinner.png"))
        itemSpinner.move(2, 212)

        itemTabView = QtGui.QLabel(self)
        itemTabView.setPixmap(QtGui.QPixmap("controls/TabView.png"))
        itemTabView.move(2, 233)

        itemTable = QtGui.QLabel(self)
        itemTable.setPixmap(QtGui.QPixmap("controls/Table.png"))
        itemTable.move(2, 254)

        itemTextArea = QtGui.QLabel(self)
        itemTextArea.setPixmap(QtGui.QPixmap("controls/TextArea.png"))
        itemTextArea.move(2, 275)

        itemTextField = QtGui.QLabel(self)
        itemTextField.setPixmap(QtGui.QPixmap("controls/TextField.png"))
        itemTextField.move(2, 296)

        itemToolBar = QtGui.QLabel(self)
        itemToolBar.setPixmap(QtGui.QPixmap("controls/ToolBar.png"))
        itemToolBar.move(2, 317)

        itemTree = QtGui.QLabel(self)
        itemTree.setPixmap(QtGui.QPixmap("controls/Tree.png"))
        itemTree.move(2, 338)

        
##        itemButton = QtGui.QPushButton(self)
##        itemButton.setGeometry(self.x(), self.y(), 250, 20)
##        itemButton.setIcon(QtGui.QIcon("controls/Button.png"))
##        itemButton.setIconSize(QtCore.QSize(250, 20))
##        itemButton.move(2, 2)
##
##        itemCheckBox = QtGui.QPushButton(self)
##        itemCheckBox.setGeometry(self.x(), self.y(), 250, 20)
##        itemCheckBox.setIcon(QtGui.QIcon("controls/CheckBox.png"))
##        itemCheckBox.setIconSize(QtCore.QSize(250, 20))
##        itemCheckBox.move(2, 23)
##
##        itemComboBox = QtGui.QPushButton(self)
##        itemComboBox.setGeometry(self.x(), self.y(), 250, 20)
##        itemComboBox.setIcon(QtGui.QIcon("controls/ComboBox.png"))
##        itemComboBox.setIconSize(QtCore.QSize(250, 20))
##        itemComboBox.move(2, 44)
##
##        itemGroupBox = QtGui.QPushButton(self)
##        itemGroupBox.setGeometry(self.x(), self.y(), 250, 20)
##        itemGroupBox.setIcon(QtGui.QIcon("controls/GroupBox.png"))
##        itemGroupBox.setIconSize(QtCore.QSize(250, 20))
##        itemGroupBox.move(2, 65)
##
##        itemIframe = QtGui.QPushButton(self)
##        itemIframe.setGeometry(self.x(), self.y(), 250, 20)
##        itemIframe.setIcon(QtGui.QIcon("controls/Iframe.png"))
##        itemIframe.setIconSize(QtCore.QSize(250, 20))
##        itemIframe.move(2, 86)
##
##        itemLabel = QtGui.QPushButton(self)
##        itemLabel.setGeometry(self.x(), self.y(), 250, 20)
##        itemLabel.setIcon(QtGui.QIcon("controls/Label.png"))
##        itemLabel.setIconSize(QtCore.QSize(250, 20))
##        itemLabel.move(2, 107)
##
##        itemList = QtGui.QPushButton(self)
##        itemList.setGeometry(self.x(), self.y(), 250, 20)
##        itemList.setIcon(QtGui.QIcon("controls/List.png"))
##        itemList.setIconSize(QtCore.QSize(250, 20))
##        itemList.move(2, 128)
##
##        itemMenuBar = QtGui.QPushButton(self)
##        itemMenuBar.setGeometry(self.x(), self.y(), 250, 20)
##        itemMenuBar.setIcon(QtGui.QIcon("controls/MenuBar.png"))
##        itemMenuBar.setIconSize(QtCore.QSize(250, 20))
##        itemMenuBar.move(2, 149)
##
##        itemPasswordField = QtGui.QPushButton(self)
##        itemPasswordField.setGeometry(self.x(), self.y(), 250, 20)
##        itemPasswordField.setIcon(QtGui.QIcon("controls/PasswordField.png"))
##        itemPasswordField.setIconSize(QtCore.QSize(250, 20))
##        itemPasswordField.move(2, 170)
##
##        itemRadioButton = QtGui.QPushButton(self)
##        itemRadioButton.setGeometry(self.x(), self.y(), 250, 20)
##        itemRadioButton.setIcon(QtGui.QIcon("controls/RadioButton.png"))
##        itemRadioButton.setIconSize(QtCore.QSize(250, 20))
##        itemRadioButton.move(2, 191)
##
##        itemSpinner = QtGui.QPushButton(self)
##        itemSpinner.setGeometry(self.x(), self.y(), 250, 20)
##        itemSpinner.setIcon(QtGui.QIcon("controls/Spinner.png"))
##        itemSpinner.setIconSize(QtCore.QSize(250, 20))
##        itemSpinner.move(2, 212)
##
##        itemTabView = QtGui.QPushButton(self)
##        itemTabView.setGeometry(self.x(), self.y(), 250, 20)
##        itemTabView.setIcon(QtGui.QIcon("controls/TabView.png"))
##        itemTabView.setIconSize(QtCore.QSize(250, 20))
##        itemTabView.move(2, 233)
##
##        itemTable = QtGui.QPushButton(self)
##        itemTable.setGeometry(self.x(), self.y(), 250, 20)
##        itemTable.setIcon(QtGui.QIcon("controls/Table.png"))
##        itemTable.setIconSize(QtCore.QSize(250, 20))
##        itemTable.move(2, 254)
##
##        itemTextArea = QtGui.QPushButton(self)
##        itemTextArea.setGeometry(self.x(), self.y(), 250, 20)
##        itemTextArea.setIcon(QtGui.QIcon("controls/TextArea.png"))
##        itemTextArea.setIconSize(QtCore.QSize(250, 20))
##        itemTextArea.move(2, 275)
##
##        itemTextField = QtGui.QPushButton(self)
##        itemTextField.setGeometry(self.x(), self.y(), 250, 20)
##        itemTextField.setIcon(QtGui.QIcon("controls/TextField.png"))
##        itemTextField.setIconSize(QtCore.QSize(250, 20))
##        itemTextField.move(2, 296)
##
##        itemToolBar = QtGui.QPushButton(self)
##        itemToolBar.setGeometry(self.x(), self.y(), 250, 20)
##        itemToolBar.setIcon(QtGui.QIcon("controls/ToolBar.png"))
##        itemToolBar.setIconSize(QtCore.QSize(250, 20))
##        itemToolBar.move(2, 317)
##
##        itemTree = QtGui.QPushButton(self)
##        itemTree.setGeometry(self.x(), self.y(), 250, 20)
##        itemTree.setIcon(QtGui.QIcon("controls/Tree.png"))
##        itemTree.setIconSize(QtCore.QSize(250, 20))
##        itemTree.move(2, 338)


    def mousePressEvent(self, event):
        
        child = self.childAt(event.pos())
        if not child:
            return

        pixmap = child.pixmap()

        itemData = QtCore.QByteArray()
        dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
        dataStream << pixmap << QtCore.QPoint(event.pos() - child.pos())

        mimeData = QtCore.QMimeData()
        mimeData.setData("application/x-dnditemdata", itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - child.pos())

        if drag.start(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            child.close()
        else:
            child.show()
            child.setPixmap(pixmap)



class MainWindow(QtGui.QMainWindow):


    def __init__(self, parent = None):

        QtGui.QMainWindow.__init__(self, parent)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()
        self.createDrawArea()

        self.centralWidget = QtGui.QScrollArea(self)
        self.centralWidget.setBackgroundRole(QtGui.QPalette.Dark)
        self.centralWidget.setWidget(self.drawArea)

        self.setCentralWidget(self.centralWidget)

        self.setWindowIcon(QtGui.QIcon("icons/mainwindow.png"))
        self.setWindowTitle("Qooxdoo GUI Builder")
        self.setMinimumSize(800, 600)


    def createActions(self):

        self.newInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_new.png"), "&New interface", self)
        self.newInterfaceAction.setDisabled(True)
        self.newInterfaceAction.setShortcut(QtCore.QString("Ctrl+N"))
        self.newInterfaceAction.setStatusTip(QtCore.QString("Create a new interface"))
        self.connect(self.newInterfaceAction, QtCore.SIGNAL("triggered()"), self.newInterfaceAct)

        self.openInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), QtCore.QString("&Open interface..."), self)
        self.openInterfaceAction.setShortcut(QtCore.QString("Ctrl+O"))
        self.openInterfaceAction.setStatusTip(QtCore.QString("Open an existing interface"))
        self.connect(self.openInterfaceAction, QtCore.SIGNAL("triggered()"), self.openInterfaceAct)

        self.openTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), QtCore.QString("Open &template..."), self)
        self.openTemplateAction.setStatusTip(QtCore.QString("Open an existing template"))
        self.connect(self.openTemplateAction, QtCore.SIGNAL("triggered()"), self.openTemplateAct)

        self.saveInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), QtCore.QString("&Save interface"), self)
        self.saveInterfaceAction.setDisabled(True)
        self.saveInterfaceAction.setShortcut(QtCore.QString("Ctrl+S"))
        self.saveInterfaceAction.setStatusTip(QtCore.QString("Save the interface"))
        self.connect(self.saveInterfaceAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAct)

        self.saveInterfaceAsAction = QtGui.QAction(QtGui.QIcon("icons/file_saveas.png"), QtCore.QString("Save interface &as..."), self)
        self.saveInterfaceAsAction.setDisabled(True)
        self.saveInterfaceAsAction.setStatusTip(QtCore.QString("Save the interface under a new name"))
        self.connect(self.saveInterfaceAsAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAsAct)

        self.configureAction = QtGui.QAction(QtGui.QIcon("icons/file_configure.png"), QtCore.QString("&Configure..."), self)
        self.configureAction.setStatusTip(QtCore.QString("Configure the application"))
        self.connect(self.configureAction, QtCore.SIGNAL("triggered()"), self.configureAct)

        self.quitAction = QtGui.QAction(QtGui.QIcon("icons/file_quit.png"), QtCore.QString("&Quit"), self)
        self.quitAction.setShortcut(QtCore.QString("Ctrl+Q"))
        self.quitAction.setStatusTip(QtCore.QString("Quit the application"))
        self.connect(self.quitAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/edit_undo.png"), QtCore.QString("&Undo"), self)
        self.undoAction.setDisabled(True)
        self.undoAction.setShortcut(QtCore.QString("Ctrl+Z"))
        self.undoAction.setStatusTip(QtCore.QString("Undo the action taken before"))
        self.connect(self.undoAction, QtCore.SIGNAL("triggered()"), self.undoAct)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/edit_redo.png"), QtCore.QString("&Redo"), self)
        self.redoAction.setDisabled(True)
        self.redoAction.setShortcut(QtCore.QString("Ctrl+Y"))
        self.redoAction.setStatusTip(QtCore.QString("Redo the action taken after"))
        self.connect(self.redoAction, QtCore.SIGNAL("triggered()"), self.redoAct)

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/edit_cut.png"), QtCore.QString("Cu&t"), self)
        self.cutAction.setDisabled(True)
        self.cutAction.setShortcut(QtCore.QString("Ctrl+X"))
        self.cutAction.setStatusTip(QtCore.QString("Cut the current selection"))
        self.connect(self.cutAction, QtCore.SIGNAL("triggered()"), self.cutAct)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/edit_copy.png"), QtCore.QString("&Copy"), self)
        self.copyAction.setDisabled(True)
        self.copyAction.setShortcut(QtCore.QString("Ctrl+C"))
        self.copyAction.setStatusTip(QtCore.QString("Copy the current selection"))
        self.connect(self.copyAction, QtCore.SIGNAL("triggered()"), self.copyAct)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/edit_paste.png"), QtCore.QString("&Paste"), self)
        self.pasteAction.setDisabled(True)
        self.pasteAction.setShortcut(QtCore.QString("Ctrl+V"))
        self.pasteAction.setStatusTip(QtCore.QString("Paste into the current selection"))
        self.connect(self.pasteAction, QtCore.SIGNAL("triggered()"), self.pasteAct)

        self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), QtCore.QString("&Delete"), self)
        self.deleteAction.setDisabled(True)
        self.deleteAction.setShortcut(QtCore.QString("Ctrl+D"))
        self.deleteAction.setStatusTip(QtCore.QString("Delete the current selection"))
        self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)

        self.previewInApplicationAction = QtGui.QAction(QtGui.QIcon("icons/preview_application.png"), QtCore.QString("Preview in the &application"), self)
        self.previewInApplicationAction.setDisabled(True)
        self.previewInApplicationAction.setStatusTip(QtCore.QString("Preview the interface in the application"))
        self.connect(self.previewInApplicationAction, QtCore.SIGNAL("triggered()"), self.previewInApplicationAct)

        self.previewInBrowserAction = QtGui.QAction(QtGui.QIcon("icons/preview_browser.png"), QtCore.QString("Preview in a &browser"), self)
        self.previewInBrowserAction.setDisabled(True)
        self.previewInBrowserAction.setStatusTip(QtCore.QString("Preview the interface in a browser"))
        self.connect(self.previewInBrowserAction, QtCore.SIGNAL("triggered()"), self.previewInBrowserAct)

        self.controlsAction = QtGui.QAction(QtCore.QString("&Controls"), self)
        self.controlsAction.setCheckable(True)
        self.controlsAction.setChecked(True)
        self.controlsAction.setStatusTip(QtCore.QString("Set whether the Controls dock window is visible or not"))
        self.connect(self.controlsAction, QtCore.SIGNAL("triggered()"), self.controlsAct)

        self.propertiesAction = QtGui.QAction(QtCore.QString("&Properties"), self)
        self.propertiesAction.setCheckable(True)
        self.propertiesAction.setChecked(True)
        self.propertiesAction.setStatusTip(QtCore.QString("Set whether the Properties dock window is visible or not"))
        self.connect(self.propertiesAction, QtCore.SIGNAL("triggered()"), self.propertiesAct)

        self.aboutAction = QtGui.QAction(QtCore.QString("&About"), self)
        self.aboutAction.setStatusTip(QtCore.QString("Show the application's About box"))
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self.aboutAct)

        self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), QtCore.QString("Apply template..."), self)
        self.applyTemplateAction.setDisabled(True)
        self.applyTemplateAction.setStatusTip(QtCore.QString("Apply an existing template"))
        self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)

        self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), QtCore.QString("Save template as..."), self)
        self.saveTemplateAsAction.setDisabled(True)
        self.saveTemplateAsAction.setStatusTip(QtCore.QString("Save the template"))
        self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)


    def createMenus(self):

        self.fileMenu = self.menuBar().addMenu(QtCore.QString("&File"))
        self.fileMenu.addAction(self.newInterfaceAction)
        self.fileMenu.addAction(self.openInterfaceAction)
        self.fileMenu.addAction(self.openTemplateAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.saveInterfaceAction)
        self.fileMenu.addAction(self.saveInterfaceAsAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.configureAction)
        self.fileMenu.addAction(self.quitAction)

        self.editMenu = self.menuBar().addMenu(QtCore.QString("&Edit"))
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.deleteAction)

        self.previewMenu = self.menuBar().addMenu(QtCore.QString("&Preview"))
        self.previewMenu.addAction(self.previewInApplicationAction)
        self.previewMenu.addAction(self.previewInBrowserAction)

        self.viewMenu = self.menuBar().addMenu(QtCore.QString("&View"))
        self.viewMenu.addAction(self.controlsAction)
        self.viewMenu.addAction(self.propertiesAction)

        self.helpMenu = self.menuBar().addMenu(QtCore.QString("&Help"))
        self.helpMenu.addAction(self.aboutAction)


    def createToolBars(self):

        self.fileToolBar = self.addToolBar(QtCore.QString("File"))
        self.fileToolBar.addAction(self.newInterfaceAction)
        self.fileToolBar.addAction(self.openInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAsAction)
        self.fileToolBar.addAction(self.configureAction)
        self.fileToolBar.addAction(self.quitAction)

        self.editToolBar = self.addToolBar(QtCore.QString("Edit"))
        self.editToolBar.addAction(self.undoAction)
        self.editToolBar.addAction(self.redoAction)
        self.editToolBar.addAction(self.cutAction)
        self.editToolBar.addAction(self.copyAction)
        self.editToolBar.addAction(self.pasteAction)
        self.editToolBar.addAction(self.deleteAction)

        self.previewToolBar = self.addToolBar(QtCore.QString("Preview"))
        self.previewToolBar.addAction(self.previewInApplicationAction)
        self.previewToolBar.addAction(self.previewInBrowserAction)


    def createStatusBar(self):

        self.statusBar().showMessage(QtCore.QString("Ready"))


    def createDockWindows(self):

        self.controlsWidget = ControlsWidget()

        self.intermediateWidget = QtGui.QScrollArea(self)
        self.intermediateWidget.setBackgroundRole(QtGui.QPalette.Light)
        self.intermediateWidget.setWidget(self.controlsWidget)

        self.controlsDockWidget = ControlsDockWidget()
        self.controlsDockWidget.setWidget(self.intermediateWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.controlsDockWidget, QtCore.Qt.Vertical)

        self.propertiesWidget = PropertiesWidget()

        self.propertiesDockWidget = PropertiesDockWidget()
        self.propertiesDockWidget.setWidget(self.propertiesWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.propertiesDockWidget, QtCore.Qt.Vertical)


    def createDrawArea(self):

        self.drawArea = DrawArea()


    def newInterfaceAct(self):

        return


    def openInterfaceAct(self):

        return


    def openTemplateAct(self):

        return


    def saveInterfaceAct(self):

        return


    def saveInterfaceAsAct(self):

        return


    def configureAct(self):

        return


    def undoAct(self):

        return


    def redoAct(self):

        return


    def cutAct(self):

        return


    def copyAct(self):

        return


    def pasteAct(self):

        return


    def deleteAct(self):

        return


    def previewInApplicationAct(self):

        return


    def previewInBrowserAct(self):

        return


    def controlsAct(self):

        if(self.controlsAction.isChecked()):
            self.controlsAction.setChecked(True)
            self.controlsDockWidget.setVisible(True)
        else:
            self.controlsAction.setChecked(False)
            self.controlsDockWidget.setVisible(False)


    def propertiesAct(self):

        if(self.propertiesAction.isChecked()):
            self.propertiesAction.setChecked(True)
            self.propertiesDockWidget.setVisible(True)
        else:
            self.propertiesAction.setChecked(False)
            self.propertiesDockWidget.setVisible(False)


    def aboutAct(self):

        QtGui.QMessageBox.about(self, QtCore.QString("About"), QtCore.QString("<b>Qooxdoo GUI Builder</b><p>System of visual construction of interfaces, for the qooxdoo framework.<p><br>Authors:<p>- Cláudia Oliveira&nbsp;&nbsp;&nbsp;<a href=claudia.i.h.oliveira@gmail.com>claudia.i.h.oliveira@gmail.com</a><p>- Cláudio Pedro&nbsp;&nbsp;&nbsp;<a href=claudio.pedro@gmail.com>claudio.pedro@gmail.com</a><p>- Nuno Coelho&nbsp;&nbsp;&nbsp;<a href=nuno.a.coelho@gmail.com>nuno.a.coelho@gmail.com</a><p><br>Official Web Site:&nbsp;&nbsp;&nbsp;<a href=http://qooxdooguibuilder.googlepages.com>http://qooxdooguibuilder.googlepages.com</a>"))


    def applyTemplateAct(self):

        return


    def saveTemplateAsAct(self):

        return



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())
