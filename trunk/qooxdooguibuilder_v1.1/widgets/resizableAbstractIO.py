#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableAbstractIO.
#
# CResizableAbstractIO class is the abstract base class of widgets that have text properties, providing commonly functions.
#
# Inherits @see CResizableWidget
class CResizableAbstractIO(CResizableWidget):

	## The constructor.	
	# Constructs a Resizable Widget owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, widget = None, parent=None):
		self.AbstractIOWidget = widget
		CResizableWidget.__init__(self, typeControl, id, self.AbstractIOWidget,  parent)
	
	##
	# Set text property by the given text.	
	#
	# @Param strText string
	def setText(self, strText):
		self.AbstractIOWidget.setText(strText)
	
	##
	# Get the text property
	#
	# @Return  string
	def getText(self):
		return self.AbstractIOWidget.text()