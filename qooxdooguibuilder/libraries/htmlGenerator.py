# !/usr/bin/env python
# -*- encoding: latin1 -*-



def customizeControlJS(control_id, properties):

    js_control = ''
    js_control_tmp = ''

    for property_key in properties.iterkeys():
        if property_key == 'Editable' and properties['Type'] == 'ComboBox':
            js_control += control_id
            js_control += '.setEditable('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'
                
        elif property_key == 'PagingInterval' and properties['Type'] == 'ComboBox':
            js_control += control_id
            js_control += '.setPagingInterval('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Selected' and properties['Type'] == 'ComboBox':
            js_control += control_id
            js_control += '.setSelected('
            js_control += control_id
            js_control += '.getList().findStringExact("'
            js_control += properties[property_key]
            js_control += '"));\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'ComboBox':
            for text in properties[property_key]:
                js_control += control_id
                js_control += '.add(new qx.ui.form.ListItem("'
                js_control += text
                js_control += '"));\n\t\t\t\t'

        elif property_key == 'Source URL' and properties['Type'] == 'Iframe':
            js_control += control_id
            js_control += '.setSource("http://'
            js_control += properties[property_key]
            js_control += '");\n\t\t\t\t'

        elif property_key == 'TextAlign' and properties['Type'] == 'Label':
            js_control += control_id
            js_control += '.setTextAlign("'
            js_control += properties[property_key]
            js_control += '");\n\t\t\t\t'

        elif property_key == 'Wrap' and properties['Type'] == 'Label':
            js_control += control_id
            js_control += '.setWrap('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'EnableInlineFind' and properties['Type'] == 'List':
            js_control += control_id
            js_control += '.setEnableInlineFind('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarkLeadingItem' and properties['Type'] == 'List':
            js_control += control_id
            js_control += '.setMarkLeadingItem('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'List':
            for text in properties[property_key]:
                js_control += control_id
                js_control += '.add(new qx.ui.form.ListItem("'
                js_control += text
                js_control += '"));\n\t\t\t\t'

        elif property_key == 'Menus' and properties['Type'] == 'MenuBar':
            for text in properties[property_key]:
                js_control += 'var '
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += ' = new qx.ui.toolbar.MenuButton("'
                js_control += text
                js_control += '");\n\t\t\t\t'
            js_control += control_id
            js_control += '.add('
            first = True
            for text in properties[property_key]:
                if not first:
                    js_control += ', '
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                first = False
            js_control += ');\n\t\t\t\t'

        elif property_key == 'HeaderCellHeight' and properties['Type'] == 'Table':
            js_control += control_id
            js_control += '.setHeaderCellHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'RowHeight' and properties['Type'] == 'Table':
            js_control += control_id
            js_control += '.setRowHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'Table':
            js_control_tmp += 'var tableModel = new qx.ui.table.SimpleTableModel();\n\t\t\t\t'
            js_control_tmp += 'var rowData = []\n\t\t\t\t'
            lastRow = 0
            lastColumn = 0
            for x, y in properties[property_key].iterkeys():
                if int(x) - 1 > lastRow:
                    lastRow = int(x) - 1
                if int(y) - 1 > lastColumn:
                    lastColumn = int(y) - 1
            js_control_tmp += 'for(var row = 0; row < '
            js_control_tmp += str(lastRow + 1)
            js_control_tmp += '; row++)\n\t\t\t\t'
            js_control_tmp += '{\n\t\t\t\t\t'
            js_control_tmp += 'rowData.push(["'
            first = True
            for x in range(0, lastColumn + 1):
                if not first:
                    js_control_tmp += '", "'
                first = False
            js_control_tmp += '"]);\n\t\t\t\t}\n\t\t\t\t'
            column_titles = []
            for x, y in properties[property_key].iterkeys():
                if x == 0:
                    column_titles.append(properties[property_key][x, y])
                elif y != 0:
                    js_control_tmp += 'rowData['
                    js_control_tmp += str(int(x) - 1)
                    js_control_tmp += ']['
                    js_control_tmp += str(int(y) - 1)
                    js_control_tmp += '] = "'
                    js_control_tmp += properties[property_key][x, y]
                    js_control_tmp += '"\n\t\t\t\t'
            js_control_tmp += 'tableModel.setData(rowData);\n\t\t\t\t'
            js_control_tmp += 'tableModel.setColumns(["'
            first = True
            for text in column_titles:
                if not first:
                    js_control_tmp += '", "'
                js_control_tmp += text
                first = False
            js_control_tmp += '"]);\n\t\t\t\t'
            js_control_tmp += 'var '
            js_control_tmp += control_id
            js_control_tmp += ' = new qx.ui.table.Table(tableModel);\n\t\t\t\t'
            js_control_tmp += control_id
            js_control_tmp += '.setBorder(qx.renderer.border.BorderPresets.getInstance().thinInset);\n\t\t\t\t'

        elif property_key == 'Tabs' and properties['Type'] == 'TabView':
            for text in properties[property_key]:
                js_control += 'var '
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += '_button'
                js_control += ' = new qx.ui.pageview.tabview.Button("'
                js_control += text
                js_control += '");\n\t\t\t\t'
                js_control += control_id
                js_control += '.getBar().add('
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += '_button'
                js_control += ');\n\t\t\t\t'
                js_control += 'var '
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += '_page'
                js_control += ' = new qx.ui.pageview.tabview.Page('
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += '_button'
                js_control += ');\n\t\t\t\t'
                js_control += control_id
                js_control += '.getPane().add('
                js_control += control_id
                js_control += '_'
                js_control += text.replace(' ', '_')
                js_control += '_page'
                js_control += ');\n\t\t\t\t'

        elif property_key == 'Wrap' and properties['Type'] == 'TextArea':
            js_control += control_id
            js_control += '.setWrap('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MaxLength' and properties['Type'] == 'TextField':
            js_control += control_id
            js_control += '.setMaxLength('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ReadOnly' and properties['Type'] == 'TextField':
            js_control += control_id
            js_control += '.setReadOnly('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ToolItems' and properties['Type'] == 'ToolBar':
            for data in properties[property_key]:                
		js_control += 'var '
                js_control += control_id
                js_control += '_'
                js_control += data[1].replace(' ', '_')
                js_control += ' = new qx.ui.toolbar.Button("'
                js_control += data[1]
                js_control += '", "'
                js_control += data[0]
                js_control += '");\n\t\t\t\t'
            js_control += control_id
            js_control += '.add('
            first = True
            for data in properties[property_key]:
                if not first:
                    js_control += ', '
                js_control += control_id
                js_control += '_'
                js_control += data[1].replace(' ', '_')
                first = False
            js_control += ');\n\t\t\t\t'

        #elif property_key == 'Items' and properties['Type'] == 'Tree':

        elif property_key == 'Top':
            js_control += control_id
            js_control += '.setTop('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Left':
            js_control += control_id
            js_control += '.setLeft('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Right':
            js_control += control_id
            js_control += '.setRight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Bottom':
            js_control += control_id
            js_control += '.setBottom('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Width':
            js_control += control_id
            js_control += '.setWidth('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MaxWidth':
            js_control += control_id
            js_control += '.setMaxWidth('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MinWidth':
            js_control += control_id
            js_control += '.setMinWidth('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Height':
            js_control += control_id
            js_control += '.setHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MaxHeigth':
            js_control += control_id
            js_control += '.setMaxHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MinHeight':
            js_control += control_id
            js_control += '.setMinHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ClipWidth':
            js_control += control_id
            js_control += '.setClipWidth('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ClipHeight':
            js_control += control_id
            js_control += '.setClipHeight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ClipLeft':
            js_control += control_id
            js_control += '.setClipLeft('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ClipTop':
            js_control += control_id
            js_control += '.setClipTop('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarginBottom':
            js_control += control_id
            js_control += '.setMarginBottom('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarginLeft':
            js_control += control_id
            js_control += '.setMarginLeft('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarginRight':
            js_control += control_id
            js_control += '.setMarginRight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarginTop':
            js_control += control_id
            js_control += '.setMarginTop('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'PaddingBottom':
            js_control += control_id
            js_control += '.setPaddingBottom('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'PaddingLeft':
            js_control += control_id
            js_control += '.setPaddingLeft('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'PaddingRight':
            js_control += control_id
            js_control += '.setPaddingRight('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'PaddingTop':
            js_control += control_id
            js_control += '.setPaddingTop('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Border':
            js_control += control_id
            js_control += '.setBorder('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Visibility':
            js_control += control_id
            js_control += '.setVisibility('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Selectable':
            js_control += control_id
            js_control += '.setSelectable('
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

    return js_control_tmp + js_control


def generateControlsJS(data):

    js_controls = ''

    for control_id in data.iterkeys():
        js_controls += '\n\t\t\t\t'
        js_controls += 'var '
        js_controls += control_id

        if data[control_id]['Type'] == 'Button':
            js_controls += ' = new qx.ui.form.Button('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'
            if 'Icon' in data[control_id]:
                js_controls += ', "'
                js_controls += data[control_id]['Icon']
                js_controls += '"'

        elif data[control_id]['Type'] == 'CheckBox':
            js_controls += ' = new qx.ui.form.CheckBox('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'
            if 'Checked' in data[control_id]:
                js_controls += ', null, null, '
                js_controls += data[control_id]['Checked']

        elif data[control_id]['Type'] == 'ComboBox':
            js_controls += ' = new qx.ui.form.ComboBox('

        elif data[control_id]['Type'] == 'GroupBox':
            js_controls += ' = new qx.ui.groupbox.GroupBox('
            if 'Legend' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Legend']
                js_controls += '"'
            if 'Icon' in data[control_id]:
                js_controls += ', "'
                js_controls += data[control_id]['Icon']
                js_controls += '"'

        elif data[control_id]['Type'] == 'Iframe':
            js_controls += ' = new qx.ui.embed.Iframe('

        elif data[control_id]['Type'] == 'Label':
            js_controls += ' = new qx.ui.basic.Label('
            if 'HTML' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['HTML']
                js_controls += '"'
            if 'Mnemonic' in data[control_id]:
                js_controls += ', "'
                js_controls += data[control_id]['Mnemonic']
                js_controls += '"'

        elif data[control_id]['Type'] == 'List':
            js_controls += ' = new qx.ui.form.List('

        elif data[control_id]['Type'] == 'MenuBar':
            js_controls += ' = new qx.ui.toolbar.ToolBar('

        elif data[control_id]['Type'] == 'PasswordField':
            js_controls += ' = new qx.ui.form.PasswordField('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'

        elif data[control_id]['Type'] == 'RadioButton':
            js_controls += ' = new qx.ui.form.RadioButton('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'
            if 'Checked' in data[control_id]:
                js_controls += ', null, null, '
                js_controls += data[control_id]['Checked']

        elif data[control_id]['Type'] == 'Spinner':
            js_controls += ' = new qx.ui.form.Spinner('
            if 'Min' in data[control_id]:
                js_controls += data[control_id]['Min']
            if 'Value' in data[control_id]:
                js_controls += ', '
                js_controls += data[control_id]['Value']
            if 'Max' in data[control_id]:
                js_controls += ', '
                js_controls += data[control_id]['Max']

        elif data[control_id]['Type'] == 'Table':
            js_controls = ''

        elif data[control_id]['Type'] == 'TabView':
            js_controls += ' = new qx.ui.pageview.tabview.TabView('

        elif data[control_id]['Type'] == 'TextArea':
            js_controls += ' = new qx.ui.form.TextArea('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'

        elif data[control_id]['Type'] == 'TextField':
            js_controls += ' = new qx.ui.form.TextField('
            if 'Text' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Text']
                js_controls += '"'

        elif data[control_id]['Type'] == 'ToolBar':
            js_controls += ' = new qx.ui.toolbar.ToolBar('

        elif data[control_id]['Type'] == 'Tree':
            js_controls += ' = new qx.ui.tree.Tree('
            if 'Label' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Label']
                js_controls += '"'

        if data[control_id]['Type'] != 'Table':
            js_controls += ');'
        js_controls += '\n\t\t\t\t'

        js_controls += customizeControlJS(control_id, data[control_id])
        js_controls += control_id
        js_controls += '.addToDocument();'

    return js_controls


def generateJS(title, data):

    js = 'qx.OO.defineClass("'
    js += title
    js += '", qx.component.AbstractApplication, function(){qx.component.AbstractApplication.call(this);});\n\t\t\tqx.Proto.main = function(e)\n\t\t\t{'
    js += generateControlsJS(data)
    js += '\n\t\t\t};'

    return js


def generateHTML(title, data):
    
    html = '<html>\n\t<head>\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n\t\t<title>'
    html += title
    html += '</title>\n\t\t<script type="text/javascript" src="script/qx.js"></script>\n\t\t<script type="text/javascript">\n\t\t\t'
    html += generateJS(title, data)
    html += '\n\t\t</script>\n\t</head>\n\t<body>\n\t\t<script type="text/javascript">\n\t\t\tqx.core.Init.getInstance().setApplication('
    html += title
    html += ');\n\t\t</script>\n\t</body>\n</html>'

    return html
