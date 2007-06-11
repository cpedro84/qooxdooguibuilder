#!/usr/bin/env python
# -*- encoding: latin1 -*-



import sys
from PyQt4 import QtCore, QtGui



from const import *
from editItemsWidget import *
from editTableItemsWidget import *
from generalFunctions import *
from projectExceptions import *
from tableWidget import *
from listWidget import *

class ResizableWidget(QtGui.QWidget):
    
	def __init__(self, typeControl, Id, widget=None, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
				
		self.childWidget = widget
		self.childWidget.setParent(self)		
				
		#Formatar output da Widget que representa o controlo
		self.childWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.childWidget.setEnabled(false)		
		#self.setEnabled(true)
		#self.blockSignals(true)
		self.childWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))		
		#self.childWidget.setFrameShape(QtGui.QFrame.Panel)
		#self.childWidget.setFrameShadow(QtGui.QFrame.Raised)
		#self.childWidget.setWindowState(self.childWidget.windowState() and not QtCore.Qt.WindowActive)
		#self.childWidget.setWindowFlags(self.childWidget.windowFlags() | QtCore.Qt.FramelessWindowHint)


		self.havePopUpMenusExtra = false
		self.popUpMenusExtraList = []
		
		
		#ID DE IDENTIFICAÇÃO DA WIDGET
		self.idControl = Id
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
		#botão de clique
		self.mouseButtonClicked =QtCore.Qt.NoButton
		#posicionamento anterior
		self.mousePressedPos = QtCore.QPoint(0,0)
		
		
		#VARIAVEL QUE CONTROLA SE A WIDGET ESTÁ SELECCIONADA
		self.isSelected = bool(0)
				
		#*************POP-UP MENU (definição de acções)************************		
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
	
		self.deleteAction = QtGui.QAction(QtGui.QIcon("icons/edit_delete.png"), self.tr("&Delete..."), self)
		self.deleteAction.setShortcut(self.tr("Ctrl+D"))
		self.deleteAction.setStatusTip(self.tr("Delete the current selection"))
		self.connect(self.deleteAction, QtCore.SIGNAL("triggered()"), self.deleteAct)
		
		self.applyTemplateAction = QtGui.QAction(QtGui.QIcon("icons/file_open.png"), self.tr("Apply template..."), self)
		self.applyTemplateAction.setStatusTip(self.tr("Apply an existing template"))
		self.connect(self.applyTemplateAction, QtCore.SIGNAL("triggered()"), self.applyTemplateAct)
	
		self.saveTemplateAsAction = QtGui.QAction(QtGui.QIcon("icons/file_save.png"), self.tr("Save template as..."), self)
		self.saveTemplateAsAction.setStatusTip(self.tr("Save the template"))
		self.connect(self.saveTemplateAsAction, QtCore.SIGNAL("triggered()"), self.saveTemplateAsAct)
		
		#Menus adicionais
		self.setExtraPopUpMenus(self.typeControl)
		
		#*************************************************
		
		
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
	
	
	#****************************************************************************************
	#**********************GESTÃO DOS MENUS EXTRA DO POP-UP MENU DA WIDGET********************
	#****************************************************************************************
	def setExtraPopUpMenus(self, typeControl):
		if self.isItemsControl(typeControl):			
			self.editItemsAction = QtGui.QAction(QtGui.QIcon("icons/editors.png"), self.tr("Edit items..."), self)
			self.editItemsAction.setStatusTip(self.tr("Edit the items"))
			self.connect(self.editItemsAction, QtCore.SIGNAL("triggered()"), self.editItems)			
			
			#Adicionar o pop-up menu extra á lista
			self.popUpMenusExtraList.append(self.editItemsAction)
			self.havePopUpMenusExtra = true	#indicação da existencia de pop-up menus extra
		
		elif self.isTabsControl(typeControl):
			self.editTabsAction = QtGui.QAction(QtGui.QIcon("icons/editors.png"), self.tr("Edit tabs..."), self)
			self.editTabsAction.setStatusTip(self.tr("Edit the tabs"))
			self.connect(self.editTabsAction, QtCore.SIGNAL("triggered()"), self.editTabs)			
			
			#Adicionar o pop-up menu extra á lista
			self.popUpMenusExtraList.append(self.editTabsAction)
			self.havePopUpMenusExtra = true	#indicação da existencia de pop-up menus extra
		
		elif self.isTableControl(typeControl):
			self.editTableAction = QtGui.QAction(QtGui.QIcon("icons/editors.png"), self.tr("Edit table..."), self)
			self.editTableAction.setStatusTip(self.tr("Edit the table"))
			self.connect(self.editTableAction, QtCore.SIGNAL("triggered()"), self.editTable)			
			
			#Adicionar o pop-up menu extra á lista
			self.popUpMenusExtraList.append(self.editTableAction)
			self.havePopUpMenusExtra = true	#indicação da existencia de pop-up menus extra
		
		#IMPLEMENTAR PARA MAIS TIPOS DE ITEMS (caso existam) ...

	
	def isItemsControl(self, typeControl):		
		try:
			itemsControls.index(typeControl) 
			return true
		except ValueError:
			return false
	
	def isTabsControl(self, typeControl):		
		try:
			tabsControls.index(typeControl) 
			return true
		except ValueError:
			return false
			
	def isTableControl(self, typeControl):
		try:
			tableControls.index(typeControl)
			return true
		except ValueError:
			return false			
	#****************************************************************************************
	#****************************************************************************************
	#****************************************************************************************
	
	
	#-------EVENTOS----------------------------------------------------------------	
	def paintEvent(self, event):
		
		#DEFINIR CURSOR DO RATO
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
		#DEFINIR PALETTE
		#self.childWidget.paletteChange(self.palette)
		
		self.widgetRect = self.geometry()
		WidgetWidth = self.widgetRect.width()
		WidgetHeight = self.widgetRect.height()
		
		#DESENHO DO REBORDO DE SELECÇÃO/ALTERAÇÃO DE TAMANHO		
		if self.isSelected: #verificar se a widget foi seleccionada
			
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
			
			#painter.drawRect(self.RectLT)
			#painter.drawRect(self.RectCT)
			#painter.drawRect(self.RectRT)
			#painter.drawRect(self.RectLB)
			#painter.drawRect(self.RectL)
			painter.drawRect(self.RectCB)
			painter.drawRect(self.RectRB)			
			painter.drawRect(self.RectR)
			
			painter.end()
		
		#REDIMENSIONAR TAMANHO DA WIDGET
		self.childWidget.setGeometry(self.RectSize,self.RectSize,WidgetWidth-self.RectSize*2, WidgetHeight-self.RectSize*2)
		
	
	def mouseMoveEvent(self, event):
		
		mouseXpos = event.x()
		mouseYpos = event.y()
		
		widgetRect = self.geometry()		
		
		#PONTOS DE REFERÊNCIA
		point = QtCore.QPoint(mouseXpos, mouseYpos)		
		
		#CASO O BOTÃO DO RATO NÃO ESTEJA PRESSIONADO ENTÃO SERÁ VERIFICADO SE A SUA POSIÇÃO ESTA DE ACORDO COM ALGUM PONTO DE ALTERAÇÃO DE DIMENSÃO
		if self.MouseState == self.MouseRelease:			
			 
			"""
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
			"""
		
			#VALIDAR POSICAO DO RATO DE ACORDO COM OS PONTOS DE REF.
			if self.IsPointInsideRect(point, self.RectCB) == bool(1): # CENTER BOTTOM
				self.pontoRef =self.RefRectCenterBottom #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
			elif self.IsPointInsideRect(point, self.RectRB) == bool(1): # RIGHT BOTTOM
				self.pontoRef =self.RefRectRightBottom #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))		
			elif self.IsPointInsideRect(point, self.RectR) == bool(1): # RIGHT
				self.pontoRef =self.RefRectRight #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))		
			else:			
				self.pontoRef = self.noRef #definir como de referência do rato
				self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
		
		#************PROCESSAMENTO DO DRAG ******************
		#CASO O BOTÃO ESQUERDO DO RATO ESTEJA PRESSIONADO ENTÃO SERÁ PROCESSADO O DRAG
		elif self.MouseState == self.MouseClicked and self.mouseButtonClicked == QtCore.Qt.LeftButton and self.pontoRef == self.noRef and (abs(event.pos().x() - self.mousePressedPos.x()) >= PIXELS_TO_DRAG or  abs(event.pos().y() - self.mousePressedPos.y()) >= PIXELS_TO_DRAG):
			
			itemData = QtCore.QByteArray()			
			dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
			dataStream << QtCore.QString(DRAG_MOVE_ACTION) << QtCore.QPoint(event.pos() - self.rect().topLeft())	
	
			mimeData = QtCore.QMimeData()
			mimeData.setData(APLICATION_RESIZABLE_TYPE, itemData)
			
			drag = QtGui.QDrag(self)			
			drag.setMimeData(mimeData)		
			drag.setHotSpot(event.pos() - self.rect().topLeft())
			
			pixmap = QtGui.QPixmap(self.rect().size())		
			pixmap.fill(QtGui.QColor(QtCore.Qt.darkCyan))
			drag.setPixmap(pixmap)
			
			#self.hide()
			
			#Vai executar o operação de drag e posteriormente verificar qual a operação que foi após o drag (Após o drag o código dentro do if vai ser executado) 			
			if drag.start(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
				self.MouseState = self.MouseRelease
				self.mouseButtonClicked = QtCore.Qt.NoButton
				self.show()
			else: #Em caso de drop inválido a widget será colocada na sua posição original
				self.MouseState = self.MouseRelease
				self.mouseButtonClicked = QtCore.Qt.NoButton
				self.show()
			self.setFocus()
			self.isSelected = true			
			self.update()
		#****************************************************************	
		#****************************************************************
		#****************************************************************
	
		#ALTERAR AS DIMENSÕES DA WIDGET DE ACORDO COM A POSIÇÃO DO RATO (caso o rato esteja pressionado numa área de alteração de tamanho)		
		if self.MouseState == self.MouseClicked:

			newRect = QtCore.QRect()
			
			if self.pontoRef == self.RefRectLeftTop: # NO OK				
				#newRect.setRect(mouseXpos, mouseYpos, widgetRect.width(), widgetRect.height())			
				self.update()
			elif self.pontoRef == self.RefRectCenterTop: # NO OK				
				self.update()
				"""
				#print "Y: "+str(mouseYpos)+" Y(ant): "+str(self.MouseLastYpos)				
				if mouseYpos >= self.MouseLastYpos:
					#print("maior")
					newRect.setRect(widgetRect.x(), widgetRect.y(), widgetRect.width(), widgetRect.height()-mouseYpos)
					
					difHeight = abs(widgetRect.height()-self.geometry().height())
					#print difHeight 
					newRect.setRect(widgetRect.x(), widgetRect.y()+difHeight, self.geometry().width(), self.geometry().height())
					#self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()-(mouseYpos - widgetRect.y()) )
					#self.setGeometry(QtCore.QRect(event.pos(), QtCore.QPoint(widgetRect.width(), widgetRect.height()-(mouseYpos - widgetRect.y()) )))
				else:
					newRect.setRect(widgetRect.x(), widgetRect.y(), widgetRect.width(), widgetRect.height()+mouseYpos)
					difHeight = abs(widgetRect.height()-self.geometry().height())
					#print difHeight 
					newRect.setRect(widgetRect.x(), widgetRect.y()-difHeight, self.geometry().width(), self.geometry().height())
					#print("menor")
					#self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()+(widgetRect.y() - mouseYpos) )
					#self.setGeometry(widgetRect.x(), mouseYpos, widgetRect.width(), widgetRect.height()+(widgetRect.y() - mouseYpos) )
					#self.setGeometry(QtCore.QRect(event.pos(), QtCore.QPoint(widgetRect.width(), widgetRect.height()+(mouseYpos - widgetRect.y()) )))
				"""
				
			elif self.pontoRef == self.RefRectRightTop:# NO OK
				#newRect.setRect(mouseXpos, widgetRect.y(), mouseXpos, mouseYpos)
				self.update()
			elif self.pontoRef == self.RefRectLeftBottom: #NO OK
				#newRect.setRect(mouseXpos, widgetRect.y(), mouseXpos, mouseYpos)
				self.update()
			elif self.pontoRef == self.RefRectCenterBottom: #OK
				newRect.setRect(widgetRect.x(), widgetRect.y(), widgetRect.width(), mouseYpos)
			elif self.pontoRef == self.RefRectRightBottom: #OK
				newRect.setRect(widgetRect.x(), widgetRect.y(), mouseXpos, mouseYpos)
			elif self.pontoRef == self.RefRectLeft: #NO OK		
				#newRect.setRect(widgetRect.x(), widgetRect.y(), mouseXpos, 0)
				self.update()
			elif self.pontoRef == self.RefRectRight: #OK
				newRect.setRect(widgetRect.x(), widgetRect.y(), mouseXpos,widgetRect.height())
			
			#VALIDAR NOVO TAMANHO DA RESIZABLE DE ACORDO COM OS LIMITES MINIMOS
			if newRect.width() > MIN_RESIZABLE_WIDTH and newRect.height() > MIN_RESIZABLE_HEIGHT: #CASO SEJA VÁLIDO ENTÃO SERÁ APLICADO O NOVO TAMANHO				
				self.resize(newRect.width(), newRect.height())
				#self.setGeometry(newRect.x(), newRect.y(), newRect.width(), newRect.height())

	def mousePressEvent(self, event):
		
		#INDICAR QUE A WIDGET FOI SELECCIONADA
		self.setFocus()
		self.isSelected = true		
		#ACTUALIZAR O ESTADO DO RATO
		self.MouseState = self.MouseClicked

		#GUARDAR POSICIONAMENTO DO RATO
		self.mousePressedPos = QtCore.QPoint(event.pos())

		#ENVIO DO SINAL DE CLIQUE PARA INFORMAR O TIPO E O ID DO CONTROLO
		self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), str(self.typeControl), str(self.idControl))
		
		self.mouseButtonClicked = event.button()
		
		self.update()
		
	def mouseReleaseEvent(self, event):
		#print "release"
		#ACTUALIZAR O ESTADO DO RATO
		self.MouseState = self.MouseRelease
		self.mouseButtonClicked = event.button()
		#ALTERAR O CURSOR DO RATO PARA O ESTADO ORIGINAL
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
	
		self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_RELEASED), str(self.typeControl), str(self.idControl))
	
	def keyPressEvent(self, event):
		#caso o evento tenha ocorrido por uma tecla desconhecida não será processado
		keyPressed = event.key()
		if  keyPressed ==  QtCore.Qt.Key_unknown or not self.isSelected:
			return
			
		#verificar se a tecla pressionada foi o DEL
		if keyPressed == QtCore.Qt.Key_Delete: #Eliminar Widget
			self.deleteAct()
		
		#obter  largura e altura da widget pai 
		widthArea = self.parentWidget().geometry().width()
		heightArea = self.parentWidget().geometry().height()
				
		height = self.geometry().height()
		width = self.geometry().width()
		
		if keyPressed == QtCore.Qt.Key_Up and validatePosition(self.x(), self.y()-STEP_MOVE, width, height, widthArea, heightArea):			
			self.move(self.x(), self.y()-STEP_MOVE)
		elif keyPressed == QtCore.Qt.Key_Down and validatePosition(self.x(), self.y()+STEP_MOVE, width, height, widthArea, heightArea):
			self.move(self.x(), self.y()+STEP_MOVE)
		elif keyPressed == QtCore.Qt.Key_Left and validatePosition(self.x()-STEP_MOVE, self.y(), width, height, widthArea, heightArea):
			self.move(self.x()-STEP_MOVE, self.y())
		elif keyPressed == QtCore.Qt.Key_Right and validatePosition(self.x()+STEP_MOVE, self.y(), width, height, widthArea, heightArea):
			self.move(self.x()+STEP_MOVE, self.y())
		elif keyPressed == QtCore.Qt.Key_Escape:
			self.clearFocus()
			self.isSelected = false
			self.repaint()
		else:		
			return
		
	
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
		#Adicionar os pop-up menus extra ao menu	
		if self.havePopUpMenusExtra:
			for menuExtra in self.popUpMenusExtraList:
				menu.addAction(menuExtra)
				menu.addSeparator()
		
		menu.addAction(self.cutAction)
		menu.addAction(self.copyAction)
		menu.addAction(self.pasteAction)
		menu.addSeparator()
		menu.addAction(self.deleteAction)
		menu.addSeparator()
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
		#ENVIO DO SINAL PARA INFORMAR QUE O CONTROLO SELECCIONADO È PARA SER ELIMINADO
		self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_DELETE), str(self.typeControl), str(self.idControl))
		
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
	def setLeft(self, left):
		left = float(left)
		self.left = left
		widgetRect = self.geometry()
		self.setGeometry(left, widgetRect.y(), widgetRect.width(), widgetRect.height())
		
	def setTop(self, top):
		top = float(top)
		self.top = top
		widgetRect = self.geometry()
		self.setGeometry(widgetRect.x(), top, widgetRect.width(), widgetRect.height())
	
	def setHeight(self, height):		
		height = float(height)
		self.height = height
		#newSize = QtCore.QSize(QtGui.QWidget(self).width(), height)
		#self.resize(newSize)
		widgetRect = self.geometry()	
		self.setGeometry(widgetRect.x(), widgetRect.y(), widgetRect.width(), height)
		

	def setWidth(self, width):		
		width = float(width)
		self.width = width
		#newSize = QtCore.QSize(width, QtGui.QWidget(self).height())
		#self.resize(newSize)
		widgetRect = self.geometry()
		self.setGeometry(widgetRect.x(), widgetRect.y(), width, widgetRect.height())
			
	def setMaxHeight(self, maxHeight):
		self.maxHeight = maxHeight
	
	def setMinHeight(self, minHeight):
		self.minHeight = minHeight
		
	def setMaxWidth(self, maxWidth):
		self.maxWidth = maxWidth
	
	def setMinWidth(self, minWidth):
		self.minWidth = minWidth
	
	
	def setMarginBottom(self, bottom):
		bottom = int(bottom)
		widgetRect = self.contentsRect()
		self.setContentsMargins(widgetRect.x(),  widgetRect.y(), widgetRect.width(), bottom) 
		
	def setMarginLeft(self, left):
		left = int(left)
		widgetRect = self.contentsRect()
		self.setContentsMargins(left,  widgetRect.y(), widgetRect.width(), widgetRect.height()) 
	
	def setMarginRight(self, right):
		right = int(right)
		widgetRect = self.contentsRect()
		self.setContentsMargins(widgetRect.x(),  widgetRect.y(), right, widgetRect.height()) 
	
	def setMarginTop(self, top):
		top = int(top)
		widgetRect = self.contentsRect()
		self.setContentsMargins(widgetRect.x(),  top, widgetRect.width(), bottom) 
	

	#função que através da indicação da margem, e registado o seu tamanho (FAZER)
	#def setMarginSize():

	def disableSelected(self):
		
		self.isSelected = false		
		self.repaint()
	
	def enableSelected(self):
		self.isSelected = true
		self.repaint()
	
	#****************PROCEDIMENTOS ESPECIAS SOBRE ACÇÕES DE POP-UP MENUS*******************
	#TCOMBO;TLIST
	def editItems(self):
		try:
			list = []
			list = self.getItems()
			widgetItems = editItemsWidget(TITLE_EDIT_ITEMS, self, list)
			if widgetItems.exec_() == QtGui.QDialog.Accepted:				 
				list = widgetItems.getItemsList()
				#Alterar na resizable respectiva do controlo os items escolhidos
				self.setItems(list)
				
				#ENVIO DO SINAL PARA INFORMAR QUE FORAM ALTERADOS ITEMS DE UM CONTROLS
				self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_ITEMS_CHANGED), str(self.typeControl), str(self.idControl), list)		
		
		except structureError_Exception, e:		
			return e.errorId
	
	#TTABVIEW
	def editTabs(self):
		try:
			list = []
			list = self.getTabs() # (....) ? 
			widgetItems = editItemsWidget(TITLE_EDIT_TABS, self, list, "Tabs")
			if widgetItems.exec_() == QtGui.QDialog.Accepted:				 
				list = widgetItems.getItemsList()
				
				#vai ser criadas as widgets dos novos items criados (...) widget = none => criação
				nelems = len(list)
				elem = 0
				while elem < nelems:					
					if list[elem].getWidget() == None:
						list[elem].setWidget(QtGui.QWidget())
					elem+=1
				
				#Alterar na resizable respectiva do controlo os items escolhidos
				self.setTabs(list)
				
				#ENVIO DO SINAL PARA INFORMAR QUE FORAM ALTERADOS ITEMS DE UM CONTROLS
				self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_TABS_CHANGED), str(self.typeControl), str(self.idControl), list)		

		except structureError_Exception, e:		
			return e.errorId
	
	#TTABLEVIEW
	def editTable(self):
		tableData = self.getTableData()
		widgetTableItems = CEditTableItemsWidget(TITLE_EDIT_TABLE, self, tableData)
		if widgetTableItems.exec_() == QtGui.QDialog.Accepted:
			#carregar as alterações efectuadas sobre a tableWidget
			tableData = widgetTableItems.getTableData()
			
			#Obter o tamanho original das colunas e linhas para posteriormente ser reposto
			#columnsWidth = self.
			
			#modificar o output tableWidget
			self.setTable(tableData)
			#alterar o tamanho das colunas e linhas de acordo com o original
			
			
			#ENVIO DO SINAL PARA INFORMAR QUE FORAM ALTERADOS ITEMS DE UM CONTROLS
			#tableData = QtCore.QObject(tableData)
			self.emit(QtCore.SIGNAL(SIGNAL_RESIZABLE_TABLE_CHANGED), str(self.typeControl), str(self.idControl), tableData.getTableItems())

	
	#********************************************************************
	
#*******************************************************************
#*******************************************************************
#*******************************************************************


class ResizableAbstractButton(ResizableWidget):
	def __init__(self, id, widget = None, parent=None):
		self.AbstractButtonWidget = widget
		ResizableWidget.__init__(self, id, self.AbstractButtonWidget,  parent)
		
	def setText(self, strText):
		self.AbstractButtonWidget.setText(strText)
				
	def getText(self):
		return self.AbstractButtonWidget.text()	


#-------------------------------------------------------------------------------------
class ResizableAbstractIO(ResizableWidget):

	def __init__(self, typeControl, id, widget = None, parent=None):
		self.AbstractIOWidget = widget
		ResizableWidget.__init__(self, typeControl, id, self.AbstractIOWidget,  parent)
		
	def setText(self, strText):
		self.AbstractIOWidget.setText(strText)
				
	def getText(self):
		return self.AbstractIOWidget.text()
	
#-------------------------------------------------------------------------------------
#??????
class ResizableDialogWindow(ResizableWidget):
	def __init__(self, typeControl, id, parent=None):
		self.DialogWindow = QtGui.QDialog()
		ResizableWidget.__init__(self, typeControl, id, self.DialogWindow, parent)

#??????
class editMenu(QtGui.QMenu):
	def __init__(self, app, parent=None):
		#QtGui.QMenu.__init__(self, "teste", parent)
		
		QtGui.QLineEdit.__init__(self, "edit",  parent)
		#self.activateWindow()
		#edit.setText("merda")
		#edit = QtGui.QLineEdit("edit",  self)	
		"""edit.selectAll()
		edit.setGeometry(self.geometry())
		edit.show()
		app.setActiveWindow(edit) 
		edit.setFocus()
		edit.grabKeyboard()
			
		self.setTitle("")
"""
#-------------------------------------------------------------------------------------
#??????
class ResizableMenuBar(ResizableWidget):	
	def __init__(self, typeControl, id, app, parent=None):
		self.MenuBar = QtGui.QMenuBar()
		ResizableWidget.__init__(self, typeControl, id, self.MenuBar, parent)
		
		self.MenuBar.setEnabled(true)
		
			
		menuHelp = editMenu(app, self.MenuBar)
		#edit = QtGui.QLineEdit("edit",  menuHelp)
		#edit.setGeometry(menuHelp.geometry().x(), menuHelp.geometry().y(), menuHelp.geometry().width(), menuHelp.geometry().height())
				
		self.MenuBar.addMenu(menuHelp)

#-------------------------------------------------------------------------------------
"""
#TESTES
class MainWidget(QtGui.QMainWindow):
	
	def __init__(self, app, parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		#self.w = ResizableButton("12","12", self)
		#self.w = ResizableTable(TTable,"12", self)
		self.w = ResizableList(TList,"12", self)
		#self.w = ResizableMenuBar(TMenuBar,"12", app, self)		
		#QtCore.QObject.connect(self.w, QtCore.SIGNAL(SIGNAL_RESIZABLE_CLICKED), self.SignalReceive)
		#QtCore.QObject.connect(self.w, QtCore.SIGNAL(SIGNAL_RESIZABLE_TABLE_CHANGED), self.Signal_tableChanged)
		#self.w.addTab(editItem("1", QtGui.QWidget()))
		#self.w.addTab(editItem("2", QtGui.QWidget()))

		Btn = QtGui.QPushButton(self)
		Btn.setGeometry(21, 49, 100,30)
		self.connect(Btn, QtCore.SIGNAL("clicked()"), 
	
	self.info)
	
	def info(self):
		self.w.removeTab(0)
	
	def SignalReceive(self, text, text2):		
		print "teste"
		#print text+" = "+text2
		
	def Signal_tableChanged(self, typeControl, idControl, map):
		print typeControl
		print idControl
		print map
#-------------------------------------------------------------------------------------

#main
app = QtGui.QApplication(sys.argv)
widget = MainWidget(app)
widget.show()
sys.exit(app.exec_())
"""
