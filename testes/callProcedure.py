#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from string import Template
from PyQt4 import QtCore, QtGui
	
#formato string procedureInfo:  <nome método>,param1,param2,param3,...,paramN
#DparametersValues: Mapa associativo com os valores dos parametros
def callProcedure(procedureInfo, DparametersValues):
		
	exec procedureInfo in DparametersValues, globals()
	


class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		procedureInfo = "a =QtGui.QPushButton(parent)"
		DparametersValues = dict(parent = self)		
			
		callProcedure(procedureInfo, DparametersValues)			
		print a
#-------------------------------------------------------------------------------------

#main 
app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())