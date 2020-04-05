import ConfigParser
configParser = ConfigParser.RawConfigParser()
configFilePath = "/home/suryaveer/github_repositories/config/check.conf"
configParser.read(configFilePath)
num = configParser.get('userinput-config', 'num')
for i in range(0, int(num)):
	print("hello world")
	
