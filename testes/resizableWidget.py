#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



class ResizebleWidget(QtGui.QWidget):
    
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)		
		self.Btn1 = QtGui.QPushButton(self)		
		self.setMouseTracking(bool(1))
		
		#DEFINIÇÃO DE TAMANHOS
		self.PenWidth = 2 
		self.RectSize = 4
		
		#DEFINIÇÃO DAS VARIAVEIS PARA OS RECT DE RESIZE
		self.RectLT = QtCore.QRect(0,0,0,0) #LEFT TOP
		self.RectCT = QtCore.QRect(0,0,0,0) #CENTER TOP
		self.RectRT = QtCore.QRect(0,0,0,0) #RIGHT TOP
		self.RectLB = QtCore.QRect(0,0,0,0) #LEFT BOTTOM
		self.RectCB = QtCore.QRect(0,0,0,0) #CENTER BOTTOM
		self.RectRB = QtCore.QRect(0,0,0,0) #RIGHT BOTTOM
		self.RectL = QtCore.QRect(0,0,0,0) #LEFT
		self.RectR = QtCore.QRect(0,0,0,0) #RIGHT
		
		#PONTO DE REFERENCIA (para controlo no clique do rato)
		self.RefRectLeftTop = 1
		self.RefRectCenterTop = 2
		self.RefRectRightTop = 3
		self.RefRectLeftBottom = 4
		self.RefRectCenterBottom = 5
		self.RefRectRightBottom = 6
		self.RefRectLeft = 7
		self.RefRectRight = 8		
		self.noRef = 0
		self.pontoRef = self.noRef
		
		#ESTADOS DO RATO
		#self.MouseDefault = 0
		self.MouseClicked = 1
		self.MouseRelease = 0
		self.MouseState = self.MouseRelease
		#posicionamento anterior
		self.MouseLastXpos = 0
		self.MouseLastYpos = 0
		
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
		painter.drawLine(0,self.widgetRect.height(), self.widgetRect.width(),self.widgetRect.height()) #BOTTOM LINE
		painter.drawLine(0,0,0,self.widgetRect.height()) #LEFT LINE		
		painter.drawLine(self.widgetRect.width(),0,self.widgetRect.width(),self.widgetRect.height()) #RIGHT LINE
		
		#RECTÂNGULOS		
		painter.setPen(penSolidLine)
		self.RectLT.setRect(0,0,self.RectSize,self.RectSize) #LEFT TOP
		self.RectCT.setRect(WidgetWidth/2.0,0,self.RectSize,self.RectSize) #CENTER TOP
		self.RectRT.setRect(WidgetWidth-self.RectSize,0,self.RectSize,self.RectSize) #RIGHT TOP
		self.RectLB.setRect(0,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #LEFT BOTTOM
		self.RectCB.setRect(WidgetWidth/2.0,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #CENTER BOTTOM
		self.RectRB.setRect(WidgetWidth-self.RectSize,WidgetHeight-self.RectSize,self.RectSize,self.RectSize) #RIGHT BOTTOM
		self.RectL.setRect(0, WidgetHeight/2.0, self.RectSize, self.RectSize)
		self.RectR.setRect(WidgetWidth-self.RectSize, WidgetHeight/2.0, self.RectSize, self.RectSize)
		
		painter.drawRect(self.RectLT)
		painter.drawRect(self.RectCT)
		painter.drawRect(self.RectRT)
		painter.drawRect(self.RectLB)
		painter.drawRect(self.RectCB)
		painter.drawRect(self.RectRB)
		painter.drawRect(self.RectL)
		painter.drawRect(self.RectR)
		
		painter.end()
						
		#REDIMENSIONAR TAMANHO DA WIDGET
		self.Btn1.setGeometry(self.RectSize,self.RectSize,WidgetWidth-self.RectSize*2, WidgetHeight-self.RectSize*2)
		
	
	def mouseMoveEvent(self, event):
		
		widgetRect = self.geometry()
		
		mouseXpos = event.x()
		mouseYpos = event.y()
		
		#PONTOS DE REFERÊNCIA
		point = QtCore.QPoint(mouseXpos, mouseYpos)
		
	
		if self.MouseState == self.MouseRelease:			
			#VALIDAR POSICAO DO RATO DE ACORDO COM OS PONTOS DE REF. 
			if self.IsPointInsideRect(point, self.RectLT) == bool(1):  # LEFT TOP
				self.pontoRef =self.RefRectLeftTop #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
			elif self.IsPointInsideRect(point, self.RectCT) == bool(1): # CENTER TOP
				self.pontoRef =self.RefRectCenterTop #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
			elif self.IsPointInsideRect(point, self.RectRT) == bool(1): # RIGHT TOP
				self.pontoRef =self.RefRectRightTop #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
			elif self.IsPointInsideRect(point, self.RectLB) == bool(1): # LEFT BOTTOM
				self.pontoRef =self.RefRectLeftBottom #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
			elif self.IsPointInsideRect(point, self.RectCB) == bool(1): # CENTER BOTTOM
				self.pontoRef =self.RefRectCenterBottom #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
			elif self.IsPointInsideRect(point, self.RectRB) == bool(1): # RIGHT BOTTOM
				self.pontoRef =self.RefRectRightBottom #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))			
			elif self.IsPointInsideRect(point, self.RectL) == bool(1): # LEFT
				self.pontoRef =self.RefRectLeft #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
			elif self.IsPointInsideRect(point, self.RectR) == bool(1): # RIGHT
				self.pontoRef =self.RefRectRight #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))		
			else:			
				self.pontoRef = self.noRef #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
						
		
		#ALTERAR AS DIMENSÕES DA WIDGET DE ACORDO COM A POSIÇÃO DO RATO (caso o rato esteja pressionado numa área de alteração de tamanho)
		if self.MouseState == self.MouseClicked:
			
			if self.pontoRef == self.RefRectCenterTop: # NO OK				
				if mouseYpos > self.MouseLastYpos:
					print("maior")
					self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()-(mouseYpos - widgetRect.y()) )
				else:
					print("menor")
					self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()+(widgetRect.y() - mouseYpos) )
			elif self.pontoRef == self.RefRectRightTop:# NO OK
				self.setGeometry(mouseXpos, widgetRect.y(), mouseXpos, mouseYpos)
			elif self.pontoRef == self.RefRectLeftBottom: #NO OK
				self.setGeometry(mouseXpos, widgetRect.y(), mouseXpos, mouseYpos)
			elif self.pontoRef == self.RefRectCenterBottom: #OK
				self.setGeometry(widgetRect.x(), widgetRect.y(), widgetRect.width(), mouseYpos)			
			elif self.pontoRef == self.RefRectRightBottom: #OK
				self.setGeometry(widgetRect.x(), widgetRect.y(), mouseXpos, mouseYpos)
			elif self.pontoRef == self.RefRectLeft: #NO OK		
				self.setGeometry(widgetRect.x(), widgetRect.y(), mouseXpos, 0)
			elif self.pontoRef == self.RefRectRight: #OK
				self.setGeometry(widgetRect.x(), widgetRect.y(), mouseXpos,widgetRect.height())
			
			
			
			#GUARDAR POSICIONAMENTO DO RATO
			self.MouseLastXpos = mouseXpos
			self.MouseLastYpos = mouseYpos
			
	def mousePressEvent(self, event):
		#ACTUALIZAR O ESTADO DO RATO
		self.MouseState = self.MouseClicked		
		
	def mouseReleaseEvent(self, event):
		#ACTUALIZAR O ESTADO DO RATO
		self.MouseState = self.MouseRelease
		#ALTERAR O CURSOR DO RATO PARA O ESTADO ORIGINAL
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



class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		#widgetRect = self.geometry()
		
		resizableWidget = ResizebleWidget(self)


#main 
app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())