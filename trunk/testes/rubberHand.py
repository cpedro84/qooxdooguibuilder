#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui



class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.rubberHand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
		self.mousePressed = bool(0)
		self.originPressed = QtCore.QPoint(0,0)
		
	def mousePressEvent(self, event):		
		self.mousePressed = bool(1)
		self.originPressed = QtCore.QPoint(event.pos())
		
		#self.rubberHand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
		self.rubberHand.setGeometry(QtCore.QRect(self.originPressed, QtCore.QSize()))
		self.rubberHand.show()
		
	def mouseReleaseEvent(self, event):
		self.mousePressed = bool(0)
		self.rubberHand.hide()

	def mouseMoveEvent(self, event):		
		if self.mousePressed:			
			self.rubberHand.setGeometry(QtCore.QRect(self.originPressed, event.pos()).normalized())
		
		

app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())


