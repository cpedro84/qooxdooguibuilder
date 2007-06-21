#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


## Documentation for CResizableLabel.
#
# Provide a Resizable Label which represents the Label Control. 
#
# Inherits @see CResizableAbstractIO
class CResizableLabel(ResizableAbstractIO):
	
	
	## The constructor.	
	# Constructs a Resizable Label owned by the given parent. 
	# The resizable is identified with a given typeControl as a id.
	#
	# @Param typeControl string
	# @Param id string
	# @Param parent QWidget
	def __init__(self, typeControl, id, parent=None):
		self.Label = QtGui.QLabel()
		ResizableAbstractIO.__init__(self, typeControl, id, self.Label, parent)
	
	
	##
	# Set Alignment of the text for the given positions types:
	# ALIGN_LEFT -> Align in the left
	# ALIGN_RIGHT -> Align in the right
	# ALIGN_CENTER -> Align in the center
	# ALIGN_JUSTIFY -> Align justified
	#
	# @Param alignment string
	def setTextAlign(self, alignment):		
		alignment = str(alignment)		
		if alignment == ALIGN_LEFT:
			self.setAlignLeft()
		elif alignment == ALIGN_RIGHT:
			self.setAlignRight()
		elif alignment == ALIGN_CENTER:
			self.setAlignCenter()
		elif alignment == ALIGN_JUSTIFY:
			self.setAlignJustify()
	
	##
	# Set Alignment in the left.
	def setAlignLeft(self):
		self.Label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
	
	##
	# Set Alignment in the right.	
	def setAlignRight(self):
		self.Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
	
	##
	# Set Alignment in the center.
	def setAlignCenter(self):
		self.Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
	
	##
	# Set Alignment justified.
	def setAlignJustify(self):
		self.Label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
	
	
	##
	# Set the wrap mode for the given enable state.
	#
	# @Param enable boolean
	def setWrap(self, enable):
		
		if enable:
			self.Label.setWordWrap(bool(1))
		else:
			self.Label.setWordWrap(bool(0))
		
	##
	# Enable the wrap mode.
	def enabledWordWrap(self):
		self.Label.setWordWrap(bool(1))
		
	##
	# Disable the wrap mode.
	def disabledWordWrap(self):
		self.Label.setWordWrap(bool(0))
		

