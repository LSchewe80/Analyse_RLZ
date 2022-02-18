#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

Die main.py startet das Programm. Zusätzlich implentiert und deklariert es alle Semaphoren

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import threading
import os
import subprocess
#import time
from multiprocessing import Pool
from multiprocessing import Manager
import multiprocessing

##Einbindung der Modules
import sRam
import GUI_IO
import th_1
import th_2

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

    ##Multiprocessing Manager
    m = Manager()
    q = m.Queue()
    list = [1]

    #--------------------------------------------------------------------------
    ##Thread erzeugen
    string0 = "Thread_1 Daten loggen wird gestartet"
    f1 = threading.Thread(target = th_1.func_th_1_thread, args=(list,q,string0))
    string1 = "Thread_2 wird gestartet"
    f2 = threading.Thread(target = th_2.func_th_2_thread, args=(list,q,string1))

    ##Thread starten
    #f1.start()
    f2.start()
    #--------------------------------------------------------------------------

    ###Multiprocessing (GUI/Animation/Spurführung)
    #multi_string0 = "Multiprocessing 1 wird gestartet"
    #multi_string1 = "Multiprocessing 2 wird gestartet"
    pool = Pool(processes=3)
    
    ##Spurführung
    # r0 = pool.apply_async(direction_of_travel.aniDrive, (list,q,multi_string0,))
    ##Transponderauswertung
    # r1 = pool.apply_async(animation_pool.ani, (list,q,multi_string1,))
    ##GUI
    r2 = pool.apply_async(GUI_IO.fenster.mainloop())
    pool.close()
    pool.join()
    print('Ende GUI Mainloop' + '-' * 60)

    print('Ende Main' + '-' * 60)
############################_Main_Ende_#######################################