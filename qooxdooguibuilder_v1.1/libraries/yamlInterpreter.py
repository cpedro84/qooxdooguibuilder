#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
import yaml
from const import *
from generalFunctions import *
from ControlInfo import *
from ControlProperty import *


class CYamlInterpreter:
	
		
	def writeInterfaceFile(self, controlsInfoList, filePath):

		self.writeInterface(controlsInfoList)
		
		writeToFile(yamlCode, filePath)


	def writeInterface(self, controlsInfoList):
		controlsList = []
		
		for controlInfo in controlsInfoList:
		
			propertiesMap = {}
			
			typeControl = controlInfo.getTypeControl()		
			controlPropertiesList = controlInfo.getControlProperties()
			
			for controlProperty in controlPropertiesList:
				propertiesMap[controlProperty.getIdProperty()] = controlProperty.getValueProperty()
				
			controlsList.append( {typeControl :  propertiesMap })
		
		return  yaml.dump(controlsList)
		

	def writeTemplate(self, controlInfo):
		
		controlMap = {}		
		propertiesMap = {}
			
		typeControl = controlInfo.getTypeControl()		
		controlPropertiesList = controlInfo.getControlProperties()
		
		for controlProperty in controlPropertiesList:
			propertiesMap[controlProperty.getIdProperty()] = controlProperty.getValueProperty()
			
		controlMap = {typeControl :  propertiesMap }

		return  yaml.dump(controlMap)

	def readInterfaceFile(self, filePath):
		
		file = open(filePath)
		yamlCode = file.read()
		
		return self.readInterface(yamlCode)
	
	
	def readInterface(self, yamlInterfaceCode):
		
		controlsList = yaml.load(yamlInterfaceCode)
		if controlsList == None:
			return -1
		
		controlsInfoList = []
		
		for ControlMap in controlsList: #Lista
			for typeControl in ControlMap.keys(): #Mapa
				propertiesMap = ControlMap[typeControl]
				
				controlInfo = CControlInfo(typeControl,"")
				
				#Carregamento das propreidades (ids e valores)
				for idProperty in propertiesMap.keys():					
					propertyValue = propertiesMap[idProperty]
					controlInfo.addControlProperty(CControlProperty(idProperty, "", propertyValue))
				
				controlsInfoList.append(controlInfo)


		return controlsInfoList

	def readTemplate(self, yamlInterfaceCode):
				
		controlMap = yaml.load(yamlInterfaceCode)		
		if controlMap == None:
			return -1
		
		controlInfo = -1		
			
		for typeControl in controlMap.keys(): 
			propertiesMap = controlMap[typeControl]
			controlInfo = CControlInfo(typeControl,"")

			#Carregamento das propreidades (ids e valores)
			for idProperty in propertiesMap.keys():					
				propertyValue = propertiesMap[idProperty]
				controlInfo.addControlProperty(CControlProperty(idProperty, "", propertyValue))
		
			break
			
		return controlInfo 
