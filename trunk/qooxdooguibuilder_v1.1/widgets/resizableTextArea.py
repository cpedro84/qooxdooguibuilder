#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *



class ResizableTextArea(ResizableWidget):
	
	def __init__(self, typeControl, id, parent=None):
		self.textArea = QtGui.QTextEdit()
		ResizableWidget.__init__(self, typeControl, id, self.textArea, parent)
	
	def setWrap(self, enabled):		
		if enabled:
			self.enableWordWrap()
		else:
			self.disableWordWrap()
	
	def setReadOnly(self, enabled):
		self.textArea.setReadOnly(enabled)

	def enableWordWrap(self):
		self.textArea.setWordWrapMode(QtGui.QTextOption.WordWrap)
	
	def disableWordWrap(self):
		self.textArea.setWordWrapMode(QtGui.QTextOption.NoWrap)

	def setText(self, text):
		self.textArea.setPlainText(text)
