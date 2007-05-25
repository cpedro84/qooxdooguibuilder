#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *
from InputMask import *

class CLineEditProperty(QtGui.QLineEdit):
	
	def __init__(self, idProperty, propertyValue = "", parent = None,  typeProperty = TINT):
		
		QtGui.QLineEdit.__init__(self, propertyValue, parent)
		
		self.typeProperty = typeProperty
		self.idProperty = idProperty
		
		#Formatar a mascara de entrada da lineEdit de acordo com o tipo de propriedade
		mask = CInputMask(typeProperty)
		self.setInputMask(mask)
	
	def getPropertyValue(self):
		return self.text()
	
	def getIdProperty(self):
		return self.idProperty
	
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	def setPropertyType(self, typeProperty):
		self.typeProperty = typeProperty