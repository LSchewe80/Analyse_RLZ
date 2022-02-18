#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
import os
import subprocess
import threading

##Einbindung der Module
import GUI_IO
import sRam

###############################################################################
##########################_Objekte_############################################
schreiben_sRam = sRam.RamSec()
lesen_sRam = sRam.RamSec()

system_info = sRam.System()
###########################_Funktionen_########################################
###############################################################################


################################_THREAD_#######################################

def func_th_2_thread(list,q,string):
    print(string)
    beginn = True

    lesen_RamSec = sRam.RamSec()

    while beginn == True:

        if lesen_RamSec.beenden[0] == 1:
            print("Thread_2 wird beendet!" + '-' * 60)
            time.sleep(4)
            beginn = False
            break

    print("Thread_2 ist beendet!" + '-' * 60)