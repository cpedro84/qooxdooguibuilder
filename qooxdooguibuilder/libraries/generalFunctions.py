#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import CEditItem
from projectExceptions import *
from tableData import *
import cPickle as pickle



def ListToQStringList(pList): #Não Utilizar
	try:
		qtList = QtCore.QStringList()
		
		for item in pList:
			qtList.append(item)
		
		return qtList
		
	except:
		raise structureError_Exception(structureError, ERROR_ACCESS_STRUCTURE)
		return structureError
		

##Documentation for a function.
# From a QStringList is created a Python List of Strings elements
#
# @param qtList QStringList
#
# @return List 
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


##Documentation for a function.
# Delete all elements from the given List.
#
# @param list List of Elements
def clearList(list):
	itr=0
	while itr<len(list):
		list.pop()
		itr +=1

##Documentation for a function.
# Convert QString to String, in latin1 format
#
# @param qtString QString
def QStringToString(qtString):
	return QtCore.QString(qtString).toLatin1().__str__()


##Documentation for a function.
# Validate an index from a given number elements of a structure
#
# @param index int
# @param structureCount  int - Number of elements of the structure
def indexValidation(index, structureCount):
	if index < 0 or index >= structureCount:
		return false
	return true


##Documentation for a function.
# Validate the position of a rectangular object with a given Size (Width and Height) from an Area
#
# @param xWidget  float Position x of the object
# @param yWidget  float Position y of the object
# @param widthWidget float  Width of the object
# @param heightWidget float Height of the object
# @param widthArea float Width of the Area
# @param heightArea float Height of the Area
def validatePosition(xWidget, yWidget, widthWidget, heightWidget, widthArea, heightArea):
	
	left = xWidget
	right = xWidget+widthWidget
	top = yWidget
	bottom = yWidget+heightWidget
	
	if left > 0 and top > 0 and right < widthArea and bottom < heightArea:
		return true
	else:
		return false
	
	
def serializeObject(object):		
	return pickle.dumps(object)

def unserializeObject(pickleObject):
	return pickle.loads(pickleObject)


def indexValue(list, value):
	
	for elem in list:
		if elem == value:
			return true
	
	return false
	
	
def writeToFile(fileContent, filePath):
	
	file = open(filePath, "w")	
	file.write(fileContent)	
	file.close()

		