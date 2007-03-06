#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class MonitorControls:
	
	TEdit = "EDT"
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
		
	PropertyValue = "PropertyValue"
	Description = "Description"
	
	deletedControl = -1
	error = -1
	true = bool(1)
	false = bool(0)
	
	#MENSAGENS DE ERRO
	ERROR_OPEN_FILE = "Erro na abertura do ficheiro."
	

	def __init__(self):
		#Mapa Associativo para armazenamento dos controlos		
		self.DControls = { }
		#Mapa associativo para armazenamento das propriedades dos controlos
		self.DControlProperties = { }
		#Mapa associativo para armazenamento da correspondencia entre as propriedades de cada tipo de controlo e os metodos das resizable widget
		self.DPropertiesMethods = { }		
		
		#Ler propriedades
		self.loadPropertiesFromFile("ControlsDataTypes.dat")
			
		
	def haveTypeControls(self, TypeControl):
		if self.DControls.has_key(TypeControl) == self.false:
			return self.false
		else:
			return self.true
	
	def haveIdControl(self, TypeControl, IdControl):
		if haveTypeControls and self.DControls[TypeControl].has_key(IdControl):
			return self.true
		else:
			return self.false
	
	def getNewIDControl(self, TypeControl):

		if self.haveTypeControls(TypeControl) == self.false:				
			return 0
		else:				
			try:				
				return self.DControls[TypeControl].values().index(self.deletedControl)			
			except ValueError:
				return len(self.DControls[TypeControl].keys())

	
	def getDefaultProperties(self, TypeControl):
		
		if self.DControlProperties.has_key(TypeControl):
			return self.DControlProperties[TypeControl]
		return self.deletedControl	
		
		
	def addNewControl(self, TypeControl):
		
		DTypeControls = {}
		DTypeControls = self.getDefaultProperties(TypeControl)
		
		#verificar se existem propriedades default
		if DTypeControls == self.error:
			return self.error
		
		#calcular um Id para o control		
		IdControl = self.getNewIDControl(TypeControl)
		#adicionar o novo controlo ao mapa
		DControl = { }
		DControl[IdControl] = DTypeControls
		
		#verificar se já existe algum controlo do tipo de dados do controlo a inserir
		if self.DControls.has_key(TypeControl) == self.false:
			self.DControls[TypeControl] = { }
		
		self.DControls[TypeControl].update(DControl)
		
		return IdControl
	
	
	def delControl(self, TypeControl, IDControl):
				
		if self.haveTypeControls(TypeControl) == self.false:
			return self.deletedControl
		else:				
			if self.DControls[TypeControl].has_key(IDControl) == self.true:
				self.DControls[TypeControl][IDControl] = self.deletedControl
			return IDControl
			

	def getControlsFromType(self, TypeControl):
		if self.haveTypeControls(TypeControl) == self.false:
			return self.error
		return self.DControls[TypeControl]
	
	def getAllControls(self):
		print self.DControls		
		
		
	def changeProperty(self, TypeControl, IdControl, IdProperty, value):
		if haveIdControl(TypeControl, IdControl) == self.false:
			return error
		else:
			#Alteração da propreidade na estrutura de dados
			self.DControls[TypeControl][IdControl][IdProperty][self.PropertyValue] = value
			
			#Executar metodo na classe resizable (...)
			resizablePropertyMethodCall = self.DPropertiesMethods[TypeControl][IdProperty]
			if len(resizablePropertyMethodCall) > 0: #caso a string na seja vazia
				print "teste" #(...)
			
	def loadTypeControlProperties(self, TypeControl, filePath):
		
		DcontrolProperties = { }
		
		try:
			fcontrol=open(filePath)
			#Ler conteudo do ficheiro
			for line in fcontrol:
				line = line.replace('\n', '')	
				line = line.split(':')		
				IdProperty = line[0]
				description = line[1]
				defaultValue = line[2]			
				resizablePropertyMethodCall = line[3]
				#Armazenar o metodo de chamada à classe resizable no mapa associativo
				if not self.DPropertiesMethods.has_key(TypeControl):
					self.DPropertiesMethods[TypeControl] = { }
				
				self.DPropertiesMethods[TypeControl][IdProperty] = resizablePropertyMethodCall
								
				#Armazenar propriedade no mapa associativo
				DcontrolProperties[IdProperty] = {self.Description:description, self.PropertyValue: defaultValue}
				
			return DcontrolProperties		
			
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
				
				#Ler Propriedades do actual tipo de controlo 
				DcontrolProperties = self.loadTypeControlProperties(typeControl, filePathTypeControl)
				#Associar ao mapa das caracteristicas dos controlos, as informações sobre as descrições (em forma de mapa associativo)
				self.DControlProperties[typeControl] = DcontrolProperties				
		
		except IOError:
			str(self.ERROR_OPEN_FILE+" File:"+filePath)
	
	
monitor = MonitorControls()
id0 = monitor.addNewControl(MonitorControls.TEdit)
id1 = monitor.addNewControl(MonitorControls.TEdit)
id2 = monitor.addNewControl(MonitorControls.TEdit)
id3 = monitor.addNewControl(MonitorControls.TEdit)
#print monitor.getControlsFromType(MonitorControls.TEdit)
#print monitor.getAllControls()
monitor.delControl(MonitorControls.TEdit, id2)
monitor.delControl(MonitorControls.TEdit, id3)
id4 = monitor.addNewControl(MonitorControls.TEdit)
print id4
#id5 = monitor.addNewControl(MonitorControls.TEdit)

print monitor.getControlsFromType(MonitorControls.TEdit)

print monitor.DPropertiesMethods

"""monitor.loadPropertiesFromFile("ControlsDataTypes.dat")
print monitor.DControlProperties.keys().index('CKB')
"""