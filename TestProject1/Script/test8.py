﻿def Main():
  WshShellExecObj = WshShell.Exec("cmd.exe");

  # Flush the stream 
  out = readTillChar(WshShellExecObj, ">")
  Log.Message(out)
  
  # Send the "ver" command and the new line character
  sendCommand(WshShellExecObj, "ver")
  out = readTillChar(WshShellExecObj, ">")
  Log.Message("See the ver command output in the Details panel of the test log", out)
  
  # Send the "ping" command and the new line character
  server_name = "www.smartbear.com"
  sendCommand(WshShellExecObj, "ping " + server_name)
  out = readTillChar(WshShellExecObj, ">")
  Log.Message("See the ping command output in the Details panel of the test log", out)
  
  # Send the "ipconfig" command and the new line character
  sendCommand(WshShellExecObj, "ipconfig")
  out = readTillChar(WshShellExecObj, ">")
  Log.Message("See the ipconfig output in the Details panel of the test log", out)
  

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