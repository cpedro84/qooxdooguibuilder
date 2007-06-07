#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableList(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.ListView = CListWidget()
		ResizableWidget.__init__(self, typeControl, id, self.ListView, parent)	
		self.items = []
		#PROPREIDADES
		self.selectable = bool(1)

		
	def addItemText(self, item):
		self.ListView.addItem(item)
	
	# textItemsList -> ELEMENT TYPE: CEditItem 
	def setItems(self, textItemsList):
		self.ListView.clear()
		for item in textItemsList:			
			self.addItemText(item.getText())

	def countItems(self):
		return self.ListView.count()

	def getItemText(self, index):		
		if indexValidation(index, self.countItems()):
			return str(self.ListView.item(index).text())
	
		return structureError
		
		
	def getItems(self):
		textItems = []
		nElements = self.countItems()
		elem = 0		
		while elem < nElements:
			textItems.append(CEditItem(self.getItemText(elem)))
			elem = elem + 1
		
		return textItems