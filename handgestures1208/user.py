

from handgesture import gestureOfHand


USER = 0
VITURE = 1
P1 = 0
P2 = 1
LeftHand  = 0
RightHand = 1


def gestureListUpdate(index, gesture):
    if (index > (gestureListLen-1)):
        index = 0
    gestures[index] = gesture
    index = index + 1
    return index

def gestureRecognize():
    print(gestures)
    contentStr = "recognizing: \t"+str(gestures)
    loginfoPrint(printFilename,1,contentStr)
    if (min(gestures) < 0):
        print('data not enough')
        contentStr = 'data not enough'
        loginfoPrint(printFilename,1,contentStr)
        return False, -1
    labelnums = []
    for label in range(gestureNUm):
        labelnums.append(gestures.count(label))
    
    Labelnummax = max(labelnums)
    contentStr = 'max quantity is :\t'+str(Labelnummax)
    loginfoPrint(printFilename,1,contentStr)
    print('max quantity is :\t', Labelnummax)
    if (Labelnummax > int(len(gestures) * 0.8)):
        return True, labelnums.index(Labelnummax)
    else:
        return False, -1
    
def resetStage27():
    Label = -1
    gestureListIndex = 0
    gestures = [-1]*30           # store the result of recognizing function
    recognized = False
    return Label, gestureListIndex, gestures, recognized
        
def gameJudge(hand1, hand2):    # first arg is label of first hand, return 0 as winner
    ''' 
    USER = 0
    VITURE = 1
    NOWINNER = -1
    0 for open hand gesture 
    1 for close hand gesture 
    2 for scissor gesture 
    '''
    if (((hand1==0) and (hand2 == 1))or((hand1==1) and (hand2 == 2))or((hand1==2) and (hand2 == 0))):
        winner = 0
    elif(((hand2==0) and (hand1 == 1))or((hand2==1) and (hand1 == 2))or((hand2==2) and (hand1 == 0))):
        winner = 1
    else:
        winner = -1
    return winner
def loginfoPrint(printFilename,firstTime,contentStr):
    contentStr=contentStr+"\n"
    if firstTime==0:
        f = open(printFilename, "w")
        f.close()
    elif firstTime>0:
        f = open(printFilename, "a")
        f.write(contentStr)
        f.close()


##**##

# region ------------------------- initialize user related values
# a class make printing information easily just via print function
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
PI=0
objNum=0
j = 0

''' 
0 for open hand gesture 
1 for close hand gesture 
2 for scissor gesture 
3 for Ok pose hand gesture 
4 for spiderman pose hand
5 for gun gesture  
6 for others      
'''


stageNoforChange = [26,22,27,24,41]
Label = -1
Labelget = -1
targetGestures = [0, 1, 2]
gestureNUm = 7
gestureListLen = 10
gestureListIndex = 0
gesturenames = ['open hand', 'close hand', 'scissor gesture', 'Ok pose', 'spiderman pose', 'gun gesture', 'others']
gestures = [-1]*gestureListLen           # store the result of recognizing function
recognized = False
nextStageStatus1 = 0
nextStageStatus2 = 0
nextStageStatus3 = 0
roundNo = 1
RUNSTR = ['don\'t run', 'run']

# endregion ------------------------- end of initialize user related values

##**##



#region -----------------this is the start of user input to get the needed initial value

InfoInputNo2.ScriptConditionNo=4
InfoInputNo2.GoodyNo=2
InfoInputNo.FGNo=6
InfoInputNo.CUSNo=0
InfoInputNo.stageNo=currentStage

gestures = [-1]*10
# Set up the log file for debugging 
dirName=LogDirIni
isdir = os.path.isdir(dirName) 
if (not isdir):
    os.mkdir(dirName)
handfilename= dirName+"\\handLog.csv"
# information stored in files
sys.stdout = Logger(dirName+'\\a.log', sys.stdout)
sys.stderr = Logger(dirName+'\\a.log_file', sys.stderr)
printFilename=dirName+"\\print.txt"
contentStr = "start"
loginfoPrint(printFilename,0,contentStr)
print("**************** user program start *******************")

HandIniLast=HandIni
continueRun=False
while (not continueRun):
    HandIni,continueRun=iCreatorData.readHandAry()

# iCreatorData.HandinfoLog(handfilename,0,HandIni,HandIniLast)
HandIniLast=HandIni

xyRatio, shiftX, shiftY, ScreenWidth, ScreenHeight= iCreatorData.calculateScreenRatio(BodyPosIni, HandIni)
# endregion -----------------end of user input to get the needed initial value
                

##**##

# region-----------------this is the start of user input to change things during the desired stage
# continueRun = False
# while (not continueRun):
#     HandIni, continueRun = iCreatorData.readHandAry()

# print("**************** user program run *******************")
# HandTrans,continueRun=iCreatorData.HandTransform(HandIni, HandIniLast, HandTrans, OBJInfoIni, PI, objNum, ScreenWidth, ScreenHeight, xyRatio, shiftX, shiftY)
# # HandIni = HandTrans


print('***firstTimeIni is:\t', firstTimeIni, 'currentStage is\t', currentStage)



if currentStage == 27:
    str27 = 'stage 27 running'
    print("**************** user program run in 27 *******************")
    if (j % 1 == 0):
        print("update gesture")
        contentStr = "stage 27 update gesture"
        loginfoPrint(printFilename,1,contentStr)
        # recognize which kind of hand gesture it is 


        handgestureTem = gestureOfHand(P1, RightHand)

        print('handgestureTem is :\t', handgestureTem)
        # accNo,x,y = handgesture.Handset(HandTrans)

        # handTem = handgesture.HandGesture(accNo,x,y)

        # handgestureTem = handTem.isWhichHandGesture()

        # if (handgestureTem != 2):
        #     iCreatorData.HandinfoLog(handfilename,1,HandIni,HandIniLast)


        # update gesture list
        gestureListIndex = gestureListUpdate(gestureListIndex, handgestureTem)

        # recognize hand gesture
        recognized, Label = gestureRecognize()
        Label = 1
        recognized = 1


    if (recognized and (Label in targetGestures)):
        print('jump to next')
        Labelget = Label    # this is the hand gesture of person 
        
        # print('firstTimeIni is: \t',firstTimeIni,'\n hand gesture is:\t'+gesturenames[Labelget])
        Label, gestureListIndex, gestures, recognized = resetStage27()
        hand2 = random.randint(0,2)
        hand2 = 0
        print("user hand is :\t",gesturenames[Labelget],"vitual hand is:\t", gesturenames[hand2])

        contentStr = "stage 27: user hand is :\t"+gesturenames[Labelget]+"vitual hand is:\t"+(gesturenames[hand2])
        loginfoPrint(printFilename,1,contentStr)
        winner = gameJudge(Labelget, hand2)
        if (winner == 0):
            scale = [2.5, 1.5]          # PLAYER win
        elif (winner == -1):
            scale = [1.5, 1.5]          # tie
        elif(winner == 1):
            scale = [1.5, 2.5]          # VIRTUAL win

        winnername = ["no one", "player", "virtual"]
        print("winner is :\t", winnername[winner],'scipt is 1, num is 0')
        contentStr = "stage 27 winner is :\t"+winnername[winner+1]+'scipt is 1, num is 0'
        loginfoPrint(printFilename,1,contentStr)
            
        nextStageStatus1 = 1            # script  1
    # else:
    #     nextStageStatus1 = 0
    
    ScriptIni.verified[0] = 1
    ScriptIni.ScriptCondition[0] = nextStageStatus1




if currentStage == 24:   
    str24 = 'stage 24 running '
    print("**************** user program run in 24 *******************")
    if (Labelget == 0):
        ihand = 0
    elif (Labelget == 1):
        ihand = 2
    elif (Labelget == 2):
        ihand = 4

    FGInfoIni.FGInfo[ihand].xstart = 240 
    FGInfoIni.FGInfo[ihand].ystart = 0
    FGInfoIni.FGInfo[ihand].xscale = scale[USER] 
    FGInfoIni.FGInfo[ihand].yscale = scale[USER] 
    FGInfoIni.verified[ihand] = 1
    print('set real hand in', gesturenames[Labelget])
    contentStr = 'stage 24: set real hand in'+gesturenames[Labelget]
    loginfoPrint(printFilename,1,contentStr)

    if (hand2 == 0):
        ihand2 = 1
    elif (hand2 == 1):
        ihand2 = 3
    elif (hand2 == 2):
        ihand2 = 5
    FGInfoIni.FGInfo[ihand2].xstart = -240
    FGInfoIni.FGInfo[ihand2].ystart = 0
    FGInfoIni.FGInfo[ihand2].xscale = scale[VITURE]  
    FGInfoIni.FGInfo[ihand2].yscale = scale[VITURE]
    FGInfoIni.verified[ihand2] = 1
    print('set virtual hand in', gesturenames[hand2])
    contentStr = 'set real hand in'+gesturenames[hand2]
    loginfoPrint(printFilename,1,contentStr)

    
    
if currentStage == 41:
    str41 = 'stage 41 running'
    print("**************** user program run in 41 *******************")
    print('stage 41: result showed, then change goodys, winner is: ', winnername[winner])
    contentStr = 'stage 41: result showed, then change goodys, winner is: '+ str(winnername[winner])
    loginfoPrint(printFilename,1,contentStr)
    # who win?
    if (winner == 1):                   # VIRTUAL win
        nextStageStatus2 = 1            # script  2
        print("VIRTUAL win, script 1 ", RUNSTR[nextStageStatus2])  
        contentStr = "VIRTUAL win, script 1 "+ RUNSTR[nextStageStatus2]
        loginfoPrint(printFilename,1,contentStr)
        ScriptIni.verified[0] = 1           # VIRTUAL win script 3, but I hope it is run when player win for script2.
        ScriptIni.ScriptCondition[0] = nextStageStatus2
    # else:
    #     nextStageStatus2 = 0 

    if (winner == 0):                   # PLAYER win
        nextStageStatus3 = 1            # script  3
        print("PLAYER win, script 3, num is 1", RUNSTR[nextStageStatus3])  
        contentStr = "PLAYER win, script 3, num is 1 "+ RUNSTR[nextStageStatus3]
        loginfoPrint(printFilename,1,contentStr)
        ScriptIni.verified[1] = 1
        ScriptIni.ScriptCondition[1] = nextStageStatus3
    # else:
    #     nextStageStatus3 = 0     

# endregion-----------------End of user input to change things during the desired stage

##**##

accNo,x,y = handgesture.Handset(HandTrans)

handTem = handgesture.HandGesture(accNo,x,y)

handgestureTem = handTem.isWhichHandGesture()


##**##

print("**********\nThis is from another file\n************")

