#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *


class CTableData(QtCore.QObject):
	
	def __init__(self, rowsList = [], columnsList = [] , tableItems = {}):
		self.tableData = { }
		self.posRows = 1
		self.posColumns = 2
		self.posItems = 3
		
		self.setTableRows(rowsList)
		self.setTableColumns(columnsList)
		self.setTableItems(tableItems)
				
	def setTableRows(self, rowsList):
		self.tableData[self.posRows] = rowsList
	
	def setTableColumns(self, columnsList):
		self.tableData[self.posColumns] = columnsList
		
	def setTableItems(self, tableItems):
		self.tableData[self.posItems] = tableItems
		
		
	def getTableRows(self):
		return self.tableData[self.posRows]
		
	def getTableColumns(self):
		return self.tableData[self.posColumns]
		
	def getTableItems(self):
		return self.tableData[self.posItems]
		
	def getTableData(self):
		return self.tableData
	