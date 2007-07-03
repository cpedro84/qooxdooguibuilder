from const import *
from projectExceptions import *
from generalFunctions import *
from InputMask import *


## Documentation for CSpinnerEditProperty.
#
# Custumized Spinner Widget that herits all properties from Qt QLineEdit.
class CSpinnerEditProperty(QtGui.QSpinBox):
	
	## The constructor.	
	# Initializes the Spinner Widget for the given parent, with a optional initial value.
	# the type of input can be set to the given typeProperty.
	# Thhis controls represents a property identified with the idProperty.
	#
	# @Param idProperty string
	# @Param propertyValue string
	# @Param parent reference
	# @Param typeProperty string
	def __init__(self, idProperty, propertyValue = 0, parent = None):
		
		propertyValue = str(propertyValue)
		
		QtGui.QSpinBox.__init__(self, parent)		
		self.setMinimum(MIN_TINT_PROPERTY_VALUE)
		self.setMaximum(MAX_TINT_PROPERTY_VALUE)
		
		if propertyValue == "-":
			propertyValue = int(0)
		
		self.setValue(int(propertyValue))
		
		self.idProperty = idProperty
		
		self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self.valueChanged)
		self.connect(self, QtCore.SIGNAL("editingFinished()"), self.valueChanged)
	
	##
	# Set the idProperty, that the controls is associated, with the given idProperty.
	#
	# @Param idProperty string
	def setIdProperty(self, idProperty):
		self.idProperty = idProperty
	
	##
	# Set the type of input with the given typeProperty.
	#
	# @Param typeProperty string
	def setPropertyType(self, typeProperty):
		self.typeProperty = typeProperty
	
	##
	# Get the value of the control, that represents the property value.
	#
	# @Return string
	def getPropertyValue(self):
		return str(self.value())
	
	##
	# Get the idProperty, that the controls is associated.
	#
	# @Return string
	def getIdProperty(self):
		return self.idProperty
	
	def valueChanged(self, value):		
		#ENVIO DO SINAL PARA  INFORMAR QUE A PROPRIEDADE FOI ALTERADA DE ESTADO
		self.emit(QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), str(self.getIdProperty()), value)
	
	def valueChanged(self):		
		#ENVIO DO SINAL PARA  INFORMAR QUE A PROPRIEDADE FOI ALTERADA DE ESTADO
		self.emit(QtCore.SIGNAL(SIGNAL_PROPERTY_CHANGED), str(self.getIdProperty()), self.getPropertyValue())