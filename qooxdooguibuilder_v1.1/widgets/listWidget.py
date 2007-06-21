#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from tableData import *

## Documentation for CListWidget.
#
# Custumized ListWidget Widget that herits all properties from Qt QListWidget.
class CListWidget(QtGui.QListWidget):
	
	## The constructor.	
	# Initializes the List Widget for the given parent.
	def __init__(self, parent=None):
		QtGui.QListWidget.__init__(self, parent)
		

	##
	# Set the list items with the given itemsList.
	#
	# @Param itemsList python list
	def setListWidget(self, itemsList):	
		for item in itemsList:
			self.addItem(item.getText())

	##
	# Get the list items associated with the control.
	#
	# @Param python list
	def getListWidgetItems(self):
		
		itemsList = []
		
		elem = 0
		nElements =  self.count()				
		while elem < nElements:
			item = self.item(elem)
			itemsList.append(CEditItem(str(item.text())))
			
		return itemsList
