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
			if CControlProperty(controlProperty).getIdProperty() == idPoperty:
				return CControlProperty(controlProperty)
			
	##
	# Check if control have properties.
	#
	# @return boolean	
	def hasProperties(self):
		if len(self.controlProperties) > 1:
			return true
		else:
			return false