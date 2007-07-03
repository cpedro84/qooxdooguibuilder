#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *

## Documentation for CComboBoxProperties.
#
# Custumized ComboBox Widget that herits all properties from Qt QComboBox.
class CComboBoxProperties(QtGui.QComboBox):
	
	## The constructor.	
	# Constructs a ComboBox owned by the given parent.
	# This widget represents a idProperty identified with the given idProperty.
	#
	# @Param idProperty string
	# @Param parent QWidget
	def __init__(self, idProperty, parent = None):
		
		QtGui.QComboBox.__init__(self, parent)
		
		self.idProperty = idProperty
		
		self.connect(self, QtCore.SIGNAL("currentIndexChanged(int)"), self.valueChanged)
		
	##
	# Add a property text.
	#
	# @Param propertyValue string
	def addPropertyValue(self, propertyValue):
		self.addItem(propertyValue)
	
	##
	# Set the idProperty property that identifies the control.
	#
	# @Param idProperty string
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	##
	# Set selected item that have the given itemText.
	#
	# @Param itemText string
	def setSelectedItem(self,itemText):
		nItem = self.findText(itemText)
		if nItem <> -1:
			self.setCurrentIndex(nItem)
	
	##
	# Returns the selected property value.
	#
	# @Param string
	def getSelectedPropertyValue(self):
		return self.currentText().toLatin1().__str__()
	
	##
	# Returns the Id property that identifies the control.
	#
	# @Param string
	def getIdProperty(self):
		return self.idProperty
	
	##
	# Remove all properties items from the ComboBox.
	def removeAllProperties(self):
		self.clear()
	
	## SLOT
	# Whenever a item selection was changed this slot emit a signal with the selected property value.
	#
	# @param nItem int
	def valueChanged(self, nItem):
		#ENVIO DO SINAL PARA  INFORMAR QUE A PROPRIEDADE FOI ALTERADA DE ESTADO
		value = str(self.getSelectedPropertyValue())		
		self.emit(QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), str(self.getIdProperty()), value)
		
		