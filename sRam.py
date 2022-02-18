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
    start_all = [0]
    stop = [1]
    beenden = [0]

    def funcClear(self):
        self.start_all.clear()
        self.stop.clear()
        self.beenden.clear()

    def funcSec(self,   start_all_content, 
                        stop_content,
                        beenden_content):
        self.start_all.append(start_all_content)
        self.stop.append(stop_content)
        self.beenden.append(beenden_content)
###############################################################################
class CAN_0(RamSec):
    start_can0 = [0]
    stop_can0 = [1]

    def funcClear(self):
        self.tart_can0.clear()
        self.stop_can0.clear()

    def funcSec(self, start_can0_content, stop_can0_content):
        self.start_can0.append(start_can0_content)
        self.stop_can0.append(stop_can0_content)
###############################################################################
class CAN_1(RamSec):
    start_can1 = [0]
    stop_can1 = [1]

    def funcClear(self):
        self.start_can1.clear()
        self.stop_can1.clear()

    def funcSec(self, start_can1_content, stop_can1_content):
        self.start_can1.append(start_can1_content)
        self.stop_can1.append(stop_can1_content)
###############################################################################
class CAN_2(RamSec):
    start_can2 = [0]
    stop_can2 = [1]

    def funcClear(self):
        self.start_can2.clear()
        self.stop_can2.clear()

    def funcSec(self, start_can2_content, stop_can2_content):
        self.start_can1.append(start_can2_content)
        self.stop_can1.append(stop_can2_content)
###############################################################################
class CAN_3(RamSec):
    start_can3 = [0]
    stop_can3 = [1]

    def funcClear(self):
        self.start_can3.clear()
        self.stop_can3.clear()

    def funcSec(self, start_can3_content, stop_can3_content):
        self.start_can1.append(start_can3_content)
        self.stop_can1.append(stop_can3_content)
###############################################################################
class CAN_Data():
    pass