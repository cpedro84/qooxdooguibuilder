#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableTable(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.tableWidget = CTableWidget()		
		ResizableWidget.__init__(self, typeControl, id, self.tableWidget, parent)
		
	
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
		
		
	def getTableData(self):
		#(...) - fazer o carregamento dos dados construindo um objecto do tipo tableData				
		return self.tableWidget.getTableData()
	
	def setTable(self, tableData):
		#alterar o conteudo da tableWidget de acordo com as alterações efectuadas
		self.tableWidget.setTableWidget(tableData)