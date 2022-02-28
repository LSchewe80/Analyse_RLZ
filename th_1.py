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
#import xlsxwriter
#import xlwt
import csv
import openpyxl

##Einbindung der Module
import sRam
import main

###########################_Funktionen_########################################
###############################################################################


################################_THREAD_#######################################

def func_th_1_thread(list,string):
    print(string)
    beginn = True

    lesen_RamSec = sRam.RamSec()
    schreiben_RamSec = sRam.RamSec()
    data_Zwischerspeicher = sRam.Zwischenspeicher()

   
    time.sleep(3)
    ##Endlosschleife (verlassen nur durch Abrechen)
    while beginn == True:

        main.semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        if lesen_RamSec.start[0] == 1:
            main.semaphor_sRam_Sema.release()    ##Inkrementiert +1
            #Daten aus der CSV auslesen
            try:
                with open('937.csv') as csvdatei:
                    column_data = 0
                    csv_reader_object = csv.reader(csvdatei, delimiter=';')
                    #print(csv_reader_object)
                    counter = 0
                    data_Zwischerspeicher.funcClear()
                    for row in csv_reader_object:
                        print(row[1])   #Inhalt 2.Spalte
                        data_Zwischerspeicher.funcSpeicher(row[1])
                        column_data += 1
                    #beginn == False
                    #break
                    print(len(row))
                    print(column_data)

            except Exception as speichern:
                print("Datei aus CSV-Datei auslesen fehlgeschlagen!")
                print(speichern)
                beginn = False
                break
        main.semaphor_sRam_Sema.release()    ##Inkrementiert +1 

    
        main.semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        if lesen_RamSec.start[0] == 1:
            main.semaphor_sRam_Sema.release()    ##Inkrementiert +1
            print("Thread_1 Analysedaten_xlsx verarbeiten, in Tabelle einfuegen und speichern!")
            try:
                print("Excel-Datei oeffnen" + '-' * 60)
                file = '20211129_937_Analyse_RLZ_23-Grad_DC-MAX_1.xlsx'
                fileXLSX = openpyxl.load_workbook(file)
                sheet = fileXLSX["Auswertung"]
                #print(sheet['C4'].value)

                print("Excel-Datei befuellen" + '-' * 60)
                zeile = 10
                for i in range(column_data - 1):
                    sheet.cell(row=zeile, column=15).value = data_Zwischerspeicher.data_csv[i]
                    print(data_Zwischerspeicher.data_csv[i])
                    zeile += 1
            except Exception as befuellen:
                print("Befuellen der Daten in Excel fehlgeschlagen!")
                print(befuellen)
                beginn = False
                break

            try:
                ##Excel-Datei speichern
                fileXLSX.save('Result.xlsx')
                print("Excel-Datei gespeichert" + '-' * 60)
                
                time.sleep(2)

                main.semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
                schreiben_RamSec.funcClear()
                schreiben_RamSec.funcSec(0,1,1)
                main.semaphor_sRam_Sema.release()    ##Inkrementiert +1

                print("Eintrag fertig" + '-' * 60)
                beginn == False
                break

            except Exception as speichern:
                print("Speichern der Messung in Excel fehlgeschlagen!")
                print(speichern)
                beginn = False
                break
        main.semaphor_sRam_Sema.release()    ##Inkrementiert +1        

        if lesen_RamSec.beenden[0] == 1:
            time.sleep(2)
            beginn = False
            break
            #sys.exit()

        # else:
        #     ##Start kann nicht durchgeführt werden
        #     print("Thread_1 Daten loggen nicht hergestellt")
        #     if lesen_RamSec.beenden[0] == 1:
        #         beginn = False
        #         break
        #         #sys.exit()

    print("Thread_1 Analysedaten_xlsx wird beendet!" + '-' * 60)