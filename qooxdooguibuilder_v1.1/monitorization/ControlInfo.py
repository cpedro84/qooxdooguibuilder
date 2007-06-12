#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from ControlProperty import *

## Documentation for CControlInfo.
#
# Store control information: typeControl, idControl, controlProperties
class CControlInfo(QtCore.QObject):
	
	## The constructor.	
	#
	# @Param typeControl string
	# @Param idControl string
	def __init__(self, typeControl, idControl):
		self.typeControl = typeControl
		self.idControl = idControl
		self.controlProperties = []
	
	##
	# Add a control property.
	#
	# @Param controlProperty CControlProperty
	# @see CControlProperty	
	def addControlProperty(self, controlProperty):
		self.controlProperties .append(controlProperty)

	##
	# Set the control type.
	#
	# @Param typeControl string
	def setTypeControl(self, typeControl):
		self.typeControl = typeControl
	
	
	##
	# Set the control Id.
	#
	# @Param idControl string
	def setIdControl(self, idControl):
		self.idControl = idControl
	
	
	##
	# Set the control Properties.
	#
	# @Param controlProperties list
	def setControlProperties(self, controlProperties):		
		if len(controlProperties) < 1:
			return
		self.controlProperties = controlProperties
	
	
	##
	# Set the value of a Property.
	#
	# @Param idProperty string
	# @Param value string
	def setControlProperty(self, idProperty, value):
		
		controlProperty = self.getControlProperty(idProperty)	
		if controlProperty == -1:
			return -1
		else:			
			controlProperty.setValueProperty(value)
		
		
		
	##
	# Get control type.
	#	
	# @return typeControl string
	def getTypeControl(self):
		return self.typeControl
	
	##
	# Get control Id.
	#	
	# @return idControl string	
	def getIdControl(self):
		return self.idControl
	
	##
	# Get control properties.
	#	
	# @return controlProperties (list of CControlProperty)
	# @see CControlProperty
	def getControlProperties(self):		
		return self.controlProperties
		
		
	##
	# Get control property.
	#
	# @param idProperty string
	#
	# @return CControlProperty
	# @see CControlProperty
	def getControlProperty(self, idProperty):
		for controlProperty in self.controlProperties:
			if controlProperty.getIdProperty() == idProperty:
				return controlProperty
		
		return -1
		
	##
	# Check if control have properties.
	#
	# @return boolean	
	def hasProperties(self):
		if len(self.controlProperties) > 1:
			return true
		else:
			return false