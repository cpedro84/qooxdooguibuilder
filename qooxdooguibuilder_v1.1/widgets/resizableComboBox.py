#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *



class ResizableComboBox(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.ComboBox = QtGui.QComboBox()
		ResizableWidget.__init__(self, typeControl, id, self.ComboBox, parent)	
	
	#??????????????????????????????????
	def addItemText(self, item):
		self.ComboBox.addItem(item)
	
	def addItemIcon(self, strText, Icon):
		self.ComboBox.addItem(Icon, strText)
	
	def insertItem(self, index, strText):
		self.ComboBox.insertItem(index, strText)
	
	
	# textItemsList -> ELEMENT TYPE: editItem
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
		self.ComboBox.count()
	
	def getItemText(self, index):		
		if indexValidation(index, self.countItems()):
			return str(self.ComboBox.itemText(index))
		
		return structureError
		
		
	def getItems(self):
		items = []
		nElements = self.countItems()
		elem = 0		
		while elem < nElements:
			textItems.append(editItem(self.getItemText(elem)))
			elem = elem + 1
		
		return items
	
	
	def getItemIcon(self, index):
		return self.ComboBox.itemIcon(index)
		
	def getSelectedItem(self):
		return self.ComboBox.currentIndex()
