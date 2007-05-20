#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui
from const import *
from exceptions import *



class editItem(QtCore.QObject):
	
	def __init__(self, text, widget = None):
		self.text = text
		self.widget = widget

	def getText(self):
		return self.text
	
	def getWidget(self):
		return self.widget
		
	def setWidget(self, widget):
		self.widget = widget
		
	def setText(self, text):
		self.text = text
		
