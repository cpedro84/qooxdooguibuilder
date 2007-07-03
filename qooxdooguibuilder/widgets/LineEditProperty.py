#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *
from InputMask import *


## Documentation for CLineEditProperty.
#
# Custumized LineEdit Widget that herits all properties from Qt QLineEdit.
class CLineEditProperty(QtGui.QLineEdit):
	
	## The constructor.	
	# Initializes the LineEdit Widget for the given parent, with a optional initial value.
	# the type of input can be set to the given typeProperty.
	# Thhis controls represents a property identified with the idProperty.
	#
	# @Param idProperty string
	# @Param propertyValue string
	# @Param parent reference
	# @Param typeProperty string
	def __init__(self, idProperty, propertyValue = "", parent = None,  typeProperty = TSTRING):
		
		propertyValue = str(propertyValue)
		
		QtGui.QLineEdit.__init__(self, propertyValue, parent)
		
		self.typeProperty = typeProperty
		self.idProperty = idProperty
		
		if typeProperty <> TSTRING:
			self.setReadOnly(true)
		
		#Formatar a mascara de entrada da lineEdit de acordo com o tipo de propriedade
		#mask = CInputMask(typeProperty)
		#self.setInputMask(mask)
	
		self.connect(self, QtCore.SIGNAL("returnPressed()"), self.valueChanged)
		self.connect(self, QtCore.SIGNAL("editingFinished()"), self.valueChanged)
		#self.connect(self, QtCore.SIGNAL("selectionChanged()"), self.valueChanged)
	
	
	##
	# Set the idProperty, that the controls is associated, with the given idProperty.
	#
	# @Param idProperty string
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	##
	# Set the type of input with the given typeProperty.
	#
	# @Param typeProperty string
	def setPropertyType(self, typeProperty):
		self.typeProperty = typeProperty
	
	##
	# Get the value of the control, that represents the property value.
	#
	# @Return string
	def getPropertyValue(self):
		return self.text().toLatin1().__str__()
	
	##
	# Get the idProperty, that the controls is associated.
	#
	# @Return string
	def getIdProperty(self):
		return self.idProperty
		
	
	def valueChanged(self):		
		#ENVIO DO SINAL PARA  INFORMAR QUE A PROPRIEDADE FOI ALTERADA DE ESTADO
		self.emit(QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), str(self.getIdProperty()), self.getPropertyValue())
		
		