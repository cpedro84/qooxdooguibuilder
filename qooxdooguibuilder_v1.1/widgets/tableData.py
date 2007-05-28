#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import *
from projectExceptions import *
from generalFunctions import *


class CTableData(QtCore.QObject):
	
	def __init__(self):
		
		self.tableData = { }
		self.rowsList = []
		self.columnsList = []
		
		self.posRows = 1
		self.posColumns = 2
		self.posItems = 3
		self.tableData[self.posItems] = {}
		
		
	def __del__(self):
		
		self.tableData.clear()		
		clearList(self.rowsList)
		clearList(self.columnsList)
			
	def addColumn(self, text):
		
		item = editItem(text)
		self.columnsList.append(item)
		self.setTableColumns(self.columnsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a coluna)
		self.tableData[self.posItems][item] = {}
				
	def addRow(self, text):
		
		item = editItem(text)
		self.rowsList.append(item)
		self.setTableRows(self.rowsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a linha para todas as colunas existentes)
		row = {item: editItem("")}
		for column in self.tableData[self.posItems].keys():
			self.tableData[self.posItems][column].update(row) 
	
	
	def setItem(self, column, row, item):
		
		if column >= len(self.columnsList) or row >= len(self.rowsList):
			return -1
				
		item = editItem(item)		
		self.tableData[self.posItems][self.getColumnItem(column)][self.getRowItem(row)] = item		
		
	
	def setTableRows(self, rowsList):
		self.tableData[self.posRows] = rowsList
	
	def setTableColumns(self, columnsList):
		#print columnsList	
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
		
	def getColumnItem(self, nColumn):		
		if nColumn >= 0 and nColumn < len(self.columnsList):			
			return self.columnsList[nColumn]
		return -1
	
	def getRowItem(self, nRow):
		if nRow >= 0 and nRow < len(self.rowsList):
			return self.rowsList[nRow]
		return -1
	