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


## Documentation for CTableWidget.
#
# # Custumized Table Widget that herits all properties from Qt QTableWidget.
class CTableWidget(QtGui.QTableWidget):
	
	
	## The constructor.	
	#	
	# @Param parent QWidget reference
	def __init__(self, parent=None):
		QtGui.QTableWidget.__init__(self, parent)
		self.setRowCount(0)
		self.setColumnCount(0)		
		self.columns = []
		self.rows = []
	
	
	##
	# Add a column text to the table.
	#
	# @Param text string
	def addColumn(self, text):
		pos = len(self.columns)
		self.insertColumn(pos)
		self.setHorizontalHeaderItem(pos, QtGui.QTableWidgetItem(text))
		self.columns.append(text)
		
	##
	# Add a row text to the table.
	# Return the position of the new Row
	#
	# @Param text string
	# @Return int	
	def addRow(self, text):		
		pos = len(self.rows)		
		self.insertRow(pos)
		self.setVerticalHeaderItem(pos, QtGui.QTableWidgetItem(text))
		self.rows.append(text)
		
		return pos
		#self.setVerticalHeaderLabels(self.rows)

	##
	# Set a cell item text to be displayed in the given row and column.
	#
	# @Param row int
	# @Param column int
	# @Param text string
	def setItemText(self, row, column, text):
		self.setItem(row, column, QtGui.QTableWidgetItem(text))
	
	
	##
	# Set the content of the table with the information stored in given tableData, that represents the table contents.
	#
	# @Param tableData CTableData
	# @see CTableData
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
			self.setHorizontalHeaderItem(itrColumn, QtGui.QTableWidgetItem(columnItem))
			itrColumn +=1
		
		#LINHAS
		for rowItem in tableData.getTableRows():
			self.insertRow(itrRow)
			self.setVerticalHeaderItem(itrRow, QtGui.QTableWidgetItem(rowItem))
			itrRow +=1
		
		itrColumn = 0
		itrRow = 0
		#percorrer a estrutura para o preenchimento dos dados na tabelWidget
		tableDataItems = tableData.getTableItems()		
		#Adicionar as colunas � tabela
		for columnItem in tableDataItems.keys():		
			itrRow=0
			#Adicionar as linhas e os respectivos items 
			for rowItem in tableDataItems[columnItem].keys():				
				#Adicionar o item � celula
				self.setItem(itrRow, itrColumn, QtGui.QTableWidgetItem(tableDataItems[columnItem][rowItem]))
			
				itrRow +=1
			itrColumn +=1
	
	
	
	
	def setTableWidget_teste(self, tableData):
		
		
		#LIMPAR OS DADOS DA TABLE_WIDGET
		self.removeAll()
		
		tableItems = { }
		#tableItems = tableData.??(...)
		
		listIdCells = tableItems.keys()
		listIdCells.sort()
		nColumns = -1
		nLines = -1
		for IdCell in listIdCells:
			if IdCell[0] > nLines:
				nLines =IdCell[0]

			if IdCell[1] > nColumns:
				nColumns = IdCell[1]
			
		
		#Criar colunas na tableWidget
		n=0
		while n < nColumns:
			self.insertRow(n)
			self.setVerticalHeaderItem(n, QtGui.QTableWidgetItem(tableItems[(0,n)]))
			itrRow +=1
			
		#Criar linhas na tableWidget
		n=0		
		while n < nLines:
			self.insertColumn(n)
			self.setHorizontalHeaderItem(n, QtGui.QTableWidgetItem(tableItems[(n,0)]))
			n +=1
		
		nL=0
		nC=0		
		while nC < nColumns: #??- OU WHILE nC <=nColumns:
		
		   
			while nL < nLines: #??- OU WHILE nL <=nLines:
				#Adicionar o item � celula
				self.setItem(nL, nC, QtGui.QTableWidgetItem(tableItems[(nL,nC)]))
				nL+=1
			
			nL=0
			nC +=1    
		
	
	#***************************************************************************
	
	##
	# Get the content of the table.
	#
	# @Return CTableData
	# @see CTableData
	def getTableData(self):
			
		tableItems = { }
		
		rowsList = []
		rowsList = self.getRowsList()
		columnsList = []
		columnsList = self.getColumnsList()
		
		itrColumn = 0
		itrRow = 0
		#copiar todos os items da self
		while itrColumn < self.columnCount():
			columnItem = QStringToString(QtGui.QTableWidgetItem(self.horizontalHeaderItem(itrColumn)).text())			
			itrRow = 0
			tableItems[columnItem] = {}
			for rowItem in rowsList:
				tableItem = self.item(itrRow, itrColumn) #Obter o item da tabela				
				if tableItem == None:
					tableItem = QtGui.QTableWidgetItem("")
				cellItem = QStringToString(QtGui.QTableWidgetItem(tableItem).text())
				tableItems[columnItem].update({rowItem: cellItem})
				itrRow +=1
				
			itrColumn +=1
		
		#print tableItems
		
		#tableData = CTableData(rowsList, columnsList, tableItems)
		tableData = CTableData()
		tableData.setTableRows(rowsList)		
		tableData.setTableColumns(columnsList)
		tableData.setTableItems(tableItems)
		
		self.getTableData_teste_dict()
		
		return tableData
	
	
	def getTableData_teste_dict(self):
		
		tableItems = { }
		
		rowsList = []
		rowsList = self.getRowsList()
		columnsList = []
		columnsList = self.getColumnsList()
		
		itrColumn = 1
		itrRow = 1
		for column in columnsList:
			tableItems[(0,itrColumn)] = column #Preencher campos de colunas identificadoras        
			for line in rowsList:
				tableItems[(itrRow,0)] = line #Preencher campos de linhas identificadores
				idCel = (itrColumn, itrRow)
				#Obter elemento da linha,coluna				
				tableItem = self.item(itrRow-1, itrColumn-1) #Obter o item da tabela				
				if tableItem == None:
					tableItem = QtGui.QTableWidgetItem("")
				cellItem = QStringToString(QtGui.QTableWidgetItem(tableItem).text())
				print cellItem
				tableItems[idCel] = cellItem
		
				itrRow +=1
			
			itrRow=1
			itrColumn +=1
		
		#tableData = CTableData()
		#return tableData 
	
	

##
	# Get the rows text of the table.
	#
	# @Return python list
	def getRowsList(self):
		rowsList = []
		itr = 0
		#armazenar todas as descri��es das linhas	da self	
		while itr < self.rowCount():
			rowsList.append(QStringToString(QtGui.QTableWidgetItem(self.verticalHeaderItem(itr)).text()))
			itr +=1
			
		return rowsList
	

	##
	# Get the rows text of the table.
	#
	# @Return python list
	def getColumnsList(self):
		columnsList = []
		itr = 0
		#armazenar todas as descri��es das linhas	da self	
		while itr < self.columnCount():
			columnsList.append(QStringToString(QtGui.QTableWidgetItem(self.horizontalHeaderItem(itr)).text()))
			itr +=1
		
		return columnsList


	
	def clearHorizontalTableItems(self):
		self.clear()
		self.setHorizontalHeaderLabels(self.columns)
	
	def clearVerticalTableItems(self):
		self.clear()
		self.setVerticalHeaderLabels(self.rows)


	##
	# Remove all Columns from the table.
	def removeColumns(self):
		column = 0
		while column < self.columnCount():
			self.removeColumn(column)			
			column +=1
		self.setColumnCount(0)
		self.columns = []
	
	##
	# Remove all Rows from the table.
	def removeRows(self):
		row = 0
		while row < self.rowCount():
			self.removeRow(row)			
			row +=1
		self.setRowCount(0)
		self.rows = []
		
	##
	# Clear all the content from the table.
	def removeAll(self):		
		self.removeRows()
		self.removeColumns()		
		self.clear()
		self.update()
	
	
	
	
	