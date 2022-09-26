def test():
   p = Sys.WaitProcess("MOZA Pit House", 4000)
   if p.Exists:
     Log.Message('######################')
     wndNotepad = p.WaitWindow("MOZA Pit House", "*", 1, 4000)
     
     wndNotepad.Click("基座配置区域")
      
   