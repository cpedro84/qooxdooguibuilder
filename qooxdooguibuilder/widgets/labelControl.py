#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui


from const import *


class CLabelControl(QtGui.QLabel):
	
	def __init__(self, parent = None):		
		QtGui.QLabel.__init__(self, parent)
		self.setMouseTracking(true)

	#-------EVENTOS----------------------------------------------------------------	
	def mouseMoveEvent(self, event):				
		#self.setFrameShadow(QtGui.QFrame.Raised)
		self.setFrameShape(QtGui.QFrame.NoFrame)
		self.update()
		