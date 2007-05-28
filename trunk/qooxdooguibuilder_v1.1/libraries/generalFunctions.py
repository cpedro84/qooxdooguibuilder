#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui
from const import *
from editItem import editItem
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

def clearList(list):
	itr=0
	while itr<len(list):
		list.pop()
		itr +=1


def QStringToString(qtString):
	return QtCore.QString(qtString).toLatin1().__str__()


def indexValidation(index, structureCount):
	if index < 0 or index >= structureCount:
		return false
	return true



#Função que valida a posição de uma widget numa area de acordo com os seus limites 
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
