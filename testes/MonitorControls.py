#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
#from  callProcedure import *
from resizableWidget import *
from string import Template
from PyQt4 import QtCore, QtGui

#****************************************************************************
#***************COLOCAR NOUTRO FICHEIRO*****

def callProcedure(procedureInfo, DparametersValues):
	print procedureInfo
	print DparametersValues
	pieces = procedureInfo.split(';')
	
	#armazenar o nome do procedimento a ser chamado
	methodName = pieces.pop(0)
	
	#Construir string para a execução do procedimento		 
	strCallProcedure = methodName + "("
	for param in pieces:
		strCallProcedure += param+","
	
	strCallProcedure = strCallProcedure[0:len(strCallProcedure)-1]
	
	strCallProcedure += ")" 	
	
	#return strCallProcedure
	exec strCallProcedure in DparametersValues, globals()


def formatProcedureCall(procedure):
	
	pieces = procedureInfo.split(';')
	
	#verificar se o procedimento contém na sua descrição paramentros
	if len(pieces) > 1:
		
		#armazenar o nome do procedimento a ser chamado
		methodName = pieces.pop(0)
		
		#Construir string para a execução do procedimento		 
		strCallProcedure = methodName + "("
		for param in pieces:
			strCallProcedure += param+","
		
		strCallProcedure = strCallProcedure[0:len(strCallProcedure)-1]
		
		strCallProcedure += ")" 
	else:
		strCallProcedure = pieces.pop(0) + "()"
	
	
	return strCallProcedure
	
	
	
def callProcedureResizableConstructor(memRefName, procedure, DparametersValues = { }):
	
	#formatedProcedure = formatProcedureCall(procedure)
	
	exec memRefName+" = "+procedure in DparametersValues, globals()
	#exec "widget = "+procedure in DparametersValues, globals()
	
	#return widget
	#return memRefName#???
	#exec "return "+memRefName

def callProcedureResizableProperty(procedure, DparametersValues = { }):
	
	#formatedProcedure = formatProcedureCall(procedure)		
		
	exec procedure in DparametersValues, globals()
	
#**********************************************************



class MonitorControls:
	
	#******************************************************************************
	#**************DEFINIÇÃO DE CONSTANTES**********************************
	#******************************************************************************
	TButton = "BTN"
	TCheckBox = "CKB"
	TCombo = "CMB"
	TGroupBox = "GRB"
	TIframe = "IFR"
	TLabel = "LBL"
	TList = "LST"
	TMenuBar = "MBR"
	TPasswordField = "PWF"
	TRadioButton = "RDB"
	TSpinner = "SPR"
	TTabView = "TBV"
	TTextArea = "TXV"
	TTextField = "TXF"
	TToolBar = "TLB"
	TTree = "TRE"
	
	#NOMES DOS INDICES DO MAPA DAS PROPRIEDADES DOS CONTROLOS
	PropertyValue = "PropertyValue"
	Property = "Property"
	Options = "Options"
	
	#NOMES DOS INDICES DO MAPA SOBRE AS REFERÊNCIAS PARA MEMÓRIA DOS CONTROLOS
	nameMemRef = "nameMemRef"
	valueMemRef = "valueMemRef"
	
	#NOMES DA PARAMETRIZAÇÃO DOS METODOS RESIZABLE
	paramTypeControl = "typeControl"
	paramIDResizable = "id"
	paramParentResizable = "parent"
	paramPropertiesResizable = "param"
	
	newControlName = "widget"	
	emptyPropertyMethod = "-"
	
	#POSIÇÕES NO TUPLO (!em forma de mapa!) RELATIVAS ÁS INFORMAÇÔES DOS CONTROLOS
	positionProperties = "PropertiesData"
	positionMemRef = "MemRef"
	
	#OUTPUT DE ERRO
	deletedControl = -1
	error = -1
	errorMethodCall = -1
	errorControlMissing = -1
	
	true = bool(1)
	false = bool(0)
	
	#MENSAGENS DE ERRO
	ERROR_OPEN_FILE = "Erro na abertura do ficheiro."	

	#***********************************************************************************
	#***********************************************************************************
	#***********************************************************************************


	def __init__(self):
		#MAPAS PARA GESTÃO DOS DADOS DOS CONTROLOS		
		#Mapa Associativo para armazenamento dos controlos e suas informações
		self.DControlsInfo = { }
		
		
		
		#MAPAS DE CONSULTA DE INFORMAÇÃO
		#Mapa associativo para armazenamento das propriedades dos controlos
		self.DControlDefaultProperties = { }
		#Mapa associativo para armazenamento da correspondencia entre as propriedades de cada tipo de controlo e os metodos das resizable widget
		self.DPropertiesMethods = { }
		#Mapa associativo para armazenamento do nome dos  metodos construtores de cada classe resizable respectiva a cada tipo de controlo
		self.DResizableInitMethods = { }

		#Ler propriedades
		self.loadPropertiesFromFile("ControlsDataTypes.dat")
			
		
	def haveTypeControls(self, TypeControl):
		if self.DControlsInfo.has_key(TypeControl) == self.false:
			return self.false
		else:
			return self.true
	
	def haveIdControl(self, TypeControl, IdControl):
		if self.haveTypeControls(TypeControl) and self.DControlsInfo[TypeControl].has_key(IdControl) and self.DControlsInfo[TypeControl][IdControl] != self.deletedControl:
			return self.true
		else:
			return self.false
	
	
	
	
	def getNewIDControl(self, TypeControl):

		if self.haveTypeControls(TypeControl) == self.false:				
			return 0
		else:				
			try:				
				return self.DControlsInfo[TypeControl].values().index(self.deletedControl)			
			except ValueError:
				return len(self.DControlsInfo[TypeControl].keys())

	
	def getDefaultProperties(self, TypeControl):
		
		if self.DControlDefaultProperties.has_key(TypeControl):
			return self.DControlDefaultProperties[TypeControl]
		
		return self.error	
		
	
	def getPropertyMethod(self, TypeControl, idProperty):
		return self.DPropertiesMethods[TypeControl][idProperty]
		
	
	def getDefaultPropertyValue(self, TypeControl, idProperty):
		return self.DControlDefaultProperties[TypeControl][idProperty][self.PropertyValue]
	
	
	def getNameMemRef(self, typeControl, idControl):
		#verificar se em memória existe o controlo
		if self.haveIdControl(typeControl, idControl):			
			return self.DControlsInfo[typeControl][idControl][self.positionMemRef][self.nameMemRef]
		else:
			return self.errorControlMissing
	
	
	def getControlsFromType(self, TypeControl):
		if self.haveTypeControls(TypeControl) == self.false:
			return self.error
		return self.DControlsInfo[TypeControl]
	
	def getAllControls(self):
		print self.DControlsInfo		
		
	
	
	
	def generateMemRefWidgetName(self, typeControl, idControl):
		return  self.newControlName+str(typeControl)+str(idControl)
	
	def addNewControl(self, TypeControl, parentWidget):
		
		DPropertiesControls = {}
		DPropertiesControls = self.getDefaultProperties(TypeControl)
						
		#verificar se existem propriedades default para o controlo a ser adicionado
		if DPropertiesControls == self.error:
			return self.error
		
		#calcular um Id para o control		
		IdControl = self.getNewIDControl(TypeControl)
		#adicionar o novo controlo ao mapa
		DControl = { }
		DControl[IdControl] = { self.positionProperties : DPropertiesControls, self.positionMemRef : { } }
		
		#verificar se já existe algum controlo do tipo de dados do controlo a inserir
		if self.haveTypeControls(TypeControl) == self.false:			
			self.DControlsInfo[TypeControl] = { }
		
		
		
		#********INICIALIZAÇÃO GRÁFICA DO NOVO CONTROLO*********
		#criação do controlo na parentWidget		
		constructorMethod =  self.DResizableInitMethods[TypeControl]
		memRefName = self.generateMemRefWidgetName(TypeControl, IdControl)		
		params = {self.paramTypeControl : TypeControl, self.paramIDResizable : IdControl, self.paramParentResizable : parentWidget }		
			
		#criar ResizableWidget
		widget = callProcedureResizableConstructor(memRefName, constructorMethod, params)		
		#widget.setVisibility("true")
		#print widget
		#Armazenar no tupo as informações relativas ás referencias em memória da widget criada		
		DControl[IdControl][self.positionMemRef] = {self.nameMemRef : memRefName, self.valueMemRef : widget}
		
		#Armazenar informações sobre o controlo na estrutura
		self.DControlsInfo[TypeControl].update(DControl)
		
		#Alteração das propriedades por defeito do controlo criado
		#(...) - o metodo changeProperty vai ser chamado n vezes, onde n é igual ao nº de propriedades a alterar	
		for idProperty in DPropertiesControls.keys():
			#Obter o nome do metodo a ser executado
			#propertyMethod = self.getPropertyMethod(TypeControl, idProperty)
			#Obter o valor a propriedade por defeito 			
			#paramProperty = {self.paramPropertiesResizable : self.getDefaultPropertyValue(TypeControl, idProperty) }
			#Executar o metodo para alteração da propriedade do controlo
			#callProcedureResizableProperty(memRefName+"."+propertyMethod, paramProperty)
			self.changeProperty(TypeControl, IdControl, idProperty, self.getDefaultPropertyValue(TypeControl, idProperty))
			
			
		#**********************************************************************************
		
		return IdControl
	
	
	def delControl(self, TypeControl, IDControl):
				
		if self.haveTypeControls(TypeControl) == self.false:
			return self.deletedControl
		else:				
			if self.DControlsInfo[TypeControl].has_key(IDControl) == self.true:
				self.DControlsInfo[TypeControl][IDControl] = self.deletedControl
			return IDControl
			

	
		
	def changeProperty(self, typeControl, idControl, idProperty, value):
		if self.haveIdControl(typeControl, idControl) == self.false:
			return error
		else:
			#Alteração da propreidade na estrutura de dados
			self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.PropertyValue] = value
			
			#Executar metodo na classe resizable (...)
			resizablePropertyMethodCall = self.getPropertyMethod(typeControl, idProperty) #carregar metodo a ser executado
			#validar string com o metodo a ser chamado
			if resizablePropertyMethodCall == self.emptyPropertyMethod or len(resizablePropertyMethodCall) == 0:
				return self.errorMethodCall
			
			#obter o nome da instancia que referencia a widget Resizable em memória
			widgetName = self.getNameMemRef(typeControl, idControl)			
			if widgetName == self.errorControlMissing:
				return self.errorMethodCall
			
			#Construir mapa com os valores dos parametros
			paramProperty = {self.paramPropertiesResizable : value }
			
			#Antes de executar o metodo é necessário saber qual a referencia ao controlo (....)
			callProcedureResizableProperty(widgetName+"."+resizablePropertyMethodCall, paramProperty)
			
	
	
	
	def loadTypeControlProperties(self, TypeControl, filePath):
		
		DControlDefaultProperties = { }
		
		try:
			fcontrol=open(filePath)
			#Ler conteudo do ficheiro
			for line in fcontrol:
				line = line.replace('\n', '')	
				line = line.split(':')		
				IdProperty = line[0]
				property = line[1]				
				options = line[2].split('/')
				defaultValue = options[0]
				resizablePropertyMethodCall = line[3]
				#Armazenar o metodo de chamada à classe resizable no mapa associativo
				if not self.DPropertiesMethods.has_key(TypeControl):
					self.DPropertiesMethods[TypeControl] = { }
				
				self.DPropertiesMethods[TypeControl][IdProperty] = resizablePropertyMethodCall
								
				#Armazenar propriedade no mapa associativo
				DControlDefaultProperties[IdProperty] = {self.Property:property, self.PropertyValue:defaultValue, self.Options:options}
				
			return DControlDefaultProperties		
			
		except IOError:
			print str(self.ERROR_OPEN_FILE+" File:"+filePath)
		
	
	def loadPropertiesFromFile(self, filePath):
		#Abrir ficheiro com a indicação de todos os controlos		
		try:
			fcontrols=open(filePath)
			#Ler conteudo do ficheiro
			for line in fcontrols:
				line = line.replace('\n', '')	
				line = line.split(':')		
				typeControl = line[0]
				filePathTypeControl = line[1]
				
				#Ler metodo constructor para a criação das resizable
				resizableContructorCall = line[2]
				#Associação do metodo ao mapa associativo
				self.DResizableInitMethods[typeControl] = resizableContructorCall
				
				#Ler Propriedades do actual tipo de controlo 
				DControlDefaultProperties = self.loadTypeControlProperties(typeControl, filePathTypeControl)
				#Associar ao mapa das caracteristicas dos controlos, as informações sobre as descrições (em forma de mapa associativo)
				self.DControlDefaultProperties[typeControl] = DControlDefaultProperties				
		
		except IOError:
			str(self.ERROR_OPEN_FILE+" File:"+filePath)




#***********************************************************************************************************
#***********************************************************************************************************

"""	
monitor = MonitorControls()
id0 = monitor.addNewControl(MonitorControls.TTextField, 0)
id1 = monitor.addNewControl(MonitorControls.TTextField, 0)
id2 = monitor.addNewControl(MonitorControls.TTextField, 0)
id3 = monitor.addNewControl(MonitorControls.TTextField, 0)
#print monitor.getControlsFromType(MonitorControls.TTextField)
#print monitor.getAllControls()
monitor.delControl(MonitorControls.TTextField, id2)
monitor.delControl(MonitorControls.TTextField, id3)
#id4 = monitor.addNewControl(MonitorControls.TTextField)
#print id4
#id5 = monitor.addNewControl(MonitorControls.TTextField)

print monitor.getControlsFromType(MonitorControls.TTextField)

print monitor.DPropertiesMethods
"""


#-------------------------------------------------------------------------------------
class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		#widgetRect = self.geometry()

                #childWidget = QtGui.QPushButton(self)
		#childWidget = QtGui.QLabel(self)
		
		#self.resizableBtn = ResizableButton(self)
		monitor = MonitorControls()
		id0 = monitor.addNewControl(MonitorControls.TTextField, self)		
		
		QtCore.QObject.connect(monitor, QtCore.SIGNAL("PySig"), self.SignalReceive)

		
		Btn = QtGui.QPushButton(self)
		Btn.setGeometry(21, 49, 100,30)
		self.connect(Btn, QtCore.SIGNAL("clicked()"), 
					self.info)
		
	def SignalReceive(self):
		print "sinal recebido da resizable"
	
	def info(self):
		#self.w.setAutoFillBackground(bool(1))
		
		self.w.setText("teste")				
		self.w.setWindowColor(QtGui.QColor(QtCore.Qt.blue))
		self.w.setTextColor(QtGui.QColor(QtCore.Qt.green))
		#print(self.resizableWidget.getWidth())
		#self.w.addItem("teste")
		#self.w.setAlignLeft()
		#print(self.w.isChecked())
			
	
#-------------------------------------------------------------------------------------

#main 
app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())
