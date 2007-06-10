# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "controls"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "data"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "icons"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "libraries"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "monitorization"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "utilities"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "widgets"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../controls"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../data"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../icons"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../libraries"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../monitorization"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../utilities"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "../widgets"))

from PyQt4 import QtCore, QtGui
from const import *
from monitorControls import *
from tableWidget import *



pathButtonPixmap = DIR_CONTROLS + "Button.png"
pathCheckPixmap = DIR_CONTROLS + "CheckBox.png"
pathComboPixmap = DIR_CONTROLS + "ComboBox.png"
pathGroupPixmap = DIR_CONTROLS + "GroupBox.png"
pathIframePixmap = DIR_CONTROLS + "Iframe.png"
pathLabelPixmap = DIR_CONTROLS + "Label.png"
pathListPixmap = DIR_CONTROLS + "List.png"
pathMenuBarPixmap = DIR_CONTROLS + "MenuBar.png"
pathPasswordFieldPixmap = DIR_CONTROLS + "PasswordField.png"
pathRadioPixmap = DIR_CONTROLS + "RadioButton.png"
pathSpinnerPixmap = DIR_CONTROLS + "Spinner.png"
pathTabViewPixmap = DIR_CONTROLS + "TabView.png"
pathTablePixmap = DIR_CONTROLS + "Table.png"
pathTextAreaPixmap = DIR_CONTROLS + "TextArea.png"
pathTextFieldPixmap = DIR_CONTROLS + "TextField.png"
pathToolbarPixmap = DIR_CONTROLS + "ToolBar.png"
pathTreePixmap = DIR_CONTROLS + "Tree.png"



class DragLabel(QtGui.QLabel):


    def __init__(self, text, parent=None):

        QtGui.QLabel.__init__(self, text, parent)

        self.setFrameShape(QtGui.QFrame.Panel)
        self.setFrameShadow(QtGui.QFrame.Raised)

    def mousePressEvent(self, event):

        itemData = QtCore.QByteArray()

        mimeData = QtCore.QMimeData()
        mimeData.setData(APLICATION_RESIZABLE_TYPE, itemData)

	drag = QtGui.QDrag(self)
	drag.setMimeData(mimeData)
	drag.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)
        if dropAction == QtCore.Qt.MoveAction:
            self.close()
            self.update()


class DrawArea(QtGui.QWidget):
    def __init__(self, monitor, parent = None):	
        
	QtGui.QWidget.__init__(self)
	
	self.parent = parent
	
	#definir que o evento MouseMove é accionado por qualquer movimento do rato mesmo que este não seja clicado
	self.setMouseTracking(true)
	self.monitor = monitor
	
	self.mouseClicked = false

	#********Variavéis que controlam o QRuberHand*********	
	self.rubberHand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
	self.mousePressed = false	
	#*********************************************
	
        self.setAcceptDrops(True)
        self.setBackgroundRole(DRAW_AREA_COLOR)
        self.setGeometry(self.x(), self.y(), self.width() * 2, self.height() * 6)	
      
	#DEFINIÇÃO DE TAMANHOS
	self.PenWidth = 2 
	self.RectSize = 4
	

    def mousePressEvent(self, event):
	self.mouseClicked = true
	#Des-Seleccionar todos os controlos que tiverem seleccionados
	self.monitor.disableAllSelectedControls()		
	self.originPressed = QtCore.QPoint(event.pos())
	
	self.rubberHand.setGeometry(QtCore.QRect(self.originPressed, QtCore.QSize()))
	self.rubberHand.show()
		
    def mouseReleaseEvent(self, event):
	self.mouseClicked = true
	rubberRect = QtCore.QRect(self.rubberHand.geometry())
	self.rubberHand.hide()	
	self.monitor.setSelectedControlsIntersection(rubberRect)

    def mouseMoveEvent(self, event):		
	if self.mouseClicked: 
		self.rubberHand.setGeometry(QtCore.QRect(self.originPressed, event.pos()).normalized())
	
	#verificar se existem vários controlos selecciondos 
	

    def dragEnterEvent(self, event):	
	if event.mimeData().hasFormat(APLICATION_RESIZABLE_TYPE):
            event.acceptProposedAction() #Indicação do possivel drop	    
	else:
            event.ignore()

    
    #***************PROCESSAMENTO DE SINAIS***************
    def SignalProcess_resizableCliked(self, typeControl, idControl):	
	typeControl = str(typeControl)
	idControl =str(idControl)
	
	#Envio do sinal de que um controlo foi clicado, com as suas propriedades
	self.emit(QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), typeControl,  idControl)
	
	self.monitor.setSelectedControl(typeControl, idControl)
    #************************************************************

    def dropEvent(self, event):
        
        if event.mimeData().hasFormat(APLICATION_RESIZABLE_TYPE):
            
	    itemData = event.mimeData().data(APLICATION_RESIZABLE_TYPE)	    
	    dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.ReadOnly)	    
	    
            offset = QtCore.QPoint()
            actionType = QtCore.QString()
	    dataStream >> actionType >> offset
	    
	    #Calcular a posição de drop de forma que o controlo fique integrado numa posição multipla do STEP_MOVE
	    dropPos = QtCore.QPoint(event.pos() - offset)
	    dropPos.setX(dropPos.x() - (dropPos.x() % STEP_MOVE))
	    dropPos.setY(dropPos.y() - (dropPos.y() % STEP_MOVE))
	    #*************************************************************************************************
	    
	    if actionType == DRAG_COPY_ACTION:

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
			
		    #*********************************************************
		    #TEXTFIELD
		    elif main_window.control_beeing_added == 15:
			#self.newIcon = DragLabel("Text Field", self)		
			self.newIcon = self.monitor.addNewControl(TList, self)
			self.newIcon.setGeometry(self.newIcon.x(), self.newIcon.y(), 100, 80)
		    #*********************************************************	    
		    
		    elif main_window.control_beeing_added == 16:
			self.newIcon = DragLabel("Tool Bar", self)
		    elif main_window.control_beeing_added == 17:
			self.newIcon = DragLabel("Tree", self)
 		    
		    QtCore.QObject.connect(self.newIcon, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		    
		    #Envio do sinal de que um controlo foi clicado, com as suas propriedades
		    #(...)-> é necessário saber o ID (monitor.getLastIdControl() ) e o tipo (typeControl acima inserido) para ir carregar as propriedades
		    self.emit(QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), TList, self.monitor.getLastIdControl())
		    
		    
		    self.newIcon.move(dropPos)
		    self.newIcon.show()
	    
	    #CASO DE UM DRAG DE "MOVE"
	    elif actionType == DRAG_MOVE_ACTION:		  
		event.source().move(dropPos)		
		
	    #Indicação de operação de Drop sucedida
            if event.source() in self.children():           
		event.setDropAction(QtCore.Qt.MoveAction) #indicação da acção de move, pois a o drop foi efectuado sobre a mesma widget da acção de drag
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



class PropertiesWidget(CTableWidget):


    def __init__(self, monitor, parent = None):

        CTableWidget.__init__(self, parent)

	self.monitor = monitor
        self.setAlternatingRowColors(True)
        
        self.addColumn(PROPERTIES_WIDGET_COLUMN1)
	self.addColumn(PROPERTIES_WIDGET_COLUMN2)
	
	#self.setItem()
	
	
        self.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.verticalHeader().hide()


    def fillControlPropertys(self, typeControl, idControl ):
	controlInfo = self.monitor.getControlInfo(typeControl, idControl)
	
	tableData = CTableData()
	tableData.addColumn(PROPERTIES_WIDGET_COLUMN1)
	tableData.addColumn(PROPERTIES_WIDGET_COLUMN2)
	
	currentRow = 0
	columnProperties = 0
	columnValues = 1
	
	if controlInfo.hasProperties():
		for controlProperty in controlInfo.getControlProperties():
			
			tableData.addRow("")
			tableData.setItem(columnProperties, currentRow, controlProperty.getNameProperty())
			tableData.setItem(columnValues, currentRow, controlProperty.getValueProperty())
			currentRow +=1
			#print controlProperty.getNameProperty()
			#print controlProperty.getValueProperty()
	
	self.setTableWidget(tableData)
	
	#(....)

class ControlsDockWidget(QtGui.QDockWidget):


    def __init__(self, parent = None):

        QtGui.QDockWidget.__init__(self, "Controls", parent)

        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.setFeatures(QtGui.QDockWidget.DockWidgetClosable | QtGui.QDockWidget.DockWidgetMovable)
        self.setFixedWidth(273)


    def closeEvent(self, event):

        main_window.controlsAction.setChecked(False)



class ControlsWidget(QtGui.QWidget):

    def __init__(self, monitor, parent = None):

        QtGui.QListWidget.__init__(self, parent)

	self.monitor = monitor

        self.setGeometry(self.x(), self.y(), 254, 360)

        itemButton = QtGui.QLabel(self)
        itemButton.setPixmap(QtGui.QPixmap(pathButtonPixmap))
        itemButton.move(2, 2)

        itemCheckBox = QtGui.QLabel(self)
        itemCheckBox.setPixmap(QtGui.QPixmap(pathCheckPixmap))
        itemCheckBox.move(2, 23)

        itemComboBox = QtGui.QLabel(self)
        itemComboBox.setPixmap(QtGui.QPixmap(pathComboPixmap))
        itemComboBox.move(2, 44)

        itemGroupBox = QtGui.QLabel(self)
        itemGroupBox.setPixmap(QtGui.QPixmap(pathGroupPixmap))
        itemGroupBox.move(2, 65)

        itemIframe = QtGui.QLabel(self)
        itemIframe.setPixmap(QtGui.QPixmap(pathIframePixmap))
        itemIframe.move(2, 86)

        itemLabel = QtGui.QLabel(self)
        itemLabel.setPixmap(QtGui.QPixmap(pathLabelPixmap))
        itemLabel.move(2, 107)

        itemList = QtGui.QLabel(self)
        itemList.setPixmap(QtGui.QPixmap(pathListPixmap))
        itemList.move(2, 128)

        itemMenuBar = QtGui.QLabel(self)
        itemMenuBar.setPixmap(QtGui.QPixmap(pathMenuBarPixmap))
        itemMenuBar.move(2, 149)

        itemPasswordField = QtGui.QLabel(self)
        itemPasswordField.setPixmap(QtGui.QPixmap(pathPasswordFieldPixmap))
        itemPasswordField.move(2, 170)

        itemRadioButton = QtGui.QLabel(self)
        itemRadioButton.setPixmap(QtGui.QPixmap(pathRadioPixmap))
        itemRadioButton.move(2, 191)

        itemSpinner = QtGui.QLabel(self)
        itemSpinner.setPixmap(QtGui.QPixmap(pathSpinnerPixmap))
        itemSpinner.move(2, 212)

        itemTabView = QtGui.QLabel(self)
        itemTabView.setPixmap(QtGui.QPixmap(pathTabViewPixmap))
        itemTabView.move(2, 233)

        itemTable = QtGui.QLabel(self)
        itemTable.setPixmap(QtGui.QPixmap(pathTablePixmap))
        itemTable.move(2, 254)

        itemTextArea = QtGui.QLabel(self)
        itemTextArea.setPixmap(QtGui.QPixmap(pathTextAreaPixmap))
        itemTextArea.move(2, 275)

        itemTextField = QtGui.QLabel(self)
        itemTextField.setPixmap(QtGui.QPixmap(pathTextFieldPixmap))
        itemTextField.move(2, 296)

        itemToolBar = QtGui.QLabel(self)
        itemToolBar.setPixmap(QtGui.QPixmap(pathToolbarPixmap))
        itemToolBar.move(2, 317)

        itemTree = QtGui.QLabel(self)
        itemTree.setPixmap(QtGui.QPixmap(pathTreePixmap))
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
	dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
	dataStream << QtCore.QString(DRAG_COPY_ACTION) << QtCore.QPoint()	
	
        mimeData = QtCore.QMimeData()
        mimeData.setData(APLICATION_RESIZABLE_TYPE, itemData)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos())

        if drag.start(QtCore.Qt.CopyAction ) == QtCore.Qt.MoveAction:
            child.close()
        else:
            child.show()


class MainWindow(QtGui.QMainWindow):


    def __init__(self, parent = None):

        QtGui.QMainWindow.__init__(self, parent)
	
	self.monitor = MonitorControls()

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()
        self.createDrawArea()

        self.centralWidget = QtGui.QScrollArea(self)
        self.centralWidget.setBackgroundRole(BACKGROUNDS_COLOR)
	self.centralWidget.setViewportMargins(MARGIN,MARGIN,MARGIN,MARGIN)
	self.centralWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	self.centralWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)	
        self.centralWidget.setWidget(self.drawArea)

	self.centralWidget.show()
        self.setCentralWidget(self.centralWidget)

        self.setWindowIcon(QtGui.QIcon("icons/mainwindow.png"))
        self.setWindowTitle("Qooxdoo GUI Builder")
        self.setMinimumSize(800, 600)


    def createActions(self):

        self.newInterfaceAction = QtGui.QAction(QtGui.QIcon("icons/file_new.png"), "&New interface...", self)
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

        self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), "&Delete...", self)
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

        self.controlsWidget = ControlsWidget(self.monitor)

        self.intermediateWidget = QtGui.QScrollArea(self)
        self.intermediateWidget.setBackgroundRole(BACKGROUNDS_COLOR)
        self.intermediateWidget.setWidget(self.controlsWidget)

        self.controlsDockWidget = ControlsDockWidget()
        self.controlsDockWidget.setWidget(self.intermediateWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.controlsDockWidget, QtCore.Qt.Vertical)

        self.propertiesWidget = PropertiesWidget(self.monitor)

        self.propertiesDockWidget = PropertiesDockWidget()
        self.propertiesDockWidget.setWidget(self.propertiesWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.propertiesDockWidget, QtCore.Qt.Vertical)


    def createDrawArea(self):

        self.drawArea = DrawArea(self.monitor)
	self.drawArea.setAttribute(QtCore.Qt.WA_AcceptDrops)

	QtCore.QObject.connect(self.drawArea, QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), self.propertiesWidget.fillControlPropertys)

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
