#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from listWidget import *


class editItemsWidget(QtGui.QDialog):
		
	def __init__(self, windowTitle, parent=None,  initialItemsList = [], itemDesignation = "Items"):
		
		QtGui.QDialog.__init__(self, parent)		
		
		self.setWindowTitle(windowTitle)				
		
		self.originalItemsList = []
		self.originalItemsList = initialItemsList
		self.ItemsList = [ ]
		self.ItemsList = initialItemsList
	
		self.newItemText = "New Item"
			
		self.noItem = -1
		self.firstElement = 0		
		
		self.ItemsGroupBox = QtGui.QGroupBox(itemDesignation+":", self)
		self.ItemsGroupBox.setGeometry(10,10,290,250)
		
		#LISTA COM OS ITEMS
		self.itemsListView = CListWidget(self.ItemsGroupBox)
		self.itemsListView.setGeometry(10,20,210,190)		
		#Processamento dos sinais emitidos pela ListWidget
		self.connect(self.itemsListView, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.listItemDoubleClicked)
		self.connect(self.itemsListView, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.listItemClicked)
		self.connect(self.itemsListView, QtCore.SIGNAL("itemSelectionChanged()"), self.listItemSelectionChanged)
		self.connect(self.itemsListView, QtCore.SIGNAL("currentTextChanged(const QString&)"), self.listItemTextChanged)
		
		#DEFINIÇÃO DOS BOTÕES
		self.okButton = QtGui.QPushButton("OK", self)		
		self.okButton.setGeometry(130, 270, 80, 25)
		self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.applyChanges)
		
		self.cancelButton = QtGui.QPushButton("Cancel", self)		
		self.cancelButton.setGeometry(220,270,80,25)
		self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancelChanges)
		
		self.addItemButton = QtGui.QPushButton("+", self.ItemsGroupBox)
		self.addItemButton.setGeometry(180, 220, 40, 20)
		self.connect(self.addItemButton, QtCore.SIGNAL("clicked()"), self.addTextItem)
				
		self.deleteItemButton = QtGui.QPushButton("-", self.ItemsGroupBox)
		self.deleteItemButton.setGeometry(230, 220, 50, 20)
		self.connect(self.deleteItemButton, QtCore.SIGNAL("clicked()"), self.deleteTextItem)
		
		self.upButton = QtGui.QPushButton("Up", self.ItemsGroupBox)
		self.upButton.setGeometry(230, 20, 50, 20)
		self.connect(self.upButton, QtCore.SIGNAL("clicked()"), self.moveItemUp)
		
		self.downButton = QtGui.QPushButton("Down", self.ItemsGroupBox)
		self.downButton.setGeometry(230, 50, 50, 20)
		self.connect(self.downButton, QtCore.SIGNAL("clicked()"), self.moveItemDown)
		
		self.textInput = QtGui.QLineEdit(self.ItemsGroupBox)
		self.textInput.setGeometry(40, 220, 130, 20)
		self.connect(self.textInput, QtCore.SIGNAL("textEdited(const QString&)"), self.setTextOnListItem)

		
		self.labelText = QtGui.QLabel("Text:", self.ItemsGroupBox)
		self.labelText.setGeometry(10, 220, 30, 20)
							
		#FIXAR O TAMANHO DA WIDGET AO TAMANHO ACTUAL
		self.setFixedSize(310, 300)		
		
		#carregar lista com os items enviados por parametro (caso existam)
		self.inicializeItems(initialItemsList)		
	
	#************SLOTS*****************
	def listItemDoubleClicked(self, listWidgetItem):
		self.itemsListView.openPersistentEditor(listWidgetItem)
		self.itemsListView.editItem(listWidgetItem)
	
	def listItemClicked(self, listWidgetItem):
		self.setLineEdit(listWidgetItem.text())
		
	def listItemSelectionChanged(self):
		#vai ser fechada a funcionalidade de edição do item da lista
		self.itemsListView.closePersistentEditor(self.itemsListView.currentItem())
	
	#NÃO ESTÁ A FUNCIONAR
	def listItemTextChanged(self, newText):		
		self.setLineEdit(newText)	
	#***************************
	
	def setTextOnListItem(self, newText):
		#saber qual o item que esta seleccionado e alterar-lhe o texto (...)
		currentItem = self.itemsListView.currentItem()
		if currentItem <> None:
			currentItem.setText(newText)

	#***********************************
	
	def inicializeItems(self, ItemsList):
		for item in ItemsList:
			self.itemsListView.addItem(str(item.getText()))
		
		#colocar o 1ºitem como seleccionado por defeito
		self.setSelectedListItem(0)			

	def addTextItem(self):		
		#if self.textInput.text() != "":			
		self.itemsListView.addItem(self.newItemText)
		
		self.ItemsList.append(editItem(self.newItemText))
		
		#focar na janela a LineEdit
		self.textInput.setFocus()
		
		#focar na ListWidget o novo Item
		self.setSelectedListItem(self.itemsListView.count()-1)
		
	def deleteTextItem(self):		
		currentRow = self.itemsListView.currentRow()
		if currentRow  != self.noItem:
			self.itemsListView.takeItem(currentRow)
					
		self.ItemsList.pop(currentRow)
		#ELIMINAR ITEM DA LISTA DE REFERÊNCIA
		#self.refList.pop(currentRow)

	def moveItemDown(self):
		currentRow = self.itemsListView.currentRow()
		nElements =  self.itemsListView.count()
		if currentRow == self.noItem or currentRow == nElements-1 or nElements == 1:
			return
		
		#nextItem = QtGui.QListWidgetItem(self.itemsListView.item(currentRow+1))
		nextItem = self.itemsListView.item(currentRow+1)

		self.itemsListView.takeItem(currentRow+1)
		self.itemsListView.insertItem(currentRow, nextItem)

		#ALTERAR ORDENAÇÃO DA LISTA DE REFERÊNCIA
		tmpItem = self.ItemsList[currentRow+1]
		self.ItemsList.pop(currentRow+1)
		self.ItemsList.insert(currentRow, tmpItem)
		
		
		
	def moveItemUp(self):
		currentRow = self.itemsListView.currentRow()
		nElements =  self.itemsListView.count()
		if currentRow == self.noItem or currentRow == self.firstElement or nElements == 1:
			return
		
		#previousItem = QtGui.QListWidgetItem(self.itemsListView.item(currentRow-1))
		previousItem = self.itemsListView.item(currentRow-1)
		
		self.itemsListView.takeItem(currentRow-1)
		self.itemsListView.insertItem(currentRow, previousItem)		
				
		#ALTERAR ORDENAÇÃO DA LISTA DE REFERÊNCIA
		tmpItem = self.ItemsList[currentRow-1]
		self.ItemsList.pop(currentRow-1)
		self.ItemsList.insert(currentRow, tmpItem)
		
	
	def setLineEdit(self, text):
		self.textInput.setText(text)
	
	def setSelectedListItem(self, row = 0):
		if row >=0 and row < self.itemsListView.count():
			self.itemsListView.setItemSelected(self.itemsListView.item(row), true)
			self.itemsListView.setCurrentItem(self.itemsListView.item(row))
		else:
			return
		
	
	def getItemsList(self):
		return self.ItemsList
	
	def cancelChanges(self):
		self.ItemsList = self.originalItemsList
		self.reject()
	
	def applyChanges(self):
		
		"""elem = 0
		nElements =  len(self.refList)		
		while elem < nElements:
			
			#verificar se o elemento é um novo elemento ou já se oncontra na lista original
			if self.refList[elem] >= len(self.originalItemsList): #caso seja um novo elemento
				#vai ser criado um novo item e adicionado à lista
				self.ItemsList.append(editItem(item))
				elem = elem+1
				
			else: #caso seja um elemento já existente
				item = self.originalItemsList[self.refList[elem]]
				self.ItemsList.append(item)
				elem = elem+1
		"""
		
		#Aplicar as alterações efectuadas no ecra aos items armazenados na lista(...)
		elem = 0
		nElements =  self.itemsListView.count()				
		while elem < nElements:
			item = self.itemsListView.item(elem)
			self.ItemsList[elem].setText(str(item.text()))			
			#Alterar/Acrescentar futuros tipos de items (ex: icones)
			
			elem+=1
			
		self.accept()
		
#main

app = QtGui.QApplication(sys.argv)
list = [1,2,3,4,5,'merda']
widget = editItemsWidget(list)
widget.show()
sys.exit(app.exec_())
