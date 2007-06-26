#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableTree.
#
# Provide a Resizable Tree which represents the Tree Control. 
#
# Inherits @see CResizableWidget
class CResizableTree(CResizableWidget):
		
	## The constructor.	
	# Constructs a Resizable Tree owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.Tree = QtGui.QTreeView()
		CResizableWidget.__init__(self, typeControl, id, self.Tree, parent)