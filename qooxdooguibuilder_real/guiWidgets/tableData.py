#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import *
from projectExceptions import *


class CTableData(QtCore.QObject):
	
	def __init__(self, rowsList = [], columnsList = [] , tableItems = {}):
		self.tableData = { }
		self.rowsList = rowsList
		self.columnsList = columnsList
		
		self.posRows = 1
		self.posColumns = 2
		self.posItems = 3
		self.tableData[self.posItems] = {}
		
		self.setTableRows(rowsList)
		self.setTableColumns(columnsList)
		self.setTableItems(tableItems)
	
	
	def addColumn(self, text):
		self.columnsList.append(editItem(text))
		self.setTableColumns(self.columnsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a coluna)
	
	def addRow(self, text):
		self.rowsList.append(editItem(text))
		self.setTableRows(self.rowsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a linha para todas as colunas existentes)
	
	def setItem(self, column, row, item):
		
		if column >= len(self.columnsList) or row >= len(self.rowsList):
			return -1
		print column
		
		item = editItem(item)
		self.tableData[self.posItems][column].update({row:item})
		
	
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
	