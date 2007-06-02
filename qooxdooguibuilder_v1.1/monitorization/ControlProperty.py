#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *

## Documentation for CControlInfo.
#
# Store property information for a control: 
# idProperty 
# nameProperty
# valueProperty
# typeProperty
# options
class CControlProperty(QtCore.QObject):
	
	## The constructor.	
	#
	# @param idProperty 
	# @param nameProperty
	# @param valueProperty
	# @param typeProperty	
	def __init__(self, idProperty, nameProperty = None, valueProperty = None, typeProperty = None ):
		self.idProperty = idProperty
		self.nameProperty = nameProperty
		self.valueProperty = valueProperty
		self.typeProperty = typeProperty
		self.options = []
	
	##
	# Add a control option.
	#
	# @Param option string
	def addOption(self, option):
		self.options.append(option)
		
	##
	# Set the property id.
	#
	# @Param idProperty string
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	##
	# Set the property name.
	#
	# @Param nameProperty string
	def setNameProperty(self, nameProperty):
		self.nameProperty = nameProperty
	
	##
	# Set the property value.
	#
	# @Param valueProperty string
	def setValueProperty(self, valueProperty):
		self.valueProperty = valueProperty
		
	##
	# Set the property type.
	#
	# @Param typeProperty string
	def setTypeProperty(self, typeProperty):
		self.typeProperty = typeProperty
	
	##
	# Set the options list.
	#
	# @Param options list
	def setOptions(self, options):
		if len(options) > 1:			
			self.options = options
		else:
			self.options = []

	##
	# Get property id.
	#	
	# @return idProperty string
	def getIdProperty(self):
		return self.idProperty
		
	##
	# Get property id.
	#	
	# @return idProperty string
	def getNameProperty(self):
		return self.nameProperty
	
	##
	# Get property value.
	#	
	# @return valueProperty string
	def getValueProperty(self):
		return self.valueProperty
		
	##
	# Get property type.
	#	
	# @return typeProperty string
	def getTypeProperty(self):
		return self.typeProperty
	
	##
	# Get options list.
	#	
	# @return options list
	def getOptions(self):
		return self.options
		
	##
	# Check if control has options.
	#
	# @return boolean
	def hasOptions(self):
		if len(self.options) > 1:
			return true
		else:
			return false