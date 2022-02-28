#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

Die main.py startet das Programm.
Zusätzlich implentiert und deklariert es alle Semaphoren

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import threading
import os
import subprocess
#import time


##Einbindung der Modules
import sRam
import th_1


##############################_Variablen_######################################
###############################################################################



##############################_Semaphoren_#####################################
###############################################################################
##Erstellen der Semaphoren (Inhalt des Sema bei Start des Programms)
semaphor_sRam_Sema = threading.Semaphore(value = 1)    #Inhalt 1 für den Zugang aufs sRAm_Security (globals)

###############################_Main_##########################################
###############################################################################
if __name__ == "__main__":
    ##Systemsdaten abfragen
    system = sRam.System()
    system.plattform()

    #--------------------------------------------------------------------------
    ##Thread erzeugen
    string0 = "Thread_1 Analyse_RLZ"
    f1 = threading.Thread(target = th_1.func_th_1_thread, args=(list,q,string0))

    ##Thread starten
    #f1.start()

    print('Ende Main' + '-' * 60)
############################_Main_Ende_#######################################