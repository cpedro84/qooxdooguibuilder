#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *

class ResizableTree(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.Tree = QtGui.QTreeView()
		ResizableWidget.__init__(self, typeControl, id, self.Tree, parent)