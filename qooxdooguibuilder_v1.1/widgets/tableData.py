#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import *
from projectExceptions import *
from generalFunctions import *


## Documentation for CTableData.
#
# Represents the contents of a CEditTableItemsWidget Object.
# The CEditTableItemsWidget is a QTableWidget. 
#This class represents the columns, rows and the cells contents of this control.
# @see CEditTableItemsWidget
class CTableData(QtCore.QObject):
	
	## The constructor.	
	#
	def __init__(self):
		
		self.tableData = { }
		self.rowsList = []
		self.columnsList = []
		
		self.posRows = 1
		self.posColumns = 2
		self.posItems = 3
		self.tableData[self.posItems] = {}
		
	
	## The destructor.	
	#	
	def __del__(self):
		
		self.tableData.clear()		
		clearList(self.rowsList)
		clearList(self.columnsList)
			
	
	##
	# Add a Column with the given text.
	#
	# @Param text string
	def addColumn(self, text):
		
		item = text
		self.columnsList.append(item)
		self.setTableColumns(self.columnsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a coluna)
		self.tableData[self.posItems][item] = {}
				
	
	##
	# Add a Row with the given text.
	#
	# @Param text string
	def addRow(self, text):
		
		item = text
		self.rowsList.append(item)
		self.setTableRows(self.rowsList)
		#(vai ser necessário ir self.tableData[self.posItems] e acrescentar a linha para todas as colunas existentes)
		row = {item: ""}
		for column in self.tableData[self.posItems].keys():
			self.tableData[self.posItems][column].update(row) 
	
	
	##
	# Set a Cell Item in the given column and row.
	# If the Cell Item doesn't exist -1 will be returned.
	#
	# @Param column int
	# @Param row int
	# @Param item string
	#
	# @return int
	def setItem(self, column, row, item):
		
		if column >= len(self.columnsList) or row >= len(self.rowsList):
			return -1
				
		item = item
		self.tableData[self.posItems][self.getColumnItem(column)][self.getRowItem(row)] = item		
		
	##
	# Set the rows with the given rows list.	
	#
	# @Param python list
	def setTableRows(self, rowsList):
		self.tableData[self.posRows] = rowsList
	
	##
	# Set the columns with the given columns list.	
	#
	# @Param python list
	def setTableColumns(self, columnsList):
		#print columnsList	
		self.tableData[self.posColumns] = columnsList
	
	##
	# Set the table items with the given items dictionary.	
	#
	# @Param tableItems python dict
	def setTableItems(self, tableItems):
		self.tableData[self.posItems] = tableItems
		
	##
	# Get rows text list.
	#	
	# @return python list
	def getTableRows(self):
		return self.tableData[self.posRows]
	
	##
	# Get columns text list.
	#	
	# @return python list
	def getTableColumns(self):
		return self.tableData[self.posColumns]
	
	
	##
	# Get table items dictionary.
	#	
	# @return python dictionary
	def getTableItems(self):
		return self.tableData[self.posItems]
	

	##
	# Get tableData reference.
	#	
	# @return CTableData
	def getTableData(self):
		return self.tableData
	
	##
	# Get nColumn Item text.
	#	
	# @return string
	def getColumnItem(self, nColumn):		
		if nColumn >= 0 and nColumn < len(self.columnsList):			
			return self.columnsList[nColumn]
		return -1
	
	##
	# Get nRow Item text.
	#	
	# @return string
	def getRowItem(self, nRow):
		if nRow >= 0 and nRow < len(self.rowsList):
			return self.rowsList[nRow]
		return -1
	