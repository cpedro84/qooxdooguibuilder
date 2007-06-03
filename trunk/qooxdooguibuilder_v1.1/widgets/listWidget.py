#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from tableData import *

class CListWidget(QtGui.QListWidget):
	
	def __init__(self, parent=None):
		QtGui.QListWidget.__init__(self, parent)
		

	def setListWidget(self, itemsList):	
		for item in itemsList:
			self.addItem(item.getText())

	def getListWidgetItems(self):
		
		itemsList = []
		
		elem = 0
		nElements =  self.count()				
		while elem < nElements:
			item = self.item(elem)
			itemsList.append(editItem(str(item.text())))
			
		return itemsList
