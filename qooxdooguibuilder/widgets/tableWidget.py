#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from exceptions import *
from editItem import *
from tableData import *
from listWidget import *



class CTableWidget(QtGui.QTableWidget):
	def __init__(self, parent=None):
		QtGui.QTableWidget.__init__(self, parent)
		self.setRowCount(0)
		self.setColumnCount(0)		
		self.columns = []
		self.rows = []
	
	def addColumn(self, text):
		self.insertColumn(len(self.columns))
		self.columns.append(text)
		self.setHorizontalHeaderLabels(self.columns)
	
	def addRow(self, text):
		self.insertRow(len(self.rows))
		self.rows.append(text)
		self.setVerticalHeaderLabels(self.rows)

	
	def setItem(self, row, column, text):
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
		
		tableData = CTableData(rowsList, columnsList, tableItems)
		return tableData
	
	def setTableWidget(self, tableData):
		
		itrColumn = 0
		itrRow = 0	
		
		#LIMPAR OS DADOS DA self
		self.clear()
		self.setRowCount(0)
		self.setColumnCount(0)
		
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
