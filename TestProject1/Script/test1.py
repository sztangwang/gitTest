﻿

def Test1():
    # Call method asynchronously
    CallResultObj = Runner.CallObjectMethodAsync(Obj, "MethodName", "Param1", "Param2")
 
    # Perform the desired user actions
    # ...
 
    # Wait until the asynchronous call is over
    while not CallResultObj.Completed:
      aqUtils.Delay(100)
 
    # Check the results
    MethodResult = CallResultObj.ReturnValue
    

def Test5():
    OCR.Recognize(Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2).BlockByText("方向盘", spNearestToCenter).Click()
    #Clicks the 'wndQt5152QWindowOwnDCIcon2' object.
    Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2.Click(384, 297)
    #Clicks the 'wndQt5152QWindowOwnDCIcon2' object.
    Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2.Click(580, 660)
    #Clicks the 'wndQt5152QWindowOwnDCIcon2' object.
    Aliases.MOZA_Pit_House.wndQt5152QWindowOwnDCIcon2.Click(194, 692)
