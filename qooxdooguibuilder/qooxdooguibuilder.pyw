# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class DrawArea(QtGui.QFrame):

    def __init__(self, parent = None):

        QtGui.QFrame.__init__(self, parent)
        
        self.setGeometry(self.x(), self.y(), self.width() * 2, self.height() * 6)
        self.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        self.setAcceptDrops(True)



class PropertiesWidget(QtGui.QTableWidget):

    def __init__(self, parent = None):

        QtGui.QTableWidget.__init__(self, parent)

        self.verticalHeader().hide()


    def preload(self):

        self.setAlternatingRowColors(True)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(QtCore.QStringList(["Property", "Value"]))
        self.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)


    def load(self, filePath):

        i = 0
        fetch = False
        restart = False
        f1 = file(filePath, 'r')
        f2 = file("data/properties.dat", 'r')

        for line1 in f1:
            for line2 in f2:
                if fetch:
                    for c in line2:
                        if c != "Q":
                            self.setRowCount(self.rowCount() + 1)
                            self.setRowHeight(i, 20)
                            self.setItem(i, 0, QtGui.QTableWidgetItem(self.tr(line2)))
                            i = i + 1
                        else:
                            restart = True
                        break
                elif line1 == line2:
                    fetch = True
                elif restart:
                    fetch = False
                    restart = False
                    break

        f2.close()
        f1.close()



class ControlsWidget(QtGui.QFrame):

    def __init__(self, parent = None):

        QtGui.QFrame.__init__(self, parent)

        self.setAcceptDrops(False)
        self.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        
        self.load()


    def load(self):

        iconCheckBox = QtGui.QLabel(self)
        iconCheckBox.setPixmap(QtGui.QPixmap("controls/check_box.png"))
        iconCheckBox.move(5, 5)
        iconCheckBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconCheckBox.show()

        iconComboBox = QtGui.QLabel(self)
        iconComboBox.setPixmap(QtGui.QPixmap("controls/combo_box.png"))
        iconComboBox.move(153, 5)
        iconComboBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconComboBox.show()

        iconFrame = QtGui.QLabel(self)
        iconFrame.setPixmap(QtGui.QPixmap("controls/frame.png"))
        iconFrame.move(5, 28)
        iconFrame.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconFrame.show()

        iconGroupBox = QtGui.QLabel(self)
        iconGroupBox.setPixmap(QtGui.QPixmap("controls/group_box.png"))
        iconGroupBox.move(153, 28)
        iconGroupBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconGroupBox.show()

        iconLabel = QtGui.QLabel(self)
        iconLabel.setPixmap(QtGui.QPixmap("controls/label.png"))
        iconLabel.move(5, 51)
        iconLabel.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconLabel.show()

        iconLineEdit = QtGui.QLabel(self)
        iconLineEdit.setPixmap(QtGui.QPixmap("controls/line_edit.png"))
        iconLineEdit.move(153, 51)
        iconLineEdit.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconLineEdit.show()

        iconListWidget = QtGui.QLabel(self)
        iconListWidget.setPixmap(QtGui.QPixmap("controls/list_widget.png"))
        iconListWidget.move(5, 74)
        iconListWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconListWidget.show()

        iconPushButton = QtGui.QLabel(self)
        iconPushButton.setPixmap(QtGui.QPixmap("controls/push_button.png"))
        iconPushButton.move(153, 74)
        iconPushButton.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconPushButton.show()

        iconRadioButton = QtGui.QLabel(self)
        iconRadioButton.setPixmap(QtGui.QPixmap("controls/radio_button.png"))
        iconRadioButton.move(5, 97)
        iconRadioButton.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconRadioButton.show()

        iconSpinBox = QtGui.QLabel(self)
        iconSpinBox.setPixmap(QtGui.QPixmap("controls/spin_box.png"))
        iconSpinBox.move(153, 97)
        iconSpinBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconSpinBox.show()

        iconTabWidget = QtGui.QLabel(self)
        iconTabWidget.setPixmap(QtGui.QPixmap("controls/tab_widget.png"))
        iconTabWidget.move(5, 120)
        iconTabWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconTabWidget.show()

        iconTableWidget = QtGui.QLabel(self)
        iconTableWidget.setPixmap(QtGui.QPixmap("controls/table_widget.png"))
        iconTableWidget.move(153, 120)
        iconTableWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconTableWidget.show()

        iconTextEdit = QtGui.QLabel(self)
        iconTextEdit.setPixmap(QtGui.QPixmap("controls/text_edit.png"))
        iconTextEdit.move(5, 143)
        iconTextEdit.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconTextEdit.show()

        iconTreeWidget = QtGui.QLabel(self)
        iconTreeWidget.setPixmap(QtGui.QPixmap("controls/tree_widget.png"))
        iconTreeWidget.move(153, 143)
        iconTreeWidget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        iconTreeWidget.show()



"""
class ControlsList(QtGui.QListWidget):

    def __init__(self, parent = None):

        QtGui.QListWidget.__init__(self, parent)

        self.setDragEnabled(True)
        self.setAcceptDrops(False)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setIconSize(QtCore.QSize(200, 20))

        self.load()


    def load(self):

        itemCheckBox = QtGui.QListWidgetItem(self)
        itemCheckBox.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemCheckBox.setIcon(QtGui.QIcon(self.tr("controls/check_box.png")))

        itemComboBox = QtGui.QListWidgetItem(self)
        itemComboBox.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemComboBox.setIcon(QtGui.QIcon(self.tr("controls/combo_box.png")))

        itemFrame = QtGui.QListWidgetItem(self)
        itemFrame.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemFrame.setIcon(QtGui.QIcon(self.tr("controls/frame.png")))

        itemGroupBox = QtGui.QListWidgetItem(self)
        itemGroupBox.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemGroupBox.setIcon(QtGui.QIcon(self.tr("controls/group_box.png")))

        itemLabel = QtGui.QListWidgetItem(self)
        itemLabel.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemLabel.setIcon(QtGui.QIcon(self.tr("controls/label.png")))

        itemLineEdit = QtGui.QListWidgetItem(self)
        itemLineEdit.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemLineEdit.setIcon(QtGui.QIcon(self.tr("controls/line_edit.png")))

        itemListWidget = QtGui.QListWidgetItem(self)
        itemListWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemListWidget.setIcon(QtGui.QIcon(self.tr("controls/list_widget.png")))

        itemPushButton = QtGui.QListWidgetItem(self)
        itemPushButton.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemPushButton.setIcon(QtGui.QIcon(self.tr("controls/push_button.png")))

        itemRadioButton = QtGui.QListWidgetItem(self)
        itemRadioButton.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemRadioButton.setIcon(QtGui.QIcon(self.tr("controls/radio_button.png")))

        itemSpinBox = QtGui.QListWidgetItem(self)
        itemSpinBox.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemSpinBox.setIcon(QtGui.QIcon(self.tr("controls/spin_box.png")))

        itemTabWidget = QtGui.QListWidgetItem(self)
        itemTabWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemTabWidget.setIcon(QtGui.QIcon(self.tr("controls/tab_widget.png")))

        itemTableWidget = QtGui.QListWidgetItem(self)
        itemTableWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemTableWidget.setIcon(QtGui.QIcon(self.tr("controls/table_widget.png")))

        itemTextEdit = QtGui.QListWidgetItem(self)
        itemTextEdit.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemTextEdit.setIcon(QtGui.QIcon(self.tr("controls/text_edit.png")))

        itemTreeWidget = QtGui.QListWidgetItem(self)
        itemTreeWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
        itemTreeWidget.setIcon(QtGui.QIcon(self.tr("controls/tree_widget.png")))
"""



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
        self.controlsDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.controlsDock.setFixedWidth(296)
        self.controlsDock.setFixedHeight(186)

        self.controlsWidget = ControlsWidget()

        self.controlsDock.setWidget(self.controlsWidget)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.controlsDock, QtCore.Qt.Vertical)

        self.propertiesDock = QtGui.QDockWidget(self.tr("Properties"), self)
        self.propertiesDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.propertiesDock.setFixedWidth(296)

        self.propertiesWidget = PropertiesWidget()

        self.propertiesDock.setWidget(self.propertiesWidget)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.propertiesDock, QtCore.Qt.Vertical)


    def createDrawArea(self):

        self.drawArea = DrawArea()


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


    def aboutAct(self):

        QtGui.QMessageBox.about(self, self.tr("About"), self.tr("<b>Qooxdoo GUI Builder</b><p>System of visual construction of interfaces, for the qooxdoo framework.<p><br>Authors:<p>- Cláudia Oliveira&nbsp;&nbsp;&nbsp;<a href=claudia.i.h.oliveira@gmail.com>claudia.i.h.oliveira@gmail.com</a><p>- Cláudio Pedro&nbsp;&nbsp;&nbsp;<a href=claudio.pedro@gmail.com>claudio.pedro@gmail.com</a><p>- Nuno Coelho&nbsp;&nbsp;&nbsp;<a href=nuno.a.coelho@gmail.com>nuno.a.coelho@gmail.com</a><p><br>Official Web Site:&nbsp;&nbsp;&nbsp;<a href=http://qooxdooguibuilder.googlepages.com>http://qooxdooguibuilder.googlepages.com</a>"))


    def applyTemplateAct(self):

        print("")


    def saveTemplateAsAct(self):

        print("")



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_widget = MainWindow()
    main_widget.showMaximized()
    sys.exit(app.exec_())
