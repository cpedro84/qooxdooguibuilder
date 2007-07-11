#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from importResizables import *
from string import Template
from string import lower
import copy

from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from tableData import *
from ControlInfo import *

#****************************************************************************
#***************COLOCAR NOUTRO FICHEIRO*****

def callProcedure(procedureInfo, DparametersValues):
	#print procedureInfo
	#print DparametersValues
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
	
	
#*********************************************************************************************************	
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
	
#*********************************************************************************************************


## Documentation for CMonitorControls.
#
# Monotorize, manage and maintain the interactions with the resizableWidgets,
# where is possible to create (@see addNewControl), delete (@see deleteControl) resizable Widgets, 
# change properties (@see changeProperties) and some more actions related with.
class CMonitorControls(QtCore.QObject):
	
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
	
	#POSIÇÕES SOBRE O CONTROLO SELECCIONADO
	positionTypeControl = "TypeControl"
	positionIdControl = "IdControl"
	noneSelected = -1
	
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
	
	## The constructor.
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
		self.DResizableInitMethods = {  }
		
		#Ler propriedades
		self.loadPropertiesFromFile(DIR_CONTROLS_DATA+FILE_CONTROLS_PROPERTIES)
		self.loadGlobalProperties(DIR_CONTROLS_DATA+FILE_GLOBAL_PROPERTIES)
		
		#controlo de selecção de resizables ´(irá conter a indicação do ultimo controlo seleccionado)
		self.controlSelected = { self.positionTypeControl : self.noneSelected ,  self.positionIdControl : self.noneSelected }
		#Lista com a informação dos controlos seleccionados
		self.LControlsSelected = [ ]
		
		self.lastIdControl = self.noneSelected
	
	##
	# Load type control's properties from the given filePath.
	# If some problem occured an error will be printed.
	#
	# @Param typeControl string
	# @Param filePath string
	#
	# @return python Dict with the properties
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
		
	
	##
	# Load global properties for all controls type, from the given filePath into memory structures.
	# If some problem occured an error will be printed.
	#
	# @Param filePath string
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
		
		
	##
	# Load all specific properties for all types of controls, from the given filePath, into memory structures.
	# If some problem occured an error will be printed.
	#
	# @Param filePath string
	def loadPropertiesFromFile(self, filePath):
		#Abrir ficheiro com a indicação de todos os controlos		
		
		try:
			fcontrols=open(filePath)
			#Ler conteudo do ficheiro
			for line in fcontrols:
				line = line.replace('\n', '')	
				line = line.split(':')		
				typeControl = line[0]
				filePathTypeControl = DIR_CONTROLS_DATA+line[1]
				
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


	##
	# Calculates a new Id for a new typeControl. 
	#
	# @Param typeControl string
	#
	# @return idControl string	
	def generateNewIDControl(self, typeControl):

		if self.haveTypeControls(typeControl) == false:				
			return str(0)
		else:				
			#return str(len(self.DControlsInfo[typeControl].keys()))
			try:					
				return self.DControlsInfo[typeControl].keys().index(self.deletedControl)			
			except ValueError:
				return str(len(self.DControlsInfo[typeControl].keys()))
			
			
			
			"""#Verificar se existe algum id disponivel entre os valores já criados
			if indexValue(self.DControlsInfo[typeControl].values())
			
			
			nElements = len(self.DControlsInfo[typeControl].keys()) 
			while itr < nElements:
				try:
					print itr
					self.DControlsInfo[typeControl].values().index(itr)
				except ValueError:
					return itr
				
				itr +=1
				
			#caso não tenha encontrado nenhuma posição vaga então é criado um novo id
			return nElements 
			"""


	##
	# A new instance of typeControls is created and maintained in internal structure. The controls properties is formated by default properties values.
	# The reference of the new control is returned.
	#
	# @Param typeControl string
	# @Param parentWidget QWidget
	#
	# @return memory reference
	def addNewControl(self, typeControl, parentWidget, controlProperties = None, applySelectEffect = true):
		
		#DPropertiesControls = {}
		DPropertiesControls = copy.deepcopy(self.getDefaultProperties(typeControl))
						
		#verificar se existem propriedades default para o controlo a ser adicionado
		if DPropertiesControls == self.error:			
			return self.error
		
		#calcular um Id para o control		
		IdControl = self.generateNewIDControl(typeControl)
		
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
		
		#QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		#QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		#QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SendResizableSignal)
		#QtCore.QObject.connect(widget, QtCore.SIGNAL("sinal()"), self.SendResizableSignal)
		
		#widget.setVisibility("true")
		#print widget
		#Armazenar no tupo as informações relativas ás referencias em memória da widget criada		
		DControl[IdControl][self.positionMemRef] = {self.nameMemRef : memRefName, self.valueMemRef : widget}
		
		#Armazenar informações sobre o controlo na estrutura
		self.DControlsInfo[typeControl].update(DControl)
		
		#verificar se existem propriedades para atribuir ao novo controlo criado
		if controlProperties == None: #serão atribuidas as propriedades por defeito
			self.assignDefaultProperties(typeControl, IdControl, DPropertiesControls)
		else: #serão atribuidas as propriedades referênciadas por parametro
			self.assignProperties(widget, typeControl, IdControl, controlProperties)
	
		
		if applySelectEffect:
			#seleccionar a Resizable criada
			self.setSelectedControl(typeControl, IdControl)
		
		#Armazenar o último IdControl
		self.lastIdControl = IdControl
		
		return widget
	
	
	##
	# The control identified by typeControl and idControl is deleted from the maintain monitor system.
	# The control's Id is returned if the delete operation was correctly performed.
	# If the control don't exist in the monitor system, the will be returned -1. 
	#
	# @Param typeControl string
	# @Param parentWidget QWidget
	#
	# @return string
	def deleteControl(self, typeControl, idControl):
		
		typeControl = str(typeControl)
		idControl = str(idControl)		
		
		if self.haveTypeControls(typeControl) == false:
			return self.deletedControl
		else:				
			if self.DControlsInfo[typeControl].has_key(idControl) == true:
				
				#obter o nome da instancia que referencia a widget Resizable em memória
				widgetName = self.getValueMemRef(str(typeControl), str(idControl))
				if widgetName <> self.errorControlMissing:					
					widgetName.setParent(QtGui.QWidget())
					del widgetName 
				
				self.DControlsInfo[typeControl][idControl] = self.deletedControl
				#del self.DControlsInfo[typeControl][idControl] 
			return idControl
	
	
	def deleteSelectedControls(self):
		
		for infoControl in self.getSelectedControls():
			typeControl = infoControl[self.positionTypeControl]
			idControl = infoControl[self.positionIdControl]
			
			self.deleteControl(typeControl, idControl)
			
		
	
	def deleteAllControls(self):
		
		#Eliminar todas as referências de memória dos controlos
		for typeControl in self.DControlsInfo.keys():
			for idControl in self.DControlsInfo[typeControl].keys():
				self.deleteControl(typeControl, idControl)
		
		# Limpar a estrutura com os dados dos controlos
		self.DControlsInfo.clear()
	
	
	

	##
	# Assign to a control, identified with tge given typeControl and idControl, the default properties
	#if a problem occured -1 will be returned
	#
	# @Param typeControl string
	# @Param idControl string	
	def assignDefaultProperties(self, typeControl, idControl, controlDefaultProperties):
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		if self.haveIdControl(typeControl, idControl) == false:
			return self.error
		
		#Alteração das propriedades por defeito do controlo criado
		#(...) - o metodo changeProperty vai ser chamado n vezes, onde n é igual ao nº de propriedades a alterar	
		for idProperty in controlDefaultProperties.keys():
			#Obter o nome do metodo a ser executado
			#propertyMethod = self.getPropertyMethod(TypeControl, idProperty)
			#Obter o valor a propriedade por defeito 			
			#paramProperty = {self.paramPropertiesResizable : self.getDefaultPropertyValue(TypeControl, idProperty) }
			#Executar o metodo para alteração da propriedade do controlo
			#callProcedureResizableProperty(memRefName+"."+propertyMethod, paramProperty)			
			typeProperty = self.getTypeProperty(typeControl, idProperty)
			
			if typeProperty == TINT or typeProperty == TBOOLEAN or typeProperty == TSTRING or typeProperty == TALIGN:
				self.changeProperty(typeControl, idControl, idProperty, self.getDefaultPropertyValue(typeControl, idProperty))
		#**********************************************************************************
	
	
	# controlProperties - list of CControlProperty
	def assignProperties(self, controlWidgetReference, typeControl, idControl, controlProperties):
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		if self.haveIdControl(typeControl, idControl) == false:
			return self.error
			
		
		for property in controlProperties:
			idProperty = property.getIdProperty()				
			typeProperty = self.getTypeProperty(typeControl, idProperty)
			valueProperty = property.getValueProperty()
			if typeProperty == TINT or typeProperty == TBOOLEAN or typeProperty == TSTRING or typeProperty == TALIGN:
				self.changeProperty(typeControl, idControl, idProperty, valueProperty)			
			elif typeProperty == TITEMS and valueProperty <> self.emptyParamValue:
				self.changeProperty(typeControl, idControl, idProperty, valueProperty)
				#Acrescentar Items ao controlo
				listItems = []
				for itemText in valueProperty:					
					listItems.append(CEditItem(itemText))
				controlWidgetReference.setItems(listItems)
			
			elif typeProperty == TMENUS and valueProperty <> self.emptyParamValue:
				self.changeProperty(typeControl, idControl, idProperty, valueProperty)
				#Acrescentar Items ao controlo
				listMenus = []
				for itemText in valueProperty:					
					listMenus.append(CEditItem(itemText))
				controlWidgetReference.setMenus(listMenus)
			
			elif typeProperty == TTABS and valueProperty <> self.emptyParamValue:
				self.changeProperty(typeControl, idControl, idProperty, valueProperty)
				#Acrescentar Items ao controlo
				listItems = []
				for itemText in valueProperty:					
					listItems.append(CEditItem(itemText, QtGui.QWidget()))
					controlWidgetReference.setTabs(listItems)

			elif typeProperty == TTABLEITEMS and valueProperty <> self.emptyParamValue:
				self.changeProperty(typeControl, idControl, idProperty, valueProperty)
				
				#Construir TableData para preencher a tabela
				
				columns = valueProperty.keys()
				rows = []
				for column in valueProperty.keys():
					rows = valueProperty[column].keys()
					break
				
				tableData = CTableData()				
				tableData.setTableColumns(columns) 
				tableData.setTableRows(rows) 
				tableData.setTableItems(valueProperty) 
				controlWidgetReference.setTable(tableData)

	##
	# Set a value property for be used in the resizable methods. This is a method used internaly inthe class.
	# The formated value is returned
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param idProperty string
	# @Param value string
	#
	# @return valueFormated string	
	def setValueProperty(self, typeControl, idControl, idProperty, value):
		typeControl = str(typeControl)
		idControl = str(idControl)
		idProperty = str(idProperty)
		
		#Para propriedades do tipo TBOOLEAN é necessário converter o valor (value) para um tipo booleano
		typeProperty = self.getTypeProperty(typeControl, idProperty)
		if typeProperty == TBOOLEAN:
			#transformar o conteudo do valor
			if value == 'false':
				value = false
			elif value == 'true':
				value = true
		

		return value

	##
	# Change a property value in tha maintain system and their layout for a given value property of a typeControl.
	#If the property value wasn't changed, then -1 is returned.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param idProperty string
	# @Param value string
	#
	# @return -1 if a problem occured
	def changeProperty(self, typeControl, idControl, idProperty, value = None):
		
		if self.haveIdControl(typeControl, idControl) == false:
			return self.error
		else:
			#Alteração da propreidade na estrutura de dados
			self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.PropertyValue] = value
			
			#carregar o metodo a ser chamado na resizable para efectuar a alteração visual
			resizablePropertyMethodCall = self.getPropertyMethod(typeControl, idProperty) #carregar metodo a ser executado
	
			#validar string com o metodo a ser chamado
			if resizablePropertyMethodCall == self.emptyPropertyMethod or len(resizablePropertyMethodCall) == 0:
				return self.errorEmptyMethod
			
			#obter o nome da instancia que referencia a widget Resizable em memória
			widgetName = self.getNameMemRef(typeControl, idControl)			
			if widgetName == self.errorControlMissing:
				return self.errorMethodCall
			
			
			value = self.setValueProperty(typeControl, idControl, idProperty, value)			
			#*************************************************************************************
			
			#Construir mapa com os valores dos parametros
			paramProperty = {self.paramPropertiesResizable : value }
			#if paramProperty == self.emptyParamValue:
			if value == self.emptyParamValue:
				return self.errorEmptyParamValue

			#Antes de executar o metodo é necessário saber qual a referencia ao controlo
			callProcedureResizableProperty(widgetName+"."+resizablePropertyMethodCall, paramProperty)
	
	
	## Special method for Controls with Items related properties.
	# Save the items values (listItems) for a control with Item property related, idendified with the given typeControl, idControl.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param listItems python List	
	def changeItemsProperties(self, typeControl, idControl, listItems):
		typeControl = str(typeControl)
		idControl = str(idControl)
	
		idPropertyItems = self.getIdItemsProperty(typeControl, idControl)
		print idPropertyItems	
		#caso tenha sido encontrada a propriedade de Items
		if idPropertyItems <> -1:
			#???????????transformar todos os items editItem em texto ?????????????
			list = []			
			for item in listItems:
				print item.getText()
				list.append(item.getText())
			#****************************************************
			#pickleList = serializeObject(listItems)
			
			#armazenar a lista de items	- Para estes controlos não existe nunhum metodo associado à resizable para a adição de items
			self.changeProperty(typeControl, idControl, idPropertyItems, list)
		
	
	## Special method for Controls with Menus related properties.
	# Save the Menus values (listMenus) for a control with Menus property related, idendified with the given typeControl, idControl.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param listMenus python List
	def changeMenusProperties(self, typeControl, idControl, listMenus):
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		self.changeItemsProperties(typeControl, idControl, listMenus)
	
	
	
	## Special method for Controls with Tabs related properties.
	# Save the Tabs values (listItems) for a control with Tabs property related, idendified with the given typeControl, idControl.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param listTabs python List
	def changeTabsProperties(self, typeControl, idControl, listTabs):
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		self.changeItemsProperties(typeControl, idControl, listTabs)
	
	
	## Special method for Controls with TableItens related properties.
	# Save the TableItems values for a control with TableItems property related, idendified with the given typeControl, idControl.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param listTabs python List
	def changeTableItemsProperties(self, typeControl, idControl, tableItems):		
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		idPropertyItems = self.getIdItemsProperty(typeControl, idControl)
		
		#caso tenha sido encontrada a propriedade de Items
		if idPropertyItems <> -1:			
			#armazenar a lista de items			
			self.changeProperty(typeControl, idControl, idPropertyItems, tableItems)
	
	
	
	##
	# Disable the selected efect of the current selected control, identified with typeControl and idControl.
	# If some problem occurred -1 will be returned.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return -1 
	def disableSelectedControl(self, typeControl, idControl):
			
		procedureInfo = METHOD_DISABLE_SELECTION		
		widgetName = self.getNameMemRef(str(typeControl), str(idControl))		
		if widgetName == self.errorControlMissing:				
				return self.errorMethodCall		
		callProcedureResizableProperty(str(widgetName)+"."+procedureInfo)
	
	
	##
	# Disable the efect of all seleted controls.	
	def disableAllSelectedControls(self):
		
		for control in self.LControlsSelected:			
			self.disableSelectedControl(str(control[self.positionTypeControl]), str(control[self.positionIdControl]))			
		
		#eliminar da lista o controlo
		self.LControlsSelected = []
		#eliminar a indicação de controlo seleccionado actual
		self.controlSelected[self.positionTypeControl] = self.noneSelected
		self.controlSelected[self.positionIdControl] = self.noneSelected
		
		
	##
	# Clear the state of selected control. None selected state will be set.
	def clearIndicationSeletedControl(self):
		self.controlSelected[self.positionTypeControl] = self.noneSelected
		self.controlSelected[self.positionIdControl] = self.noneSelected
	
	
	##
	# Set a new control to be selected. The new control is identified with typeControl and idControl.
	# If unSelectedOtherControls is true, then other seleted controls will be deselecte. Otherwise maintain the selected effect.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param unSelectedOtherControls boolean	
	def setSelectedControl(self, typeControl, idControl, unSelectedOtherControls = true):
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		#caso o controlo já seleccionado seja igual ao que se pretende seleccionar então não será processada a selecção
		if self.controlSelected[self.positionTypeControl] == typeControl and self.controlSelected[self.positionIdControl] == idControl:			
			return
		
		#des-seleccionar os restantes controlos
		if unSelectedOtherControls:
			#retirar  o rebordo de selecção a todos os controlos que estiverem seleccionados
			self.disableAllSelectedControls()
			"""for control in self.LControlsSelected:
				self.disableSelectedControl(control[self.positionTypeControl], control[self.positionIdControl])
				#eliminar da lista o controlo
				self.LControlsSelected.remove(control)
			"""			
			
		self.controlSelected[self.positionTypeControl] = str(typeControl)
		self.controlSelected[self.positionIdControl] = str(idControl)
		
		#Adicionar o controlo seleccionado à lista
		self.LControlsSelected.append(copy.deepcopy(self.controlSelected))
		
		#Alterar interface da resizableWidget de forma a parecer seleccionada
		self.getValueMemRef(str(typeControl), str(idControl)).enableSelected()
	
	##
	# The controls in the given intersection will be put a selection effect on.
	#
	# @Param intersection QRect(QT class)	
	def setSelectedControlsIntersection(self, intersection):
		LWidgetsRects = []
		LWidgetsRects = self.getResizableWidgetsRects()
		
		nControlsSelected = 0
		typeControlSel = -1
		idControlSel = -1
		
		for widgetInfo in LWidgetsRects:			
			typeControl = str(widgetInfo[0])
			idControl = str(widgetInfo[1])
			widgetRect = widgetInfo[2]
			
			if intersection.intersects(widgetRect):				
				self.setSelectedControl(str(typeControl), str(idControl), false)
				nControlsSelected +=1
				
		if nControlsSelected > 1:
			self.clearIndicationSeletedControl()			
		elif nControlsSelected  == 1 and typeControlSel <> -1 and idControlSel <> -1:
			self.setSelectedControl(typeControlSel, idControlSel)
	
	
	
	
	
	##
	# Check if a control property, identidied with typeControl, idControl and idProperty, is a multi-property.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param idProperty string
	#
	# @return boolean
	def isMultiProperty(self, typeControl, idControl, idProperty):
		property = self.getTypeProperty(typeControl, idProperty)
		
		if property <> self.error:
			try:
				multiPropretyValues.index(property)
				return true
			except ValueError:
				return false
		else:
			return false

	
	

	##
	# Check if already exists, on memory, a control with the given typeControl.
	#
	# @Param typeControl string
	#
	# @return boolean
	def haveTypeControls(self, typeControl):
		if self.DControlsInfo.has_key(typeControl) == false:
			return false
		else:
			return true
	
	
	##
	# Check if already exists on memory a control with the given typeControl an idControl.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return boolean
	def haveIdControl(self, typeControl, idControl):
		typeControl = str(typeControl)
		idControl = idControl
		
		if self.haveTypeControls(typeControl) and self.DControlsInfo[typeControl].has_key(idControl) and self.DControlsInfo[typeControl][idControl] != self.deletedControl:
			return true
		else:
			return false
	
	
	##
	# Generate a memory name reference for a resizableWidget, identified with the given typeControl and idControl
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return memoryReference string	
	def generateMemRefWidgetName(self, typeControl, idControl):
		return  self.newControlName+str(typeControl)+str(idControl)
	
	

	def getLastIdControl(self):
		return self.lastIdControl

	##
	# Returns the default properties from a given typeControl. If no default properties is found then is returned -1.
	#
	# @Param typeControl string
	#
	# @return python dict type  
	def getDefaultProperties(self, typeControl):		
		if self.DControlDefaultProperties.has_key(typeControl):
			mapProperties = copy.deepcopy(self.DControlDefaultProperties[typeControl])
			return mapProperties
		
		return self.error	

	##
	# Returns the default property value from a given typeControl and idProperty.
	#
	# @Param typeControl string
	# @Param idProperty string
	#
	# @return value string
	def getDefaultPropertyValue(self, typeControl, idProperty):
		return self.DControlDefaultProperties[typeControl][idProperty][self.PropertyValue]
	
	
	##
	# Returns the property value from a given typeControl and idProperty. If no property value is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idProperty string
	#
	# @return value string
	def getPropertyControlValue(self, typeControl, idControl, idProperty):
		if self.haveIdControl(typeControl, idControl):
			return self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.PropertyValue]
		else:
			return self.errorControlMissing
	
	##
	# Returns the method name related with a property of a typeControl. 
	# This method belongs to the resizableWidget that represents the typeControl.
	#
	# @Param typeControl string
	# @Param idProperty string
	#
	# @return methodName string	
	def getPropertyMethod(self, typeControl, idProperty):
		return self.DPropertiesMethods[typeControl][idProperty]
	
	
	
	##
	# Returns the property name related with a property of a typeControl. If no property name is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param idProperty string
	#
	# @return propertyName string
	def getPropertyControlName(self, typeControl, idControl, idProperty):
		if self.haveIdControl(typeControl, idControl):
			return self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.Property]
		else:
			return self.errorControlMissing
	
	
	##
	# Returns control properties from a given typeControl and idControl. If no control properties is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return python dict type
	def getControlProperties(self, typeControl, idControl):
			
		if self.haveIdControl(typeControl, idControl):
			return  copy.copy(self.DControlsInfo[typeControl][idControl][self.positionProperties])
			#return  copy.deepcopy(self.DControlsInfo[typeControl][idControl][self.positionProperties])
		else:
			return self.errorControlMissing
	
	
	## Special method for Controls with Items related properties.
	# Returns the idProperty value from a control type with Item property related.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return idProperty string
	def getIdItemsProperty(self, typeControl, idControl):
		typeControl = str(typeControl)
		idControl = str(idControl)
	
		idPropertyItems = -1
	
		#carregar as informações do controlo
		controlInfo = self.getControlInfo(typeControl, idControl)
		
		#Verificar qual a propriedade de Items
		if controlInfo.hasProperties():
			for controlProperty in controlInfo.getControlProperties():
				"""if controlProperty.getTypeProperty() == TITEMS 
					or controlProperty.getTypeProperty() == TMENUS
					or controlProperty.getTypeProperty() ==  TTABS 
					or controlProperty.getTypeProperty() ==  TTABLEITEMS:
				"""
				if indexValue(specificTypeProperties, controlProperty.getTypeProperty()):
					
					idPropertyItems = controlProperty.getIdProperty()
					break
		
		return idPropertyItems
	
	
	
	##
	# Returns the related information from Control identified with the given typeControl and idControl.
	#
	# @Param typeControl string
	# @Param idControl string	
	#
	# @return CControlInfo
	# @see CControlInfo
	def getControlInfo(self, typeControl, idControl):
		
		typeControl = str(typeControl)
		idControl = str(idControl)
		
		controlInfo = CControlInfo(typeControl, idControl)
		#carregar as propriedades para o objecto
		propertiesList = { }		
		propertiesList = self.getControlProperties(typeControl, idControl)		
		
		#print typeControl+"-"+idControl
		#print propertiesList
		
		if propertiesList <> self.errorControlMissing: #verificar se as propeidades existem
			for idProperty in propertiesList.keys():
				
				nameProperty = propertiesList[idProperty][self.Property]
				valueProperty = propertiesList[idProperty][self.PropertyValue]
				typeProperty = propertiesList[idProperty][self.TypeProperty]
				options = propertiesList[idProperty][self.Options]
				controlProperty = CControlProperty(idProperty, nameProperty, valueProperty, typeProperty)
				controlProperty.setOptions(options)

				controlInfo.addControlProperty(controlProperty)
				
		return controlInfo
	
	
	##
	# Returns the related information from all Control.
	#
	# @return list of CControlInfo
	# @see CControlInfo
	def getControlsInfo(self):
		
		controlsInfoList = []
		
		for typeControl in self.DControlsInfo.keys():			
			for idControl in self.DControlsInfo[typeControl]:
				if self.DControlsInfo[typeControl][idControl] <> self.deletedControl: #verificar se o controlo não está referênciado como apagado
					controlsInfoList.append(self.getControlInfo(typeControl, idControl))
		
		return controlsInfoList
	
	##
	# Returns the name in memory that makes reference to the Control identified with the given typeControl and idControl.
	# If no name reference is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return name memory reference
	def getNameMemRef(self, typeControl, idControl):
		#verificar se em memória existe o controlo		
		typeControl = str(typeControl)
		idControl = idControl
		
		if self.haveIdControl(typeControl, idControl):			
			return self.DControlsInfo[typeControl][idControl][self.positionMemRef][self.nameMemRef]
		else:
			return self.errorControlMissing
	
	##
	# Returns the value reference in momory that makes reference to the Control identified with the given typeControl and idControl.
	# If no value reference is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idControl string
	#
	# @return value memory reference
	def getValueMemRef(self, typeControl, idControl):
		#verificar se em memória existe o controlo		
		typeControl = str(typeControl)
		idControl = idControl
		
		if self.haveIdControl(typeControl, idControl):			
			return self.DControlsInfo[typeControl][idControl][self.positionMemRef][self.valueMemRef]
		else:
			return self.errorControlMissing
	
	"""
	##
	# Returns all the values references in momory that makes reference to all Controls.
	# If no value reference is found then is returned -1.
	#
	#
	# @return python List
	def getValuesMemRef(self):
		controlsMenRefList = []
		
		for typeControl in self.DControlsInfo.keys():			
			for idControl in self.DControlsInfo[typeControl]:
				if self.DControlsInfo[typeControl][idControl] <> self.deletedControl: #verificar se o controlo não está referênciado como apagado
					widgetItem = QtGui.QWidgetItem(self.DControlsInfo[typeControl][idControl][self.positionMemRef][self.valueMemRef])
					controlsMenRefList.append(widgetItem.widget())
	
		return controlsMenRefList
	"""
	
	##
	# Returns all the controls information from a given typeControl. If no controls is found then is returned -1.
	#
	# @Param typeControl string	
	#
	# @return python Dict
	def getControlsFromType(self, typeControl):
		if self.haveTypeControls(typeControl) == false:
			return self.error
		return copy.deepcopy(self.DControlsInfo[typeControl])
	
		
	#def getAllControls(self): #(...)
	#	print self.DControlsInfo	
		
		
	##
	# Returns the property type from a given typeControl, idControl and idProperty. If no property type is found then is returned -1.
	#
	# @Param typeControl string
	# @Param idControl string
	# @Param idProperty string
	#
	# @return typeProperty string
	def getTypeProperty(self,  typeControl, idProperty):
		typeControl = str(typeControl)		
		idProperty = str(idProperty)
		
		"""
		if  self.haveTypeControls(typeControl) == false:
			return self.error
			
		try:			
			#return self.DControlsInfo[typeControl][idControl][self.positionProperties][self.TypeProperty]
			return self.DControlsInfo[typeControl][idControl][self.positionProperties][idProperty][self.TypeProperty]
		except:
			return self.error
		"""
		
		try:
			return self.DControlDefaultProperties[typeControl][idProperty][self.TypeProperty]
		except:
			return self.error
	
		
	
	#SIGNALS
	"""def SendResizableSignal(self, typeControl, idControl):
		#ENVIO DO SINAL DE CLIQUE PARA INFORMAR O TIPO E O ID DO CONTROLO
		print "teste monitor signal"
		self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), typeControl, idControl)
	"""
		
	##
	# Return the type of the selected control.
	#
	# @return string
	def getTypeSelectedControl(self):
		return self.controlSelected[self.positionTypeControl]
	
	
	
	##
	# Returns the Id of the selected control.
	# Ifnone control is selected -1 will be returned.
	#
	# @Param string
	def getIdSelectedControl(self):
		return self.controlSelected[self.positionIdControl]
	
	##
	# Returns a list with the sizes (QRect) of all widgets saved in the structures.
	#
	# @Param python list
	def getResizableWidgetsRects(self):
		
		LWidgetsRects = []
		
		for typeControl in self.DControlsInfo:
			for idControl in self.DControlsInfo[typeControl]:
				widgetName = self.getValueMemRef(str(typeControl), str(idControl))
				if widgetName == self.errorControlMissing:
					continue
				widgetRect = QtCore.QRect(widgetName.geometry())				
				#exec "widgetRect = QtGui.QWidget("+widgetName+").geometry()"
				dataTuple = str(typeControl), str(idControl), widgetRect
				LWidgetsRects.append(dataTuple)
		
		return LWidgetsRects


	##
	# Returns a list with the information about all selected controls.
	#
	# @Param python list
	def getSelectedControls(self):		
		return self.LControlsSelected

	
	
	
	def getControlsDataHTMLGenerator(self):
		LControlsInfo = self.getControlsInfo()
		
		MapHTMLGenerator = {}
		controlKey = ""
		designControl = ""
		for controlInfo in LControlsInfo:
			designControl = getTypeControlDesignation(controlInfo.getTypeControl())
			controlKey = lower(designControl)+""+controlInfo.getIdControl()
			MapHTMLGenerator[controlKey] = {}
			#Definir primeiro elemento: Tipo de controlo
			MapHTMLGenerator[controlKey].update({"Type": designControl})
			#Definir as propriedades dos controlos
			for controlProperty in controlInfo.getControlProperties():
				if controlProperty.getValueProperty() <> "-":
					MapHTMLGenerator[controlKey].update({controlProperty.getNameProperty():controlProperty.getValueProperty() })
		

		return MapHTMLGenerator

	
	
		
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
		widget = self.monitor.addNewControl(TTable, self)
		widget.setGeometry(40,40,80,20)
		QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		QtCore.QObject.connect(widget, QtCore.SIGNAL(SIGNAL_RESIZABLE_TABLE_CHANGED), self.SignalProcess_tableChanged)
		#QtCore.QObject.connect(self.w, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		
		#widget2 = self.monitor.addNewControl(TTabView, self)		
		#QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalProcess_resizableCliked)
		#QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_TABS_CHANGED), self.SignalProcess_itemsChanged)
		
		
		
		#widget2 = self.monitor.addNewControl(TTextField, self)		
		#QtCore.QObject.connect(widget2, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		
		
		Btn = QtGui.QPushButton(self)
		Btn.setGeometry(21, 49, 100,30)
		self.connect(Btn, QtCore.SIGNAL("clicked()"), 
					self.info)
		
		
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
	
	def SignalProcess_tableChanged(self, typeControl, idControl, map):
		print typeControl
		print idControl
		print map.getTableData()
	
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
"""