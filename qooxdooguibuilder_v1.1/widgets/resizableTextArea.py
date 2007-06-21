#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableTextArea.
#
# Provide a Resizable TextArea which represents the TextArea Control. 
#
# Inherits @see CResizableWidget
class CResizableTextArea(ResizableWidget):
	
	
	## The constructor.	
	# Constructs a Resizable TextArea owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.textArea = QtGui.QTextEdit()
		ResizableWidget.__init__(self, typeControl, id, self.textArea, parent)
	
	##
	# Set the text of the TextArea with the given text.
	def setText(self, text):
		self.textArea.setPlainText(text)
	
	##
	# Set the wrap mode for the given enable state.
	#
	# @Param enable boolean
	def setWrap(self, enabled):		
		if enabled:
			self.enableWordWrap()
		else:
			self.disableWordWrap()
	
	##
	# Set readOnly mode for the given enable state.
	#
	# @Param enable boolean
	def setReadOnly(self, enabled):
		self.textArea.setReadOnly(enabled)

	##
	# Enable the wrap mode.
	def enableWordWrap(self):
		self.textArea.setWordWrapMode(QtGui.QTextOption.WordWrap)
	
	##
	# Disable the wrap mode.
	def disableWordWrap(self):
		self.textArea.setWordWrapMode(QtGui.QTextOption.NoWrap)

	
