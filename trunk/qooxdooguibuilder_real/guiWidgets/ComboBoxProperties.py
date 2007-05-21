#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *


class CComboBoxProperties(QtGui.QComboBox):
	
	def __init__(self, idProperty, parent = None):
		
		QtGui.QComboBox.__init__(self, parent)
		
		self.idProperty = idProperty
		
	def addPropertyValue(self, propertyValue):
		self.addItem(propertyValue)
		
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	def getSelectedPropertyValue(self):
		return self.currentText()
	
	def getIdProperty(self):
		return self.idProperty
	
	def removeAllProperties(self):
		self.clear()