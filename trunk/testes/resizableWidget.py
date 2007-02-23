#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui




class ResizableWidget(QtGui.QWidget):
    
	def __init__(self, widget=None, parent=None):
		
		QtGui.QWidget.__init__(self, parent)				
		
		self.childWidget = widget
		self.childWidget.setParent(self)
		#self.childWidget = QtGui.QPushButton(self)		
		#self.childWidget.setEnabled(bool(0))
		
		self.setSizeIncrement(10,10)
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
		
		
		#POP-UP MENU (definição de acções)		
		self.cutAction = QtGui.QAction(QtGui.QIcon("icons/edit_cut.png"), self.tr("Cu&t"), self)
		self.cutAction.setShortcut(self.tr("Ctrl+X"))
		self.cutAction.setStatusTip(self.tr("Cut the current selection"))
		self.connect(self.cutAction, QtCore.SIGNAL("triggered()"), self.cutAct)
	
		self.copyAction = QtGui.QAction(QtGui.QIcon("icons/edit_copy.png"), self.tr("&Copy"), self)
		self.copyAction.setShortcut(self.tr("Ctrl+C"))
		self.copyAction.setStatusTip(self.tr("Copy the current selection"))
		self.connect(self.copyAction, QtCore.SIGNAL("triggered()"), self.copyAct)
	
		self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/edit_paste.png"), self.tr("&Paste"), self)
		self.pasteAction.setShortcut(self.tr("Ctrl+V"))
		self.pasteAction.setStatusTip(self.tr("Paste into the current selection"))
		self.connect(self.pasteAction, QtCore.SIGNAL("triggered()"), self.pasteAct)
	
		self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), self.tr("&Delete"), self)
		self.deleteAction.setShortcut(self.tr("Ctrl+D"))
		self.deleteAction.setStatusTip(self.tr("Delete the current selection"))
		self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)
		
		self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("Apply template..."), self)
		self.applyTemplateAction.setStatusTip(self.tr("Apply an existing template"))
		self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)
	
		self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), self.tr("Save template as..."), self)
		self.saveTemplateAsAction.setStatusTip(self.tr("Save the template"))
		self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)
		
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
	
	
	def getChildWidget(self):
		return self.childWidget

	def getX(self):
		return self.x()
		
	def getY(self):
		return self.y()
		
	def getWidth(self):
		return self.width()
		
	def getHeight(self):
		return self.height()		
	
	#-------EVENTOS----------------------------------------------------------------	
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
		self.childWidget.setGeometry(self.RectSize,self.RectSize,WidgetWidth-self.RectSize*2, WidgetHeight-self.RectSize*2)
		
	
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
			
		
		#print(mouseYpos, self.MouseLastYpos)
		"""if mouseYpos > self.MouseLastYpos:
			print("maior")					
		else:
			print("menor")
		"""
		
		#ALTERAR AS DIMENSÕES DA WIDGET DE ACORDO COM A POSIÇÃO DO RATO (caso o rato esteja pressionado numa área de alteração de tamanho)
		if self.MouseState == self.MouseClicked:
			#print(mouseYpos, self.MouseLastYpos)
			if self.pontoRef == self.RefRectLeftTop: # NO OK				
				self.setGeometry(mouseXpos, mouseYpos, widgetRect.width(), widgetRect.height())			
			elif self.pontoRef == self.RefRectCenterTop: # NO OK				
				if mouseYpos > self.MouseLastYpos:
					#print("maior")
					self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()-(mouseYpos - widgetRect.y()) )
					
				else:
					#print("menor")
					self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()+(widgetRect.y() - mouseYpos) )
					#self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()+(widgetRect.y() - mouseYpos) )
				
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


	def contextMenuEvent(self, event):

		menu = QtGui.QMenu(self)
		menu.addAction(self.cutAction)
		menu.addAction(self.copyAction)
		menu.addAction(self.pasteAction)
		menu.addAction(self.deleteAction)
		menu.addSeparator();
		menu.addAction(self.applyTemplateAction)
		menu.addAction(self.saveTemplateAsAction)
		menu.exec_(event.globalPos())
	
	def cutAct(self):
		print("")

	def copyAct(self):
		print("")

	def pasteAct(self):
		print("")

	def deleteAct(self):
		print("")
		
	def applyTemplateAct(self):
		print("")

	def saveTemplateAsAct(self):
		print("")


	#DEFINIÇÃO DE FUNÇÕES GLOBAIS
	"""def setText(self,text):
		self.childWidget.setText(text)
	"""
	def setFont(self, Font):
		self.childWidget.setFont(Font)


#-------------------------------------------------------------------------------------
class ResizableAbstractButton(ResizableWidget):
	def __init__(self, widget = None, parent=None):
		self.AbstractButtonWidget = widget
		ResizableWidget.__init__(self, self.AbstractButtonWidget,  parent)
		
	def setText(self, strText):
		self.AbstractButtonWidget.setText(strText)
				
	def getText(self):
		return self.AbstractButtonWidget.text()	
		

class ResizableAbstractIO(ResizableWidget):

	def __init__(self, widget = None, parent=None):
		self.AbstractIOWidget = widget
		ResizableWidget.__init__(self, self.AbstractIOWidget,  parent)
		
	def setText(self, strText):
		self.AbstractIOWidget.setText(strText)
				
	def getText(self):
		return self.AbstractIOWidget.text()	
		

#-------------------------------------------------------------------------------------
class ResizableButton(ResizableAbstractButton):
	def __init__(self, parent=None):
		self.Button = QtGui.QPushButton()
		ResizableAbstractButton.__init__(self, self.Button,  parent)	
	
	"""def __init__(self, strText, parent=None):
		self.Button = QtGui.QPushButton(strText)
		ResizableWidget.__init__(self, self.Button,  parent)	
		
	def __init__(self, strText, Icon, parent=None):
		self.Button = QtGui.QPushButton(strText, Icon)
		ResizableWidget.__init__(self, self.Button,  parent)	
	"""
	
	def setIcon(self, Icon):
		self.Button.setIcon(Icon)


#-------------------------------------------------------------------------------------
class ResizableCheckBox(ResizableAbstractButton):
	def __init__(self, parent=None):
		self.checkBox = QtGui.QCheckBox()
		ResizableAbstractButton.__init__(self, self.checkBox,  parent)	
	
	def setChecked(self):
		self.checkBox.setCheckedState(QtCore.Qt.Checked)
	
	def setUnchecked(self):
		self.checkBox.setCheckedState(QtCore.Qt.Unchecked)
		
	def isChecked(self):
		checked = bool(0)		
		
		if self.checkBox.checkState() == QtCore.Qt.Checked:
			checked = bool(1)
		
		return checked


#-------------------------------------------------------------------------------------
class ResizableLabel(ResizableAbstractIO):
	def __init__(self, parent=None):
		self.Label = QtGui.QLabel()
		ResizableAbstractIO.__init__(self, self.Label,  parent)
	
	def setAlign(self, Alignment):
		self.Label.setAlignment(Alignment)
	
	def setAlignLeft(self):
		self.Label.setAlignment(QtCore.Qt.AlignLeft)
		
	def setAlignRight(self):
		self.Label.setAlignment(QtCore.Qt.AlignRight)
		
	def setAlignCenter(self):
		self.Label.setAlignment(QtCore.Qt.AlignHCenter)
		
	def setAlignJustify(self):
		self.Label.setAlignment(QtCore.Qt.AlignJustify)
	
	
	def setText(self, strText):
		self.Label.setText(strText)	
	
	def enabledWordWrap(self):
		self.Label.setWordWrap(bool(1))
		
	def disabledWordWrap(self):
		self.Label.setWordWrap(bool(0))
		
		
#-------------------------------------------------------------------------------------
class ResizableLineEdit(ResizableAbstractIO):
	def __init__(self, parent=None):
		self.LineEdit = QtGui.QLineEdit()
		ResizableAbstractIO.__init__(self, self.LineEdit, parent)
	
	def setLength(self, lenght):
		self.LineEdit.setMaxLenght(lenght)
		
	def enableReadOnly(self):
		sself.LineEdit.setReadOnly(bool(1))
		
	def disableReadOnly(self):
		self.LineEdit.setReadOnly(bool(0))

	def getText(self):
		return self.LineEdit.text()
	

class ResizableTextEdit(ResizableAbstractIO):
	def __init__(self, parent=None):
		self.TextEdit = QtGui.QTextEdit()
		ResizableAbstractIO.__init__(self, self.TextEdit, parent)	
	
	def enableReadOnly(self):
		self.TextEdit.setReadOnly(bool(1))
		
	def disableReadOnly(self):
		self.TextEdit.setReadOnly(bool(0))
	
	def enableWordWrap(self):
		self.TextEdit.setWordWrapMode(QtCore.QTextOption.WordWrap)
	
	"""def getText(self):
		return self.TextEdit.toPlainText()
	"""


		
	
	
#-------------------------------------------------------------------------------------
class ResizableComboBox(ResizableWidget):
	def __init__(self, parent=None):
		self.ComboBox = QtGui.QComboBox()
		ResizableWidget.__init__(self, self.ComboBox,  parent)	

#-------------------------------------------------------------------------------------
class ResizableGroupBox(ResizableWidget):
	def __init__(self, parent=None):
		self.GroupBox = QtGui.QGroupBox()
		ResizableWidget.__init__(self, self.GroupBox,  parent)	


#-------------------------------------------------------------------------------------
class ResizableListView(ResizableWidget):
	def __init__(self, parent=None):
		self.ListView = QtGui.QListView()
		ResizableWidget.__init__(self, self.ListView,  parent)	


#-------------------------------------------------------------------------------------
#Associar com um QButtonGroup....
class ResizableRadioButton(ResizableWidget):
	def __init__(self, parent=None):
		self.RadioButton = QtGui.QRadioButton()
		ResizableWidget.__init__(self, self.RadioButton,  parent)	
			

#-------------------------------------------------------------------------------------
class ResizableTabBar(ResizableWidget):
	def __init__(self, parent=None):
		self.TabBar = QtGui.QTabBar()
		ResizableWidget.__init__(self, self.TabBar,  parent)
		
	def addTab(self, text):
		self.TabBar.addTab(text)
 
#-------------------------------------------------------------------------------------
class ResizableTreeView(ResizableWidget):
	def __init__(self, parent=None):
		self.TreeView = QtGui.QTreeView()
		ResizableWidget.__init__(self, self.TreeView,  parent)
 

#-------------------------------------------------------------------------------------
class ResizableToolBar(ResizableWidget):
	def __init__(self, parent=None):
		self.ToolBar = QtGui.QToolBar()
		ResizableWidget.__init__(self, self.ToolBar,  parent)


#-------------------------------------------------------------------------------------
class ResizableDialogWindow(ResizableWidget):
	def __init__(self, parent=None):
		self.DialogWindow = QtGui.QDialog()
		ResizableWidget.__init__(self, self.DialogWindow,  parent)
#(..... CONTINUAR WIDGETS)








#-------------------------------------------------------------------------------------
class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		#widgetRect = self.geometry()

                #childWidget = QtGui.QPushButton(self)
		#childWidget = QtGui.QLabel(self)
		
		#self.resizableBtn = ResizableButton(self)
		self.w = ResizableCheckBox(self)
		
		
		Btn = QtGui.QPushButton(self)
		Btn.setGeometry(21, self.w.getHeight(), 100,30)
		self.connect(Btn, QtCore.SIGNAL("clicked()"), 
					self.info)
		
		
	def info(self):
		#print(self.resizableWidget.getWidth())
		self.w.setText("teste")
		#self.w.setAlignLeft()
		print(self.w.isChecked())
		
#-------------------------------------------------------------------------------------

#main 
app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())
