#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableTabView(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.TabView = QtGui.QTabWidget()
		ResizableWidget.__init__(self, typeControl, id, self.TabView, parent)
		self.TabView.setEnabled(true)
		
	def addTab(self, tab):
		widget = QtGui.QWidget()
		self.TabView.addTab(widget, tab.getText())
	
	def removeTab(self, tabIndex):
		self.TabView.removeTab(tabIndex)
		
	def removeTabs(self):
		nTabs = self.TabView.count()		
		tab = 0
		while tab < nTabs:			
			self.TabView.removeTab(0)			
			tab = tab + 1			
		
	def setTabs(self, tabsList):
		self.removeTabs()
		for tab in tabsList:			
			self.addTab(tab)
	
	def countTabs(self):
		return self.TabView.count()	
	
	def getTabText(self, index):
		if indexValidation(index, self.countTabs()):
			return self.TabView.tabText(index)
		
		return structureError
	
	def getTabWidget(self, index):
		if indexValidation(index, self.countTabs()):
			return self.TabView.widget(index)
		
		return structureError
	
	def getTabs(self):
		tabsList = []
		nElements = self.countTabs()
		elem = 0		
		while elem < nElements:
			tabsList.append(editItem(self.getTabText(elem), self.getTabWidget(elem)))
			elem = elem + 1
		
		return tabsList	