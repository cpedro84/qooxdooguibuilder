#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableCheckBox.
#
# Provide a Resizable CheckBox which represents the CheckBox Control. 
#
# Inherits @see CResizableAbstractIO
class CResizableCheckBox(CResizableAbstractIO):
	
	
	## The constructor.	
	# Constructs a Resizable CheckBox owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.checkBox = QtGui.QCheckBox()
		CResizableAbstractIO.__init__(self, typeControl, id, self.checkBox, parent)
	
	
	##
	# Set the checked state by the given enable value.
	#
	# @Param enable boolean
	def setChecked(self, enable):		
		if enable:
			self.checkBox.setCheckState(QtCore.Qt.Checked)
		else:
			self.checkBox.setCheckState(QtCore.Qt.Unchecked)
		
	##
	# Check if the "checked state" is enabled.
	#
	# @Param boolean
	def isChecked(self):
		checked = bool(0)		
		
		if self.checkBox.checkState() == QtCore.Qt.Checked:
			checked = bool(1)
		
		return checked
		
