#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableSpinner(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.Spinner = QtGui.QSpinBox()
		ResizableWidget.__init__(self, typeControl, id, self.Spinner, parent)