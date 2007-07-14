#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableSpinner.
#
# Provide a Resizable Spinner which represents the Spinner Control. 
#
# Inherits @see CResizableWidget
class CResizableSpinner(CResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable Spinner owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.Spinner = QtGui.QSpinBox()
		CResizableWidget.__init__(self, typeControl, id, self.Spinner, parent)
		
	##
	# Set value property by the given value.	
	#
	# @Param value string
	def setValue(self, value):
		self.Spinner.setValue(int(value))