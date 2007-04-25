#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import *
from projectExceptions import *
from tableData import *

def ListToQStringList(pList):
	try:
		qtList = QtCore.QStringList()
		
		for item in pList:
			qtList.append(item)
		
		return qtList
		
	except:
		raise structureError_Exception(structureError, ERROR_ACCESS_STRUCTURE)
		return structureError
		

def QStringListToList(qtList):
	try:
		list = []
		
		#qtList = QtCore.QStringList(qtList)
		nElements = qtList.count()
		elem = 0		
		while elem < nElements:
			list.append(str(qtList.takeFirst()))
			elem = elem +1
					
		return list
		
	except:
		raise structureError_Exception(structureError, ERROR_ACCESS_STRUCTURE)
		return structureError
		


def indexValidation(index, structureCount):
	if index < 0 or index >= structureCount:
		return false
	return true


"""
#FUNÇÕES SOBRE TABLEWIDGETs	
def getTableData(tableWidget): #alterar função de forma a retornar um objecto do tipo tableData
		
	tableItems = { }
	
	rowsList = []
	rowsList = getRowsFromTableWidget(tableWidget)
	columnsList = []
	columnsList = getColumnsFromTableWidget(tableWidget)
	
	itrColumn = 0
	itrRow = 0
	#copiar todos os items da tableWidget
	while itrColumn < tableWidget.columnCount():
		columnItem = editItem(QtGui.QTableWidgetItem(tableWidget.horizontalHeaderItem(itrColumn)).text())
		itrRow = 0 
		tableItems[columnItem] = {}
		for rowItem in rowsList:
			tableItem = tableWidget.item(itrRow, itrColumn)
			if tableItem == None:
				tableItem = QtGui.QTableWidgetItem("")
			cellItem = editItem(QtGui.QTableWidgetItem(tableItem).text())
			tableItems[columnItem].update({rowItem: cellItem})
			itrRow +=1
			
		itrColumn +=1
	
	tableData = CTableData(rowsList, columnsList, tableItems)
	return tableData

def setTableWidget(tableWidget, tableData):
	
	itrColumn = 0
	itrRow = 0	
	
	#LIMPAR OS DADOS DA TABLEWIDGET
	tableWidget.clear()
	tableWidget.setRowCount(0)
	tableWidget.setColumnCount(0)
	
	#adicionar as colunas e linhas em primeiro lugar para que as celulas sejam criadas	
	#COLUNAS	
	#adicionar as colunas e linhas em primeiro lugar para que as celulas sejam criadas	
	for columnItem in tableData.getTableColumns():
		tableWidget.insertColumn(itrColumn)
		tableWidget.setHorizontalHeaderItem(itrColumn, QtGui.QTableWidgetItem(columnItem.getText()))
		itrColumn +=1
	
	#LINHAS
	for rowItem in tableData.getTableRows():
		tableWidget.insertRow(itrRow)
		tableWidget.setVerticalHeaderItem(itrRow, QtGui.QTableWidgetItem(rowItem.getText()))
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
			tableWidget.setItem(itrRow, itrColumn, QtGui.QTableWidgetItem(tableDataItems[columnItem][rowItem].getText()))
		
			itrRow +=1
		itrColumn +=1
	

def getRowsFromTableWidget(tableWidget):
	rowsList = []
	itr = 0
	#armazenar todas as descrições das linhas	da tableWidget	
	while itr < tableWidget.rowCount():
		rowsList.append(editItem(QtGui.QTableWidgetItem(tableWidget.verticalHeaderItem(itr)).text()))
		itr +=1
	
	return rowsList
	
	
def getColumnsFromTableWidget(tableWidget):
	columnsList = []
	itr = 0
	#armazenar todas as descrições das linhas	da tableWidget	
	while itr < tableWidget.columnCount():
		columnsList.append(editItem(QtGui.QTableWidgetItem(tableWidget.horizontalHeaderItem(itr)).text()))
		itr +=1
	
	return columnsList


#FUNÇÕES SOBRE LISTWIDGETs
def setListWidget(listWidget, itemsList):	
	for item in itemsList:
		listWidget.addItem(str(item.getText()))

def getListWidgetItems(listWidget):
	
	itemsList = []
	
	elem = 0
	nElements =  listWidget.count()				
	while elem < nElements:
		item = listWidget.item(elem)
		itemsList.append(editItem(str(item.text())))
		
	return itemsList

"""