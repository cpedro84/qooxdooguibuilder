# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class MainWindow(QtGui.QMainWindow):


    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()

        self.centralWidget = QtGui.QScrollArea(self)
        self.centralWidget.setBackgroundRole(QtGui.QPalette.Dark)

        self.drawArea = QtGui.QFrame(self.centralWidget)
        self.drawArea.setBackgroundRole(QtGui.QPalette.Light)
        self.drawArea.setGeometry(self.x(), self.y(), self.width() * 2, self.height() * 6)

        self.centralWidget.setWidget(self.drawArea)
        self.setCentralWidget(self.centralWidget)

        self.setWindowIcon(QtGui.QIcon("icons/mainwindow.png"))
        self.setWindowTitle(self.tr("Qooxdoo GUI Builder"))
        self.setMinimumSize(800, 600)


    def createActions(self):

        self.newInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_new.png"), self.tr("&New interface"), self)
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
        self.saveInterfaceAction.setShortcut(self.tr("Ctrl+S"))
        self.saveInterfaceAction.setStatusTip(self.tr("Save the interface"))
        self.connect(self.saveInterfaceAction, QtCore.SIGNAL("triggered()"), self.saveInterfaceAct)

        self.saveInterfaceAsAction = QtGui.QAction(QtGui.QIcon("icons/file_saveas.png"), self.tr("Save interface &as..."), self)
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
        self.undoAction.setShortcut(self.tr("Ctrl+Z"))
        self.undoAction.setStatusTip(self.tr("Undo the action taken before"))
        self.connect(self.undoAction, QtCore.SIGNAL("triggered()"), self.undoAct)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/edit_redo.png"), self.tr("&Redo"), self)
        self.redoAction.setShortcut(self.tr("Ctrl+Y"))
        self.redoAction.setStatusTip(self.tr("Redo the action taken after"))
        self.connect(self.redoAction, QtCore.SIGNAL("triggered()"), self.redoAct)

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/edit_cut.png"), self.tr("Cu&t"), self)
        self.cutAction.setShortcut(self.tr("Ctrl+X"))
        self.cutAction.setStatusTip(self.tr("Cut the current selection"))
        self.connect(self.cutAction, QtCore.SIGNAL("triggered()"), self.cutAct)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/edit_copy.png"), self.tr("&Copy"), self)
        self.copyAction.setShortcut(self.tr("Ctrl+C"))
        self.copyAction.setStatusTip(self.tr("Copy the current selection"))
        self.connect(self.copyAction, QtCore.SIGNAL("triggered()"), self.copyAct)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/edit_paste.png"), self.tr("&Paste"), self)
        self.pasteAction.setShortcut(self.tr("Ctrl+V"))
        self.pasteAction.setStatusTip(self.tr("Paste into the current selection"))
        self.connect(self.pasteAction, QtCore.SIGNAL("triggered()"), self.pasteAct)

        self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), self.tr("&Delete"), self)
        self.deleteAction.setShortcut(self.tr("Ctrl+D"))
        self.deleteAction.setStatusTip(self.tr("Delete the current selection"))
        self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)

        self.previewInApplicationAction = QtGui.QAction(QtGui.QIcon("icons/preview_application.png"), self.tr("Preview in the &application"), self)
        self.previewInApplicationAction.setStatusTip(self.tr("Preview the interface in the application"))
        self.connect(self.previewInApplicationAction, QtCore.SIGNAL("triggered()"), self.previewInApplicationAct)

        self.previewInBrowserAction = QtGui.QAction(QtGui.QIcon("icons/preview_browser.png"), self.tr("Preview in a &browser"), self)
        self.previewInBrowserAction.setStatusTip(self.tr("Preview the interface in a browser"))
        self.connect(self.previewInBrowserAction, QtCore.SIGNAL("triggered()"), self.previewInBrowserAct)

        self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("Apply template..."), self)
        self.applyTemplateAction.setStatusTip(self.tr("Apply an existing template"))
        self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)

        self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), self.tr("Save template as..."), self)
        self.saveTemplateAsAction.setStatusTip(self.tr("Save the template"))
        self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)

        self.aboutAction = QtGui.QAction(QtGui.QIcon("icons/help_about.png"), self.tr("&About"), self)
        self.aboutAction.setStatusTip(self.tr("Show the application's About box"))
        self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self.aboutAct)


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

        self.helpToolBar = self.addToolBar(self.tr("Help"))
        self.helpToolBar.addAction(self.aboutAction)


    def createStatusBar(self):

        self.statusBar().showMessage(self.tr("Ready"))


    def createDockWindows(self):

        self.controlsDock = QtGui.QDockWidget(self.tr("Controls"), self)
        self.controlsDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.controlsDock.setFixedWidth(self.width() * 0.25)

        self.controlsList = QtGui.QListWidget(self.controlsDock)
        #self.controlsList.addItems()

        self.controlsDock.setWidget(self.controlsList)
                                   
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.controlsDock, QtCore.Qt.Vertical)

        self.propertiesDock = QtGui.QDockWidget(self.tr("Properties"), self)
        self.propertiesDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.propertiesDock.setFixedWidth(self.width() * 0.25)

        self.propertiesList = QtGui.QListWidget(self.propertiesDock)
        #self.propertiesList.addItems()

        self.propertiesDock.setWidget(self.propertiesList)
                                   
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.propertiesDock, QtCore.Qt.Vertical)


    def contextMenuEvent(self, event):

        menu = QtGui.QMenu(self)
        menu.addAction(self.cutAction)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.deleteAction)
        menu.addSeparator();
        menu.addAction(self.applyTemplateAction)
        menu.addAction(self.saveTemplateAsAction)
        menu.exec_(event.globalPos())


    def newInterfaceAct(self):

        print("")


    def openInterfaceAct(self):

        print("")


    def openTemplateAct(self):

        print("")


    def saveInterfaceAct(self):

        print("")


    def saveInterfaceAsAct(self):

        print("")


    def configureAct(self):

        print("")


    def undoAct(self):

        print("")


    def redoAct(self):

        print("")


    def cutAct(self):

        print("")


    def copyAct(self):

        print("")


    def pasteAct(self):

        print("")


    def deleteAct(self):

        print("")


    def previewInApplicationAct(self):

        print("")


    def previewInBrowserAct(self):

        print("")


    def applyTemplateAct(self):

        print("")


    def saveTemplateAsAct(self):

        print("")


    def aboutAct(self):

        QtGui.QMessageBox.about(self, self.tr("About"), self.tr("<b>Qooxdoo GUI Builder</b> provides visual construction of interfaces, using the qooxdoo framework."))



def main():
    app = QtGui.QApplication(sys.argv)
    main_widget = MainWindow()
    main_widget.showMaximized()
    sys.exit(app.exec_())



main()
