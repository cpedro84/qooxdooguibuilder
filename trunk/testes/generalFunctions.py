#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from projectExceptions import *

def ListToQStringList(pList):
	try:
		qtList = QtCore.QStringList()
		
		for item in pList:
			qtList.append(item)
		
		return qtList
		
	except:
		raise structureError_Exception(structureError, ERROR_ACCESS_STRUCTURE)
		return structureError
		

def QStringListToList(qtList):
	try:
		list = []
		
		#qtList = QtCore.QStringList(qtList)
		nElements = qtList.count()
		elem = 0		
		while elem < nElements:
			list.append(str(qtList.takeFirst()))
			elem = elem +1
					
		return list
		
	except:
		raise structureError_Exception(structureError, ERROR_ACCESS_STRUCTURE)
		return structureError
		


def indexValidation(index, structureCount):
	if index < 0 or index >= structureCount:
		return false
	return true
	
	
	