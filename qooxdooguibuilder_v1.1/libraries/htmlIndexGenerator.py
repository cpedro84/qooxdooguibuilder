# !/usr/bin/env python
# -*- encoding: latin1 -*-



def generateHTMLIndex():

    code = '<html>\n\t<head>\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n\t\t<title>Application</title>\n\t\t<script type="text/javascript" src="script/qx.js"></script>\n\t\t<script type="text/javascript" src="Application.js"></script>\n\t</head>\n\t<body>\n\t\t<script type="text/javascript">\n\t\t\tqx.core.Init.getInstance().setApplication(Application);\n\t\t</script>\n\t</body>\n</html>'

    return code
