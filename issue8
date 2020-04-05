import ConfigParser
import webbrowser
configParser = ConfigParser.RawConfigParser()
configParser.read("/home/suryaveer/check.conf")
num = configParser.get('userinput-config', 'num')
num2 = int(num)
message = "hello world"
with open('test.txt', 'wb') as f:  
  max_size = num2 * 1024  
  msg_bytes = message.encode('utf-8')
  bytes_written = 0
  while bytes_written < max_size:  
    f.write(msg_bytes) 
    bytes_written += len(msg_bytes)
