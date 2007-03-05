# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



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

##        i = 0
##        f1 = file(filePath, 'r')
##        f2 = file("data/properties.dat", 'r')
##
##        for line1 in f1:
##            fetch = False
##            f2 = file("data/properties.dat", 'r')
##            for line2 in f2:
##                if "Q" in line2:
##                    if fetch:
##                        break
##                    elif line1 == line2:
##                        fetch = True
##                else:
##                    if fetch:
##                        self.setRowCount(self.rowCount() + 1)
##                        self.setRowHeight(i, 20)
##                        item = QtGui.QTableWidgetItem(self.tr(line2))
##                        item.setFlags(QtCore.Qt.ItemIsEnabled)
##                        self.setItem(i, 0, item)
##                        i = i + 1
##
##        f2.close()
##        f1.close()



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

        QtGui.QWidget.__init__(self, parent)

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
        self.setWindowTitle(self.tr("Qooxdoo GUI Builder"))
        self.setMinimumSize(800, 600)


    def createActions(self):

        self.newInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_new.png"), self.tr("&New interface"), self)
        self.newInterfaceAction.setDisabled(True)
        self.newInterfaceAction.setShortcut(self.tr("Ctrl+N"))
        self.newInterfaceAction.setStatusTip(self.tr("Create a new interface"))
        self.connect(self.newInterfaceAction, QtCore.SIGNAL("triggered()"), self.newInterfaceAct)

        self.openInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("&Open interface..."), self)
        self.openInterfaceAction.setShortcut(self.tr("Ctrl+O"))
        self.openInterfaceAction.setStatusTip(self.tr("Open an existing interface"))
        self.connect(self.openInterfaceAction, QtCore.SIGNAL("triggered()"), self.openInterfaceAct)

        self.openTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("Open &template..."), self)
        self.openTemplateAction.setStatusTip(self.tr("Open an existing template"))
        self.connect(self.openTemplateAction, QtCore.SIGNAL("triggered()"), self.openTemplateAct)

        self.saveInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), self.tr("&Save interface"), self)
        self.saveInterfaceAction.setDisabled(True)
        self.saveInterfaceAction.setShortcut(self.tr("Ctrl+S"))
        self.saveInterfaceAction.setStatusTip(self.tr("Save the interface"))
        self.connect(self.saveInterfaceAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAct)

        self.saveInterfaceAsAction = QtGui.QAction(QtGui.QIcon("icons/file_saveas.png"), self.tr("Save interface &as..."), self)
        self.saveInterfaceAsAction.setDisabled(True)
        self.saveInterfaceAsAction.setStatusTip(self.tr("Save the interface under a new name"))
        self.connect(self.saveInterfaceAsAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAsAct)

        self.configureAction = QtGui.QAction(QtGui.QIcon("icons/file_configure.png"), self.tr("&Configure..."), self)
        self.configureAction.setStatusTip(self.tr("Configure the application"))
        self.connect(self.configureAction, QtCore.SIGNAL("triggered()"), self.configureAct)

        self.quitAction = QtGui.QAction(QtGui.QIcon("icons/file_quit.png"), self.tr("&Quit"), self)
        self.quitAction.setShortcut(self.tr("Ctrl+Q"))
        self.quitAction.setStatusTip(self.tr("Quit the application"))
        self.connect(self.quitAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/edit_undo.png"), self.tr("&Undo"), self)
        self.undoAction.setDisabled(True)
        self.undoAction.setShortcut(self.tr("Ctrl+Z"))
        self.undoAction.setStatusTip(self.tr("Undo the action taken before"))
        self.connect(self.undoAction, QtCore.SIGNAL("triggered()"), self.undoAct)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/edit_redo.png"), self.tr("&Redo"), self)
        self.redoAction.setDisabled(True)
        self.redoAction.setShortcut(self.tr("Ctrl+Y"))
        self.redoAction.setStatusTip(self.tr("Redo the action taken after"))
        self.connect(self.redoAction, QtCore.SIGNAL("triggered()"), self.redoAct)

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/edit_cut.png"), self.tr("Cu&t"), self)
        self.cutAction.setDisabled(True)
        self.cutAction.setShortcut(self.tr("Ctrl+X"))
        self.cutAction.setStatusTip(self.tr("Cut the current selection"))
        self.connect(self.cutAction, QtCore.SIGNAL("triggered()"), self.cutAct)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/edit_copy.png"), self.tr("&Copy"), self)
        self.copyAction.setDisabled(True)
        self.copyAction.setShortcut(self.tr("Ctrl+C"))
        self.copyAction.setStatusTip(self.tr("Copy the current selection"))
        self.connect(self.copyAction, QtCore.SIGNAL("triggered()"), self.copyAct)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/edit_paste.png"), self.tr("&Paste"), self)
        self.pasteAction.setDisabled(True)
        self.pasteAction.setShortcut(self.tr("Ctrl+V"))
        self.pasteAction.setStatusTip(self.tr("Paste into the current selection"))
        self.connect(self.pasteAction, QtCore.SIGNAL("triggered()"), self.pasteAct)

        self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), self.tr("&Delete"), self)
        self.deleteAction.setDisabled(True)
        self.deleteAction.setShortcut(self.tr("Ctrl+D"))
        self.deleteAction.setStatusTip(self.tr("Delete the current selection"))
        self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)

        self.previewInApplicationAction = QtGui.QAction(QtGui.QIcon("icons/preview_application.png"), self.tr("Preview in the &application"), self)
        self.previewInApplicationAction.setDisabled(True)
        self.previewInApplicationAction.setStatusTip(self.tr("Preview the interface in the application"))
        self.connect(self.previewInApplicationAction, QtCore.SIGNAL("triggered()"), self.previewInApplicationAct)

        self.previewInBrowserAction = QtGui.QAction(QtGui.QIcon("icons/preview_browser.png"), self.tr("Preview in a &browser"), self)
        self.previewInBrowserAction.setDisabled(True)
        self.previewInBrowserAction.setStatusTip(self.tr("Preview the interface in a browser"))
        self.connect(self.previewInBrowserAction, QtCore.SIGNAL("triggered()"), self.previewInBrowserAct)

        self.aboutAction = QtGui.QAction(self.tr("&About"), self)
        self.aboutAction.setStatusTip(self.tr("Show the application's About box"))
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self.aboutAct)

        self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("Apply template..."), self)
        self.applyTemplateAction.setDisabled(True)
        self.applyTemplateAction.setStatusTip(self.tr("Apply an existing template"))
        self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)

        self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), self.tr("Save template as..."), self)
        self.saveTemplateAsAction.setDisabled(True)
        self.saveTemplateAsAction.setStatusTip(self.tr("Save the template"))
        self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)


    def createMenus(self):

        self.fileMenu = self.menuBar().addMenu(self.tr("&File"))
        self.fileMenu.addAction(self.newInterfaceAction)
        self.fileMenu.addAction(self.openInterfaceAction)
        self.fileMenu.addAction(self.openTemplateAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.saveInterfaceAction)
        self.fileMenu.addAction(self.saveInterfaceAsAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.configureAction)
        self.fileMenu.addAction(self.quitAction)

        self.editMenu = self.menuBar().addMenu(self.tr("&Edit"))
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.deleteAction)

        self.previewMenu = self.menuBar().addMenu(self.tr("&Preview"))
        self.previewMenu.addAction(self.previewInApplicationAction)
        self.previewMenu.addAction(self.previewInBrowserAction)

        self.helpMenu = self.menuBar().addMenu(self.tr("&Help"))
        self.helpMenu.addAction(self.aboutAction)


    def createToolBars(self):

        self.fileToolBar = self.addToolBar(self.tr("File"))
        self.fileToolBar.addAction(self.newInterfaceAction)
        self.fileToolBar.addAction(self.openInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAsAction)
        self.fileToolBar.addAction(self.configureAction)
        self.fileToolBar.addAction(self.quitAction)

        self.editToolBar = self.addToolBar(self.tr("Edit"))
        self.editToolBar.addAction(self.undoAction)
        self.editToolBar.addAction(self.redoAction)
        self.editToolBar.addAction(self.cutAction)
        self.editToolBar.addAction(self.copyAction)
        self.editToolBar.addAction(self.pasteAction)
        self.editToolBar.addAction(self.deleteAction)

        self.previewToolBar = self.addToolBar(self.tr("Preview"))
        self.previewToolBar.addAction(self.previewInApplicationAction)
        self.previewToolBar.addAction(self.previewInBrowserAction)


    def createStatusBar(self):

        self.statusBar().showMessage(self.tr("Ready"))


    def createDockWindows(self):

        self.controlsDock = QtGui.QDockWidget(self.tr("Controls"), self)
        self.controlsDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.controlsDock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.controlsDock.setFixedWidth(273)
        self.controlsDock.setMaximumHeight(384)

        self.controlsWidget = ControlsWidget()

        self.intermediateWidget = QtGui.QScrollArea(self)
        self.intermediateWidget.setBackgroundRole(QtGui.QPalette.Light)
        self.intermediateWidget.setWidget(self.controlsWidget)

        self.controlsDock.setWidget(self.intermediateWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.controlsDock, QtCore.Qt.Vertical)

        self.propertiesDock = QtGui.QDockWidget(self.tr("Properties"), self)
        self.propertiesDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.propertiesDock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.propertiesDock.setFixedWidth(273)

        self.propertiesWidget = PropertiesWidget()

        self.propertiesDock.setWidget(self.propertiesWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.propertiesDock, QtCore.Qt.Vertical)


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


    def aboutAct(self):

        QtGui.QMessageBox.about(self, self.tr("About"), self.tr("<b>Qooxdoo GUI Builder</b><p>System of visual construction of interfaces, for the qooxdoo framework.<p><br>Authors:<p>- Cláudia Oliveira&nbsp;&nbsp;&nbsp;<a href=claudia.i.h.oliveira@gmail.com>claudia.i.h.oliveira@gmail.com</a><p>- Cláudio Pedro&nbsp;&nbsp;&nbsp;<a href=claudio.pedro@gmail.com>claudio.pedro@gmail.com</a><p>- Nuno Coelho&nbsp;&nbsp;&nbsp;<a href=nuno.a.coelho@gmail.com>nuno.a.coelho@gmail.com</a><p><br>Official Web Site:&nbsp;&nbsp;&nbsp;<a href=http://qooxdooguibuilder.googlepages.com>http://qooxdooguibuilder.googlepages.com</a>"))


    def applyTemplateAct(self):

        return


    def saveTemplateAsAct(self):

        return



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_widget = MainWindow()
    main_widget.showMaximized()
    sys.exit(app.exec_())
