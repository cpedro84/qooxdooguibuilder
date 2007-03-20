#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui




class ResizableWidget(QtGui.QWidget):
    
	def __init__(self, typeControl, Id, widget=None, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
				
		self.childWidget = widget
		self.childWidget.setParent(self)
		
		#ID DE IDENTIFICAÇÃO DA WIDGET
		self.IdControl = Id
		self.typeControl = typeControl
		
		self.setSizeIncrement(10,10)
		self.setMouseTracking(bool(1))
		
		#DEFINIÇÃO De ANCORAS (CLIPING)
		self.clipHeight = bool(0)
		self.clipWidth = bool(0)
		self.clipLeft = bool(0)
		self.clipTop = bool(0)
		
		#DEFINIÇÃO DO POSICIONAMENTO (x->left; y->top)
		self.left = 0.0
		self.top = 0.0
		
		#DEFINIÇÃO DAS DIMENSÕES da WIDGET resizable (width, height)		
		self.height = 0.0
		self.maxHeight = 0.0
		self.minHeight = 0.0
				
		self.width = 0.0
		self.maxWidth = 0.0
		self.minWidth = 0.0
				
		#DEFINIÇÃO DAS MARGENS
		self.marginTop = 0.0
		self.marginBotton = 0.0
		self.marginLeft = 0.0
		self.marginRight= 0.0
		
		#DEFINIÇÃO ORIENTAÇÃO
		self.horizontal = 1
		self.vertical = 2		
		self.orientation = self.horizontal
		
		#DEFINIÇÃO DA PALETTE
		self.palette = QtGui.QPalette()
		self.childWidget.setPalette(self.palette)
		self.childWidget.setUpdatesEnabled(bool(1))
			
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
	
	#-------EVENTOS----------------------------------------------------------------	
	def paintEvent(self, event):
		
		#DEFINIR CURSOR DO RATO
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
		#DEFINIR PALETTE
		#self.childWidget.paletteChange(self.palette)
		
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

		
		self.emit(QtCore.SIGNAL("clicked_(const QString &)"), 'benfica')

	
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

#*******************************************************************
	#DEFINIÇÃO DE FUNÇÕES GLOBAIS
	def getChildWidget(self):
		return self.childWidget

	def getX(self):
		return self.childWidget.x()
		
	def getY(self):
		return self.childWidget.y()
		
	def getWidth(self):
		return self.childWidget.width()
		
	def getHeight(self):
		return self.childWidget.height()	
	
	
	def setFont(self, Font):
		self.childWidget.setFont(Font)

	def disable(self):
		self.childWidget.setDisable(bool(1))
	
	def enable(self):
		self.childWidget.setEnable(bool(1))
	
	
	def setVisibility(self, isVisible):
		
		if isVisible == "true":
			self.childWidget.setVisible(bool(1))
		else:
			self.childWidget.setVisible(bool(0))
		
	

	def clipHeight(self):
		self.clipHeight = bool(1)
		
	def clipWidth(self):
		self.clipWidth = bool(1)		
		
	def clipLeft(self):
		self.clipLeft = bool(1)
		
	def clipTop(self):
		self.clipTop = bool(1)
		
	#def removeClip(self, clipName):
	
	def removeAllClips(self):
		self.clipHeight = bool(0)
		self.clipWidth = bool(0)
		self.clipLeft = bool(0)
		self.clipTop = bool(0)
		
		
	#************DEFINIÇÃO DE CORES************???
	#BackGround Color
	def setBaseColor(self, color):
		self.palette.setColor( QtGui.QPalette.Base, color)		
		self.childWidget.update()
		
		
	def setTextColor(self, color):
		self.palette.setColor(QtGui.QPalette.Text, color)		
		self.childWidget.update()
		
	
	def setWindowColor(self, color):
		self.palette.setColor(QtGui.QPalette.Window, color)
		#self.childWidget.setAutoFillBackground(bool(1))
		self.childWidget.update()
	
	#************************************************
	
	def setHeight(self, height):
		self.height = height
		widgetRect = self.geometry()
		self.setGeometry(widgetRect.x(), widgetRect.y(), widgetRect.width(), height)

	def setWidth(self, width):
		self.width = width
		widgetRect = self.geometry()
		self.setGeometry(widgetRect.x(), widgetRect.y(), width, widgetRect.height())
		
	def setLeft(self, left):
		self.left = left
		widgetRect = self.geometry()
		self.setGeometry(left, widgetRect.y(), widgetRect.width(), widgetRect.height())
		
	def setTop(self, top):
		self.top = top
		widgetRect = self.geometry()
		self.setGeometry(widgetRect.x(), top, widgetRect.width(), widgetRect.height())
	
	def setMaxHeight(self, maxHeight):
		self.maxHeight = maxHeight
	
	def setMinHeight(self, minHeight):
		self.minHeight = minHeight
		
	def setMaxWidth(self, maxWidth):
		self.maxWidth = maxWidth
	
	def setMinWidth(self, minWidth):
		self.minWidth = minWidth
		
	#função que através da indicação da margem, e registado o seu tamanho (FAZER)
	#def setMarginSize():

	
	
#*******************************************************************


	
#-------------------------------------------------------------------------------------
class ResizableAbstractButton(ResizableWidget):
	def __init__(self, id, widget = None, parent=None):
		self.AbstractButtonWidget = widget
		ResizableWidget.__init__(self, id, self.AbstractButtonWidget,  parent)
		
	def setText(self, strText):
		self.AbstractButtonWidget.setText(strText)
				
	def getText(self):
		return self.AbstractButtonWidget.text()	
		

class ResizableAbstractIO(ResizableWidget):

	def __init__(self, typeControl, id, widget = None, parent=None):
		self.AbstractIOWidget = widget
		ResizableWidget.__init__(self, typeControl, id, self.AbstractIOWidget,  parent)
		
	def setText(self, strText):
		self.AbstractIOWidget.setText(strText)
				
	def getText(self):
		return self.AbstractIOWidget.text()	
		

#-------------------------------------------------------------------------------------
class ResizableButton(ResizableAbstractIO):
	def __init__(self, id, parent=None):
		self.Button = QtGui.QPushButton()
		ResizableAbstractIO.__init__(self, id, self.Button,  parent)	
	
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
	
	def enabledWordWrap(self):
		self.Label.setWordWrap(bool(1))
		
	def disabledWordWrap(self):
		self.Label.setWordWrap(bool(0))
		
		
#-------------------------------------------------------------------------------------
class resizableTextField(ResizableAbstractIO):
	def __init__(self, typeControl, id, parent=None, interactiveMode = QtGui.QLineEdit.Normal):
		self.LineEdit = QtGui.QLineEdit()
		ResizableAbstractIO.__init__(self, typeControl, id, self.LineEdit, parent)
		self.LineEdit.setEchoMode(interactiveMode)
	
	def setLength(self, lenght):
		self.LineEdit.setMaxLenght(lenght)
		
	def enableReadOnly(self):
		sself.LineEdit.setReadOnly(bool(1))
		
	def disableReadOnly(self):
		self.LineEdit.setReadOnly(bool(0))
		

class ResizableTextArea(ResizableAbstractIO):
	def __init__(self, parent=None):
		self.TextEdit = QtGui.QTextEdit()
		ResizableAbstractIO.__init__(self, self.TextEdit, parent)	
	
	def enableReadOnly(self):
		self.TextEdit.setReadOnly(bool(1))
		
	def disableReadOnly(self):
		self.TextEdit.setReadOnly(bool(0))
	
	def enableWordWrap(self):
		self.TextEdit.setWordWrapMode(QtCore.QTextOption.WordWrap)
	

#-------------------------------------------------------------------------------------
class ResizableComboBox(ResizableWidget):
	def __init__(self, parent=None):
		self.ComboBox = QtGui.QComboBox()
		ResizableWidget.__init__(self, self.ComboBox,  parent)	

	def addItem(self, strText):
		self.ComboBox.addItem(strText)
		
	def addItemIcon(self, strText, Icon):
		self.ComboBox.addItem(Icon, strText)
		
	def addItems(self, vTexts):
		self.ComboBox.addItems(self, vTexts)
	
	def insertItem(self, index, strText):
		self.ComboBox.insertItem(index, strText)
	
	def insertItem(self, index, strText, icon):
		self.ComboBox.insertItem(index, icon, strText)

	def insertItems(self, index, vTexts):
		self.ComboBox.insertItems(index, vTexts)

		
	def enableEditable(self):
		self.ComboBox.setEditable(bool(1))
		
	def disableEditable(self):
		self.ComboBox.setEditable(bool(0))
		
	def isEditable(self):
		return self.ComboBox.isEditable()
		
	def setCurrentIndex(self, index):
		self.ComboBox.setCurrentIndex(index)

	def setEditText(self, strText):
		self.ComboBox.setEditText(strText)
	
	def setItemText(self, index, strText):
		self.ComboBox.setItemText(self, index, strText)
	
	def setItemIcon(self, index, icon):
		self.ComboBox.setItemIcon(self, index, icon)

	def count(self):
		self.ComboBox.count()

	
	def getItemText(self, index):
		return self.ComboBox.itemText(index)
		
	def getItemIcon(self, index):
		return self.ComboBox.itemIcon(index)
		
	"""def getItems(self):
		#(...) - conjunto de todos os item de texto...
	"""
	
	def getSelectedItem(self):
		return self.ComboBox.currentIndex()
	
	

#-------------------------------------------------------------------------------------
class ResizableList(ResizableWidget):
	def __init__(self, parent=None):
		self.ListView = QtGui.QListWidget()
		ResizableWidget.__init__(self, self.ListView,  parent)
		self.items = []
		#PROPREIDADES
		self.selectable = bool(1)

	def enableSelectable(self):
		self.selectable = bool(1)
		
	def disableSelectable(self):
		self.selectable = bool(0)
		
	#def setBackgroundImage(strPath):
	
	def addItem(self, item):
		self.append(item)
	

#-------------------------------------------------------------------------------------
class ResizableGroupBox(ResizableWidget):
	def __init__(self, parent=None):
		self.GroupBox = QtGui.QGroupBox()
		ResizableWidget.__init__(self, self.GroupBox,  parent)	



#-------------------------------------------------------------------------------------
#Associar com um QButtonGroup....
class ResizableRadioButton(ResizableWidget):
	def __init__(self, parent=None):
		self.RadioButton = QtGui.QRadioButton()
		ResizableWidget.__init__(self, self.RadioButton,  parent)	
			

#-------------------------------------------------------------------------------------
class ResizableTabView(ResizableWidget):
	def __init__(self, parent=None):
		self.TabBar = QtGui.QTabBar()
		ResizableWidget.__init__(self, self.TabBar,  parent)
		
	def addTab(self, text):
		self.TabBar.addTab(text)
 
#-------------------------------------------------------------------------------------
class ResizableTree(ResizableWidget):
	def __init__(self, parent=None):
		self.TreeView = QtGui.QTreeView()
		ResizableWidget.__init__(self, self.TreeView,  parent)
 

#-------------------------------------------------------------------------------------
class ResizableToolBar(ResizableWidget):
	def __init__(self, parent=None):
		self.ToolBar = QtGui.QToolBar()
		ResizableWidget.__init__(self, self.ToolBar,  parent)


#-------------------------------------------------------------------------------------
#??????
class ResizableDialogWindow(ResizableWidget):
	def __init__(self, parent=None):
		self.DialogWindow = QtGui.QDialog()
		ResizableWidget.__init__(self, self.DialogWindow,  parent)
#(..... CONTINUAR WIDGETS)

#-------------------------------------------------------------------------------------



class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		self.w = resizableTextField("12","12", self)
		
		QtCore.QObject.connect(self.w, QtCore.SIGNAL("clicked_(const QString &)"), self.SignalReceive)
		

	def SignalReceive(self, text):		
		
		print text
	
#-------------------------------------------------------------------------------------

#main 
app = QtGui.QApplication(sys.argv)
widget = MainWidget()
widget.show()
sys.exit(app.exec_())


