#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableLabel.
#
# Provide a Resizable IFrame which represents the IFrame Control. 
#
# Inherits @see CResizableWidget
class CResizableIFrame(CResizableWidget):
	
	## The constructor.	
	# Constructs a Resizable IFrame owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.iFrame = QtGui.QTextEdit()
		CResizableWidget.__init__(self, typeControl, id, self.iFrame, parent)
		self.iFrame.setReadOnly(true)
		self.iFrame.setEnabled(false)
		self.fixedText = "IFrame - Source URL: "		
	
	##
	# Set the text of the IFrame with the given text.
	def setURL(self, text):
		self.iFrame.setPlainText(self.fixedText+text)