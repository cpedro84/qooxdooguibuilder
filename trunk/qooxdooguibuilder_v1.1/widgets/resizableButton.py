#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from resizableWidget import *


## Documentation for CResizableButton.
#
# Provide a Resizable Button which represents the Button Control. 
#
# Inherits @see CResizableAbstractIO
class CResizableButton(ResizableAbstractIO):
	
	## The constructor.	
	# Constructs a Resizable Button owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		
		self.Button = QtGui.QPushButton()		
		ResizableAbstractIO.__init__(self, typeControl, id, self.Button, parent)
	
	##
	# Set a icon for the Resizable Button
	#
	# @Param icon QtGui.QIcon	
	def setIcon(self, icon):
		self.Button.setIcon(icon)

	##
	# Set the icon width.
	#
	# @Param width int
	def setIconWidth(self, width):		
		height = self.iconSize().height()
		self.setIconSize(QtCore.QSize(width, height))
	
	##
	# Set the icon height.
	#
	# @Param height int
	def setIconHeight(self, height):
		width = self.iconSize().width()
		self.setIconSize(QtCore.QSize(width, height))
