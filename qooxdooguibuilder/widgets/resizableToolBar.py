#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableToolBar.
#
# Provide a Resizable ToolBar which represents the ToolBar Control. 
#
# Inherits @see CResizableWidget
class CResizableToolBar(CResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable ToolBar owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.ToolBar = QtGui.QToolBar()
		CResizableWidget.__init__(self, typeControl, id, self.ToolBar, parent)
	
		self.nToolItems = 0
		self.listToolItems = []


	#item -> CEditItem
	def addItem(self, item):
		
		if item.getIconPath() == "":
			self.ToolBar.addAction(item.getText())
		else:
			self.ToolBar.addAction(QtGui.QIcon(item.getIconPath()), item.getText())
		
		self.nToolItems +=1

	#listToolItems -> list of CEditItem
	def setItems(self, listToolItems):
		
		self.ToolBar.clear()
		self.listToolItems = listToolItems
		for toolItem in listToolItems:
			self.addItem(toolItem)
		
		
	##
	# Get the number of items in the List.
	#
	# @Param int
	def countItems(self):
		return self.nToolItems
	
	
	##
	# Return the list of items (CEditItem) from the List.
	# @see CEditItem
	#
	# @Return python list
	def getItems(self):		
		return self.listToolItems
		