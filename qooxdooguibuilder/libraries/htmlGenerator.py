# !/usr/bin/env python
# -*- encoding: latin1 -*-



##def readTags(properties_file_path, lowerIndex, higherIndex):
##
##    index = 0
##    tags = []
##    properties_file = file(properties_file_path, 'r')
##
##    for line in properties_file:
##        if index >= lowerIndex and index <= higherIndex:
##            tmp = line.split(':')
##            tags.append(tmp[1])
##        index += 1
##
##    properties_file.close()
##
##    return tags


def customizeControlJS(control_id, properties):

    js_control = ''

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

        elif property_key == 'TextAlign' and properties['Type'] == 'Label':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Wrap' and properties['Type'] == 'Label':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'EnableInlineFind' and properties['Type'] == 'List':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MarkLeadingItem' and properties['Type'] == 'List':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'List':
            for text in properties[property_key]:
                js_control += control_id
                js_control += '.add(new qx.ui.form.ListItem("'
                js_control += text
                js_control += '"));\n\t\t\t\t'

        elif property_key == 'Menus' and properties['Type'] == 'MenuBar':#por acabar
            js_control += control_id
            js_control += ');\n\t\t\t\t'

        elif property_key == 'HeaderCellHeight' and properties['Type'] == 'Table':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'RowHeight' and properties['Type'] == 'Table':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'Table':#por acabar
            js_control += control_id
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Tabs' and properties['Type'] == 'TabView':#por acabar
            js_control += control_id
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Text' and properties['Type'] == 'TextArea':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Wrap' and properties['Type'] == 'TextArea':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Read Only' and properties['Type'] == 'TextArea':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Text' and properties['Type'] == 'TextField':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'MaxLength' and properties['Type'] == 'TextField':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'ReadOnly' and properties['Type'] == 'TextField':#por acabar
            js_control += control_id
            js_control += properties[property_key]
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Icons' and properties['Type'] == 'ToolBar':#por acabar
            js_control += control_id
            js_control += ');\n\t\t\t\t'

        elif property_key == 'Items' and properties['Type'] == 'Tree':#por acabar
            js_control += control_id
            js_control += ');\n\t\t\t\t'

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

    return js_control


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
                js_controls += ', null, null, "'
                js_controls += data[control_id]['Checked']
                js_controls += '"'

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
            if 'Source' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Source']
                js_controls += '"'

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
            js_controls += ' = new qx.ui.menubar.MenuBar('

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
                js_controls += ', null, null, "'
                js_controls += data[control_id]['Checked']
                js_controls += '"'

        elif data[control_id]['Type'] == 'Spinner':
            js_controls += ' = new qx.ui.form.Spinner('
            if 'Min' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Min']
                js_controls += '"'
            if 'Value' in data[control_id]:
                js_controls += ', "'
                js_controls += data[control_id]['Value']
                js_controls += '"'
            if 'Max' in data[control_id]:
                js_controls += ', "'
                js_controls += data[control_id]['Max']
                js_controls += '"'

        elif data[control_id]['Type'] == 'Table':
            js_controls += ' = new qx.ui.table.Table(new qx.ui.table.SimpleTableModel()'

        elif data[control_id]['Type'] == 'TabView':
            js_controls += ' = new qx.ui.pageview.tabview.TabView('

        elif data[control_id]['Type'] == 'TextArea':
            js_controls += ' = new qx.ui.form.TextArea('

        elif data[control_id]['Type'] == 'TextField':
            js_controls += ' = new qx.ui.form.TextField('

        elif data[control_id]['Type'] == 'ToolBar':
            js_controls += ' = new qx.ui.toolbar.ToolBar('

        elif data[control_id]['Type'] == 'Tree':
            js_controls += ' = new qx.ui.tree.Tree('
            if 'Label' in data[control_id]:
                js_controls += '"'
                js_controls += data[control_id]['Label']
                js_controls += '"'
                

        js_controls += ');\n\t\t\t\t'

        
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
