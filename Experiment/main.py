#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:04:44 2019

@author: marcoaqil
"""
import sys
import os
from session import PRFSession
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    subject = sys.argv[1]
    sess =  sys.argv[2]
    # 3 conditions: AS0, AS1, AS2
    # (no scotoma, scotoma at [0,0], scotoma at [2,0])
    task = sys.argv[3]
    #in the full experiment we would do 3 runs?
    run = sys.argv[4]
    
    try:
        eye = sys.argv[5]
    except:
        eye = 0

    if eye == 0:
        eyetracker_on = False
    else:
        eyetracker_on = True
    
    
    output_str= f"sub-{subject}_ses-{sess}_task-{task}_run-{run}"
    
    output_dir = './logs/'+output_str+'_Logs'
    
    # CHANGED -> Always include exact date & time in logs, so if in doubt we can reconstruct the order of scans
    output_dir = output_dir + datetime.now().strftime('%Y%m%d%H%M%S')

    # if os.path.exists(output_dir):
    #     print("Warning: output directory already exists. Renaming to avoid overwriting.")
    #     output_dir = output_dir + datetime.now().strftime('%Y%m%d%H%M%S')
    
    settings_file='./expsettings_'+task+'.yml'

    ts = PRFSession(output_str=output_str, output_dir=output_dir, settings_file=settings_file, eyetracker_on=eyetracker_on)
    ts.run()

if __name__ == '__main__':
    main()