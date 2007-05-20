#!/usr/bin/env python
# -*- encoding: latin1 -*-


import sys
from const import *
import exceptions


class structureError_Exception(exceptions.Exception):
	def __init__(self, errorId, msg):
		self.errorId = errorId
		self.msg = msg
		
		

"""
#TESTE
def rais():
	raise structureError_Exception(1, "teste")
	

try:
	rais()
except structureError_Exception, e:
	print e.msg
"""