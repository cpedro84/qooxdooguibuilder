# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class DragLabel(QtGui.QLabel):


    def __init__(self, text, parent=None):

        QtGui.QLabel.__init__(self, text, parent)

        self.setFrameShape(QtGui.QFrame.Panel)
        self.setFrameShadow(QtGui.QFrame.Raised)


    def mousePressEvent(self, event):

        itemData = QtCore.QByteArray()

        mimeData = QtCore.QMimeData()
        mimeData.setData("application/x-dnditemdata", itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

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
            event.acceptProposedAction()
        else:
            event.ignore()


    def dropEvent(self, event):
        
        if event.mimeData().hasFormat("application/x-dnditemdata"):
            if main_window.control_beeing_added == 1:
                self.newIcon = DragLabel("Button", self)
            elif main_window.control_beeing_added == 2:
                self.newIcon = DragLabel("Check Box", self)
            elif main_window.control_beeing_added == 3:
                self.newIcon = DragLabel("Combo Box", self)
            elif main_window.control_beeing_added == 4:
                self.newIcon = DragLabel("Group Box", self)
            elif main_window.control_beeing_added == 5:
                self.newIcon = DragLabel("Iframe", self)
            elif main_window.control_beeing_added == 6:
                self.newIcon = DragLabel("Label", self)
            elif main_window.control_beeing_added == 7:
                self.newIcon = DragLabel("List", self)
            elif main_window.control_beeing_added == 8:
                self.newIcon = DragLabel("Menu Bar", self)
            elif main_window.control_beeing_added == 9:
                self.newIcon = DragLabel("Password Field", self)
            elif main_window.control_beeing_added == 10:
                self.newIcon = DragLabel("Radio Button", self)
            elif main_window.control_beeing_added == 11:
                self.newIcon = DragLabel("Spinner", self)
            elif main_window.control_beeing_added == 12:
                self.newIcon = DragLabel("Tab View", self)
            elif main_window.control_beeing_added == 13:
                self.newIcon = DragLabel("Table", self)
            elif main_window.control_beeing_added == 14:
                self.newIcon = DragLabel("Text Area", self)
            elif main_window.control_beeing_added == 15:
                self.newIcon = DragLabel("Text Field", self)
            elif main_window.control_beeing_added == 16:
                self.newIcon = DragLabel("Tool Bar", self)
            elif main_window.control_beeing_added == 17:
                self.newIcon = DragLabel("Tree", self)
            self.newIcon.move(event.pos())
            self.newIcon.show()

            if event.source() in self.children():
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()



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
        self.setHorizontalHeaderLabels(["Property", "Value"])

        self.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.verticalHeader().hide()



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


    def mousePressEvent(self, event):

        child = self.childAt(event.pos())

        if not child:
            return
        elif event.y() >= 2 and event.y() < 23:
            main_window.control_beeing_added = 1
        elif event.y() >= 23 and event.y() < 44:
            main_window.control_beeing_added = 2
        elif event.y() >= 44 and event.y() < 65:
            main_window.control_beeing_added = 3
        elif event.y() >= 65 and event.y() < 86:
            main_window.control_beeing_added = 4
        elif event.y() >= 86 and event.y() < 107:
            main_window.control_beeing_added = 5
        elif event.y() >= 107 and event.y() < 128:
            main_window.control_beeing_added = 6
        elif event.y() >= 128 and event.y() < 149:
            main_window.control_beeing_added = 7
        elif event.y() >= 149 and event.y() < 170:
            main_window.control_beeing_added = 8
        elif event.y() >= 170 and event.y() < 191:
            main_window.control_beeing_added = 9
        elif event.y() >= 191 and event.y() < 212:
            main_window.control_beeing_added = 10
        elif event.y() >= 212 and event.y() < 233:
            main_window.control_beeing_added = 11
        elif event.y() >= 233 and event.y() < 254:
            main_window.control_beeing_added = 12
        elif event.y() >= 254 and event.y() < 275:
            main_window.control_beeing_added = 13
        elif event.y() >= 275 and event.y() < 296:
            main_window.control_beeing_added = 14
        elif event.y() >= 296 and event.y() < 317:
            main_window.control_beeing_added = 15
        elif event.y() >= 317 and event.y() < 338:
            main_window.control_beeing_added = 16
        elif event.y() >= 338 and event.y() < 359:
            main_window.control_beeing_added = 17

        itemData = QtCore.QByteArray()

        mimeData = QtCore.QMimeData()
        mimeData.setData("application/x-dnditemdata", itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos())

        if drag.start(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            child.close()
        else:
            child.show()



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
        self.newInterfaceAction.setShortcut("Ctrl+N")
        self.newInterfaceAction.setStatusTip("Create a new interface")
        self.connect(self.newInterfaceAction, QtCore.SIGNAL("triggered()"), self.newInterfaceAct)

        self.openInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), "&Open interface...", self)
        self.openInterfaceAction.setShortcut("Ctrl+O")
        self.openInterfaceAction.setStatusTip("Open an existing interface")
        self.connect(self.openInterfaceAction, QtCore.SIGNAL("triggered()"), self.openInterfaceAct)

        self.openTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), "Open &template...", self)
        self.openTemplateAction.setStatusTip("Open an existing template")
        self.connect(self.openTemplateAction, QtCore.SIGNAL("triggered()"), self.openTemplateAct)

        self.saveInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), "&Save interface", self)
        self.saveInterfaceAction.setDisabled(True)
        self.saveInterfaceAction.setShortcut("Ctrl+S")
        self.saveInterfaceAction.setStatusTip("Save the interface")
        self.connect(self.saveInterfaceAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAct)

        self.saveInterfaceAsAction = QtGui.QAction(QtGui.QIcon("icons/file_saveas.png"), "Save interface &as...", self)
        self.saveInterfaceAsAction.setDisabled(True)
        self.saveInterfaceAsAction.setStatusTip("Save the interface under a new name")
        self.connect(self.saveInterfaceAsAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAsAct)

        self.configureAction = QtGui.QAction(QtGui.QIcon("icons/file_configure.png"), "&Configure...", self)
        self.configureAction.setStatusTip("Configure the application")
        self.connect(self.configureAction, QtCore.SIGNAL("triggered()"), self.configureAct)

        self.quitAction = QtGui.QAction(QtGui.QIcon("icons/file_quit.png"), "&Quit", self)
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.setStatusTip("Quit the application")
        self.connect(self.quitAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/edit_undo.png"), "&Undo", self)
        self.undoAction.setDisabled(True)
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.setStatusTip("Undo the action taken before")
        self.connect(self.undoAction, QtCore.SIGNAL("triggered()"), self.undoAct)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/edit_redo.png"), "&Redo", self)
        self.redoAction.setDisabled(True)
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.setStatusTip("Redo the action taken after")
        self.connect(self.redoAction, QtCore.SIGNAL("triggered()"), self.redoAct)

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/edit_cut.png"), "Cu&t", self)
        self.cutAction.setDisabled(True)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.setStatusTip("Cut the current selection")
        self.connect(self.cutAction, QtCore.SIGNAL("triggered()"), self.cutAct)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/edit_copy.png"), "&Copy", self)
        self.copyAction.setDisabled(True)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.setStatusTip("Copy the current selection")
        self.connect(self.copyAction, QtCore.SIGNAL("triggered()"), self.copyAct)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/edit_paste.png"), "&Paste", self)
        self.pasteAction.setDisabled(True)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.setStatusTip("Paste into the current selection")
        self.connect(self.pasteAction, QtCore.SIGNAL("triggered()"), self.pasteAct)

        self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), "&Delete", self)
        self.deleteAction.setDisabled(True)
        self.deleteAction.setShortcut("Ctrl+D")
        self.deleteAction.setStatusTip("Delete the current selection")
        self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)

        self.previewInApplicationAction = QtGui.QAction(QtGui.QIcon("icons/preview_application.png"), "Preview in the &application", self)
        self.previewInApplicationAction.setDisabled(True)
        self.previewInApplicationAction.setStatusTip("Preview the interface in the application")
        self.connect(self.previewInApplicationAction, QtCore.SIGNAL("triggered()"), self.previewInApplicationAct)

        self.previewInBrowserAction = QtGui.QAction(QtGui.QIcon("icons/preview_browser.png"), "Preview in a &browser", self)
        self.previewInBrowserAction.setDisabled(True)
        self.previewInBrowserAction.setStatusTip("Preview the interface in a browser")
        self.connect(self.previewInBrowserAction, QtCore.SIGNAL("triggered()"), self.previewInBrowserAct)

        self.controlsAction = QtGui.QAction("&Controls", self)
        self.controlsAction.setCheckable(True)
        self.controlsAction.setChecked(True)
        self.controlsAction.setStatusTip("Set whether the Controls dock window is visible or not")
        self.connect(self.controlsAction, QtCore.SIGNAL("triggered()"), self.controlsAct)

        self.propertiesAction = QtGui.QAction("&Properties", self)
        self.propertiesAction.setCheckable(True)
        self.propertiesAction.setChecked(True)
        self.propertiesAction.setStatusTip("Set whether the Properties dock window is visible or not")
        self.connect(self.propertiesAction, QtCore.SIGNAL("triggered()"), self.propertiesAct)

        self.aboutAction = QtGui.QAction("&About", self)
        self.aboutAction.setStatusTip("Show the application's About box")
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self.aboutAct)

        self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), "Apply template...", self)
        self.applyTemplateAction.setDisabled(True)
        self.applyTemplateAction.setStatusTip("Apply an existing template")
        self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)

        self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), "Save template as...", self)
        self.saveTemplateAsAction.setDisabled(True)
        self.saveTemplateAsAction.setStatusTip("Save the template")
        self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)


    def createMenus(self):

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newInterfaceAction)
        self.fileMenu.addAction(self.openInterfaceAction)
        self.fileMenu.addAction(self.openTemplateAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.saveInterfaceAction)
        self.fileMenu.addAction(self.saveInterfaceAsAction)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.configureAction)
        self.fileMenu.addAction(self.quitAction)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.deleteAction)

        self.previewMenu = self.menuBar().addMenu("&Preview")
        self.previewMenu.addAction(self.previewInApplicationAction)
        self.previewMenu.addAction(self.previewInBrowserAction)

        self.viewMenu = self.menuBar().addMenu("&View")
        self.viewMenu.addAction(self.controlsAction)
        self.viewMenu.addAction(self.propertiesAction)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAction)


    def createToolBars(self):

        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newInterfaceAction)
        self.fileToolBar.addAction(self.openInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAction)
        self.fileToolBar.addAction(self.saveInterfaceAsAction)
        self.fileToolBar.addAction(self.configureAction)
        self.fileToolBar.addAction(self.quitAction)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.undoAction)
        self.editToolBar.addAction(self.redoAction)
        self.editToolBar.addAction(self.cutAction)
        self.editToolBar.addAction(self.copyAction)
        self.editToolBar.addAction(self.pasteAction)
        self.editToolBar.addAction(self.deleteAction)

        self.previewToolBar = self.addToolBar("Preview")
        self.previewToolBar.addAction(self.previewInApplicationAction)
        self.previewToolBar.addAction(self.previewInBrowserAction)


    def createStatusBar(self):

        self.statusBar().showMessage("Ready")


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

        QtGui.QMessageBox.about(self, "About", "<b>Qooxdoo GUI Builder</b><p>System of visual construction of interfaces, for the qooxdoo framework.<p><br>Authors:<p>- Cláudia Oliveira&nbsp;&nbsp;&nbsp;<a href=claudia.i.h.oliveira@gmail.com>claudia.i.h.oliveira@gmail.com</a><p>- Cláudio Pedro&nbsp;&nbsp;&nbsp;<a href=claudio.pedro@gmail.com>claudio.pedro@gmail.com</a><p>- Nuno Coelho&nbsp;&nbsp;&nbsp;<a href=nuno.a.coelho@gmail.com>nuno.a.coelho@gmail.com</a><p><br>Official Web Site:&nbsp;&nbsp;&nbsp;<a href=http://qooxdooguibuilder.googlepages.com>http://qooxdooguibuilder.googlepages.com</a>")


    def applyTemplateAct(self):

        return


    def saveTemplateAsAct(self):

        return


    control_beeing_added = 0



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())
