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
		
	DefaultValue = "DefaultValue"
	Description = "Description"
	
	#MENSAGENS DE ERRO
	ERROR_OPEN_FILE = "Erro na abertura do ficheiro."
	

	def __init__(self):
		#Mapa Associativo para o armazenamento dos controlos		
		self.DControls = { }
		#Mapas associativos das propiredades de cada tipo de controlo
		self.DControlProperties = { }
		
		"""self.DEditProperties = {}
		self.DCheckBoxProperties = {}
		self.DComboProperties = {}
		self.DGroupBoxProperties = {}
		self.DIFrameProperties = {}
		self.DLabelProperties = {}
		self.DListProperties = {}
		self.DMenuBarProperties = {}
		self.DPasswordFieldProperties = {}
		self.DRadioButtonProperties = {}
		self.DSpinnerProperties = {}
		self.DTabViewProperties = {}
		self.DTextAreaProperties = {}
		self.DTextFieldProperties = {}
		self.DToolBarProperties = {}
		self.DTreeProperties = {}
		"""		
		
	def haveControls(self, TypeControl):
		if self.DControls.has_key(TypeControl) == bool(0):
			return bool(0)
		else:
			return bool(1)

	def getNewIDControl(self, TypeControl):
				
		if self.haveControls(TypeControl) == bool(0):				
			return 0
		else:			
			for control in self.DControls[TypeControl]:
				if control == -1:
					return self.DControls[TypeControl].index(-1)
			
			return len(self.DControls[TypeControl])
		
		
	def addNewControl(self, TypeControl):
			
		Lcontrols = []
		
		#calcular um Id para o control		
		IDControl = self.getNewIDControl(TypeControl)
		
		if self.haveControls(TypeControl) == bool(0):
			Lcontrols.append(IDControl)
			self.DControls[TypeControl] = Lcontrols			
		else: #caso no mapa já exista elementos deste tipo de controlo
			if IDControl == len(self.DControls[TypeControl]):
				self.DControls[TypeControl].append(IDControl)
			else:
				self.DControls[TypeControl][int(IDControl)] = IDControl		
		
		return IDControl
		
	def delControl(self, TypeControl, IDControl):
				
		if self.haveControls(TypeControl) == bool(0):
			return -1
		else:
			try:	
				self.DControls[TypeControl].index(IDControl)
				self.DControls[TypeControl][int(IDControl)] = -1
				return IDControl
			except ValueError:
				return -1
		
	def getControlsFromType(self, TypeControl):
		if self.DControls.has_key(TypeControl) == bool(0):
			return -1
		return self.DControls[TypeControl]
	
	def getAllControls(self):
		print "teste"
	
	
	def loadTypeControlProperties(self, filePath):
		
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
				
				#Armazenar propriedade no mapa associativo
				DcontrolProperties[IdProperty] = {self.Description:description, self.DefaultValue: defaultValue}
				
			return DcontrolProperties		
			
		except IOError:
			print str(self.ERROR_OPEN_FILE+" File:"+filePath)
		
	
	def loadPropertiesFromFile(self, filePath):
		#Abrir ficheiro com a indicação de todos os controlos
		print str(self.ERROR_OPEN_FILE+" File:"+filePath)
		try:
			fcontrols=open(filePath)
			#Ler conteudo do ficheiro
			for line in fcontrols:
				line = line.replace('\n', '')	
				line = line.split(':')		
				typeControl = line[0]
				fileTypeControl = line[1]
				
				#Ler Propriedades do actual tipo de controlo 
				DcontrolProperties = self.loadTypeControlProperties(fileTypeControl)
				#Associar ao mapa das caracteristicas dos controlos, as informações sobre as descrições (em forma de mapa associativo)
				self.DControlProperties[typeControl] = DcontrolProperties				
		
		except IOError:
			str(self.ERROR_OPEN_FILE+" File:"+filePath)
	
monitor = MonitorControls()
"""id0 = monitor.addNewControl(MonitorControls.TEdit)
id1 = monitor.addNewControl(MonitorControls.TEdit)
id2 = monitor.addNewControl(MonitorControls.TEdit)
id3 = monitor.addNewControl(MonitorControls.TEdit)
monitor.delControl(MonitorControls.TEdit, id0)
monitor.delControl(MonitorControls.TEdit, id1)
monitor.delControl(MonitorControls.TEdit, id3)
print monitor.getControlsFromType(MonitorControls.TEdit)

id4 = monitor.addNewControl(MonitorControls.TEdit)
id5 = monitor.addNewControl(MonitorControls.TEdit)

print monitor.getControlsFromType(MonitorControls.TEdit)
"""

monitor.loadPropertiesFromFile("ControlsDataTypes.dat")
print monitor.DControlProperties
