import iCreatorData
import handgesture
import sys
from datetime import datetime
from time import time 
import mmap
import ctypes
from random import randint
import logging
import os
import random


MAX_INFO_ENTITIES= 8
CURRENT_VERSION_NO=2
BODYNUMBER=6



dirName = os.path.dirname( os.path.abspath(__file__) )
userfile = os.path.join(dirName, "user.py")
userUtilsfile = os.path.join(dirName, "userUtils.py")
usercode = open(userfile,"r").read().split('##**##')
usercode0 = usercode[0]
usercode0len = len(usercode[0])
usercode1 = usercode[1]
usercode1len = len(usercode[1])
usercode2 = usercode[2]
usercode2len = len(usercode[2])
usercode3 = usercode[3]
usercode3len = len(usercode[3])
del usercode                # delete variable



looprun = True
while(looprun):
    if len(usercode0) == usercode0len:
        print('usercode0 starts to run \n')
        exec(usercode0)
        looprun = False
    else:
        print('usercode0 is broken, reload. \n')
        usercode0 = open(userfile,"r").read().split('##**##')[0]


# initialize the log settings
filename='C:\\temp\\pythonLog\\logError.log'

try:

    # region ############ Must declare related variable.
    FGInfoIni=iCreatorData.strFGInfoInputAry()
    FGCIni=iCreatorData.strFGCInputAry()
    BGInfoIni=iCreatorData.strBGInfoInputAry()
    BGCIni=iCreatorData.strBGCInputAry()
    CUSInfoIni=iCreatorData.strCUSInfoInputAry()
    CUSCIni=iCreatorData.strCUSCInputAry()
    OBJInfoIni=iCreatorData.strOBJInfoInputAry()
    OBJCIni=iCreatorData.strOBJCInputAry()
    InfoInputNo=iCreatorData.strInfoInputNo()
    InfoInputNo.VersionNo=CURRENT_VERSION_NO
    InfoInputNo2=iCreatorData.strInfoInputNo2()
    GoodyIni=iCreatorData.strGoodyAry()
    infoOut=iCreatorData.readInfoOut()
    BodyPosIni=iCreatorData.strBodyPosAry()
    ScriptIni=iCreatorData.strScriptConditionAry()
    HandIni=iCreatorData.strHandAry()
    HandIniLast=iCreatorData.strHandAry()
    HandTrans=iCreatorData.strHandAry()
    LogDirIni=str("")
    endSignal=0
    firstTimeIni=0
    firstTime = 0
    previousStage=0
    time_interval=0.015
    init_time = time()
    # endregion ########### end of Must declare related variable.

    
    # region ------------------------- initialize user related values
    
    j = 0
    stageNoforChange = 26
    looprun = True
    while(looprun):
        if len(usercode1) == usercode1len:
            print('usercode1 starts to run \n')
            exec(usercode1)
            looprun = False
        else:
            print('usercode1 is broken, reload. \n')
            usercode1 = open(userfile,"r").read().split('##**##')[1]

    
    # endregion ------------------------- end of initialize user related values

    # region ################# Must setup initial communication.
    initialList=iCreatorData.SetupInitial()
    print('SetupInitial complete')
    # endregion ################# end of Must setup initial communication.


    while (endSignal==0):
        # run every time_interval
        if init_time + time_interval <= time():
            init_time = time()
            j += 1

            # region ########## Must get initial vaules from main program.
            infoOut,PersonExist, FGInfoIni, FGCIni,BGInfoIni,BGCIni,CUSInfoIni,CUSCIni,OBJInfoIni,OBJCIni,GoodyIni,BodyPosIni,LogDirIni,ScriptIni,firstTimeIni,previousStage=iCreatorData.ReadStageInitial(stageNoforChange,FGInfoIni,FGCIni,BGInfoIni,BGCIni,CUSInfoIni,CUSCIni,OBJInfoIni,OBJCIni,GoodyIni,BodyPosIni,LogDirIni,ScriptIni,firstTimeIni,previousStage)

            endSignal=infoOut.endSignal
            currentStage=infoOut.stageNo
            print('currentStage='+str(currentStage))
            print('firstTimeIni='+str(firstTimeIni))

            # endregion ########## End of Must get initial vaules from main program.

            

            if (firstTimeIni==1):

                # region ########### Must clear all the numbers to zero.
                iCreatorData.clearInfoInputNo(InfoInputNo)
                if InfoInputNo.VersionNo==CURRENT_VERSION_NO:
                    iCreatorData.clearInfoInputNo2(InfoInputNo2)

                # endregion ########### End of Must clear all the numbers to zero.

                #region -----------------this is the start of user input to get the needed initial value

                looprun = True
                while(looprun):
                    if len(usercode2) == usercode2len:
                        print('usercode2 starts to run \n')
                        exec(usercode2)
                        looprun = False
                    else:
                        print('usercode2 is broken, reload. \n')
                        usercode2 = open(userfile,"r").read().split('##**##')[1]

                print("********************** run second part *************************")

                # endregion -----------------end of user input to get the needed initial value
                

            # firstTimeIni will increase accordingly in the related stage.
            if (firstTimeIni>=1):

                # region-----------------this is the start of user input to change things during the desired stage
                looprun = True
                while(looprun):
                    if len(usercode3) == usercode3len:
                        print('usercode3 starts to run \n')
                        exec(usercode3)
                        looprun = False
                    else:
                        print('usercode3 is broken, reload. \n')
                        usercode3 = open(userfile,"r").read().split('##**##')[3]

                print("********************** run third part *************************")

                # endregion-----------------End of user input to change things during the desired stage


                # region ############### must output the changes to the main program
                if InfoInputNo.VersionNo==CURRENT_VERSION_NO: #additional due to version change
                    iCreatorData.OutputStageChanges2(GoodyIni,BodyPosIni,ScriptIni,InfoInputNo2)
                iCreatorData.OutputStageChanges(FGInfoIni,FGCIni,BGInfoIni,BGCIni,CUSInfoIni,CUSCIni,OBJInfoIni,OBJCIni,InfoInputNo)
                # endregion ############### must output the changes to the main program

# region create error log for user to debug
except Exception as e:
    print('this is error message:'+str(e))
    dirName=LogDirIni
    isdir = os.path.isdir(dirName)
    if (not isdir):
        os.mkdir(dirName)
    filename= dirName+"\\logError.log"
    print('filename is:'+filename)
    logging.basicConfig(filename = filename, level = logging.INFO)
    logging.exception(str(e))
# endregion
           
                
   



