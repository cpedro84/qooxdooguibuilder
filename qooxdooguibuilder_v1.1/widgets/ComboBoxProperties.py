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
		
		self.connect(self, QtCore.SIGNAL("currentIndexChanged(int)"), self.valueChanged)
		
	def addPropertyValue(self, propertyValue):
		self.addItem(propertyValue)
		
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	def setSelectedItem(self,itemText):
		nItem = self.findText(itemText)
		if nItem <> -1:
			self.setCurrentIndex(nItem)
	
	def getSelectedPropertyValue(self):
		return self.currentText().toLatin1().__str__()
	
	def getIdProperty(self):
		return self.idProperty
	
	def removeAllProperties(self):
		self.clear()
	
	def valueChanged(self, nItem):
		#ENVIO DO SINAL PARA  INFORMAR QUE A PROPRIEDADE FOI ALTERADA DE ESTADO
		value = str(self.getSelectedPropertyValue())		
		self.emit(QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), str(self.getIdProperty()), value)
		
		