#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
# from can import Message
# import can
# from bitarray import bitarray
import os
import subprocess
import threading

##Einbindung der Module
import GUI_IO
import sRam

###########################_Funktionen_########################################
###############################################################################


################################_THREAD_#######################################

def func_th_1_thread(list,q,string):
    print(string)
    beginn = True

    lesen_RamSec = sRam.RamSec()

   
    time.sleep(2)
    ##Endlosschleife (verlassen nur durch Abrechen)
    while beginn == True:

        if lesen_RamSec.start[0] == 1:
            print("Thread_1 Analyse wird begonnen!")


            # try:


        if lesen_RamSec.start[0] == 0:
            pass
            #beginn = False
            #break
        #     #sys.exit()

        # else:
        #     ##Start kann nicht durchgeführt werden
        #     print("Thread_1 Daten loggen nicht hergestellt")
        #     if lesen_RamSec.beenden[0] == 1:
        #         beginn = False
        #         break
        #         #sys.exit()

    print("Thread_1 Daten loggen wird geschlossen!" + '-' * 60)