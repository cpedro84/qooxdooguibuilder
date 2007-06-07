#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from resizableWidget import *



class ResizableButton(ResizableAbstractIO):
	def __init__(self, typeControl, id, parent=None):
		
		self.Button = QtGui.QPushButton()		
		ResizableAbstractIO.__init__(self, typeControl, id, self.Button, parent)
		
	def setIcon(self, Icon):
		self.Button.setIcon(Icon)

	def setIconWidth(self, width):		
		height = self.iconSize().height()
		self.setIconSize(QtCore.QSize(width, height))
	
	def setIconHeight(self, height):
		width = self.iconSize().width()
		self.setIconSize(QtCore.QSize(width, height))
