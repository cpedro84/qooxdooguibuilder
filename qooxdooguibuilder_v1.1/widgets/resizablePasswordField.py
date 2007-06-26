#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

## Documentation for ResizablePasswordField.
#
# Provide a Resizable PasswordField which represents the PasswordField Control. 
#
# Inherits @see CResizableAbstractIO
class CResizablePasswordField(CResizableAbstractIO):
	
	
	## The constructor.	
	# Constructs a Resizable PasswordField owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.PasswordEdit = QtGui.QLineEdit()
		CResizableAbstractIO.__init__(self, typeControl, id, self.PasswordEdit, parent)
		self.PasswordEdit.setEchoMode(QtGui.QLineEdit.Password)