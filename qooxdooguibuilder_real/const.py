#!/usr/bin/env python
# -*- encoding: latin1 -*-

import sys
from PyQt4 import QtCore, QtGui

#DEFINIÇÃO DAS DIRECTORIAS
DIR_CONTROLS_REPRESENTATION = "controlsRepresentation/"
DIR_ICONS = "icons/"
DIR_CONTROLS_DATA = "controlsData/"
DIR_MONITOR = "guiMonitor/"
DIR_WIDGETS = "guiWidgets/"
DIR_LIBS = "libs/"


#DEFINIÇÃO DE SINAIS
SIGNAL_RESIZABLE_CLICKED = "Resizable_Clicked(const QString &, const QString &)" #ENVIO DE: typeControl; idControl
SIGNAL_RESIZABLE_SELECTED = "Resizable_Selected()" #indicação que foi seleccionada a resizable (para que das outras resizable seja retirado o rebordo)
SIGNAL_RESIZABLE_ITEMS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de items
SIGNAL_RESIZABLE_TABS_CHANGED = "Resizable_Clicked(const QString &, const QString &, const QStringList &)" #ENVIO DE: typeControl; idControl; lista de tabs
SIGNAL_RESIZABLE_TABLE_CHANGED = "Resizable_Clicked" #ENVIO IMPLICITO DE: typeControl; idControl; tableData (objecto com os dados da tabela)

#DEFINICÃO DOS FICHEIROS COM AS INFORMAÇÕES SOBRE OS CONTROLOS
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
TDEFAULT = "TDefault"
TITEMS = "TItems"
TTABS = "TTabs"

#LISTA QUE IDENTIFICA OS CONTROLOS ESPECIAIS QUE UTILZAM ITEMS COMO PROPRIEDADE
itemsControls = [TList, TCombo]
tabsControls = [TTabView]
tableControls = [TTable]

#TIPOS DE ERROS
generalError = -1
structureError = -2

#MENSAGENS DE ERRO
ERROR_OPEN_FILE = "Erro na abertura do ficheiro."
ERROR_ACCESS_STRUCTURE = "Erro no acesso á estrutura de dados."

#TITULOS DAS JANELAS
TITLE_EDIT_ITEMS = "Qooxdoo GUI Builder - Edit Items"
TITLE_EDIT_TABS = "Qooxdoo GUI Builder - Edit Tabs"
TITLE_EDIT_TABLE = "Qooxdoo GUI Builder - Edit Table"

#DRAW AREA VIEWPORT MARGINS
MARGIN = 15

#LIMITES MINIMOS DE REDIMENSIONAMENTO
MIN_RESIZABLE_WIDTH = 15
MIN_RESIZABLE_HEIGHT = 15

#DEFINIÇÃO DE CORES
DRAW_AREA_COLOR = QtGui.QPalette.Button
BACKGROUNDS_COLOR = QtGui.QPalette.Dark

#DEFINIÇÃO DAS ACÇÃO DE DRAG
DRAG_COPY_ACTION = "DCopy"
DRAG_MOVE_ACTION = "DMove"

#DEFINIÇÃO DE UM MIME DATA PARA O DRAG E DROP
APLICATION_RESIZABLE_TYPE = "application/x-dnditemdata"

#DEFINIÇÃO DAS FUNÇÕES DA CLASSE RESIZABLE_WIDGET SOBRE O PROCESSO DE SELECÇÃO (marcar um controlo como seleccionado)
METHOD_DISABLE_SELECTION = "disableSelected()"
METHOD_ENABLE_SELECTION = "enableSelected()"

#DEFINIÇÃO DO TAMANHO DO PASSO DE MOVIMENTAÇÃO DOS CONTROLOS (pelo teclado)
STEP_MOVE = 5

#DEFINIÇÃO DO Nº DE PIXELS MINIMO À EXECUÇÃO DO DRAG E DROP
PIXELS_TO_DRAG = 5
