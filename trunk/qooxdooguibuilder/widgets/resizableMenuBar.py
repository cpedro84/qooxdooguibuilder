#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

## Documentation for CResizableList.
#
# Provide a Resizable List which represents the List Control. 
#
# Inherits @see CResizableWidget
class CResizableMenuBar(CResizableWidget):	
	
	
	
	def __init__(self, typeControl, id, parent=None):	
		self.MenuBar = QtGui.QMenuBar()
		CResizableWidget.__init__(self, typeControl, id, self.MenuBar, parent)
				
		self.menus = []
			
		"""
		menuHelp = editMenu(app, self.MenuBar)
		#edit = QtGui.QLineEdit("edit",  menuHelp)
		#edit.setGeometry(menuHelp.geometry().x(), menuHelp.geometry().y(), menuHelp.geometry().width(), menuHelp.geometry().height())
				
		self.MenuBar.addMenu(menuHelp)
		"""
		
		
	##
	# Add a Menu text to the List.
	#
	# @Param Menu string
	def addMenuText(self, Menu):
		self.MenuBar.addMenu(Menu)
		self.menus.append(Menu)
	
	##
	# Set the Menus of the List with teh given list of CEditItem.
	# @see CEditItem
	#
	# @Param textMenusList python list
	def setMenus(self, textMenusList):
		self.MenuBar.clear()
		clearList(self.menus)		
		for menu in textMenusList:			
			self.addMenuText(menu.getText())

	##
	# Get the number of Menus in the List.
	#
	# @Param int
	def countMenus(self):
		return len(self.menus)

	##
	# Get a Menu text inthe given index from the List.
	#
	# @Param index int
	def getMenuText(self, index):		
		if indexValidation(index, self.countMenus()):
			return str(self.menus[index])
	
		return structureError
		
	##
	# Return the list of Menus (CEditItem) from the List.
	# @see CEditItem
	#
	# @Return python list
	def getMenus(self):
		textMenus = []
		nElements = self.countMenus()
		elem = 0		
		while elem < nElements:
			textMenus.append(CEditItem(self.getMenuText(elem)))
			elem = elem + 1
		
		return textMenus