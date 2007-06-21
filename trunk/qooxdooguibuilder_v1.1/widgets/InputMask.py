#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *
from generalFunctions import *


## Documentation for CInputMask.
#
# Input Mask that Inherits Qt QString.
# To be used with the Qt QTextField or other Controls that support input mask, will restrict the users entrys values from the keyboard.
# For default this class custumize 4 types os input masks:
# TINT_MASK -  For integer type input -> only entrys for numbers. 
# TFLOAT_MASK - For float type input -> only entryes for float values.
# TSTRING_MASK - For string type input -> any type of characters.
# TLONG_STRING_MASK - For string type input -> any type of characters (Longer in number of characters for input than TSTRING_MASK).
class CInputMask(QtCore.QString):
	
	
	TINT_MASK = "TInt"	
	TFLOAT_MASK = "TFloat"	
	TSTRING_MASK = "TString"	
	TLONG_STRING_MASK = "TLong_String"

	## The constructor.	
	# Contructs a instance os CInputMask  formated with the given type
	#
	# @Param type string
	def __init__(self, type = TINT_MASK):
		
		self.mask = ""
		
		if type == self.TINT_MASK:			
			self.mask = "#0000"
			#self.mask = "9999999"
		elif type == self.TFLOAT_MASK:
			self.mask = "#0000,000"
		elif type == self.TSTRING_MASK:
			self.mask = "nnnnnnnnnnnnnnnnnnnnnnnnn"
		elif type == self.TLONG_STRING_MASK:
			self.mask = """nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
					nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
					nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
					"""
		
		QtCore.QString.__init__(self, self.mask)
	
	
	##
	# Set the Input Mask with the given mask.
	#
	# @Param mask string
	def setMask(self, mask):		
		self = QtCore.QString(mask)
	
	
	##
	# Get the Input Mask.
	#
	# @Return string
	def getMask(self):
		return QStringToString(self)
		
