#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from exceptions import *
from controlProperty import *


class CControlInfo(QtCore.QObject):
	
	def __init__(self, typeControl, idControl):
		self.typeControl = typeControl
		self.idControl = idControl
		self.controlProperties = []
		
		
	def setTypeControl(self, typeControl):
		self.typeControl = typeControl
		
	def setIdControl(self, idControl):
		self.idControl = idControl
	
	def setControlProperties(self, controlProperties):		
		if len(controlProperties) < 1:
			return
		self.controlProperties = controlProperties
	
	# controlProperty -> CControlProperty
	def addControlProperty(self, controlProperty):
		self.controlProperties .append(controlProperty)
	
	def getTypeControl(self):
		return self.typeControl
	
	def getIdControl(self):
		return self.idControl
		
	def getControlProperties(self):		
		return self.controlProperties
		
	def getControlProperty(self, idProperty):
		for controlProperty in self.controlProperties:
			if CControlProperty(controlProperty).getIdProperty() == idPoperty:
				return CControlProperty(controlProperty)
			
	def hasProperties(self):
		if len(self.controlProperties) > 1:
			return true
		else:
			return false
