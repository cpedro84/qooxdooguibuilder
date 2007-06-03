#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableGroupBox(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.GroupBox = QtGui.QGroupBox()
		ResizableWidget.__init__(self, typeControl, id, self.GroupBox, parent)

	def setLegend(self, text):
		self.GroupBox.setTitle(text)

	def setWindowIcon(self, icon):
		self.GroupBox.setWindowIcon(icon)