#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableTabView.
#
# Provide a Resizable TabView which represents the TabView Control. 
#
# Inherits @see CResizableWidget
class CResizableTabView(CResizableWidget):
	
	## The constructor.	
	# Constructs a Resizable TabView owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.TabView = QtGui.QTabWidget()
		CResizableWidget.__init__(self, typeControl, id, self.TabView, parent)
		
	
	##
	# Add a tab to the TabView.
	#
	# @Param tab CEditItem
	# @see CEditItem
	def addTab(self, tab):
		widget = QtGui.QWidget()
		self.TabView.addTab(widget, tab.getText())
	
	##
	# Remove a tab in the given tabIndex from the TabView.
	def removeTab(self, tabIndex):
		self.TabView.removeTab(tabIndex)
	
	##
	# Remove all the taba from the TabView.
	def removeTabs(self):
		nTabs = self.TabView.count()		
		tab = 0
		while tab < nTabs:			
			self.TabView.removeTab(0)			
			tab = tab + 1			
	
	##
	# Set the tabs of the TableView with the tabs (CEditItem) saved in the given tabsList.
	#
	# @Param tabsList CEditItem
	# @see CEditItem
	def setTabs(self, tabsList):
		self.removeTabs()
		for tab in tabsList:			
			self.addTab(tab)
	
	
	##
	# Get the number of tabs in the TabView.
	#
	# @Param int
	def countTabs(self):
		return self.TabView.count()	
	
	
	##
	# Get the the tab text in the given index.
	#
	# @Param string
	def getTabText(self, index):
		if indexValidation(index, self.countTabs()):
			return self.TabView.tabText(index)
		
		return structureError
	
	
	##
	# Get the the tab widget in the given index.
	#
	# @Param QtGui.QWidget
	def getTabWidget(self, index):
		if indexValidation(index, self.countTabs()):
			return self.TabView.widget(index)
		
		return structureError
	
	
	##
	# Get the list of tabs (CEditItem) from the TabView.
	#
	# @Param python list
	# @see CEditItem
	def getTabs(self):
		tabsList = []
		nElements = self.countTabs()
		elem = 0		
		while elem < nElements:
			tabsList.append(CEditItem(self.getTabText(elem), self.getTabWidget(elem)))
			elem = elem + 1
		
		return tabsList	
