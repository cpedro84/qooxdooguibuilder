# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



"""
CLASS HelpWindow
"""
class HelpWindow(QtGui.QDialog):


	"""
	FUNCTION __init__
	"""
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self, parent)
				
		self.quit = QtGui.QPushButton("Close", self)
		self.quit.setGeometry(62, 40, 75, 30)
		self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.close)
		
		self.setFixedSize(250, 100)
		self.setWindowTitle(self.tr("About Qooxdoo GUI Builder"))
		
		
		
"""
CLASS ApplicationWindow
"""
class ApplicationWindow(QtGui.QMainWindow):


	"""
	FUNCTION __init__
	"""
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.widgetRect = self.geometry()
		self.menu = self.createMenu()
		self.menuRect = self.menu.geometry()
		self.menuRect.setWidth(self.widgetRect.width())
		self.menu.setGeometry(self.menuRect)
		self.setMenuBar(self.menu)
		
		self.Toolbar = self.createToolBar()
		self.Toolbar.setGeometry(0, self.menuRect.height(), 0, 0)
		self.toolBarRect = self.Toolbar.geometry()
		self.addToolBar(QtCore.Qt.TopToolBarArea, self.Toolbar)
		
		self.WidgetBox = self.createWidgetBox()
		self.WidgetBox.setMinimumWidth(0.2*self.width())
		self.WidgetBox.setMaximumWidth(0.3*self.width())
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.WidgetBox, QtCore.Qt.Vertical)
		
		self.WidgetProperties = self.createWidgetBox()
		self.WidgetProperties.setMinimumWidth(0.2*self.width())
		self.WidgetProperties.setMaximumWidth(0.3*self.width())
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.WidgetProperties, QtCore.Qt.Vertical)
		
		self.CentralWidget = QtGui.QScrollArea(self)
		self.CentralWidget.setBackgroundRole(QtGui.QPalette.Dark)
		
		self.RectCentralWidget = QtCore.QRect()
		self.RectCentralWidget.setWidth(self.widgetRect.width()*0.8)
		self.RectCentralWidget.setHeight(self.widgetRect.height())
		self.CentralWidget.setGeometry(self.RectCentralWidget)
		
		self.drawWidget = QtGui.QFrame(self.CentralWidget)
		self.drawWidget.setAutoFillBackground(bool(0))
		self.drawWidget.setGeometry(self.RectCentralWidget.x() + self.RectCentralWidget.width() * 0.2, self.RectCentralWidget.y() + self.RectCentralWidget.height() * 0.2, self.RectCentralWidget.width(), self.RectCentralWidget.height())
		self.drawWidget.setBackgroundRole(QtGui.QPalette.Midlight)
		
		self.drawLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		self.drawLayout.addStretch(1)
		self.drawLayout.setMargin(11)
		self.drawLayout.addWidget(self.drawWidget)
		
		self.CentralWidget.setWidget(self.drawWidget)
		self.setCentralWidget(self.CentralWidget)
		
		self.setMinimumSize(800, 600)
		self.setWindowTitle(self.tr("Qooxdoo GUI Builder"))
		
		
	def createMenu(self):
		
		# MENU "FILE"
		self.menuFile = QtGui.QMenu("&File")
		self.newInterfaceAction = self.menuFile.addAction("&New interface...")
		self.openInterfaceAction = self.menuFile.addAction("&Open interface...")
		self.openTemplateAction = self.menuFile.addAction("Open &template...")
		self.menuFile.addSeparator()
		self.saveInterfaceAction = self.menuFile.addAction("&Save interface")
		self.saveInterfaceAsAction = self.menuFile.addAction("Save interface &as...")
		self.menuFile.addSeparator()
		self.configureAction = self.menuFile.addAction("&Configure...")
		self.menuFile.addSeparator()
		self.exitAction = self.menuFile.addAction("E&xit")
		self.connect(self.exitAction, QtCore.SIGNAL("triggered()"), QtGui.qApp, QtCore.SLOT("quit()"))
		#**********
		
		# MENU "EDIT"
		self.menuEdit = QtGui.QMenu("&Edit")
		self.undoAction = self.menuEdit.addAction(QtGui.QIcon("./icons/back.xpm"), "&Undo (Ctrl+Z)")
		self.redoAction = self.menuEdit.addAction(QtGui.QIcon("./icons/forward.xpm"), "&Redo (Ctrl+Y)")
		self.menuEdit.addSeparator()
		self.cutAction = self.menuEdit.addAction("&Cut (Ctrl+X)")
		self.copyAction = self.menuEdit.addAction("C&opy (Ctrl+C)")
		self.pasteAction = self.menuEdit.addAction("&Paste (Ctrl+V)")
		#**********
		
		# MENU "CONTROL"
		self.menuControl = QtGui.QMenu("&Control")
		self.statusMenu = self.menuControl.addMenu("&Status")
		self.protectedAction = self.statusMenu.addAction("&Protected")
		self.visibleAction = self.statusMenu.addAction("&Visible")
		#**********
		
		# MENU "PREVIEW"
		self.menuPreview = QtGui.QMenu("&Preview")
		self.previewInApplicationAction = self.menuPreview.addAction("Preview in &application")
		self.previewInBrowserAction = self.menuPreview.addAction("Preview in &browser")
		#**********
		
		# MENU "HELP"
		self.menuHelp = QtGui.QMenu("&Help")
		self.aboutAction = self.menuHelp.addAction("&On-line documentation")
		self.aboutAction = self.menuHelp.addAction("&About Qooxdoo GUI Builder")
		self.connect(self.aboutAction, QtCore.SIGNAL("triggered()"), self.openHelpWindow)
		#**********
		
		self.menuBar = QtGui.QMenuBar(self)
		self.menuBar.addMenu(self.menuFile)
		self.menuBar.addMenu(self.menuEdit)
		self.menuBar.addMenu(self.menuControl)
		self.menuBar.addMenu(self.menuPreview)
		self.menuBar.addMenu(self.menuHelp)
		
		return self.menuBar
		
		
	def createToolBar(self):
		self.toolBar = QtGui.QToolBar(self)
		self.toolBar.setMovable(1)
		self.openAction = self.toolBar.addAction(QtGui.QIcon("./icons/forward.xpm"), "Open interface")
		
		return self.toolBar
		
		
	def createWidgetBox(self):
		self.WidgetBox = QtGui.QDockWidget("Widget Box", self)	
		
		return self.WidgetBox
		
		
	def openHelpWindow(self):
		self.wdw_help = HelpWindow()
		self.wdw_help.show()
		
		
		
def main(): 
	app = QtGui.QApplication(sys.argv)
	main_widget = ApplicationWindow()
	main_widget.show()
	sys.exit(app.exec_())
	
	
	
main()