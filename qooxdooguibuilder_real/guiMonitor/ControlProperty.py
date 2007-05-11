#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *


class CControlProperty(QtCore.QObject):
	
	def __init__(self, idProperty, nameProperty = None, valueProperty = None, typeProperty = None ):
		self.idProperty = idProperty
		self.nameProperty = nameProperty
		self.valueProperty = valueProperty
		self.typeProperty = typeProperty
		self.options = []
		
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	def setNameProperty(self, nameProperty):
		self.nameProperty = nameProperty
	
	def setValueProperty(self, valueProperty):
		self.valueProperty = valueProperty
		
	def setTypeProperty(self, typeProperty):
		self.typeProperty = typeProperty
	
	
	def setOptions(self, options):
		if len(options) > 1:			
			self.options = options
		else:
			self.options = []
			
	def addOption(self, option):
		self.options.append(option)
	
	def getIdProperty(self):
		return self.idProperty
		
	def getNameProperty(self):
		return self.nameProperty
		
	def getValueProperty(self):
		return self.valueProperty
		
	def getTypeProperty(self):
		return self.typeProperty
		
	def hasOptions(self):
		if len(self.options) > 1:
			return true
		else:
			return false