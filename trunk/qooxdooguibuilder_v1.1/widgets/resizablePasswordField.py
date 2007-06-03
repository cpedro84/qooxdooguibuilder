#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizablePasswordField(ResizableAbstractIO):
	
	def __init__(self, typeControl, id, parent=None):
		self.PasswordEdit = QtGui.QLineEdit()
		ResizableAbstractIO.__init__(self, typeControl, id, self.PasswordEdit, parent)
		self.PasswordEdit.setEchoMode(QtGui.QLineEdit.Password)