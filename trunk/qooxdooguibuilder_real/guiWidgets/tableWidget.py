#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from tableData import *
from listWidget import *
from generalFunctions import *



class CTableWidget(QtGui.QTableWidget):
	def __init__(self, parent=None):
		QtGui.QTableWidget.__init__(self, parent)
		self.setRowCount(0)
		self.setColumnCount(0)		
		self.columns = []
		self.rows = []
	
	
	def addColumn(self, text):
		pos = len(self.columns)
		self.insertColumn(pos)
		self.setHorizontalHeaderItem(pos, QtGui.QTableWidgetItem(text))
		self.columns.append(text)
		
	
	def addRow(self, text):		
		pos = len(self.rows)		
		self.insertRow(pos)
		self.setVerticalHeaderItem(pos, QtGui.QTableWidgetItem(text))
		self.rows.append(text)
		
		#self.setVerticalHeaderLabels(self.rows)

	def setItemText(self, row, column, text):
		self.setItem(row, column, QtGui.QTableWidgetItem(text))
	
	
	def clearHorizontalTableItems(self):
		self.clear()
		self.setHorizontalHeaderLabels(self.columns)
	
	def clearVerticalTableItems(self):
		self.clear()
		self.setVerticalHeaderLabels(self.rows)

	def getTableData(self): #alterar função de forma a retornar um objecto do tipo tableData
			
		tableItems = { }
		
		rowsList = []
		rowsList = self.getRowsList()
		columnsList = []
		columnsList = self.getColumnsList()
		
		itrColumn = 0
		itrRow = 0
		#copiar todos os items da self
		while itrColumn < self.columnCount():
			columnItem = editItem(QtGui.QTableWidgetItem(self.horizontalHeaderItem(itrColumn)).text())
			itrRow = 0 
			tableItems[columnItem] = {}
			for rowItem in rowsList:
				tableItem = self.item(itrRow, itrColumn)
				if tableItem == None:
					tableItem = QtGui.QTableWidgetItem("")
				cellItem = editItem(QtGui.QTableWidgetItem(tableItem).text())
				tableItems[columnItem].update({rowItem: cellItem})
				itrRow +=1
				
			itrColumn +=1
		
		#tableData = CTableData(rowsList, columnsList, tableItems)
		tableData = CTableData()
		tableData.setTableRows(rowsList)		
		tableData.setTableColumns(columnsList)
		tableData.setTableItems(tableItems)
		
		return tableData
	
	def setTableWidget(self, tableData):
		
		itrColumn = 0
		itrRow = 0	
		
		#LIMPAR OS DADOS DA TABLE_WIDGET
		self.removeAll()
	
		#adicionar as colunas e linhas em primeiro lugar para que as celulas sejam criadas	
		#COLUNAS	
		#adicionar as colunas e linhas em primeiro lugar para que as celulas sejam criadas	
		for columnItem in tableData.getTableColumns():
			self.insertColumn(itrColumn)
			self.setHorizontalHeaderItem(itrColumn, QtGui.QTableWidgetItem(columnItem.getText()))
			itrColumn +=1
		
		#LINHAS
		for rowItem in tableData.getTableRows():
			self.insertRow(itrRow)
			self.setVerticalHeaderItem(itrRow, QtGui.QTableWidgetItem(rowItem.getText()))
			itrRow +=1
		
		itrColumn = 0
		itrRow = 0
		#percorrer a estrutura para o preenchimento dos dados na tabelWidget
		tableDataItems = tableData.getTableItems()	
		#Adicionar as colunas à tabela
		for columnItem in tableDataItems.keys():		
			itrRow=0
			#Adicionar as linhas e os respectivos items 
			for rowItem in tableDataItems[columnItem].keys():				
				#Adicionar o item á celula
				self.setItem(itrRow, itrColumn, QtGui.QTableWidgetItem(tableDataItems[columnItem][rowItem].getText()))
			
				itrRow +=1
			itrColumn +=1

	def getRowsList(self):
		rowsList = []
		itr = 0
		#armazenar todas as descrições das linhas	da self	
		while itr < self.rowCount():
			rowsList.append(editItem(QtGui.QTableWidgetItem(self.verticalHeaderItem(itr)).text()))
			itr +=1
			
		return rowsList
		
	def getColumnsList(self):
		columnsList = []
		itr = 0
		#armazenar todas as descrições das linhas	da self	
		while itr < self.columnCount():
			columnsList.append(editItem(QtGui.QTableWidgetItem(self.horizontalHeaderItem(itr)).text()))
			itr +=1
		
		return columnsList


	def removeColumns(self):
		column = 0
		while column < self.columnCount():
			self.removeColumn(column)			
			column +=1
		self.setColumnCount(0)
		self.columns = []
		
	def removeRows(self):
		row = 0
		while row < self.rowCount():
			self.removeRow(row)			
			row +=1
		self.setRowCount(0)
		self.rows = []
		
	def removeAll(self):		
		self.removeRows()
		self.removeColumns()		
		self.clear()
		self.update()
	