#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *



#Associar com um QButtonGroup....
class ResizableRadioButton(ResizableAbstractIO):
	
	def __init__(self, typeControl, id, parent=None):
		self.RadioButton = QtGui.QRadioButton()		
		ResizableAbstractIO.__init__(self, typeControl, id, self.RadioButton, parent)

	def setChecked(self, enable):		
		self.RadioButton.setChecked(enable)