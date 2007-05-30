#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui

#DEFINI��O DAS DIRECTORIAS
DIR_CONTROLS = "controls/"
DIR_ICONS = "icons/"
DIR_CONTROLS_DATA = "data/"
DIR_MONITOR = "monitorization/"
DIR_WIDGETS = "widgets/"
DIR_LIBS = "libraries/"
DIR_UTILITIES = "utilities/"


#DEFINI��O DE SINAIS
SIGNAL_RESIZABLE_CLICKED = "Resizable_Clicked(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
SIGNAL_RESIZABLE_SELECTED = "Resizable_Selected()" #indica��o que foi seleccionada a resizable (para que das outras resizable seja retirado o rebordo)
#SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de items
SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Items_Changed" #ENVIO DE: typeControl; idControl; lista de items
#SIGNAL_RESIZABLE_TABS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de tabs
SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Tabs_Changed" #ENVIO DE: typeControl; idControl; lista de tabs
SIGNAL_RESIZABLE_TABLE_CHANGED = "Resizable_Clicked" #ENVIO IMPLICITO DE: typeControl; idControl; tableData (objecto com os dados da tabela)
SIGNAL_RESIZABLE_RELEASED = "Resizable_Released(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
SIGNAL_CONTROL_CLICKED = "Control_Clicked(const QString &, const QString &)"
SIGNAL_PROPERTY_CHANGED = "Property_Changed" #ENVIO IMPLICITO DE: idProperty; propertyValue
SIGNAL_NONE_CONTROL_SELECTED = "None_Control_Selected" # INDICA��O QUE A DRAW AREA FOI CLICADA

#DEFINIC�O DOS FICHEIROS COM AS INFORMA��ES SOBRE OS CONTROLOS
FILE_CONTROLS_PROPERTIES= "ControlsDataTypes.dat"
FILE_GLOBAL_PROPERTIES= "Global_Properties.dat"

#BOOLEANOS
true = bool(1)
false = bool(0)

#TIPOS DE CONTROLOS
TButton = "BTN"
TCheckBox = "CKB"
TCombo = "CMB"
TGroupBox = "GRB"
TIframe = "IFR"
TLabel = "LBL"
TList = "LST"
TMenuBar = "MBR"
TPasswordField = "PWF"
TRadioButton = "RDB"
TSpinner = "SPR"
TTabView = "TBV"
TTextArea = "TXV"
TTextField = "TXF"
TToolBar = "TLB"
TTree = "TRE"
TTable = "TBL"

#TIPOS DE PROPRIEDADES
TINT = "TInt"
TFLOAT = "TFloat"
TSTRING = "TString"
TBOOLEAN = "TBoolean"
TITEMS = "TItems"
TTABS = "TTabs"
TICON = "TIcon"
TALIGN = "TAlign"


#DEFINI��O DA PROPRIEDADE DE ALINHAMENTO
ALIGN_LEFT = "left"
ALIGN_RIGHT = "right"
ALIGN_CENTER = "center"
ALIGN_JUSTIFY = "justify" 


#LISTA QUE IDENTIFICA OS CONTROLOS ESPECIAIS QUE UTILZAM ITEMS COMO PROPRIEDADE
itemsControls = [TList, TCombo]
tabsControls = [TTabView]
tableControls = [TTable]

#LISTA QUE IDENTIFICA QUAIS OS TIPOS DE PROPRIEDADES COM MAIS QUE UMA OP��O
multiPropretyValues = [TBOOLEAN]

#LISTA QUE IDENTIFICA QUAIS OS TIPOS DE DADOS DE PROPRIEDADE QUE N�O S�O PARA SER APRESENTADOS NA WIDGET DE ALTERA��O DE PROPRIEDADES
specificTypeProperties = [TITEMS, TTABS]

#TIPOS DE ERROS
generalError = -1
structureError = -2

#MENSAGENS DE ERRO
ERROR_OPEN_FILE = "Erro na abertura do ficheiro."
ERROR_ACCESS_STRUCTURE = "Erro no acesso � estrutura de dados."

#TITULOS DAS JANELAS
TITLE_EDIT_ITEMS = "Qooxdoo GUI Builder - Edit Items"
TITLE_EDIT_TABS = "Qooxdoo GUI Builder - Edit Tabs"
TITLE_EDIT_TABLE = "Qooxdoo GUI Builder - Edit Table"

#DRAW AREA VIEWPORT MARGINS
MARGIN = 15

#LIMITES MINIMOS DE REDIMENSIONAMENTO
MIN_RESIZABLE_WIDTH = 15
MIN_RESIZABLE_HEIGHT = 15

#DEFINI��O DE CORES
DRAW_AREA_COLOR = QtGui.QPalette.Button
BACKGROUNDS_COLOR = QtGui.QPalette.NoRole

#DEFINI��O DAS AC��O DE DRAG
DRAG_COPY_ACTION = "DCopy"
DRAG_MOVE_ACTION = "DMove"

#DEFINI��O DE UM MIME DATA PARA O DRAG E DROP
APLICATION_RESIZABLE_TYPE = "application/x-dnditemdata"

#DEFINI��O DAS FUN��ES DA CLASSE RESIZABLE_WIDGET SOBRE O PROCESSO DE SELEC��O (marcar um controlo como seleccionado)
METHOD_DISABLE_SELECTION = "disableSelected()"
METHOD_ENABLE_SELECTION = "enableSelected()"

#DEFINI��O DO TAMANHO DO PASSO DE MOVIMENTA��O DOS CONTROLOS (pelo teclado)
STEP_MOVE = 5

#DEFINI��O DO N� DE PIXELS MINIMO � EXECU��O DO DRAG E DROP
PIXELS_TO_DRAG = 5

#DEFINI��O DO TAMANHO DA DRAW AREA
DRAW_AREA_WIDTH = 2000
DRAW_AREA_HEIGHT = 5000

#DEFINI��O DOS TITULOS DA PROPERTIES_WIDGET (Ecr� Principal)
PROPERTIES_WIDGET_COLUMN1 = "Property"
PROPERTIES_WIDGET_COLUMN2 = "Value"


#ID's de Propriedades GENERICAS
ID_LEFT = "G02"
ID_TOP = "G01"
ID_HEIGHT = "G08"
ID_WIDTH = "G05"
