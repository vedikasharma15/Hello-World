import  ConfigParser
import webbrowser

configParser = ConfigParser.RawConfigParser()
configParser.read("/home/suryaveer/check.conf")
num = configParser.get('userinput-config', 'num')
num2 = int(num)
hello = """"hello world """
hello2 = hello*num2
message = """<html><head>
</head><body><p>"""+hello2+"""</p></body>
</html>"""
f = open('x.html', 'w')
f.write(message*num2)
f.close()
webbrowser.open("file:///home/suryaveer/x.html")
