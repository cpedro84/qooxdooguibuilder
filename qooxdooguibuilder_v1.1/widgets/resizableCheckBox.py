#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

class ResizableCheckBox(ResizableAbstractIO):
	
	def __init__(self, typeControl, id, parent=None):
		self.checkBox = QtGui.QCheckBox()
		ResizableAbstractIO.__init__(self, typeControl, id, self.checkBox, parent)
	
	def setChecked(self, enable):		
		if enable:
			self.checkBox.setCheckState(QtCore.Qt.Checked)
		else:
			self.checkBox.setCheckState(QtCore.Qt.Unchecked)
		
	
	def isChecked(self):
		checked = bool(0)		
		
		if self.checkBox.checkState() == QtCore.Qt.Checked:
			checked = bool(1)
		
		return checked