#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *


## Documentation for CEditItem.
#
# Store the information, text and widget, about items. This items is related with the controls that have Item properties.
# @see CTableData
# @see CEditItemsWidget
# @see CEditTableItemsWidget
class CEditItem(QtCore.QObject):
	
	## The constructor.	
	#
	# @Param text string
	# @Param widget reference
	def __init__(self, text, widget = None, iconPath = ""):
		self.text = text
		self.widget = widget
		self.iconPath = iconPath
	
	##
	# Set the item's widget .
	#
	# @Param widget reference
	def setWidget(self, widget):
		self.widget = widget
		
	
	##
	# Set the item's text .
	#
	# @Param text string
	def setText(self, text):
		self.text = text
	
	##
	# Set the item's icon path .
	#
	# @Param iconPath string
	def setIconPath(self, iconPath):
		self.iconPath = iconPath
	
	
	#*****************************************
	
	##
	# Get item's text.
	#	
	# @return string
	def getText(self):
		return self.text
	
	##
	# Get item's widget.
	#	
	# @return reference
	def getWidget(self):
		return self.widget
		
		
	##
	# Get item's icon path.
	#	
	# @return string
	def getIconPath(self):
		#return QStringToString(self.iconPath)
		return self.iconPath
