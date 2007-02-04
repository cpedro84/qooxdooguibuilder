#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui



class ResizebleWidget(QtGui.QFrame):
    
	def __init__(self, parent=None):
		
		QtGui.QLabel.__init__(self, parent)		
		self.Btn1 = QtGui.QPushButton(self)		
		self.setMouseTracking(bool(1))
		
		#DEFINIÇÃO DE TAMANHOS
		self.PenWidth = 2 
		self.RectSize = 4
		
		#DEFINIÇÃO DAS VARIAVEIS PARA OS RECT DE RESIZE
		self.RectLT = QtCore.QRect(0,0,0,0) #LEFT TOP
		self.RectCT = QtCore.QRect(0,0,0,0) #CENTER TOP
		self.RectRT = QtCore.QRect(0,0,0,0) #RIGHT TOP
		self.RectLB = QtCore.QRect(0,0,0,0) #LEFT BOTTON
		self.RectCB = QtCore.QRect(0,0,0,0) #CENTER BOTTON
		self.RectRB = QtCore.QRect(0,0,0,0) #RIGHT BOTTON
				
		"""text = "teste"
		
		fm = QtGui.QFontMetrics(self.font())
		size = fm.size(QtCore.Qt.TextSingleLine, text)
	
		image = QtGui.QImage(size.width() + 12, size.height() + 12,
				     QtGui.QImage.Format_ARGB32_Premultiplied)
		image.fill(QtGui.qRgba(0, 0, 0, 0))
	
		font = QtGui.QFont()
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
	
		painter = QtGui.QPainter()
		painter.begin(image)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		painter.setBrush(QtCore.Qt.white)
		painter.drawRoundRect(QtCore.QRectF(0.5, 0.5, image.width()-1, image.height()-1), 25, 25)
		
		painter.setFont(font)
		painter.setBrush(QtCore.Qt.black)
		painter.drawText(QtCore.QRect(QtCore.QPoint(6, 6), size),
				 QtCore.Qt.AlignCenter, text)
		painter.end()		
		 
		self.setPixmap(QtGui.QPixmap.fromImage(image))
		self.labelText = text"""
		
	def paintEvent(self, event):
		
		#DEFINIR CURSOR DO RATO
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
		self.widgetRect = self.geometry()
		WidgetWidth = self.widgetRect.width()
		WidgetHeight = self.widgetRect.height()
						
		#DEFINIÇÃO DAS FERRAMENTAS DE PINTURA
		#************FONT*****************
		font = QtGui.QFont()
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		#**********PEN*********************
		
		penDotLine = QtGui.QPen(QtGui.QBrush(QtCore.Qt.SolidPattern),self.PenWidth, QtCore.Qt.DotLine)
		penSolidLine = QtGui.QPen(QtGui.QBrush(QtCore.Qt.SolidPattern),self.PenWidth, QtCore.Qt.SolidLine)
		
		#PINTAR		
		painter = QtGui.QPainter()		
		painter.begin(self)			
		
		painter.setBrush(QtCore.Qt.black)
		painter.setFont(font)
		painter.setPen(penDotLine)
		#LINHAS
		painter.drawLine(0,0, self.widgetRect.width(),0) #TOP LINE
		painter.drawLine(0,self.widgetRect.height(), self.widgetRect.width(),self.widgetRect.height()) #BOTTON LINE
		painter.drawLine(0,0,0,self.widgetRect.height()) #LEFT LINE		
		painter.drawLine(self.widgetRect.width(),0,self.widgetRect.width(),self.widgetRect.height()) #RIGHT LINE
		
		#RECTÂNGULOS		
		painter.setPen(penSolidLine)
		self.RectLT.setRect(0,0,self.RectSize,self.RectSize) #LEFT TOP
		self.RectCT.setRect(WidgetWidth/2.0,0,self.RectSize,self.RectSize) #CENTER TOP
		self.RectRT.setRect(WidgetWidth-self.RectSize,0,self.RectSize,self.RectSize) #RIGHT TOP
		self.RectLB.setRect(0,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #LEFT BOTTON
		self.RectCB.setRect(WidgetWidth/2.0,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #CENTER BOTTON
		self.RectRB.setRect(WidgetWidth-self.RectSize,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #RIGHT BOTTON
		
		painter.drawRect(self.RectLT)
		painter.drawRect(self.RectCT)
		painter.drawRect(self.RectRT)
		painter.drawRect(self.RectLB)
		painter.drawRect(self.RectCB)
		painter.drawRect(self.RectRB)
		
		
		
		painter.end()
						
		#REDIMENSIONAR TAMANHO DA WIDGET
		self.Btn1.setGeometry(self.RectSize,self.RectSize,WidgetWidth-self.RectSize*2, WidgetHeight-self.RectSize*2)
		
	
	def mouseMoveEvent(self, event):
		
		self.widgetRect = self.geometry()
		
		mouseXpos = event.x()
		mouseYpos = event.y()
		
		#PONTOS DE REFERÊNCIA
		point = QtCore.QPoint(mouseXpos, mouseYpos)
		
				
		#VALIDAR POSICAO DO RATO DE ACORDO COM OS PONTOS DE REF. 
		if self.IsPointInsideRect(point, self.RectLT) == bool(1):  # LEFT TOP	
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
		elif self.IsPointInsideRect(point, self.RectCT) == bool(1): # CENTER TOP
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
		elif self.IsPointInsideRect(point, self.RectRT) == bool(1): # RIGHT TOP
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
		elif self.IsPointInsideRect(point, self.RectLB) == bool(1): # LEFT BOTTON
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
		elif self.IsPointInsideRect(point, self.RectCB) == bool(1): # CENTER BOTTON
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
		elif self.IsPointInsideRect(point, self.RectRB) == bool(1): # RIGHT BOTTON
			self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
		else:			
			self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
			
	
	def IsPointInsideRect(self, point, rect):
		
		px = point.x()
		py = point.y()
		
		rx = rect.x()
		ry = rect.y()
		rw = rect.width()
		rh = rect.height()
		
		if px>=rx and px <=rx+rw and py>=ry and py<=ry+rh:
			
			return bool(1) #TRUE
		else:
			return bool(0) #FALSE

#main 
app = QtGui.QApplication(sys.argv)
widget = ResizebleWidget()
widget.show()
sys.exit(app.exec_())