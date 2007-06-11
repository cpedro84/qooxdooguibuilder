#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from generalFunctions import *
from tableData import *
from tableWidget import *


class CEditTableItemsWidget(QtGui.QDialog):
		
	def __init__(self, windowTitle, parent=None, inicialTableData = { }):
		
		QtGui.QDialog.__init__(self, parent)		
		
		self.setWindowTitle(windowTitle)
		self.setWindowIcon(QtGui.QIcon("icons/editors.png"))
		
		#FIXAR O TAMANHO DA WIDGET AO TAMANHO ACTUAL
		self.setFixedSize(513, 292)
		
		self.originalTableData = { }
		self.originalItemsList = inicialTableData
		self.tableData = { }
		self.tableData = inicialTableData		
		
		self.newItemText = "New Item"
		self.newColumnText = "New Column"
		self.newRowText = "New Row"
		
		self.ColumnTypeItem = 1
		self.RowTypeItem = 2
				
		self.noItem = -1
		self.firstElement = 0		
		
		#Estados possivies sobre os botões de Rename/Apply
		self.ApplyState = "Apply"
		self.RenameState = "Rename"		
		self.btnColumnState = self.ApplyState
		self.btnRowState = self.ApplyState
		#*************CONTROLOS DA INTERFACE*********************		
		#definição das posições iniciais e seuas tamanhos
		self.RTableItemsGroupBox = QtCore.QRect(10,10,271,241)
		self.RTableItems = QtCore.QRect(10,30,251,200)
		self.RLabelText = QtCore.QRect(10, 190,221,20)
		self.RLineEdit = QtCore.QRect(40,190,221,20)
		
		self.RColumnsGroupBox = QtCore.QRect(290,10,221,121)
		self.RColumnsList = QtCore.QRect(10,20,141,71)
		self.RColumnsBtnUp = QtCore.QRect(160,20,41,21)
		self.RColumnsBtnDown = QtCore.QRect(160,50,41,21)
		self.RColumnsBtnAdd = QtCore.QRect(10,100,31,16)
		self.RColumnsBtnRemove = QtCore.QRect(50,100,31,16)
		self.RColumnsBtnRename = QtCore.QRect(90,100,61,16)
		
		self.RRowsGroupBox = QtCore.QRect(290,130,221,121)
		self.RRowsList = QtCore.QRect(10,20,141,71)
		self.RRowsBtnUp = QtCore.QRect(160,20,41,21)
		self.RRowsBtnDown = QtCore.QRect(160,50,41,21)
		self.RRowsBtnAdd = QtCore.QRect(10,100,31,16)
		self.RRowsBtnRemove = QtCore.QRect(50,100,31,16)
		self.RRowsBtnRename = QtCore.QRect(90,100,61,16)		
		
		self.ROkButton = QtCore.QRect(350,260,77,25)
		self.RCancelButton = QtCore.QRect(430,260,77,25)
		
		#GROUPBOX TABLE ITEMS
		self.TableItemsGroupBox = QtGui.QGroupBox("Table Items:", self)
		self.TableItemsGroupBox.setGeometry(self.RTableItemsGroupBox)		
		#table Items
		self.TableItems = CTableWidget(self.TableItemsGroupBox)
		self.TableItems.setGeometry(self.RTableItems)		
		#self.connect(self.TableItems, QtCore.SIGNAL("itemClicked(QTableWidgetItem *)"), self.SLOT_setLineEditText)
		
		
		#Label Text
		#self.LabelText = QtGui.QLabel("Text:", self.TableItemsGroupBox)
		#self.LabelText.setGeometry(self.RLabelText)
		#Line Edit
		#self.textInput = QtGui.QLineEdit(self.TableItemsGroupBox)
		#self.textInput.setGeometry(self.RLineEdit)		
		
		
		#GROUPBOX COLUMNS
		self.ColumnsGroupBox = QtGui.QGroupBox("Columns:", self)
		self.ColumnsGroupBox.setGeometry(self.RColumnsGroupBox)		
		#ListWidget
		self.ListColumns = CListWidget(self.ColumnsGroupBox)
		self.ListColumns.setGeometry(self.RColumnsList)
		self.connect(self.ListColumns, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.SLOT_startColumnEditMode)
		self.connect(self.ListColumns, QtCore.SIGNAL("itemSelectionChanged()"), self.SLOT_endColumnEditMode)
		#self.connect(self.ListColumns, QtCore.SIGNAL("currentTextChanged(const QString&)"), self.SLOT_changeColumnText)
		self.connect(self.ListColumns, QtCore.SIGNAL("currentItemChanged(QListWidgetItem *, QListWidgetItem *)"),  self.SLOT_currentColumnItemChanged)
		#BtnUp
		self.upColumnsButton = QtGui.QPushButton("Up", self.ColumnsGroupBox)
		self.upColumnsButton.setGeometry(self.RColumnsBtnUp)
		self.connect(self.upColumnsButton, QtCore.SIGNAL("clicked()"), self.SLOT_moveColumnUp)
		#BtnDown
		self.downColumnsButton = QtGui.QPushButton("Down", self.ColumnsGroupBox)
		self.downColumnsButton.setGeometry(self.RColumnsBtnDown)
		self.connect(self.downColumnsButton, QtCore.SIGNAL("clicked()"), self.SLOT_moveColumnDown)
		#BtnAdd
		self.addItemColumnsButton = QtGui.QPushButton("+", self.ColumnsGroupBox)
		self.addItemColumnsButton.setGeometry(self.RColumnsBtnAdd)
		self.connect(self.addItemColumnsButton, QtCore.SIGNAL("clicked()"), self.SLOT_addColumnItem)
		#BtnRemove
		self.removeItemColumnsButton = QtGui.QPushButton("-", self.ColumnsGroupBox)
		self.removeItemColumnsButton.setGeometry(self.RColumnsBtnRemove)
		self.connect(self.removeItemColumnsButton, QtCore.SIGNAL("clicked()"), self.SLOT_removeColumnItem)
		#BtnRename
		self.renameColumnsButton = QtGui.QPushButton(self.ApplyState, self.ColumnsGroupBox)
		self.renameColumnsButton.setGeometry(self.RColumnsBtnRename)
		self.renameColumnsButton.setEnabled(false)
		self.connect(self.renameColumnsButton, QtCore.SIGNAL("clicked()"), self.SLOT_changeStateBtnColumn)
		
		#GROUPBOX ROWS
		self.RowsGroupBox = QtGui.QGroupBox("Rows:", self)
		self.RowsGroupBox.setGeometry(self.RRowsGroupBox)
		#ListWidget
		self.ListRows = CListWidget(self.RowsGroupBox)
		self.ListRows.setGeometry(self.RRowsList)
		self.connect(self.ListRows, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.SLOT_startRowEditMode)
		self.connect(self.ListRows, QtCore.SIGNAL("itemSelectionChanged()"), self.SLOT_endRowEditMode)		
		#self.connect(self.ListRows, QtCore.SIGNAL("currentTextChanged(const QString&)"), self.SLOT_changeRowText)
		self.connect(self.ListRows, QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,QListWidgetItem *)"),  self.SLOT_currentRowItemChanged)
		#BtnUp
		self.upRowsButton = QtGui.QPushButton("Up", self.RowsGroupBox)
		self.upRowsButton.setGeometry(self.RRowsBtnUp)
		self.connect(self.upRowsButton, QtCore.SIGNAL("clicked()"), self.SLOT_moveRowUp)
		#BtnDown
		self.downRowsButton = QtGui.QPushButton("Down", self.RowsGroupBox)
		self.downRowsButton.setGeometry(self.RRowsBtnDown)
		self.connect(self.downRowsButton, QtCore.SIGNAL("clicked()"), self.SLOT_moveRowDown)
		#BtnAdd
		self.addItemRowsButton = QtGui.QPushButton("+", self.RowsGroupBox)
		self.addItemRowsButton.setGeometry(self.RRowsBtnAdd)
		self.connect(self.addItemRowsButton, QtCore.SIGNAL("clicked()"), self.SLOT_addRowItem)
		#BtnAdd
		self.removeItemRowsButton = QtGui.QPushButton("-", self.RowsGroupBox)
		self.removeItemRowsButton.setGeometry(self.RRowsBtnRemove)
		self.connect(self.removeItemRowsButton, QtCore.SIGNAL("clicked()"), self.SLOT_removeRowItem)
		#BtnRename
		self.renameRowsButton = QtGui.QPushButton(self.ApplyState, self.RowsGroupBox)
		self.renameRowsButton.setGeometry(self.RRowsBtnRename)
		self.renameRowsButton.setEnabled(false)
		self.connect(self.renameRowsButton, QtCore.SIGNAL("clicked()"), self.SLOT_changeStateBtnRow)
				
		#BtnOK
		self.okButton = QtGui.QPushButton("OK", self)		
		self.okButton.setGeometry(self.ROkButton)
		self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.SLOT_applyChanges)
		#BtnCancel
		self.cancelButton = QtGui.QPushButton("Cancel", self)		
		self.cancelButton.setGeometry(self.RCancelButton)
		self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.SLOT_cancelChanges)
	
			
		#carregar dados iniciais para a tabela
		self.inicializeTableData(inicialTableData)
	

	def inicializeTableData(self, tableData):
		self.TableItems.setTableWidget(tableData)
		
		#Inicializar a lista com as colunas
		listColumns_ = []
		for column in tableData.getTableColumns():
			listColumns_.append(CEditItem(column))
		self.ListColumns.setListWidget(listColumns_)
		
		#Inicializar lista com as linhas
		listRows_ = []
		for column in tableData.getTableRows():
			listRows_.append(CEditItem(column))
		self.ListRows.setListWidget(listRows_)
		
		if self.ListColumns.count() > 0:
			self.renameColumnsButton.setEnabled(true)
			
		if self.ListRows.count() > 0:
			self.renameRowsButton.setEnabled(true)
	
	#TRATAMENTO DOS SINAIS
	#SLOTS
	def SLOT_addColumnItem(self):
		self.addListItem(self.ColumnTypeItem, self.ListColumns)
		self.renameColumnsButton.setEnabled(true)

	def SLOT_removeColumnItem(self):
		self.removeListItem(self.ColumnTypeItem, self.ListColumns)
		
		#Caso o nº de items após remoção seja igual a 0 então alguns controlos ficaram inactivos
		if self.ListColumns.count() == 0:
			self.renameColumnsButton.setEnabled(false)
		
	def SLOT_addRowItem(self):
		self.addListItem(self.RowTypeItem, self.ListRows)
		self.renameRowsButton.setEnabled(true)

	def SLOT_removeRowItem(self):
		self.removeListItem(self.RowTypeItem, self.ListRows) 
		#Caso o nº de items após remoção seja igual a 0 então alguns controlos ficaram inactivos		
		if self.ListRows.count() == 0:
			self.renameRowsButton.setEnabled(false)

	def SLOT_moveColumnUp(self):
		self.moveListItemUp(self.ColumnTypeItem, self.ListColumns)
		
	def SLOT_moveColumnDown(self):
		self.moveListItemDown(self.ColumnTypeItem, self.ListColumns)
		
	def SLOT_moveRowUp(self):
		self.moveListItemUp(self.RowTypeItem, self.ListRows)
		
	def SLOT_moveRowDown(self):
		self.moveListItemDown(self.RowTypeItem, self.ListRows)
		
	def SLOT_startColumnEditMode(self, listWidgetItem=None):
		#self.ListColumns.editItem(listWidgetItem)		
		if listWidgetItem == None:
			listWidgetItem  = self.ListColumns.currentItem()
		
		self.ListColumns.openPersistentEditor(listWidgetItem)
		self.changeStateBtnColumn()	
		
	def SLOT_endColumnEditMode(self):		
		self.ListColumns.closePersistentEditor(self.ListColumns.currentItem())		
		if self.btnColumnState == self.ApplyState:
			self.changeStateBtnColumn()
		
	def SLOT_startRowEditMode(self, listWidgetItem=None):
		#self.ListRows.editItem(listWidgetItem)
		if listWidgetItem == None:
			listWidgetItem  = self.ListRows.currentItem()
		
		self.ListRows.openPersistentEditor(listWidgetItem)
		self.changeStateBtnRow()
		
	def SLOT_endRowEditMode(self):
		self.ListRows.closePersistentEditor(self.ListRows.currentItem())
		if self.btnRowState == self.ApplyState:
			self.changeStateBtnRow()
		
	#slot que efectua a alteração do texto da respectiva coluna na tableWidget de acordo com o texto editado na listWidget
	def SLOT_changeColumnText(self, text):
		currentRow = self.ListColumns.currentRow()		
		if currentRow  == self.noItem:
			return
	
		self.TableItems.setHorizontalHeaderItem(currentRow, QtGui.QTableWidgetItem(text) )
	
	def SLOT_changeRowText(self, text):
		currentRow = self.ListRows.currentRow()		
		if currentRow  == self.noItem:
			return
	
		self.TableItems.setVerticalHeaderItem(currentRow, QtGui.QTableWidgetItem(text) )
	
	
	def SLOT_currentColumnItemChanged(self, currentColumn, previousColumn):
		#alterar na tableWidget o texto da coluna de acordo com o item posterior		
		if previousColumn  == None:
			return		
		previousListRow = self.ListColumns.row(previousColumn)
		self.TableItems.setHorizontalHeaderItem(previousListRow, QtGui.QTableWidgetItem(previousColumn.text()))
		
	def SLOT_currentRowItemChanged(self, currentRow, previousRow):
		#alterar na tableWidget o texto da coluna de acordo com o item posterior
		if previousRow == None:
			return
		previousListRow = self.ListRows.row(previousRow)
		self.TableItems.setVerticalHeaderItem(previousListRow, QtGui.QTableWidgetItem(previousRow.text()))
	
	
	def SLOT_changeStateBtnColumn(self):
		
		if self.btnColumnState == self.RenameState:			
			listWidgetItem  = self.ListColumns.currentItem()
			self.ListColumns.openPersistentEditor(listWidgetItem)
			self.ListColumns.setFocus()
			self.renameColumnsButton.setText(self.ApplyState)
			self.btnColumnState = self.ApplyState
		elif self.btnColumnState == self.ApplyState:			
			self.ListColumns.closePersistentEditor(self.ListColumns.currentItem())
			self.renameColumnsButton.setText(self.RenameState)
			self.renameColumnsButton.setFocus()
			self.btnColumnState = self.RenameState
			
	def SLOT_changeStateBtnRow(self):
		
		if self.btnRowState == self.RenameState:			
			listWidgetItem  = self.ListRows.currentItem()
			self.ListRows.openPersistentEditor(listWidgetItem)
			self.ListRows.setFocus()
			self.renameRowsButton.setText(self.ApplyState)
			self.btnRowState = self.ApplyState
		elif self.btnRowState == self.ApplyState:			
			self.ListRows.closePersistentEditor(self.ListRows.currentItem())
			self.renameRowsButton.setText(self.RenameState)
			self.renameRowsButton.setFocus()
			self.btnRowState = self.RenameState
	
	def SLOT_setLineEditText(self, itemTable):
		self.textInput.setText(itemTable.text())
		self.textInput.setFocus()
	
	def SLOT_cancelChanges(self):
		#self.ItemsList = self.originalItemsList
		self.reject()

	def SLOT_applyChanges(self):
		
		"""#Aplicar as alterações efectuadas no ecra aos items armazenados na lista(...)
		elem = 0
		nElements =  self.itemsListView.count()				
		while elem < nElements:
			item = self.itemsListView.item(elem)
			self.ItemsList[elem].setText(str(item.text()))			
			#Alterar/Acrescentar futuros tipos de items (ex: icones)
			
			elem+=1
		"""
		self.accept()
		
		
	#METODOS PARA O CONTROLOS DAS LISTWIDGET QUE ARMAZENAM AS INFORMAÇÕES DAS COLUNAS E DAS LINHAS DA TABELA		
	def addListItem(self, itemType, listWidget):		
		
		itemText = ""
		
		#Verificar qual o tipo de item a ser adicionado (COLUMN ou ROW)
		if itemType == self.ColumnTypeItem:
			itemText = self.newColumnText
			#Adicionar a coluna na tableWidget			
			self.TableItems.insertColumn(self.TableItems.columnCount())			
			self.TableItems.setHorizontalHeaderItem(self.TableItems.columnCount()-1, QtGui.QTableWidgetItem(itemText) )
			
		elif itemType == self.RowTypeItem:
			itemText = self.newRowText
			#Adicionar a linha na tableWidget
			self.TableItems.insertRow(self.TableItems.rowCount())			
			self.TableItems.setVerticalHeaderItem(self.TableItems.rowCount()-1, QtGui.QTableWidgetItem(itemText) )
		
		#Adicionar à ListWidget o novo item
		listWidget.addItem(itemText)
		
		#focar na ListWidget o novo Item
		self.setSelectedListItem(listWidget, listWidget.count()-1)
		
	
		
		#self.ItemsList.append(editItem(self.newItemText))
		
			
	def removeListItem(self, itemType, listWidget):		
		currentRow = listWidget.currentRow()
		
		if currentRow  == self.noItem:
			return false
		
		#remover o item da tableWidget
		if itemType == self.ColumnTypeItem:
			self.TableItems.removeColumn(currentRow)
		elif itemType == self.RowTypeItem:
			self.TableItems.removeRow(currentRow)
				
		#remover o item da ListWidget
		listWidget.takeItem(currentRow)
				
		return true
		#self.self.ItemsList.pop(currentRow)
		#ELIMINAR ITEM DA LISTA DE REFERÊNCIA
		#self.refList.pop(currentRow)

	
	def moveListItemDown(self, itemType, listWidget):
		currentRow = listWidget.currentRow()
		nElements =  listWidget.count()
		if currentRow == self.noItem or currentRow == nElements-1 or nElements == 1:
			return false
		
		#nextItem = QtGui.QListWidgetItem(self.itemsListView.item(currentRow+1))
		nextItem = listWidget.item(currentRow+1)

		listWidget.takeItem(currentRow+1)
		listWidget.insertItem(currentRow, nextItem)



		if itemType == self.ColumnTypeItem:
			#****Mover os items da tableWidget - COLUMN
			previousColumnItem = QtGui.QTableWidgetItem(self.TableItems.horizontalHeaderItem(currentRow+1))
			
			listTableItems = []			
			itr = 0
			#copiar todos os items da tableWidget relativo à coluna anterior
			while itr < self.TableItems.columnCount():
				tableItem = self.TableItems.item(itr, currentRow+1)
				if tableItem == None: #para o caso de o item ser None (quando as celulas da tabela estão vazias) então serão criados items 
					tableItem = QtGui.QTableWidgetItem("")				
				listTableItems.append(QtGui.QTableWidgetItem(tableItem))
				itr =itr + 1
			
			#eliminar coluna na tabela
			self.TableItems.removeColumn(currentRow+1)
			#inserir a coluna anterior na posição corrente
			self.TableItems.insertColumn(currentRow)			
			self.TableItems.setHorizontalHeaderItem(currentRow, previousColumnItem)
			#adicionar os items à tabela
			itr=0
			for item in listTableItems:
				self.TableItems.setItem(itr, currentRow, item)
				itr =itr + 1
			#********************************************
			
			
		elif itemType == self.RowTypeItem:
			#****Mover os items da tableWidget - ROW
			previousRowItem = QtGui.QTableWidgetItem(self.TableItems.verticalHeaderItem(currentRow+1))
			
			listTableItems = []			
			itr = 0
			#copiar todos os items da tableWidget relativo à coluna anterior
			while itr < self.TableItems.rowCount():
				tableItem = self.TableItems.item(currentRow+1, itr)
				if tableItem == None: #para o caso de o item ser None (quando as celulas da tabela estão vazias) então serão criados items 
					tableItem = QtGui.QTableWidgetItem("")
				listTableItems.append(QtGui.QTableWidgetItem(tableItem))			
				itr =itr + 1

			#eliminar coluna na tabela
			self.TableItems.removeRow(currentRow+1)
			#inserir a coluna anterior na posição corrente
			self.TableItems.insertRow(currentRow)
			self.TableItems.setVerticalHeaderItem(currentRow, previousRowItem)
			#adicionar os items à tabela
			itr=0			
			for item in listTableItems:
				self.TableItems.setItem(currentRow, itr, item)				
				itr = itr + 1


		return true

		#ALTERAR ORDENAÇÃO DA LISTA DE REFERÊNCIA
		#tmpItem = self.ItemsList[currentRow+1]
		#self.ItemsList.pop(currentRow+1)
		#self.ItemsList.insert(currentRow, tmpItem)		
		
		
	def moveListItemUp(self, itemType, listWidget):
		currentRow = listWidget.currentRow()
		nElements =  listWidget.count()
		if currentRow == self.noItem or currentRow == self.firstElement or nElements == 1:
			return false
		
		#previousItem = QtGui.QListWidgetItem(self.itemsListView.item(currentRow-1))
		previousItem = listWidget.item(currentRow-1)
		
		listWidget.takeItem(currentRow-1)
		listWidget.insertItem(currentRow, previousItem)		
		
		
		if itemType == self.ColumnTypeItem:
			#****Mover os items da tableWidget - COLUMN
			previousColumnItem = QtGui.QTableWidgetItem(self.TableItems.horizontalHeaderItem(currentRow-1))
			
			listTableItems = []			
			itr = 0
			#copiar todos os items da tableWidget relativo à coluna anterior
			while itr < self.TableItems.columnCount():
				tableItem = self.TableItems.item(itr, currentRow-1)
				if tableItem == None: #para o caso de o item ser None (quando as celulas da tabela estão vazias) então serão criados items 
					tableItem = QtGui.QTableWidgetItem("")				
				listTableItems.append(QtGui.QTableWidgetItem(tableItem))
				itr =itr + 1
			
			#eliminar coluna na tabela
			self.TableItems.removeColumn(currentRow-1)
			#inserir a coluna anterior na posição corrente
			self.TableItems.insertColumn(currentRow)			
			self.TableItems.setHorizontalHeaderItem(currentRow, previousColumnItem)
			#adicionar os items à tabela
			itr=0
			for item in listTableItems:
				self.TableItems.setItem(itr, currentRow, item)
				itr =itr + 1
			#********************************************
			
			
		elif itemType == self.RowTypeItem:
			#****Mover os items da tableWidget - ROW
			previousRowItem = QtGui.QTableWidgetItem(self.TableItems.verticalHeaderItem(currentRow-1))
			
			listTableItems = []			
			itr = 0
			#copiar todos os items da tableWidget relativo à coluna anterior
			while itr < self.TableItems.rowCount():
				tableItem = self.TableItems.item(currentRow-1, itr)
				if tableItem == None: #para o caso de o item ser None (quando as celulas da tabela estão vazias) então serão criados items 
					tableItem = QtGui.QTableWidgetItem("")
				listTableItems.append(QtGui.QTableWidgetItem(tableItem))			
				itr =itr + 1

			#eliminar coluna na tabela
			self.TableItems.removeRow(currentRow-1)
			#inserir a coluna anterior na posição corrente
			self.TableItems.insertRow(currentRow)
			self.TableItems.setVerticalHeaderItem(currentRow, previousRowItem)
			#adicionar os items à tabela
			itr=0			
			for item in listTableItems:
				self.TableItems.setItem(currentRow, itr, item)				
				itr = itr + 1
				
				
		return true

		#ALTERAR ORDENAÇÃO DA LISTA DE REFERÊNCIA
		#tmpItem = self.ItemsList[currentRow-1]
		#self.ItemsList.pop(currentRow-1)
		#self.ItemsList.insert(currentRow, tmpItem)

		

	def setSelectedListItem(self, listWidget, row = 0):
		if row >=0 and row < listWidget.count():
			listWidget.setItemSelected(listWidget.item(row), true)
			listWidget.setCurrentItem(listWidget.item(row))
		else:
			return
			
			
	def changeStateBtnColumn(self):
		
		if self.btnColumnState == self.RenameState:			
			self.renameColumnsButton.setText(self.ApplyState)
			self.btnColumnState = self.ApplyState
		elif self.btnColumnState == self.ApplyState:			
			self.renameColumnsButton.setText(self.RenameState)
			self.btnColumnState = self.RenameState
			
	def changeStateBtnRow(self):
		
		if self.btnRowState == self.RenameState:			
			self.renameRowsButton.setText(self.ApplyState)
			self.btnRowState = self.ApplyState
		elif self.btnRowState == self.ApplyState:			
			self.renameRowsButton.setText(self.RenameState)
			self.btnRowState = self.RenameState
	
	
	def getTableData(self):
		return self.TableItems.getTableData()
	
	
#main
"""
app = QtGui.QApplication(sys.argv)
dataItems = { editItem("c1") : {editItem("r1"):editItem("cell_1_1"), editItem("r2"):editItem("cell_1_2")},   editItem("c2") : {editItem("r1"):editItem("cell_1_1")}}

data = CTableData()
data.setTableItems(dataItems)
data.setTableRows([editItem("r1"),editItem("r2")])
data.setTableColumns([editItem("c1"), editItem("c2")])


widget = CEditTableItemsWidget("Window Table Items", None, data )
widget.exec_()
print widget.getTableData()
widget.done(QtGui.QDialog.Accepted)

sys.exit(app.exec_())
"""