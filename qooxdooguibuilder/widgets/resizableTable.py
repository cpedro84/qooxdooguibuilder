#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableTable.
#
# Provide a Resizable Table which represents the Table Control. 
#
# Inherits @see CResizableWidget
class CResizableTable(CResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable Table owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	#
	# @see CTableWidget
	def __init__(self, typeControl, id, parent=None):
		self.tableWidget = CTableWidget()		
		CResizableWidget.__init__(self, typeControl, id, self.tableWidget, parent)
		self.tableWidget.setEnabled(false)
	
	"""def setHeaderCellHeight(self, height):
		self.table.
	"""
	
	
	def setRowsHeight(self, height):		
		height = int(height)
		row = 0 
		while row < self.tableWidget.rowCount():
			self.tableWidget.setRowHeight(row, height)
			row +=1

	def setColumnsWidth(self, width):		
		width = int(width)
		column = 0
		
		while column < self.tableWidget.columnCount():			
			self.tableWidget.setColumnWidth(column, width)
			column +=1
		
	def setRowCount(self, count):
		count = int(count)
		self.tableWidget.setRowCount(count)
		
	def setColumnCount(self, count):
		count = int(count)
		self.tableWidget.setColumnCount(count)
		
	
	##
	# Get the content of the table.
	#
	# @Return CTableData
	# @see CTableData
	def getTableData(self):		
		return self.tableWidget.getTableData()
	
	
	##
	# Set the content of the table with the information stored in given tableData, that represents the table contents.
	#
	# @Param tableData CTableData
	# @see CTableData
	def setTable(self, tableData):
		
		self.tableWidget.setTableWidget(tableData)
		
