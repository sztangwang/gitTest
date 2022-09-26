def GetRecognizedText():
   p = Sys.WaitProcess("notepad", 4000)
   if p.Exists:
     # Get the Notepad window
     wndNotepad = p.WaitWindow("Notepad", "*", 1, 4000)
     if wndNotepad.Exists:
       wndNotepad.MainMenu.Click("帮助(H)|关于记事本(A)")
       # Get the About Notepad window
       wndAbout = p.WaitWindow("#32770", "About Notepad", 1, 4000)
       if wndAbout.Exists:
         # Recognize the text that the About Notepad window contains
         recognizedText = OCR.Recognize(wndAbout)

         # Post the recognized text to the test log
         Log.Message("View all the recognized text in the Details panel", recognizedText.FullText)

         # Post portions of the recognized text to the test log
         if recognizedText.BlockCount > 0:
           Log.AppendFolder("Recognized text by blocks")
           for i in range(0, recognizedText.BlockCount):
             Log.Message(recognizedText.Block[i].Text)
           Log.PopLogFolder()

   else:
     Log.Warning("Notepad is not running.")