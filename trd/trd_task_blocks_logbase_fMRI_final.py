#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Mon Jun 23 12:50:59 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division #so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, seed
from random import choice
import os #handy system and path functions
from itertools import islice
from math import floor
from random import randint

#store info about the experiment session
expName='trd_task_block_mri'#from the Builder filename that created this script
expInfo={'participant':'', 'version':'1'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s_version%s' %(expName, expInfo['participant'], expInfo['version'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    
trd_datFile=open(filename+'.txt','a')
trd_datFile.write('Run\tTrial\tChoice1\tChoice2\tDelay1\tDelay2\tChosenValue\tChosenDelay\tResponse\tRT\tCurrMoney\tChoiceOnset\tGoOnset\tFBOnset\n')

#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb')
    
num_trls_each_condition = 10

#Initialise components for Routine "waiting"
waitingClock=core.Clock()
scanner=visual.TextStim(win=win, ori=0, name='scanner',
    text='nonsense',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)


#Initialise components for Routine "trial"
trialClock=core.Clock()

init_fixClock=core.Clock()
init_fix=visual.TextStim(win=win, ori=0, name='init_fix',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=0.3,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)
choiceimage1 = visual.ImageStim(win=win, name='choiceimage1',
    image=None, mask=None,
    ori=0, pos=[-0.5, 0], size=[0.5, 0.5],
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
choiceimage2 = visual.ImageStim(win=win, name='choiceimage2',
    image=None, mask=None,
    ori=0, pos=[0.5, 0], size=[0.5, 0.5],
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
choicetext1=visual.TextStim(win=win, ori=0, name='choicetext1',
    text='nonsense',
    font=u'Arial',
    pos=[-0.5, -0.5], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
choicetext2=visual.TextStim(win=win, ori=0, name='choicetext2',
    text='nonsense',
    font=u'Arial',
    pos=[0.5, -0.5], height=0.1,wrapWidth=1.5,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)
gocuetext=visual.TextStim(win=win, ori=0, name='gocuetext',
    text='Go!',
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=1.5,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)
fix=visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=0.3,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)
feedback=visual.TextStim(win=win, ori=0, name='feedback',
    text=u'nonsense',
    font=u'Arial',
    pos=[0, 0], height=0.2,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)
    
final_fixClock=core.Clock()
final_fix=visual.TextStim(win=win, ori=0, name='final_fix',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=0.3,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)

if expInfo['version'] == '1':
    immediatesmall_choicetext = '10 cents now!'
    immediatelarge_choicetext = '15 cents now!'
    fourseclarge_choicetext = '15 cents, in 4 secs!'
    eightseclarge_choicetext = '15 cents, in 8 secs!'
    sixteenseclarge_choicetext = '15 cents, in 16 secs!'
    thirtytwoseclarge_choicetext = '15 cents, in 32 secs!'
    sixtyfourseclarge_choicetext = '15 cents, in 64 secs!'
    onetwentyeighteclarge_choicetext = '15 cents, in 128 secs!'
else:
    immediatesmall_choicetext = ''
    immediatelarge_choicetext = ''
    fourseclarge_choicetext = ''
    eightseclarge_choicetext = ''
    sixteenseclarge_choicetext = ''
    thirtytwoseclarge_choicetext = ''
    sixtyfourseclarge_choicetext = ''
    onetwentyeighteclarge_choicetext = ''

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 
begExpClock=core.Clock() #to track the time since the actual paradigm started (after the scanner screen)

#set up handler to look after randomisation of conditions etc
no_delay = np.ones(num_trls_each_condition)
four_delay = np.ones(num_trls_each_condition)*2
eight_delay = np.ones(num_trls_each_condition)*3
sixteen_delay = np.ones(num_trls_each_condition)*4
thirtytwo_delay = np.ones(num_trls_each_condition)*5
sixtyfour_delay = np.ones(num_trls_each_condition)*6
onetwentyeight_delay = np.ones(num_trls_each_condition)*7

all_stim = os.listdir(os.getcwd() + os.path.sep + 'pics')
all_stim_path = [os.getcwd() + os.path.sep + 'pics' + os.path.sep + curr_stim for curr_stim in all_stim]

# I think I added this to randomize across delay conditions but we are not
# currently using this thus the code is commented out
#all_large_delay = np.concatenate((no_delay,four_delay,eight_delay,sixteen_delay,thirtytwo_delay,sixtyfour_delay,onetwentyeight_delay),axis=0)
#np.random.shuffle(all_large_delay)

run_nums = range(1,8)
#np.random.shuffle(run_nums)

myarray_runs = []
for i in range(len(run_nums)):
    myarray_runs.append({'curr_run_num': run_nums[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
runs=data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=myarray_runs,
    seed=None, name='runs')
thisExp.addLoop(runs)#add the loop to the experiment
thisRun=runs.trialList[0]#so we can initialise stimuli with some values

for thisRun in runs:
    
    if thisRun!=None:
        for paramName in thisRun.keys():
            exec(paramName+'=thisRun.'+paramName)
    
    if curr_run_num == 1:
        other_choicestim_text = immediatelarge_choicetext
        curr_block_stim = no_delay
        post_delay = 0.0
    elif curr_run_num == 2:
        other_choicestim_text = fourseclarge_choicetext
        curr_block_stim = four_delay
        post_delay = 4.0
    elif curr_run_num == 3:
        other_choicestim_text = eightseclarge_choicetext
        curr_block_stim = eight_delay
        post_delay = 8.0
    elif curr_run_num == 4:
        other_choicestim_text = sixteenseclarge_choicetext
        curr_block_stim = sixteen_delay
        post_delay = 16.0
    elif curr_run_num == 5:
        other_choicestim_text = thirtytwoseclarge_choicetext
        curr_block_stim = thirtytwo_delay
        post_delay = 32.0
    elif curr_run_num == 6:
        other_choicestim_text = sixtyfourseclarge_choicetext
        curr_block_stim = sixtyfour_delay
        post_delay = 64.0
    elif curr_run_num == 7:
        other_choicestim_text = onetwentyeighteclarge_choicetext
        curr_block_stim = sixtyfour_delay
        post_delay = 128.0
    
    jitter_delay_list = []
    while len(jitter_delay_list) < num_trls_each_condition:
        if random() > 0.5:
            jitter_delay_list.append(6-randint(0,4))
        else:
            jitter_delay_list.append(6+randint(0,4))
    
    fb_jitter_delay_list = []
    while len(fb_jitter_delay_list) < num_trls_each_condition:
        if random() > 0.5:
            fb_jitter_delay_list.append(6-randint(0,4))
        else:
            fb_jitter_delay_list.append(6+randint(0,4))
            
    all_times = jitter_delay_list + fb_jitter_delay_list + [post_delay * 10] + [6*2]
    total_run_time = np.sum(all_times)
    num_TRs_needed = total_run_time/2.0
    
    #------Prepare to start Routine"waiting"-------
    scanner.text = 'When you see "Go!" on the screen \n\n Select one of the two options\n\n by pressing the B and Y keys.\n\n This run needs %s TRs.\n\n Press Return to continue'%num_TRs_needed
    t=0; waitingClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    sync_pulse = event.BuilderKeyResponse() #create an object of type KeyResponse
    sync_pulse.status=NOT_STARTED
    #keep track of which components have finished
    waitingComponents=[]
    waitingComponents.append(scanner)
    waitingComponents.append(sync_pulse)
    for thisComponent in waitingComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "waiting"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=waitingClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*scanner* updates
        if t>=0.0 and scanner.status==NOT_STARTED:
            #keep track of start time/frame for later
            scanner.tStart=t#underestimates by a little under one frame
            scanner.frameNStart=frameN#exact frame index
            scanner.setAutoDraw(True)
        
        #*sync_pulse* updates
        if t>=0.0 and sync_pulse.status==NOT_STARTED:
            #keep track of start time/frame for later
            sync_pulse.tStart=t#underestimates by a little under one frame
            sync_pulse.frameNStart=frameN#exact frame index
            sync_pulse.status=STARTED
            #keyboard checking is just starting
            sync_pulse.clock.reset() # now t=0
            event.clearEvents()
        if sync_pulse.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['+', 'num_add', 'return'])
            if len(theseKeys)>0:#at least one key was pressed
                sync_pulse.keys=theseKeys[-1]#just the last key pressed
                sync_pulse.rt = sync_pulse.clock.getTime()
                #abort routine on response
                continueRoutine=False
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in waitingComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # This allows for GE prep scans to run without triggering the actual experiment
    core.wait(5)
    
    #End of Routine "waiting"
    for thisComponent in waitingComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

    # The two waiting periods may deal with the prep scans on the GE scanner
    scanner.text = 'Press the Return key to\n begin the current block.'
    #scanner.text = 'Waiting for scanner to\n begin the current block.'
    #------Prepare to start Routine"waiting"-------
    t=0; waitingClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    sync_pulse = event.BuilderKeyResponse() #create an object of type KeyResponse
    sync_pulse.status=NOT_STARTED
    #keep track of which components have finished
    waitingComponents=[]
    waitingComponents.append(scanner)
    waitingComponents.append(sync_pulse)
    for thisComponent in waitingComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "waiting"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=waitingClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*scanner* updates
        if t>=0.0 and scanner.status==NOT_STARTED:
            #keep track of start time/frame for later
            scanner.tStart=t#underestimates by a little under one frame
            scanner.frameNStart=frameN#exact frame index
            scanner.setAutoDraw(True)
        
        #*sync_pulse* updates
        if t>=0.0 and sync_pulse.status==NOT_STARTED:
            #keep track of start time/frame for later
            sync_pulse.tStart=t#underestimates by a little under one frame
            sync_pulse.frameNStart=frameN#exact frame index
            sync_pulse.status=STARTED
            #keyboard checking is just starting
            sync_pulse.clock.reset() # now t=0
            event.clearEvents()
        if sync_pulse.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['+', 'num_add', 'return'])
            if len(theseKeys)>0:#at least one key was pressed
                sync_pulse.keys=theseKeys[-1]#just the last key pressed
                sync_pulse.rt = sync_pulse.clock.getTime()
                #abort routine on response
                continueRoutine=False
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in waitingComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "waiting"
    for thisComponent in waitingComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    
    myarray = []
    for i in range(len(curr_block_stim)):
        myarray.append({'stim_num': int(curr_block_stim[i]), 'jitter_delay': float(jitter_delay_list[i]), 'fb_jitter_delay': float(fb_jitter_delay_list[i])}) #puts data into an array of dictionaries that the TrialHandler function will accept
    trials=data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=myarray,
        seed=None, name='trials')
    thisExp.addLoop(trials)#add the loop to the experiment
    thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
    #abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    #if thisTrial!=None:
    #    for paramName in thisTrial.keys():
    #        exec(paramName+'=thisTrial.'+paramName)
    
    begExpClock.reset()
    t=0; init_fixClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    #keep track of which components have finished
    init_fixComponents=[]
    init_fixComponents.append(init_fix)
    for thisComponent in init_fixComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "init_fix"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=init_fixClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*init_fix* updates
        if t>=0.0 and init_fix.status==NOT_STARTED:
            #keep track of start time/frame for later
            init_fix.tStart=t#underestimates by a little under one frame
            init_fix.frameNStart=frameN#exact frame index
            init_fix.setAutoDraw(True)
        elif init_fix.status==STARTED and t>=(0.0 + 6.0):
            init_fix.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in init_fixComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
    
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "waiting"
    for thisComponent in init_fixComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    
    response_window = 2.0 #this is the time screen 'Go!' is on (PR check notes)
    
    if int(expInfo['participant'])%2:
        choiceimage1.image = all_stim_path[0]
        choicetext1.text = immediatesmall_choicetext
        choice1 = '10'
        delay1 = 0.0
        
        choiceimage2.image = all_stim_path[1]
        choicetext2.text = other_choicestim_text
        choice2 = '15'
        delay2 = post_delay
    else:
        choiceimage1.image = all_stim_path[1]
        choicetext1.text = other_choicestim_text
        choice1 = '15'
        delay1 = post_delay
        
        choiceimage2.image = all_stim_path[0]
        choicetext2.text = immediatesmall_choicetext
        choice2 = '10'
        delay2 = 0.0

    total_money = 0.0
    for thisTrial in trials:
        currentLoop = trials
        #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
        if thisTrial!=None:
            for paramName in thisTrial.keys():
                exec(paramName+'=thisTrial.'+paramName)
    
        #------Prepare to start Routine"trial"-------
        t=0; trialClock.reset() #clock 
        frameN=-1
        key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
        key_resp.status=NOT_STARTED
        #keep track of which components have finished
        choiceComponents=[]
        choiceComponents.append(choicetext1)
        choiceComponents.append(choicetext2)
        choiceComponents.append(choiceimage1)
        choiceComponents.append(choiceimage2)
        choiceComponents.append(gocuetext)
        choiceComponents.append(key_resp)
        for thisComponent in choiceComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        #-------Start Routine "trial"-------
        continueRoutine=True
        while continueRoutine:
            #get current time
            t=trialClock.getTime()
            frameN=frameN+1#number of completed frames (so 0 in first frame)
            #update/draw components on each frame
            
            if t>=0.0 and choicetext1.status==NOT_STARTED:
                #keep track of start time/frame for later
                choicetext1.tStart=t#underestimates by a little under one frame
                choicetext1.frameNStart=frameN#exact frame index
                choicetext1.setAutoDraw(True)
                choiceOnset=begExpClock.getTime()
            elif choicetext1.status==STARTED and t>=(0.0 + jitter_delay + response_window):
                choicetext1.setAutoDraw(False)
            
            if t>=0.0 and choicetext2.status==NOT_STARTED:
                #keep track of start time/frame for later
                choicetext2.tStart=t#underestimates by a little under one frame
                choicetext2.frameNStart=frameN#exact frame index
                choicetext2.setAutoDraw(True)
            elif choicetext2.status==STARTED and t>=(0.0 + jitter_delay + response_window):
                choicetext2.setAutoDraw(False) 
            
            if t>=0.0 and choiceimage1.status==NOT_STARTED:
                #keep track of start time/frame for later
                choiceimage1.tStart=t#underestimates by a little under one frame
                choiceimage1.frameNStart=frameN#exact frame index
                choiceimage1.setAutoDraw(True)
            elif choiceimage1.status==STARTED and t>=(0.0 + jitter_delay + response_window):
                choiceimage1.setAutoDraw(False)
            
            if t>=0.0 and choiceimage2.status==NOT_STARTED:
                #keep track of start time/frame for later
                choiceimage2.tStart=t#underestimates by a little under one frame
                choiceimage2.frameNStart=frameN#exact frame index
                choiceimage2.setAutoDraw(True)
            elif choiceimage2.status==STARTED and t>=(0.0 + jitter_delay + response_window):
                choiceimage2.setAutoDraw(False)
            
            if t>=jitter_delay and gocuetext.status==NOT_STARTED:
                gocuetext.tStart=t #underestimates by a little under one frameN
                gocuetext.frameNStart=frameN #exact frame index
                gocuetext.setAutoDraw(True)
                gocueOnset=begExpClock.getTime()
            elif gocuetext.status==STARTED and t>=(jitter_delay + response_window):
                gocuetext.setAutoDraw(False)
            
            #*key_resp* updates
            if t>=jitter_delay and key_resp.status==NOT_STARTED:
                #keep track of start time/frame for later
                key_resp.tStart=t#underestimates by a little under one frame
                key_resp.frameNStart=frameN#exact frame index
                key_resp.status=STARTED
                #keyboard checking is just starting
                key_resp.clock.reset() # now t=0
                event.clearEvents(eventType='keyboard')
            elif key_resp.status==STARTED and t>=(jitter_delay+response_window):#only update if being drawn
                key_resp.status = STOPPED
            if key_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['b', 'y'])
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys)>0:#at least one key was pressed
                    if key_resp.keys==[]:#then this was the first keypress
                        key_resp.keys=theseKeys[0]#just the first key pressed
                        key_resp.rt = key_resp.clock.getTime()
                    
            #check if all components have finished
            if not continueRoutine: #a component has requested that we end
                routineTimer.reset() #this is the new t0 for non-slip Routines
                break
            continueRoutine=False#will revert to True if at least one component still running
            for thisComponent in choiceComponents:
                if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                    continueRoutine=True; break#at least one component has not yet finished
            
            #check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            #refresh the screen
            if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        if key_resp.keys == 'b' and choice1 == '10':
            curr_choice = 0.10
            delay = 0.0
            chosenvalue = '10'
        elif key_resp.keys == 'y' and choice2 == '10':
            curr_choice = 0.10
            delay = 0.0
            chosenvalue = '10'
        elif key_resp.keys == 'b' and choice1 == '15':
            curr_choice = 0.15
            delay = post_delay
            chosenvalue = '15'
        elif key_resp.keys == 'y' and choice2 == '15':
            curr_choice = 0.15
            delay = post_delay
            chosenvalue = '15'
        else:
            curr_choice = 0.00
            delay = 0.0
            chosenvalue = 'NA'
        
        t=0; trialClock.reset() #clock 
        fbComponents=[]
        fbComponents.append(fix)
        fbComponents.append(feedback)
        
        feedback.text = "You get $%.2f!" %curr_choice
        total_money = total_money + curr_choice
        
        for thisComponent in fbComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        continueRoutine=True
        while continueRoutine:
            t=trialClock.getTime()
            #*fix* updates
            if t>=0.0 and fix.status==NOT_STARTED:
                #keep track of start time/frame for later
                fix.tStart=t#underestimates by a little under one frame
                fix.frameNStart=frameN#exact frame index
                fix.setAutoDraw(True)
            elif fix.status==STARTED and t>=(0.0+delay):
                fix.setAutoDraw(False)
            
            if t>=delay and feedback.status==NOT_STARTED:
                feedback.tStart=t
                feedback.frameNStart=frameN
                feedback.setAutoDraw(True)
                fbOnset=begExpClock.getTime()
            elif feedback.status==STARTED and t>=(delay+fb_jitter_delay):
                feedback.setAutoDraw(False)
            
            #check if all components have finished
            if not continueRoutine: #a component has requested that we end
                routineTimer.reset() #this is the new t0 for non-slip Routines
                break
            continueRoutine=False#will revert to True if at least one component still running
            for thisComponent in fbComponents:
                if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                    continueRoutine=True; break#at least one component has not yet finished
            
            #check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            #refresh the screen
            if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #End of Routine "trial"
        for thisComponent in choiceComponents:
            if hasattr(thisComponent,"setAutoDraw"): 
                thisComponent.setAutoDraw(False)
                
        for thisComponent in fbComponents:
            if hasattr(thisComponent,"setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        trd_datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(curr_run_num,trials.thisTrialN+1,choice1,choice2,delay1,delay2,chosenvalue,delay,key_resp.keys,key_resp.rt,total_money,choiceOnset,gocueOnset,fbOnset))
                
    t=0; final_fixClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    #keep track of which components have finished
    final_fixComponents=[]
    final_fixComponents.append(final_fix)
    for thisComponent in final_fixComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "init_fix"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=final_fixClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*init_fix* updates
        if t>=0.0 and final_fix.status==NOT_STARTED:
            #keep track of start time/frame for later
            final_fix.tStart=t#underestimates by a little under one frame
            final_fix.frameNStart=frameN#exact frame index
            final_fix.setAutoDraw(True)
        elif final_fix.status==STARTED and t>=(0.0 + 6.0):
            final_fix.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in final_fixComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "final_fix"
    for thisComponent in final_fixComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    
        

#Shutting down:
win.close()
core.quit()
