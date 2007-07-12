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
SIGNAL_PROPERTIES_TO_CHANGE = "PropertiesToChange(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
#SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de items
SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Items_Changed" #ENVIO DE: typeControl; idControl; lista de items
SIGNAL_RESIZABLE_MENUS_CHANGED = "Resizable_Menus_Changed" #ENVIO DE: typeControl; idControl; lista de items
#SIGNAL_RESIZABLE_TABS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de tabs
SIGNAL_RESIZABLE_TABS_CHANGED = "Resizable_Tabs_Changed" #ENVIO DE: typeControl; idControl; lista de tabs
SIGNAL_RESIZABLE_TABLE_CHANGED = "Resizable_Clicked" #ENVIO IMPLICITO DE: typeControl; idControl; tableData (objecto com os dados da tabela)
SIGNAL_RESIZABLE_RELEASED = "Resizable_Released(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
SIGNAL_RESIZABLE_KEYBOARD_MOVED = "Resizable_Released(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
SIGNAL_CONTROL_CLICKED = "Control_Clicked(const QString &, const QString &)"
SIGNAL_PROPERTY_CHANGED = "Property_Changed" #ENVIO IMPLICITO DE: idProperty; propertyValue
SIGNAL_NONE_CONTROL_SELECTED = "None_Control_Selected" # INDICA��O QUE A DRAW AREA FOI CLICADA
SIGNAL_RESIZABLE_DELETE = "Resizable_Delete" #INDICA��O PARA ELIMINAR OS CONTROLOS SELECCIONADOS
SINGNAL_INTERFACE_CHANGED = "InterfaceChanged" #INDICA��O QUE A INTERFACE FOI ALTERADA
SIGNAL_RESIZABLE_SAVE_TEMPLATE = "Resizable_SaveTemplate(const QString &, const QString &)" #ENVIO DE: typeControl; idControl 
SIGNAL_RESIZABLE_APPLY_TEMPLATE = "Resizable_ApplyTemplate(const QString &, const QString &)" #ENVIO DE: typeControl; idControl 


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

#DESIGNA��O DOS CONTROLOS
BTN = "Button"
CKB = "CheckBox"
CMB = "ComboBox"
GRB = "GroupBox"
IFR = "Iframe"
LBL = "Label"
LST = "List"
MBR = "MenuBar"
PWF = "PasswordField"
RDB = "RadioButton"
SPR = "Spinner"
TBV = "TabView"
TXV = "TextArea"
TXF = "TextField"
TLB = "ToolBar"
TRE = "Tree"
TBL = "Table"

#MAPA COM OS TIPOS DE CONTROLOS E SUAS RESPECTIVAS DESIGNA��ES
CONTROLS_DESIGNATIONS = {
TButton : BTN,
TCheckBox : CKB,
TCombo : CMB,
TGroupBox : GRB,
TIframe : IFR,
TLabel : LBL,
TList : LST,
TMenuBar : MBR,
TPasswordField : PWF,
TRadioButton : RDB,
TSpinner : SPR,
TTabView : TBV,
TTextArea : TXV,
TTextField : TXF,
TToolBar : TLB,
TTree : TRE,
TTable : TBL
}


#STANDART CONTROL NAME INFORMATION
CONTROL_LABEL = "Control: "

#TIPOS DE PROPRIEDADES
TINT = "TInt"
TFLOAT = "TFloat"
TSTRING = "TString"
TBOOLEAN = "TBoolean"
TITEMS = "TItems"
TMENUS = "TMenus"
TTABLEITEMS = "TTableItems" 
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
menusControls = [TMenuBar]
tabsControls = [TTabView]
tableControls = [TTable]

#LISTA QUE IDENTIFICA QUAIS OS TIPOS DE PROPRIEDADES COM MAIS QUE UMA OP��O
multiPropretyValues = [TBOOLEAN]

#LISTA QUE IDENTIFICA QUAIS OS TIPOS DE DADOS DE PROPRIEDADE QUE N�O S�O PARA SER APRESENTADOS NA WIDGET DE ALTERA��O DE PROPRIEDADES
specificTypeProperties = [TITEMS, TMENUS, TTABLEITEMS, TTABS]

#TIPOS DE ERROS
generalError = -1
structureError = -2

#MENSAGENS DE ERRO
ERROR_OPEN_FILE = "Error opening file."
ERROR_ACCESS_STRUCTURE = "Error accessing the data structure."

#TITULOS DAS JANELAS
TITLE_MAIN_WINDOW = "Qooxdoo GUI Builder"
TITLE_EDIT_ITEMS = TITLE_MAIN_WINDOW+" - "+"Edit items"
TITLE_EDIT_TABS = TITLE_MAIN_WINDOW+" - "+"Edit tabs"
TITLE_EDIT_TABLE = TITLE_MAIN_WINDOW+" - "+"Edit table"
TITLE_EDIT_MENUS = TITLE_MAIN_WINDOW+" - "+"Edit menus"
TITLE_PREVIEW_APP = TITLE_MAIN_WINDOW+" - "+"Preview Interface"

#DRAW AREA VIEWPORT MARGINS
MARGIN = 15

#LIMITES MINIMOS DE REDIMENSIONAMENTO
MIN_RESIZABLE_WIDTH = 15
MIN_RESIZABLE_HEIGHT = 15

#ALTURA DAS LINHAS DA DOCK DAS PROPRIEDADES
PROPERTIES_ROWS_HEIGHT = 20

#DEFINI��O DOS VALORES MINIMOS E M�XIMOS QUE AS PRORIEDADES INT PODEM ASSUMIR
MIN_TINT_PROPERTY_VALUE = -100
MAX_TINT_PROPERTY_VALUE = 1000

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
"""PERCENT_LARGURA_POR_ALTURA = 0.7516
DRAW_AREA_HEIGHT = 950
DRAW_AREA_WIDTH = DRAW_AREA_HEIGHT * PERCENT_LARGURA_POR_ALTURA
"""
DRAW_AREA_HEIGHT = 560
DRAW_AREA_WIDTH = 1000

DESIGN_AREA_HEIGHT = DRAW_AREA_HEIGHT + 30
DESIGN_AREA_WIDTH = DRAW_AREA_WIDTH + 30

#DEFINI��O DOS TITULOS DA PROPERTIES_WIDGET (Ecr� Principal)
PROPERTIES_WIDGET_COLUMN1 = "Property"
PROPERTIES_WIDGET_COLUMN2 = "Value"


#ID's de Propriedades GENERICAS
ID_TOP = "G01"
ID_LEFT = "G02"
ID_HEIGHT = "G08"
ID_WIDTH = "G05"


#DEFINI��ES SOBRE AS DIALOGS DE ABRIR/GRAVAR FICHEIROS
TITLE_OPEN_DIALOG = "Open interface"
TITLE_SAVE_DIALOG = "Save interface"
TITLE_OPEN_TEMPLATE_DIALOG = "Open template"
TITLE_SAVE_TEMPLATE_DIALOG = "Save template"
TITLE_APPLY_TEMPLATE_DIALOG = "Apply template"
ROOT_DIRECTORY = "./"
FILES_FILTER_INTERFACE = "YAML Interface Files (*.ymli)"
FILES_FILTER_TEMPLATE = "YAML Template Files (*.ymlt)"
FILES_FILTER_HTML = "HTML Files (*.html)"
FILE_EXTENSION_INTERFACE = ".ymli"
FILE_EXTENSION_TEMPLATE = ".ymlt"
FILE_EXTENSION_HTML = ".html"



#DEFINI��O DO TIMEOUT DAS MENSAGENS DA STATUSBAR
TIMEOUT_MSG = 2000

#MENSAGENS UTILIZADOR
MSG_FILE_ALREADY_EXISTS = "File &1 already exists.\n"+"Do you want to overwrite it?"
MSG_CANNOT_SAVE_FILE = "Cannot write YAML file %1:\n %2."
MSG_CANNOT_READ_FILE = "Cannot read file %1:\n%2."
MSG_FILE_SAVED = "File saved"
MSG_FILE_LOADED = "File loaded"
MSG_INTERFACE_TO_SAVE = "Do you want to save the changes you made?"
MSG_INTERFACE_FILE_TO_SAVE = "Do you want to save the changes you made to '%1'?"
MSG_QUESTION_DELETE_CONTROL = "Do you really wish to delete the selected control(s)?"


#DIRECTORIO + NOME FICHEIRO, SOBRE O FICHEIRO TEMPOR�RIO HTML PARA PR�_VISUALIZA��O NUM BROWSER
TMP_DIR_HTML_FILE = ".\\generatedHTMLs\\_TMP_PAGE_.html"

