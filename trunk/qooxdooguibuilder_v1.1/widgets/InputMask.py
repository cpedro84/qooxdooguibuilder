#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *

class CInputMask(QtCore.QString):

	
	def __init__(self, type = TINT):
		
		self.mask = ""
		
		if type == TINT:			
			self.mask = "#0000"
			#self.mask = "9999999"
		elif type == TFLOAT:
			self.mask = "#0000,000"
		elif type == TSTRING:
			self.mask = "nnnnnnnnnnnnnnnnnnnnnn"
		
		QtCore.QString.__init__(self, self.mask)
	

	def setMask(self, mask):
		
		self = QtCore.QString(mask)