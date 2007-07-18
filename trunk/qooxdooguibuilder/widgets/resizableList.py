#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

## Documentation for CResizableList.
#
# Provide a Resizable List which represents the List Control. 
#
# Inherits @see CResizableWidget
class CResizableList(CResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable List owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.ListView = CListWidget()
		CResizableWidget.__init__(self, typeControl, id, self.ListView, parent)	
		#self.ListView.setEnabled(false)
		
		self.items = []
		#PROPREIDADES
		self.selectable = bool(1)

	
	##
	# Add a item text to the List.
	#
	# @Param item string
	def addItemText(self, item):
		self.ListView.addItem(item)
	
	
	##
	# Set the items of the List with teh given list of CEditItem.
	# @see CEditItem
	#
	# @Param textItemsList python list
	def setItems(self, textItemsList):
		self.ListView.clear()
		for item in textItemsList:			
			self.addItemText(item.getText())

	##
	# Get the number of items in the List.
	#
	# @Param int
	def countItems(self):
		return self.ListView.count()

	##
	# Get a item text inthe given index from the List.
	#
	# @Param index int
	def getItemText(self, index):		
		if indexValidation(index, self.countItems()):
			return str(self.ListView.item(index).text())
	
		return structureError
		
	##
	# Return the list of items (CEditItem) from the List.
	# @see CEditItem
	#
	# @Return python list
	def getItems(self):
		textItems = []
		nElements = self.countItems()
		elem = 0		
		while elem < nElements:
			textItems.append(CEditItem(self.getItemText(elem)))
			elem = elem + 1
		
		return textItems