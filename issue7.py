import  ConfigParser
import webbrowser
import random
def test():
    r = lambda: random.randint(0, 255)
    return('#%02X%02X%02X' % (r(),r(),r()))
configParser = ConfigParser.RawConfigParser()
configParser.read("/home/suryaveer/check.conf")
num = configParser.get('userinput-config', 'num')
num2 = int(num)
message = """<p style='color:{};'>hello world</p>"""
print "number read from file : " + str(num2)
f = open('out.html', 'w')
for i in range(0, num2):
	print message
	f.write(message.format(test()))
f.close()
webbrowser.open("file:///home/suryaveer/out.html")
