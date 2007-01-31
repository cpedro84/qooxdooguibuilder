#-*-encoding:latin1 -*-

import sys
from PyQt4 import QtCore, QtGui



class WidgetHelp(QtGui.QDialog):
    
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
	
		self.setFixedSize(400, 220)
		self.quit = QtGui.QPushButton("Quit", self)
		self.quit.setGeometry(62, 40, 75, 30)
		self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.close)
		

class MyWidget(QtGui.QMainWindow):
    
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.widgetRect = self.geometry()
		#self.widgetRect.setWidth(sizeWint())
		#self.widgetRect.setHeight(sizeHint())
		#self.setFixedSize(400, 220)
				
		self.menu = self.createMenu()
		self.menuRect = self.menu.geometry()
		self.menuRect.setWidth(self.widgetRect.width())
		self.menu.setGeometry(self.menuRect)
		self.setMenuBar(self.menu)
		
		
		self.Toolbar = self.createToolBar()		
		self.Toolbar.setGeometry(0, self.menuRect.height(), 0, 0 )
		self.toolBarRect = self.Toolbar.geometry()
		
		self.addToolBar(QtCore.Qt.TopToolBarArea, self.Toolbar)
		
		#criar as DockWidgets
		#WIDGETBOX
		self.WidgetBox = self.createWidgetBox()
		self.WidgetBox.setMinimumWidth(0.2*self.width())		
		self.WidgetBox.setMaximumWidth(0.3*self.width())
		#self.WidgetBox.resize(0.2*self.width(), self.height())
		
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.WidgetBox, QtCore.Qt.Vertical)
		
		#WIDGET PROPERTIES
		self.WidgetProperties = self.createWidgetBox()
		self.WidgetProperties.setMinimumWidth(0.2*self.width())
		self.WidgetProperties.setMaximumWidth(0.3*self.width()) 
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.WidgetProperties, QtCore.Qt.Vertical)
		
		#definir CentralWidget
		self.CentralWidget = QtGui.QScrollArea(self)
		self.CentralWidget.setBackgroundRole(QtGui.QPalette.Dark)

		#self.CentralWidget_.setAutoFillBackground(bool(1))
		#self.CentralWidget_.setFrameShadow(QtGui.QFrame.Plain)
		#self.CentralWidget_.setFrameStyle(QtGui.QFrame.StyledPanel)
		
		#definir widget de desenho		
		self.RectCentralWidget = QtCore.QRect()
		self.RectCentralWidget.setWidth(self.widgetRect.width()*0.8)
		self.RectCentralWidget.setHeight(self.widgetRect.height())
		self.CentralWidget.setGeometry(self.RectCentralWidget)
		
		self.drawWidget = QtGui.QFrame(self.CentralWidget)
		self.drawWidget.setAutoFillBackground(bool(0))		
		self.drawWidget.setGeometry(self.RectCentralWidget.x()+self.RectCentralWidget.width()*0.2, self.RectCentralWidget.y()+self.RectCentralWidget.height()*0.2,
							self.RectCentralWidget.width(), self.RectCentralWidget.height())
		self.drawWidget.setBackgroundRole(QtGui.QPalette.Midlight)
			
			
			
		self.drawLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		self.drawLayout.addStretch(1)
		self.drawLayout.setMargin(11)
		self.drawLayout.addWidget(self.drawWidget)
			
		
		#definir a widget da SrollArea
		self.CentralWidget.setWidget(self.drawWidget)		
		#self.CentralWidget.setWidgetResizable(bool(1))
		#definir a widget central da MainWindow
		self.setCentralWidget(self.CentralWidget)
		
		
		
		
		
		
		#self.drawWidget = QtGui.QFrame(self.CentralWidget)
		
		#self.drawLayout = QtGui.QHBoxLayout()
		#self.drawLayout.addStretch(1)
		#self.drawLayout.setMargin(20)
		#self.drawLayout.addWidget(self.drawWidget)
		
		
		#self.drawWidget.setAutoFillBackground(bool(0))		
		#self.drawWidget.setGeometry(self.RectCentralWidget.x()+self.RectCentralWidget.width()*0.2, self.RectCentralWidget.y()+self.RectCentralWidget.height()*0.2,
		#self.RectCentralWidget.width(), self.RectCentralWidget.height())
		#self.drawWidget.setBackgroundRole(QtGui.QPalette.Midlight)
		#self.drawWidget.setMouseTracking(bool(1))
	
		#definir a widget da SrollArea
		#self.CentralWidget.setWidget(self.drawWidget)		
		#self.CentralWidget.setWidgetResizable(bool(1))
		#definir a widget central da MainWindow
		#self.setCentralWidget(self.CentralWidget)
		#self.setCentralWidget(self.drawWidget)
		
		
		
		#self.WidgetBox.setGeometry(0,self.toolBarRect.y(), 0, 0)
		#self.Toolbar.setMovable(bool(1))
		
		#organização geometrica			
		
	
	
	
	def createWidgetBox(self):
		self.WidgetBox = QtGui.QDockWidget("Widget Box", self)	
		return self.WidgetBox
		
	def createMenu(self):
		#Criação dos menu items
		
		#**************MENU FILE********************************
		self.menuFile = QtGui.QMenu("File")
		
		self.newinterfaceAction = self.menuFile.addAction("New interface...")
		self.openinterfaceAction = self.menuFile.addAction("Open interface...")
		self.openTemplateAction = self.menuFile.addAction("Open Template...")
		self.newinterfaceAction = self.menuFile.addAction("Close...")
		
		#Adicionar separador
		self.menuFile.addSeparator()
		
		self.saveAction = self.menuFile.addAction("Save")
		self.saveAsAction = self.menuFile.addAction("Save As...")
		self.saveAsTemplateAction = self.menuFile.addAction("Save As Template...")
		
		#Adicionar separador
		self.menuFile.addSeparator()
		
		self.exitAction = self.menuFile.addAction("Exit")		
		self.connect(self.exitAction, QtCore.SIGNAL("triggered()"),  
			QtGui.qApp, QtCore.SLOT("quit()"))
		#*********************************************************
		
		#**************MENU EDIT********************************
		self.menuEdit = QtGui.QMenu("Edit")
		
		self.undoAction = self.menuEdit.addAction(QtGui.QIcon("./icons/back.xpm"),"Undo")
		self.redoAction = self.menuEdit.addAction(QtGui.QIcon("./icons/forward.xpm"),"Redo")
				
		#Adicionar separador
		self.menuEdit.addSeparator()
		
		self.cutAction = self.menuEdit.addAction("Cut")
		self.copyAction = self.menuEdit.addAction("Copy")
		self.pasteAction = self.menuEdit.addAction("Paste")
		#*********************************************************
		
		#**************MENU VIEW********************************
		self.menuView = QtGui.QMenu("View")
				
		#*********************************************************		
		
		#**************MENU INSERT********************************
		self.menuInsert = QtGui.QMenu("Insert")
				
		#*********************************************************
		
		#**************MENU CONTROL********************************
		self.menuControl = QtGui.QMenu("Control")
		
		self.statusControlMenu = self.menuControl.addMenu("Status Control")
		self.VisibleAction = self.statusControlMenu.addAction("Visible")
		self.ReadOnlyAction = self.statusControlMenu.addAction("Read only")		
		#*********************************************************
		
		#**************MENU CONFIGURE*************************
		self.menuConfigure = QtGui.QMenu("Configure")
				
		#*********************************************************
		
		#**************MENU TEST*************************
		self.menuTest = QtGui.QMenu("Test")
		
		self.testinterfaceFormatAppAction = self.menuTest.addAction("Test interface App")
		self.testinterfaceFormatWebAction = self.menuTest.addAction("Test interface Web")
		#*********************************************************
				
		#**************MENU HELP********************************
		self.menuHelp = QtGui.QMenu("Help")
		self.helpAction = self.menuHelp.addAction("About...")		
		self.connect(self.helpAction, QtCore.SIGNAL("triggered()"),  self.openHelpWindow)
		#*********************************************************
		
				
		self.MenuBar = QtGui.QMenuBar(self)
		self.MenuBar.addMenu(self.menuFile)
		self.MenuBar.addMenu(self.menuEdit)
		self.MenuBar.addMenu(self.menuView)
		self.MenuBar.addMenu(self.menuInsert)
		self.MenuBar.addMenu(self.menuControl)
		self.MenuBar.addMenu(self.menuConfigure)
		self.MenuBar.addMenu(self.menuTest)
		self.MenuBar.addMenu(self.menuHelp)
		
		return self.MenuBar
	
	def createToolBar(self):
						
		self.ToolBar = QtGui.QToolBar(self)
		self.ToolBar.setMovable(1)
				
		self.OpenAction = self.ToolBar.addAction(QtGui.QIcon("./icons/forward.xpm"), "Open")
		return self.ToolBar
	
	
	def openHelpWindow(self):
		
		self.wdw_help = WidgetHelp()
		self.wdw_help.show()
	

	
#main 
app = QtGui.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())