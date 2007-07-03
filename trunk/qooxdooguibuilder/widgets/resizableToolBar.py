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
	
