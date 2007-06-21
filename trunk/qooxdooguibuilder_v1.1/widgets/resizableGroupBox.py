#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

## Documentation for ResizableGroupBox.
#
# Provide a Resizable GroupBox which represents the GroupBox Control. 
#
# Inherits @see CResizableWidget
class CResizableGroupBox(ResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable GroupBox owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.GroupBox = QtGui.QGroupBox()
		ResizableWidget.__init__(self, typeControl, id, self.GroupBox, parent)


	##
	# Set the legend title, with the given text, of the GroupBox
	#
	# @Param text string
	def setLegend(self, text):
		self.GroupBox.setTitle(text)

	##
	# Set the window icon with the given icon.
	#
	# @Param icon QtGui.QIcon
	def setWindowIcon(self, icon):
		self.GroupBox.setWindowIcon(icon)
		

