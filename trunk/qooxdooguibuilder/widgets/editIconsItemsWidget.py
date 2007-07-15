#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from editItem import *
from listWidget import *


## Documentation for CEditIconsItemsWidget.
#
# Dialog Window for setting edit items Icons. It's possible add, delete and change the entry order of the items. 
class CEditIconsItemsWidget(QtGui.QDialog):
	
	## The constructor.
	# Initializes the window dialog and sets the parent with given parent reference.
	# The window title is formated width the given windowTitle string.
	# A initial set of items, designated with the given itemDesignation, can be formated with the given initialIconsItemsList.
	#
	# @Param windowTitle string
	# @Param parent QWidget reference
	# @Param initialIconsItemsList python list
	# @Param itemDesignation string
	def __init__(self, windowTitle, parent=None,  initialIconsItemsList = [], itemDesignation = "Items"):
		
		QtGui.QDialog.__init__(self, parent)		
		
		self.setWindowTitle(windowTitle)
		self.setWindowIcon(QtGui.QIcon("icons/editors.png"))		
		
		self.originalIconsItemsList = []
		self.originalIconsItemsList = initialIconsItemsList
		
		#Listas de referência para alteração dos dados
		self.IconsItemsList = [ ]		
		self.IconsItemsList = initialIconsItemsList	
		
		self.newItemText = "New Item"
			
		self.noItem = -1
		self.firstElement = 0		
		
		self.ItemsGroupBox = QtGui.QGroupBox(itemDesignation+":", self)
		self.ItemsGroupBox.setGeometry(10,10,290,280)
		
		#LISTA COM OS ITEMS
		self.itemsListView = CListWidget(self.ItemsGroupBox)
		self.itemsListView.setGeometry(10,20,210,190)		
		#Processamento dos sinais emitidos pela ListWidget
		self.connect(self.itemsListView, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.listItemDoubleClicked)
		self.connect(self.itemsListView, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.listItemClicked)
		self.connect(self.itemsListView, QtCore.SIGNAL("itemSelectionChanged()"), self.listItemSelectionChanged)
		self.connect(self.itemsListView, QtCore.SIGNAL("currentTextChanged(const QString&)"), self.listItemTextChanged)
		self.connect(self.itemsListView, QtCore.SIGNAL("currentItemChanged (QListWidgetItem *,QListWidgetItem *)"), self.currentItemChanged) 
		
		#DEFINIÇÃO DOS BOTÕES
		self.okButton = QtGui.QPushButton("OK", self)		
		self.okButton.setGeometry(130, 300, 80, 25)
		self.connect(self.okButton, QtCore.SIGNAL("clicked()"), self.applyChanges)
		
		self.cancelButton = QtGui.QPushButton("Cancel", self)		
		self.cancelButton.setGeometry(220,300,80,25)
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
		
		self.labelText = QtGui.QLabel("Text:", self.ItemsGroupBox)
		self.labelText.setGeometry(10, 220, 30, 20)
		
		self.textInput = QtGui.QLineEdit(self.ItemsGroupBox)
		self.textInput.setGeometry(40, 220, 130, 20)
		self.connect(self.textInput, QtCore.SIGNAL("textEdited(const QString&)"), self.setTextOnListItem)

		#CONTROLOS PARA INSERçÂO DE ICONS
		self.labelText = QtGui.QLabel("Icon:", self.ItemsGroupBox)
		self.labelText.setGeometry(10, 250, 30, 20)
		
		self.iconButton = QtGui.QPushButton("...", self.ItemsGroupBox)
		self.iconButton.setGeometry(40, 250, 30, 25)
		self.connect(self.iconButton, QtCore.SIGNAL("clicked()"), self.selectIconFile)
		
		self.removeIconButton = QtGui.QPushButton("-", self.ItemsGroupBox)
		self.removeIconButton.setGeometry(80, 250, 20, 20)
		self.connect(self.removeIconButton, QtCore.SIGNAL("clicked()"), self.removeIconFile)
		
		if len(initialIconsItemsList) == 0:
			self.setEnableIconEdit(false)
		
		#FIXAR O TAMANHO DA WIDGET AO TAMANHO ACTUAL
		self.setFixedSize(310, 330)		
		
		#carregar lista com os items enviados por parametro (caso existam)
		self.inicializeItems(initialIconsItemsList)		
	
	
	"""
	def inicializeRefsLists(self, IconsItemsList):
		for itemIcon in ItemsIconsList:			
			self.IconsList.append(itemIcon[0]) #Icon
			self.IconsItemsList.append(itemIcon[1]) #Text
	"""
	
	def inicializeItems(self, IconsItemsList):
		for itemIcon in IconsItemsList:			
			item = QtGui.QListWidgetItem(QtGui.QIcon(str(itemIcon.getIconPath())), str(itemIcon.getText()))
			self.itemsListView.addItem(item)
		
		#colocar o 1ºitem como seleccionado por defeito
		self.setSelectedListItem(0)
	
	
	#************SLOTS*****************
	def selectIconFile(self):
		iconFileName = QtGui.QFileDialog.getOpenFileName(self, 
				TITLE_OPEN_ICON, 
				ROOT_DIRECTORY, 
				FILES_FILTER_IMAGES,
				FILES_FILTER_IMAGES,
				QtGui.QFileDialog.DontUseNativeDialog)
		
		if not iconFileName.isEmpty():
			#Carregar icon seleccionado
			icon = QtGui.QIcon(iconFileName)
			self.iconButton.setText("")
			self.iconButton.setIcon(icon)
			self.iconButton.setIconSize(self.iconButton.size())
			
			currentRow = self.itemsListView.currentRow()
			nElements =  self.itemsListView.count()
			
			if currentRow == self.noItem or nElements == 0:
				return
			
			
			item = self.itemsListView.item(currentRow)
			item.setIcon(icon)
			
			#Actualizar o inco na lista de referência, na posição current da listWidget
			self.IconsItemsList[currentRow].setIconPath(str(iconFileName))


	def removeIconFile(self):
		currentRow = self.itemsListView.currentRow()

		emptyIcon = QtGui.QIcon()
		item = self.itemsListView.item(currentRow)
		item.setIcon(emptyIcon)
		
		self.iconButton.setIcon(emptyIcon)
		self.iconButton.setText("...")
	
		#Actualizar a lista de referência, eleiminando a referência do iconPath, relativamente ao item seleccionado da listWidget
		self.IconsItemsList[currentRow].setIconPath("")

	
	def listItemDoubleClicked(self, listWidgetItem):
		self.itemsListView.openPersistentEditor(listWidgetItem)
		#self.itemsListView.CEditItem(listWidgetItem) ??????
	
	def listItemClicked(self, listWidgetItem):
		self.setLineEdit(listWidgetItem.text())
		
	def listItemSelectionChanged(self):
		#vai ser fechada a funcionalidade de edição do item da lista
		self.itemsListView.closePersistentEditor(self.itemsListView.currentItem())
	
	def currentItemChanged(self, currentListWidgetItem, previousListWidgetItem):
		icon = currentListWidgetItem.icon()
		if not icon.isNull():
			self.iconButton.setIcon(currentListWidgetItem.icon())
			self.iconButton.setText("")
		else:
			self.iconButton.setIcon(currentListWidgetItem.icon())
			self.iconButton.setText("...")
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
	

	def addTextItem(self):		
		#if self.textInput.text() != "":			
		self.itemsListView.addItem(self.newItemText)
		
		#Adicionar um item à lista de referência
		self.IconsItemsList.append(CEditItem(self.newItemText))
		
		#focar na janela a LineEdit
		self.textInput.setFocus()
		
		#focar na ListWidget o novo Item
		self.setSelectedListItem(self.itemsListView.count()-1)
		
		#Colocar enable os butões para edição de icons para os items da lista
		self.setEnableIconEdit(true)
		
	def deleteTextItem(self):		
		currentRow = self.itemsListView.currentRow()
		if currentRow  != self.noItem:
			self.itemsListView.takeItem(currentRow)
			#Eliminar o item da lista de referência
			self.IconsItemsList.pop(currentRow)		
		
		#ELIMINAR ITEM DA LISTA DE REFERÊNCIA
		#self.refList.pop(currentRow)
		
		nElements =  self.itemsListView.count()
		if nElements == 0:
			self.setEnableIconEdit(false)
			
			
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
		tmpItem = self.IconsItemsList[currentRow+1]
		self.IconsItemsList.pop(currentRow+1)
		self.IconsItemsList.insert(currentRow, tmpItem)
		
		
		
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
		tmpItem = self.IconsItemsList[currentRow-1]
		self.IconsItemsList.pop(currentRow-1)
		self.IconsItemsList.insert(currentRow, tmpItem)
		
	
	def setLineEdit(self, text):
		self.textInput.setText(text)
	
	def setSelectedListItem(self, row = 0):
		if row >=0 and row < self.itemsListView.count():
			self.itemsListView.setItemSelected(self.itemsListView.item(row), true)
			self.itemsListView.setCurrentItem(self.itemsListView.item(row))
		else:
			return
	
	
	def setEnableIconEdit(self, enable):		
		self.iconButton.setEnabled(enable)
		self.removeIconButton.setEnabled(enable)
	
	##
	# Get the items list, formated in the window dialog.
	#
	# @Return python list
	def getItemsList(self):
		return self.IconsItemsList
	
	def cancelChanges(self):
		self.IconsItemsList = self.originalIconsItemsList
		self.reject()
	
	def applyChanges(self):
	
		#Aplicar as alterações efectuadas no ecra aos items armazenados na lista(...)
		elem = 0
		nElements =  self.itemsListView.count()				
		while elem < nElements:
			item = self.itemsListView.item(elem)
			self.IconsItemsList[elem].setText(str(item.text()))			
			#Alterar/Acrescentar futuros tipos de items (ex: icones) (...)
			
			elem+=1
		
		#TESTE
		"""
		for item in self.IconsItemsList:
			print item.getText()
			print item.getIconPath()
		#*********
		"""
		
		self.accept()
		
		
