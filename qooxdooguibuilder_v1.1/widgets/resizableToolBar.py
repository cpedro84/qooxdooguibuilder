#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableToolBar(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.ToolBar = QtGui.QToolBar()
		ResizableWidget.__init__(self, typeControl, id, self.ToolBar, parent)