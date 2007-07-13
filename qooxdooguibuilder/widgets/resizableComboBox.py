#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableComboBox.
#
# Provide a Resizable ComboBox which represents the ComboBox Control. 
#
# Inherits @see CResizableWidget
class CResizableComboBox(CResizableWidget):
		
	## The constructor.	
	# Constructs a Resizable ComboBox owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.ComboBox = QtGui.QComboBox()
		CResizableWidget.__init__(self, typeControl, id, self.ComboBox, parent)	
	
	
	##
	# Add a item text to the ComboBox.
	#
	# @Param item string	
	def addItemText(self, item):
		self.ComboBox.addItem(item)
	
	##
	# Insert a item text to the ComboBox in the given index.
	#
	# @Param index int
	# @Param item string
	def insertItem(self, index, strText):
		self.ComboBox.insertItem(index, strText)
	
	##
	# Add a item text, with a associated Icon, to the ComboBox.
	#
	# @Param strText string
	# @Param icon QtGui.QIcon	
	def addItemIcon(self, strText, icon):
		self.ComboBox.addItem(icon, strText)
		
	##
	# Set the items of the ComboBox with teh given list of CEditItem.
	# @see CEditItem
	#
	# @Param textItemsList python list
	def setItems(self, textItemsList):
		self.ComboBox.clear()		
		for item in textItemsList:			
			self.addItemText(item.getText())
	
	
	def setCurrentIndex(self, index):
		self.ComboBox.setCurrentIndex(index)

	def setEditText(self, strText):
		self.ComboBox.setEditText(strText)
	
	def setItemText(self, index, strText):
		self.ComboBox.setItemText(self, index, strText)
	
	def setItemIcon(self, index, icon):
		self.ComboBox.setItemIcon(self, index, icon)
	
	
	def isEditable(self):
		return self.ComboBox.isEditable()
	
	def countItems(self):
		return self.ComboBox.count()
	
	
	##
	# Get a item text inthe given index from the ComboBox.
	#
	# @Param index int
	def getItemText(self, index):		
		if indexValidation(index, self.countItems()):
			return str(self.ComboBox.itemText(index))
		
		return structureError
		
	##
	# Return the list of items (CEditItem) from the ComboBox.
	# @see CEditItem
	#
	# @Return python list
	def getItems(self):
		items = []
		nElements = self.countItems()
		elem = 0		
		while elem < nElements:
			items.append(CEditItem(self.getItemText(elem)))
			elem = elem + 1
		
		return items
	
	
	def getItemIcon(self, index):
		return self.ComboBox.itemIcon(index)
		
	def getSelectedItem(self):
		return self.ComboBox.currentIndex()
