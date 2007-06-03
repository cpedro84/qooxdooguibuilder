
#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

class resizableTextField(ResizableAbstractIO):
	
	def __init__(self, typeControl, id, parent=None):
		self.TextField = QtGui.QLineEdit()
		ResizableAbstractIO.__init__(self, typeControl, id, self.TextField, parent)
		self.TextField.setEchoMode(QtGui.QLineEdit.Normal)