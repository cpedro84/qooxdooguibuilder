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
	def __init__(self, text, widget = None):
		self.text = text
		self.widget = widget

	
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
