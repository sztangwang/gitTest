import os


def blue_test():
  WshShellExecObj = WshShell.Exec("cmd.exe");
  # Flush the stream 
  out = readTillChar(WshShellExecObj, ">")
  Log.Message(out)
  
  path = os.getcwd()
  filename = '\Script\TestBlue.py'
  sendCommand(WshShellExecObj, "python.exe " +path+filename)
  out = readTillChar(WshShellExecObj, ">")
  Log.Message(out)
  with open(r'%s\log.txt'%path,'r')as f:
    Log.Message(f.readline())
  
  
# Read the console output stream
def readTillChar(WshShellExecObj, endChar):
  out = ""
  while not WshShellExecObj.StdOut.AtEndOfStream:
    curChar = WshShellExecObj.StdOut.Read(1)
    out = out + curChar
    if (curChar == endChar):
      return out
      

# Send a command to the console input stream
def sendCommand(WshShellExecObj, command):
  if WshShellExecObj != None:
    WshShellExecObj.StdIn.Write(command + "\n")
    
    
    