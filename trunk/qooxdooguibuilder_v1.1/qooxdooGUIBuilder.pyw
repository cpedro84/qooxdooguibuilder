# !/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
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
from MonitorControls import *
from tableWidget import *
from ComboBoxProperties import *
from LineEditProperty import *
from InputMask import *

pathButtonPixmap = DIR_CONTROLS+"Button.png"
pathCheckPixmap = DIR_CONTROLS+"CheckBox.png"
pathComboPixmap = DIR_CONTROLS+"ComboBox.png"
pathGroupPixmap = DIR_CONTROLS+"GroupBox.png"
pathIframePixmap = DIR_CONTROLS+"Iframe.png"
pathLabelPixmap = DIR_CONTROLS+"Label.png"
pathListPixmap = DIR_CONTROLS+"List.png"
pathMenuBarPixmap = DIR_CONTROLS+"MenuBar.png"
pathPasswordFieldPixmap = DIR_CONTROLS+"PasswordField.png"
pathRadioPixmap = DIR_CONTROLS+"RadioButton.png"
pathSpinnerPixmap = DIR_CONTROLS+"Spinner.png"
pathTabViewPixmap = DIR_CONTROLS+"TabView.png"
pathTablePixmap = DIR_CONTROLS+"Table.png"
pathTextAreaPixmap = DIR_CONTROLS+"TextArea.png"
pathTextFieldPixmap = DIR_CONTROLS+"TextField.png"
pathToolbarPixmap = DIR_CONTROLS+"ToolBar.png"
pathTreePixmap = DIR_CONTROLS+"Tree.png"

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
	
	#definir que o evento MouseMove é assionado por qualquer movimento do rato mesmo que este não seja clicado
	self.setMouseTracking(true)
	self.monitor = monitor
	
	self.mouseClicked = false

	#********Variavéis que controlam o QRuberHand*********	
	self.rubberHand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
	self.mousePressed = false
	#*********************************************
	
	self.setAcceptDrops(True)
	self.setAutoFillBackground(true)
	self.setBackgroundRole(QtGui.QPalette.Light)
	
	
	#self.setGeometry(self.x(), self.y(), self.width() * 2, self.height() * 6)	
	self.setGeometry(self.x(), self.y(), DRAW_AREA_WIDTH, DRAW_AREA_HEIGHT)

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
	
	#enviar sinal para inicar que nenhum controlo está seleccionado
	self.emit(QtCore.SIGNAL(SIGNAL_NONE_CONTROL_SELECTED))
	
    def mouseReleaseEvent(self, event):
	self.mouseClicked = true
	rubberRect = QtCore.QRect(self.rubberHand.geometry())
	self.rubberHand.hide()	
	self.monitor.setSelectedControlsIntersection(rubberRect)

    def mouseMoveEvent(self, event):		
	if self.mouseClicked: 
		self.rubberHand.setGeometry(QtCore.QRect(self.originPressed, event.pos()).normalized())
	
	#verificar se existem vários controlos selecciondos 

    
    #***************PROCESSAMENTO DE SINAIS***************
    def SignalProcess_resizableReleased(self, typeControl, idControl):	
	typeControl = str(typeControl)
	idControl =str(idControl)
	
	#Envio do sinal de que um controlo foi clicado, com as suas propriedades
	self.emit(QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), typeControl,  idControl)


    def SignalProcess_resizableClicked(self, typeControl, idControl):
	typeControl = str(typeControl)
	idControl =str(idControl)
    
	self.monitor.setSelectedControl(typeControl, idControl)
    
    def deleteControl(self, typeControl, idControl):
	typeControl = str(typeControl)
	idControl =str(idControl)
	
	#enviar sinal para inicar que nenhum controlo está seleccionado	
	self.monitor.deleteControl(typeControl, idControl)
	self.emit(QtCore.SIGNAL(SIGNAL_NONE_CONTROL_SELECTED))

    # Items -> QStringList
    def saveTListItems(self, typeControl, idControl, items):
	self.monitor.changeItemsProperties(typeControl, idControl, Items)
	
    def saveTTabViewTabs(self, typeControl, idControl, tabs):
	self.monitor.changeTabsProperties(typeControl, idControl, Tabs)

    def changeTableItemsProperties(self, typeControl, idControl, tableItems):
	self.monitor.changeTabsProperties(typeControl, idControl, tableItems)

    #********************************************************* 
    #************************************************************
    
    def dragEnterEvent(self, event):	
	if event.mimeData().hasFormat(APLICATION_RESIZABLE_TYPE):
            event.acceptProposedAction() #Indicação do possivel drop	    
	else:
            event.ignore()

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
		    
		    newControlWidget = self.monitor.addNewControl(main_window.control_beeing_added, self)
		    
		    QtCore.QObject.connect(newControlWidget, QtCore.SIGNAL(SIGNAL_RESIZABLE_RELEASED), self.SignalProcess_resizableReleased)
		    QtCore.QObject.connect(newControlWidget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableClicked)
		    QtCore.QObject.connect(newControlWidget, QtCore.SIGNAL(SIGNAL_RESIZABLE_DELETE), self.deleteControl)
		    
		    #PARA  CONTROLOS QUE TENHAM PROPRIEDADES DE ITEMS  (Colocar este código nos if desses controlos e criar metodos para tratar cada um dos sinais)
		    QtCore.QObject.connect(newControlWidget, QtCore.SIGNAL(SIGNAL_RESIZABLE_ITEMS_CHANGED), self.saveTListItems)
		    #PARA  CONTROLOS QUE TENHAM PROPRIEDADES DE TABS  (Colocar este código nos if desses controlos e criar metodos para tratar cada um dos sinais)
		    QtCore.QObject.connect(newControlWidget, QtCore.SIGNAL(SIGNAL_RESIZABLE_ITEMS_CHANGED), self.saveTTabViewTabs)		    
		    #*****************************************************************
		    
		    newControlWidget.move(dropPos)
		    newControlWidget.show()
	    
	    #CASO DE UM DRAG DE "MOVE"
	    elif actionType == DRAG_MOVE_ACTION:		  
		event.source().move(dropPos)		
		
	    
	    #Indicação de operação de Drop sucedida
            if event.source() in self.children():           
		event.setDropAction(QtCore.Qt.MoveAction) #indicação da acção de move, pois a o drop foi efectuado sobre a mesma widget da acção de drag
                event.accept()
            else:
                event.acceptProposedAction()
	
	    typeControl = str(self.monitor.getTypeSelectedControl())
	    idControl = str(self.monitor.getIdSelectedControl())
	    	
	    #Alterar as prorpriedades Left e Top de acordo com a nova posição
	    
	    self.monitor.changeProperty(typeControl, idControl, ID_LEFT, str(dropPos.x()))
	    self.monitor.changeProperty(typeControl, idControl, ID_TOP, str(dropPos.y()))
	    
	    #*************FAZER**********************************************
	    #print QtGui.QWidget(event.source()).geometry().width()
	    #self.monitor.changeProperty(typeControl, idControl, ID_WIDTH, str(event.source().width()))
	    #self.monitor.changeProperty(typeControl, idControl, ID_HEIGHT, str(event.source().height()))
	    #******************************************************************
	
	    #Envio do sinal de que um controlo foi clicado, com as suas propriedades (para repreencher as propriedades na dockWidget das propriedades)
    	    #(...)-> é necessário saber o ID (monitor.getLastIdControl() ) e o tipo (typeControl acima inserido) para ir carregar as propriedades
	    self.emit(QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), typeControl, idControl)

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
	self.connect(self, QtCore.SIGNAL("cellClicked(int, int)"), self.cellClicked)
	#self.connect(self, QtCore.SIGNAL("cellDoubleClicked(int, int)"), self.cellDoubleClicked)
	
	self.monitor = monitor
       
	self.setAlternatingRowColors(True)
        
        self.addColumn(PROPERTIES_WIDGET_COLUMN1)
	self.addColumn(PROPERTIES_WIDGET_COLUMN2)
	
	self.columnProperties = 0
	self.columnValues = 1
		
	
        self.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.verticalHeader().hide()



    def fillControlPropertys(self, typeControl, idControl):
	
	typeControl = str(typeControl)
	idControl = str(idControl)	
		
	#carregar as informações do controlo clicado
	controlInfo = self.monitor.getControlInfo(typeControl, idControl)
		
	#self.addColumn(PROPERTIES_WIDGET_COLUMN1)
	#self.addColumn(PROPERTIES_WIDGET_COLUMN2)
	self.clearProperties()	
	
	currentRow = 0
	if controlInfo.hasProperties():
		for controlProperty in controlInfo.getControlProperties():			
			
			#Verificar se a propriedade é especifica (caso seja não pode ser apresentada na dock Widget)
			try:
				specificTypeProperties.index(controlProperty.getTypeProperty())
				continue
			except ValueError: #caso a propriedade não seja especifica será adicionada à lista na interface		
				self.addRow("")

				#Coluna 1 - NOME DA PROPRIEDADE
				item = QtGui.QTableWidgetItem(controlProperty.getNameProperty())
				item.setFlags(QtCore.Qt.ItemIsEnabled)			
				self.setItem(currentRow, self.columnProperties, item)			
	
				#Coluna 2 - VALOR DA PROPRIEDADE
				typeControl = controlInfo.getTypeControl()
				idControl = controlInfo.getIdControl()
				idProperty = controlProperty.getIdProperty()
				
				#De acordo com o tipo de propriedade, colocar a widget mais indicada na cell			
				if controlProperty.hasOptions():
					cellValue = CComboBoxProperties(idProperty, self)
					for option in controlProperty.getOptions():
						cellValue.addPropertyValue(option)	
					#posicionar na propriedade por defeito
					propertyVal = str(controlProperty.getValueProperty())
					cellValue.setSelectedItem(propertyVal)
				else:
					cellValue = CLineEditProperty(idProperty, controlProperty.getValueProperty(), self, controlProperty.getTypeProperty())
					
				#conectar o sinal de alteração de propriedade da cell com o valor da propriedade
				self.connect(cellValue, QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), self.changePropertyValue)
				
				self.setCellWidget(currentRow, self.columnValues, cellValue)
	
				currentRow +=1
		
		#ordenar a tabela por ordem alfabética na coluna dos nomes das propriedes
		self.sortItems(self.columnProperties, QtCore.Qt.AscendingOrder)

    def clearProperties(self):
	self.removeRows()

    def changePropertyValue(self, idProperty, propertyValue):

	typeControl = str(self.monitor.getTypeSelectedControl())
	idControl = str(self.monitor.getIdSelectedControl())
	idProperty = str(idProperty)
	
	#print typeControl+"-"+idControl+"-"+idProperty
	#print "******"
	#print self.monitor.getControlProperties(typeControl, idControl)
	#print self.monitor.getPropertyControlValue(typeControl, idControl, idProperty)
	self.monitor.changeProperty(typeControl, idControl, idProperty, propertyValue)	
	#print self.monitor.getControlProperties(typeControl, idControl)
	#print self.monitor.getPropertyControlValue(typeControl, idControl, idProperty)
	
	#print idProperty+"-"+propertyValue
	
	
    def cellClicked(self, row, column):
	#seleccionar toda a linha
	self.selectRow(row)
	#if column == self.columnProperties:
	#	self.setCurrentCell(row, self.columnValues)
     
     
    #def cellDoubleClicked(self, row, column):
	
	
	
	#if column == self.columnProperties:
	#	self.setCurrentCell(row, self.columnValues)
     

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
            main_window.control_beeing_added = TButton
        elif event.y() >= 23 and event.y() < 44:
            main_window.control_beeing_added = TCheckBox
        elif event.y() >= 44 and event.y() < 65:
            main_window.control_beeing_added = TCombo
        elif event.y() >= 65 and event.y() < 86:
            main_window.control_beeing_added = TGroupBox
        elif event.y() >= 86 and event.y() < 107:
            main_window.control_beeing_added = TIframe
        elif event.y() >= 107 and event.y() < 128:
            main_window.control_beeing_added = TLabel
        elif event.y() >= 128 and event.y() < 149:
            main_window.control_beeing_added = TList
        elif event.y() >= 149 and event.y() < 170:
            main_window.control_beeing_added = TMenuBar
        elif event.y() >= 170 and event.y() < 191:
            main_window.control_beeing_added = TPasswordField
        elif event.y() >= 191 and event.y() < 212:
            main_window.control_beeing_added = TRadioButton
        elif event.y() >= 212 and event.y() < 233:
            main_window.control_beeing_added = TSpinner
        elif event.y() >= 233 and event.y() < 254:
            main_window.control_beeing_added = TTabView
        elif event.y() >= 254 and event.y() < 275:
            main_window.control_beeing_added = TTable
        elif event.y() >= 275 and event.y() < 296:
            main_window.control_beeing_added = TTextArea
        elif event.y() >= 296 and event.y() < 317:
            main_window.control_beeing_added = TTextField
        elif event.y() >= 317 and event.y() < 338:
            main_window.control_beeing_added = TToolBar
        elif event.y() >= 338 and event.y() < 359:
            main_window.control_beeing_added = TTree

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
	
	self.monitor = CMonitorControls()

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.createDockWindows()
        self.createDrawArea()

	#Conectar o evento de clique na drawArea (para que sejam des-seleccionados todos os controlos) com a remoção das propriedades
	self.connect(self.drawArea, QtCore.SIGNAL(SIGNAL_NONE_CONTROL_SELECTED), self.propertiesWidget.clearProperties)
	self.connect(self.drawArea, QtCore.SIGNAL(SIGNAL_NONE_CONTROL_SELECTED), self.clearControlName)

	#formatar a central Widget
        self.centralWidget = QtGui.QScrollArea()
        self.centralWidget.setBackgroundRole(BACKGROUNDS_COLOR)
	#self.centralWidget.setViewportMargins(MARGIN,MARGIN,MARGIN,MARGIN)
	self.centralWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	self.centralWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)	

	#Widget intermédia entre a scrollBar e a DrawArea
	designWidget = QtGui.QWidget()
	self.centralWidget.setWidget(designWidget)
	designWidget.setGeometry(designWidget.x(), designWidget.y(), DRAW_AREA_WIDTH, DRAW_AREA_HEIGHT)	
	designWidget.setBackgroundRole(BACKGROUNDS_COLOR)
	
	#Colocar a drawArea na zona intermédia (designWidget)	
	self.drawArea.setParent(designWidget)
	#self.drawArea.setGeometry(MARGIN, MARGIN, self.drawArea.width()-(MARGIN*2), self.drawArea.height()-(MARGIN*2))
	self.drawArea.setGeometry(MARGIN, MARGIN, DRAW_AREA_WIDTH-(MARGIN), DRAW_AREA_HEIGHT-(MARGIN*2))
		
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

	#CONTROLS
        self.controlsWidget = ControlsWidget(self.monitor)

        self.intermediateWidget = QtGui.QScrollArea(self)
        self.intermediateWidget.setBackgroundRole(BACKGROUNDS_COLOR)
        self.intermediateWidget.setWidget(self.controlsWidget)

        self.controlsDockWidget = ControlsDockWidget()
        self.controlsDockWidget.setWidget(self.intermediateWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.controlsDockWidget, QtCore.Qt.Vertical)

        
	#PROPERTIES 	
	self.controlInfoWidget = QtGui.QWidget()	
	
	self.controlName = QtGui.QLabel("Control: ")
	self.propertiesWidget = PropertiesWidget(self.monitor)
	
	
	propertiesLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
	propertiesLayout.addWidget(self.controlName)
	propertiesLayout.addWidget(self.propertiesWidget)
	
	self.controlName.setParent(self.controlInfoWidget)
	self.propertiesWidget.setParent(self.controlInfoWidget)
	
	self.controlInfoWidget.setLayout(propertiesLayout) 

        self.propertiesDockWidget = PropertiesDockWidget()
        #self.propertiesDockWidget.setWidget(self.propertiesWidget)
        self.propertiesDockWidget.setWidget(self.controlInfoWidget)
	self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.propertiesDockWidget, QtCore.Qt.Vertical)


    def createDrawArea(self):

        self.drawArea = DrawArea(self.monitor)
	self.drawArea.setAttribute(QtCore.Qt.WA_AcceptDrops)

	QtCore.QObject.connect(self.drawArea, QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), self.propertiesWidget.fillControlPropertys)
	QtCore.QObject.connect(self.drawArea, QtCore.SIGNAL(SIGNAL_CONTROL_CLICKED), self.changeControlName)
    
    def changeControlName(self, typeControl, idControl):
	typeControl = str(typeControl)
	idControl = str(idControl)
	
	#Preencher a label com o nome do controlo	
	self.controlName.setText(CONTROL_LABEL + CONTROLS_DESIGNATIONS[typeControl])
    
    def clearControlName(self):
	self.controlName.setText(CONTROL_LABEL)
    
    
    def newInterfaceAct(self):
	
        return


    def openInterfaceAct(self):
	print self.monitor.DControlsInfo[TList]
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
