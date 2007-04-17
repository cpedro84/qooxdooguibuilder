#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
#from  callProcedure import *
from resizableWidget import *
from string import Template
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *

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
	exec "widget = "+memRefName
	return widget
	
	
	#exec "widget = "+procedure in DparametersValues, globals()
	#return memRefName#???
	#exec "return "+memRefName

def callProcedureResizableProperty(procedure, DparametersValues = { }):	
	#formatedProcedure = formatProcedureCall(procedure)		
	exec procedure in DparametersValues, globals()
	
#**********************************************************



class MonitorControls(QtCore.QObject):
	
	#******************************************************************************
	#**************DEFINIÇÃO DE CONSTANTES**********************************
	#******************************************************************************
		
	#NOMES DOS INDICES DO MAPA DAS PROPRIEDADES DOS CONTROLOS
	PropertyValue = "PropertyValue"
	Property = "Property"
	Options = "Options"
	TypeProperty = "TypeProperty"
	
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
	emptyParamValue = "-"
	
	#POSIÇÕES NO TUPLO (!em forma de mapa!) RELATIVAS ÁS INFORMAÇÔES DOS CONTROLOS
	positionProperties = "PropertiesData"
	positionMemRef = "MemRef"
	
	#OUTPUT DE ERRO
	deletedControl = -1
	error = -1
	errorMethodCall = -1
	errorEmptyMethod = 0
	errorEmptyParamValue = 0
	errorControlMissing = -1
		
		
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
		self.loadPropertiesFromFile(FILE_CONTROLS_PROPERTIES)
		self.loadGlobalProperties(FILE_GLOBAL_PROPERTIES)
			
		
	def haveTypeControls(self, typeControl):
		if self.DControlsInfo.has_key(typeControl) == false:
			return false
		else:
			return true
	
	def haveIdControl(self, typeControl, idControl):
		typeControl = str(typeControl)
		idControl = idControl
		
		if self.haveTypeControls(typeControl) and self.DControlsInfo[typeControl].has_key(idControl) and self.DControlsInfo[typeControl][idControl] != self.deletedControl:
			return true
		else:
			return false
	
	
	
	def getNewIDControl(self, typeControl):

		if self.haveTypeControls(typeControl) == false:				
			return str(0)
		else:				
			try:				
				return self.DControlsInfo[typeControl].values().index(self.deletedControl)			
			except ValueError:
				return str(len(self.DControlsInfo[typeControl].keys()))

	
	def getDefaultProperties(self, typeControl):
		
		if self.DControlDefaultProperties.has_key(typeControl):
			return self.DControlDefaultProperties[typeControl]
		
		return self.error	
		
	
	def getPropertyMethod(self, typeControl, idProperty):
		return self.DPropertiesMethods[typeControl][idProperty]
		
	
	def getDefaultPropertyValue(self, typeControl, idProperty):
		return self.DControlDefaultProperties[typeControl][idProperty][self.PropertyValue]
	
	
	def getNameMemRef(self, typeControl, idControl):
		#verificar se em memória existe o controlo
		
		typeControl = str(typeControl)
		idControl = idControl
		
		if self.haveIdControl(typeControl, idControl):			
			return self.DControlsInfo[typeControl][idControl][self.positionMemRef][self.nameMemRef]
		else:
			return self.errorControlMissing
	
	
	def getControlsFromType(self, TypeControl):
		if self.haveTypeControls(TypeControl) == false:
			return self.error
		return self.DControlsInfo[TypeControl]
	
	def getAllControls(self): #(...)
		print self.DControlsInfo	
		
		
	def generateMemRefWidgetName(self, typeControl, idControl):
		return  self.newControlName+str(typeControl)+str(idControl)
		
	def getTypeProperty(self,  typeControl, idControl, idProperty):
		if  self.haveTypeControls(typeControl) == false:
			return self.error
		
		try:
			return self.Dcontrols[typeControl][idControl][self.positionProperties][self.TypeProperty]
		except:
			return self.error
			
			
	def addNewControl(self, typeControl, parentWidget):
		
		DPropertiesControls = {}
		DPropertiesControls = self.getDefaultProperties(typeControl)
						
		#verificar se existem propriedades default para o controlo a ser adicionado
		if DPropertiesControls == self.error:
			return self.error
		
		#calcular um Id para o control		
		IdControl = self.getNewIDControl(typeControl)
		#adicionar o novo controlo ao mapa
		DControl = { }
		DControl[IdControl] = { self.positionProperties : DPropertiesControls, self.positionMemRef : { } }
		
		#verificar se já existe algum controlo do tipo de dados do controlo a inserir
		if self.haveTypeControls(typeControl) == false:			
			self.DControlsInfo[typeControl] = { }
			
		#********INICIALIZAÇÃO GRÁFICA DO NOVO CONTROLO*********
		#criação do controlo na parentWidget		
		constructorMethod =  self.DResizableInitMethods[typeControl]
		memRefName = self.generateMemRefWidgetName(typeControl, IdControl)		
		params = {self.paramTypeControl : typeControl, self.paramIDResizable : IdControl, self.paramParentResizable : parentWidget }		
			
		#criar ResizableWidget
		widget = callProcedureResizableConstructor(memRefName, constructorMethod, params)		
		#QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		#QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SendResizableSignal)
		#QtCore.QObject.connect(widget, QtCore.SIGNAL("sinal()"), self.SendResizableSignal)
		
		#widget.setVisibility("true")
		#print widget
		#Armazenar no tupo as informações relativas ás referencias em memória da widget criada		
		DControl[IdControl][self.positionMemRef] = {self.nameMemRef : memRefName, self.valueMemRef : widget}
		
		#Armazenar informações sobre o controlo na estrutura
		self.DControlsInfo[typeControl].update(DControl)
		
		#Alteração das propriedades por defeito do controlo criado
		#(...) - o metodo changeProperty vai ser chamado n vezes, onde n é igual ao nº de propriedades a alterar	
		for idProperty in DPropertiesControls.keys():
			#Obter o nome do metodo a ser executado
			#propertyMethod = self.getPropertyMethod(TypeControl, idProperty)
			#Obter o valor a propriedade por defeito 			
			#paramProperty = {self.paramPropertiesResizable : self.getDefaultPropertyValue(TypeControl, idProperty) }
			#Executar o metodo para alteração da propriedade do controlo
			#callProcedureResizableProperty(memRefName+"."+propertyMethod, paramProperty)			
			if self.getTypeProperty(typeControl, IdControl, idProperty) == TDEFAULT: #Só as propriedades do tipo TDEFAULT é que serão inicialmente ser inicializadas
				self.changeProperty(typeControl, IdControl, idProperty, self.getDefaultPropertyValue(typeControl, idProperty))
			
			
		#**********************************************************************************
		
		return widget
	
	
	def delControl(self, TypeControl, IDControl):
				
		if self.haveTypeControls(TypeControl) == false:
			return self.deletedControl
		else:				
			if self.DControlsInfo[TypeControl].has_key(IDControl) == true:
				self.DControlsInfo[TypeControl][IDControl] = self.deletedControl
			return IDControl


	def changeProperty(self, typeControl, idControl, idProperty, value = None):
		if self.haveIdControl(typeControl, idControl) == false:
			return self.error
		else:
			#Alteração da propreidade na estrutura de dados
			self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.PropertyValue] = value
			
			#Executar metodo na classe resizable (...)		
			resizablePropertyMethodCall = self.getPropertyMethod(typeControl, idProperty) #carregar metodo a ser executado
				
			#validar string com o metodo a ser chamado
			if resizablePropertyMethodCall == self.emptyPropertyMethod or len(resizablePropertyMethodCall) == 0:
				return self.errorEmptyMethod
			
			#obter o nome da instancia que referencia a widget Resizable em memória
			widgetName = self.getNameMemRef(typeControl, idControl)			
			if widgetName == self.errorControlMissing:
				return self.errorMethodCall
			
			#Para propriedades do tipo TBOOLEAN é necessário converter o valor (value) para um tipo booleano
			if self.getTypeProperty(typeControl, idControl, idProperty) == TBOOLEAN:
				#transformar o conteudo do valor
				if value == 'false':
					value = false
				elif value == 'true':
					value = true
			#*************************************************************************************
			
			#Construir mapa com os valores dos parametros
			paramProperty = {self.paramPropertiesResizable : value }
			if paramProperty == self.emptyParamValue:
				return self.errorEmptyParamValue
			
			#Antes de executar o metodo é necessário saber qual a referencia ao controlo (....)
			callProcedureResizableProperty(widgetName+"."+resizablePropertyMethodCall, paramProperty)
			
	def disableSelectedResizable(self, typeControl, idControl):
			
		procedureInfo = "disableSelected()"
		widgetName = self.getNameMemRef(str(typeControl), str(idControl))		
		if widgetName == self.errorControlMissing:
				return self.errorMethodCall		
		callProcedureResizableProperty(str(widgetName)+"."+procedureInfo)
	
		
	def loadTypeControlProperties(self, TypeControl, filePath):
		
		try:
			DControlDefaultPropertiesInfo = { }
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
				typeProperty = line[4]
				#Armazenar o metodo de chamada à classe resizable no mapa associativo
				if not self.DPropertiesMethods.has_key(TypeControl):
					self.DPropertiesMethods[TypeControl] = { }
				
				#Armazenar metodo respectivo que é executado na classe Resizable
				self.DPropertiesMethods[TypeControl][IdProperty] = resizablePropertyMethodCall
				
				#Armazenar propriedade no mapa associativo
				DControlDefaultPropertiesInfo[IdProperty] = {self.Property:property, self.PropertyValue:defaultValue, self.Options:options, self.TypeProperty:typeProperty}
				
			return DControlDefaultPropertiesInfo
			
		except IOError:
			print str(ERROR_OPEN_FILE+" File:"+filePath)
		
	
	def loadGlobalProperties(self, filePath):
		
		try:
			DControlDefaultPropertiesInfo = { }
			DPropertiesMethodsInfo = { } 
			fproperties = open(filePath)
			#Ler conteudo do ficheiro
			for line in fproperties:
				line = line.replace('\n', '')	
				line = line.split(':')
				idProperty = line[0]
				property = line[1]				
				options = line[2].split('/')
				defaultValue = options[0]
				resizablePropertyMethodCall = line[3]				
				typeProperty = line[4]
				#Armazenar as caracteristicas globais na estrutura que armazerna as propriedades globais de todos os tipos de controlos				
				DControlDefaultPropertiesInfo[idProperty] = {self.Property:property, self.PropertyValue:defaultValue, self.Options:options, self.TypeProperty:typeProperty}
				
				DPropertiesMethodsInfo[idProperty] = resizablePropertyMethodCall

			#adicionar a todos os controlos as propriedades globais
			for typeControl in self.DControlDefaultProperties.keys():				
				#Armazenar as propreidades Globais
				D = self.DControlDefaultProperties[typeControl]
				D.update(DControlDefaultPropertiesInfo)
		
				#Armazenar os metodos da propriedades globais
				D = self.DPropertiesMethods[typeControl]
				D.update(DPropertiesMethodsInfo)
			
		except IOError:
			str(ERROR_OPEN_FILE+" File:"+filePath)
		
		
	
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
			str(ERROR_OPEN_FILE+" File:"+filePath)
		
	
	#SIGNALS
	"""def SendResizableSignal(self, typeControl, idControl):
		#ENVIO DO SINAL DE CLIQUE PARA INFORMAR O TIPO E O ID DO CONTROLO
		print "teste monitor signal"
		self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), typeControl, idControl)
	"""
	
	
	def SendResizableSignal(self, typeControl, idControl):
		print "valor"
		

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
		
		self.actualTypeControl = ""
		self.actualIdControl = -1
		#widgetRect = self.geometry()
		self.abola = 4
                #childWidget = QtGui.QPushButton(self)
		#childWidget = QtGui.QLabel(self)
		
		#self.resizableBtn = ResizableButton(self)
		self.monitor = MonitorControls()
		widget = self.monitor.addNewControl(TCombo, self)		
		widget.setGeometry(40,40,80,20)
		QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_ITEMS_CHANGED), self.SignalProcess_itemsChanged)
		#QtCore.QObject.connect(self.w, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		
		widget2 = self.monitor.addNewControl(TTabView, self)		
		QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_TABS_CHANGED), self.SignalProcess_itemsChanged)
		
		
		
		#widget2 = self.monitor.addNewControl(TTextField, self)		
		#QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		
		
		"""Btn = QtGui.QPushButton(self)
		Btn.setGeometry(21, 49, 100,30)
		self.connect(Btn, QtCore.SIGNAL("clicked()"), 
					self.info)
		"""
		
	#COLOCAR ESTE SINAL NA PROPRIA CLASSE MONITOR?????
	def SignalProcess_resizableCliked(self, typeControl, idControl):				
		#self.monitor.disableSelectedResizable(typeControl, idControl)		
		typeControl = str(typeControl)
		idControl = idControl
		
		if (self.actualTypeControl == typeControl) and (self.actualIdControl == idControl):
			return
		else:			
			#Armazenar informações do controlo actualmente seleccionado
			self.monitor.disableSelectedResizable(self.actualTypeControl, self.actualIdControl)
			self.actualTypeControl = typeControl
			self.actualIdControl = idControl
	
	def SignalProcess_itemsChanged(self, typeControl, idControl, qtList):
		list = []
		list = QStringListToList(qtList)
		print list
	
	
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
