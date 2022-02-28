#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
import platform

##Einbindung der Module
#import main

###############################################################################
##################################_CLASS_######################################
##Systemklasse
class System():
    sys_vers = []
    python_vers = []

    def plattform(self):
        self.sys_vers.append(platform.platform())
        self.python_vers.append(platform.python_version())
        print(self.sys_vers[-1])
        print(self.python_vers[-1])
###############################################################################
##Befehlsklasse
class RamSec():
    start = [0]
    stop = [1]
    beenden = [0]

    def funcClear(self):
        self.start.clear()
        self.stop.clear()
        self.beenden.clear()

    def funcSec(self,   start_content, 
                        stop_content,
                        beenden_content):
        self.start.append(start_content)
        self.stop.append(stop_content)
        self.beenden.append(beenden_content)