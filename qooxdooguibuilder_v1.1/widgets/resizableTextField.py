
#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableTextField.
#
# Provide a Resizable TextField which represents the TextField Control. 
#
# Inherits @see CResizableAbstractIO
class CResizableTextField(ResizableAbstractIO):
	
	## The constructor.	
	# Constructs a Resizable TextField owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.TextField = QtGui.QLineEdit()
		ResizableAbstractIO.__init__(self, typeControl, id, self.TextField, parent)
		self.TextField.setEchoMode(QtGui.QLineEdit.Normal)