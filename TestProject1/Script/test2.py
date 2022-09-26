import time


# @test
def Test2():
    #Runs the "MOZA_Pit_House" tested application. 
    
    TestedApps.MOZA_Pit_House.Run(1, True)
    Log.Picture(Sys.Desktop.Picture())
    time.sleep(3)
    OCR.Recognize(Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2).BlockByText("*方向盘*")
    text = OCR.Recognize(Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2).FullText
    Log.Message(text)
    
    #Aliases.MOZA_Pit_House.Picture()
    Log.Message(aqString.Find('对中'))
    Log.Message('#############'+TestedApps.MOZA_Pit_House.FileName)
    Log.Message('#############'+TestedApps.MOZA_Pit_House.Path)
    Log.Message('#############'+TestedApps.MOZA_Pit_House.FullFileName)
    Log.Message('#############%s'%TestedApps.MOZA_Pit_House.Terminate())
    Log.Message('#############%s'%TestedApps.MOZA_Pit_House.Count)
    Log.Picture(Sys.Desktop.ActiveWindow(), "Message Text", "Extended Message Text", pmHighest)
    
    
    # 写文件
    sPath = "E:\\log.txt"
    aqFile.Create(sPath)
    myFile = aqFile.OpenTextFile(sPath,aqFile.faReadWrite,aqFile.ctUnicode)
    myFile.WriteLine("line1")
    myFile.Close()
    
    
    #写文件
    with open (sPath,"a+") as f:
      f.write('########################')
    
    
    
   
    
    #Clicks the 'wndQt5152QWindowOwnDCIcon' object.
    #Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon.Click(460, 511)
    #Clicks the 'wndQt5152QWindowOwnDCIcon' object.
    #Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon.Click(540, 346)
    #OCR.Recognize(Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon).BlockByText("MOZA").Click()
