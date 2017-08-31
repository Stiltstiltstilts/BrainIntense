#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#another random edit to test GitHub

# Function Imports
from __future__ import division
from psychopy import core, visual, sound, logging, gui, event, parallel
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
GlobalClock = core.Clock() # Track time since experiment starts

#port = parallel.ParallelPort(address=0xd050)
#port.setData(0)

#port.setData(respCode)
#core.wait(0.02)
#port.setData(0)

# Ensures that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


# Store info about the experiment session (from prompt box)
expName = 'New_Metrical_test'  
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
#expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)


# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file



# ====================== #
# ===== VARIABLES ====== #
# ====================== #
#Auditory Stimuli
beat_stim = sound.Sound(u'Stimuli/beat_stim.wav', secs=-1)
beat_stim.setVolume(1) #Beat stimulus
beat_cont1 = sound.Sound(u'Stimuli/beat_interr_slow.wav', secs=-1) #Control interruption stim1
beat_cont1.setVolume(1)
beat_cont2 = sound.Sound(u'Stimuli/beat_interr_fast.wav', secs =-1) #Control interruption stim2
beat_cont2.setVolume(1)

win = visual.Window(fullscr=False,
                monitor='Laptop',
                units='deg',
                allowGUI=False)
                

#Metrical conditions
colour_binary = visual.ImageStim(
    win=win, image=u'Stimuli/Col_2.png', mask=None,
    ori=0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)
colour_ternary = visual.ImageStim(
    win=win, image=u'Stimuli/Col_3.png', mask=None,
    ori=0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)
gesture_binary = visual.ImageStim(
    win=win, image=u'Stimuli/Gest_2.png', mask=None,
    ori=0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)
gesture_ternary = visual.ImageStim(
    win=win, image=u'Stimuli/Gest_3.png', mask=None,
    ori=0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=0.0)

#Instruction durations
condition_duration = 3 #duration for condition instructions prior to each trial
eye_duration = 2 #duration for prompt to close eyes

#Control list construction

norm_list = [{'condition':'control',
                    'stim':beat_stim,
                    'ref':1}] 
interr_list1 = [{'condition':'interr',
                    'stim':beat_cont1,
                    'ref':2}] 
interr_list2 = [{'condition':'interr',
                    'stim':beat_cont2,
                    'ref':3}]

control_list = (norm_list * 6) + interr_list1 + interr_list2 # 10 standard trials and two interruption trials CHANGE BACK TO 10
shuffle(control_list) #randomised
control_list = (norm_list * 2) + control_list

#Colour list construction

col2_list = [{'condition':'col_2',
                'stim':beat_stim,
                'cond':colour_binary,
                'ref':4}]
col3_list = [{'condition':'col_3',
                'stim':beat_stim,
                'cond':colour_ternary,
                'ref':5}]

colour_list = (col2_list + col3_list) * 10

#Gestural list construction

gest2_list = [{'condition':'gest_2',
                'stim':beat_stim,
                'cond':gesture_binary,
                'ref':6}]
gest3_list = [{'condition':'gest_3',
                'stim':beat_stim,
                'cond':gesture_ternary,
                'ref':7}]

gesture_list = (gest2_list + gest3_list) * 10

# Control condition messages
topControl = ["Part 1",
    "Welcome to the experiment and thank you for participating.",
    "This experiment will be in three sections/blocks, each of these contain a number of 'trials'.",
    "In this first section, the trials will require you to listen attentively to an auditory beat that lasts for 33 seconds.",
    "Listen carefully to the durations of the beats.",
    "Some of the trials will contain interruptions, your task is to identify these.",
    "An interruption will consist of just one beat being subtly faster or slower than the others.",
    "Let the experimenter know if it is unclear what this means",
    "At the end of each trial you will be questioned on whether the trial you just heard contained an interruption.",
    "Indicate you response by clicking on either 'yes' or 'no' with the mouse.",
    "Once you respond, it will automatically proceed to the next trial. Don't confirm your answer until you are ready for the next trial.",
    "During each trial, a black cross will appear at the centre of the screen. Keep your eyes fixated on this.",
    "This is to ensure that your eyes do not move during recording as this can affect the data.",
    "Also, while this cross is on the screen, try and keep your body as still and relaxed as possible.",
    "So don't tap your foot or even move your face or tongue in time with the beat",
    "If any of these instructions aren't clear, let the experimenter know now."]
    
bottomControl = ["Press space to continue.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "WHEN YOU'RE READY TO BEGIN, press space."]

#Colour condition messages
topColour = ["Part 2",
    "This time, you will hear the same beat but there will be no interruptions.",
    "Your task is to use visual mental imagery to help you feel the beat in either 2 or 3 beat patterns",
    "Specifically, you are to imagine the colours RED then BLUE in either groups of 2 or 3, changing colours in time with the beeps.",
    "For a group of two RED BLUE RED BLUE RED BLUE etc.",
    "And for a group of three RED BLUE BLUE RED BLUE BLUE etc.",
    "You will be told which of these patterns to imagine before the sound starts.",
    "Start this imagery from the first beep and maintain it all the way through as vividly as you can.",
    "You will also be asked to close your eyes during the sound. Open them again once the sound stops.",
    "Let the experimenter know if you have questions before continuing."]
bottomColour = ["Press space to continue.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "WHEN YOU'RE READY TO BEGIN, press space."]

#Gesture condition messages
topGesture = ["Part 3",
    "This time your task is to imagine UP and DOWN gestures in time with the beeps",
    "Like before, these will come in either groups of 2 or 3 and you will be told which before each test.",
    "The experimenter will come in and demonstrate what this means.",
    "Like before, you will also be asked to close your eyes during the sound. And opening them again once the sound stops.",
    "Let the experimenter know if you have questions before continuing."]
bottomGesture = ["Press space to continue.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "Press space to continue or backspace to go back.",
    "WHEN YOU'RE READY TO BEGIN, press space."]

# ====================== #
# ===== START EXP ====== #
# ====================== #

try: 
    #Set up variables
    message1 = visual.TextStim(win, pos=[0,+3], color='#000000', alignHoriz='center', name='topMsg', text="placeholder") 
    message2 = visual.TextStim(win, pos=[0,-3], color='#000000', alignHoriz='center', name='bottomMsg', text="placeholder") 
    ratingCont = visual.RatingScale(win=win, name='ratingCont', marker=u'triangle', size=1.0, pos=[0.0, -0.4], choices=[u'No', u'Yes'], tickHeight=-1) #Rating for interruption control condition
    ratingCont_question = visual.TextStim(win, pos=[0,+3], color='#000000', alignHoriz='center', text="Was there an interruption?")
    fixation = visual.TextStim(win,  pos=[0,0], color='#000000', alignHoriz='center', text="+")
    circle = visual.TextStim(win,  pos=[0,0], color='#000000', alignHoriz='center', text="+")
    endMessage = visual.TextStim(win,  pos=[0,0], color='#000000', alignHoriz='center', text="The end!")
    ratingImag = visual.RatingScale(win=win, name='ratingCol', marker=u'triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[u'no image at all', u'fairly vivid', u'vivid as actual'], scale=u'') #Mental imagery rating
    ratingImag_question = visual.TextStim(win, pos=[0,+3], color='#000000', alignHoriz='center', text="How vivid was your mental imagery?")
    
    trialClock = core.Clock()
    """
    # ===== CONTROL BLOCK ====== #
    # Introduction text
    counter = 0
    while counter < len(topControl):
        message1.setText(topControl[counter])
        message2.setText(bottomControl[counter])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1

    #Trials
    for trial in control_list:
        fixation.draw()
        win.flip() 
        core.wait(2) # Wait 3 seconds
        trial['stim'].play()
        #port.setData(trial['ref']) #Stim starts
        #core.wait(0.002)
        #port.setData(0)
        core.wait(33) #wait 33 seconds 
        trial['stim'].stop()
        # Interruption probe  #Somethign needs fixing heree.....
        win.flip() #clear
        while ratingCont.noResponse:
            ratingCont_question.draw()
            ratingCont.draw()
            win.flip()
        ratingControl = ratingCont.getRating()
        ratingCont.reset() # update rating parameters for each repeat
    
    """
    # ===== COLOUR BLOCK ====== #
    # Introduction text
    win.flip()
    counter = 0
    while counter < len(topColour):
        message1.setText(topColour[counter])
        message2.setText(bottomColour[counter])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1
    #Trials
    for trial in colour_list:
        trial['cond'].draw()
        win.flip()
        core.wait(2)
        circle.draw()
        win.flip() 
        core.wait(3) # Wait 3 seconds
        trial['stim'].play()
        #port.setData(trial['ref']) #Stim starts
        #core.wait(0.02)
        #port.setData(0)
        core.wait(33) #wait 33 seconds
        trial['stim'].stop()
        # Interruption probe  #Somethign needs fixing heree.....
        win.flip() #clear
        while ratingImag.noResponse:
            ratingImag_question.draw()
            ratingImag.draw()
            win.flip()
        ratingImagery = ratingImag.getRating()
        ratingImag.reset() # update rating parameters for each repeat
        core.wait(1)
    
    
    # ===== GESTURE BLOCK ====== #
    # Introduction text
    win.flip()
    counter = 0
    while counter < len(topGesture):
        message1.setText(topGesture[counter])
        message2.setText(bottomGesture[counter])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1
    #Trials
    for trial in gesture_list:
        trial['cond'].draw()
        win.flip()
        core.wait(2)
        fixation.draw()
        win.flip() 
        core.wait(3) # Wait 3 seconds
        trial['stim'].play()
        #port.setData(trial['ref']) #Stim starts
        #core.wait(0.02)
        #port.setData(0)
        core.wait(1) #wait 33 seconds
        trial['stim'].stop()
        # Interruption probe  
        win.flip() #clear
        while ratingImag.noResponse:
            ratingImag_question.draw()
            ratingImag.draw()
            win.flip()
        ratingImagery = ratingImag.getRating()
        ratingImag.reset() # update rating parameters for each repeat
        core.wait(5)
    win.flip()
    endMessage.draw()
    win.flip()

    core.wait(5)
finally: 
    win.close()
