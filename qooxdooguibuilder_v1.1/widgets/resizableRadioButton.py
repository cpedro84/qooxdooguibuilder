#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *



#Associar com um QButtonGroup....


## Documentation for CResizableRadioButton.
#
# Provide a Resizable Radio Button which represents the Radio Button Control. 
#
# Inherits @see CResizableAbstractIO
class CResizableRadioButton(ResizableAbstractIO):
	
	
	## The constructor.	
	# Constructs a Resizable Radio Button owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.RadioButton = QtGui.QRadioButton()		
		ResizableAbstractIO.__init__(self, typeControl, id, self.RadioButton, parent)


	##
	# Set the checked state by the given enable value.
	#
	# @Param enable boolean
	def setChecked(self, enable):		
		self.RadioButton.setChecked(enable)
		
