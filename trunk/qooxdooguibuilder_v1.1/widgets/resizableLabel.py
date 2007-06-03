#!/usr/bin/env python
# -*- encoding: latin1 -*-

from PyQt4 import QtCore, QtGui
from resizableWidget import *
from const import *


class ResizableLabel(ResizableAbstractIO):
	
	def __init__(self, typeControl, id, parent=None):
		self.Label = QtGui.QLabel()
		ResizableAbstractIO.__init__(self, typeControl, id, self.Label, parent)
	
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
	
	def setAlignLeft(self):
		self.Label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		
	def setAlignRight(self):
		self.Label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
		
	def setAlignCenter(self):
		self.Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
		
	def setAlignJustify(self):
		self.Label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
	
	def setWrap(self, enable):
		
		if enable:
			self.Label.setWordWrap(bool(1))
		else:
			self.Label.setWordWrap(bool(0))
		
	def enabledWordWrap(self):
		self.Label.setWordWrap(bool(1))
		
	def disabledWordWrap(self):
		self.Label.setWordWrap(bool(0))
		