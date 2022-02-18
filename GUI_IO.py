# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:44:40 2019

@author: schewel
"""

###########################_Einbindung_import_#################################
import tkinter
from tkinter import *
from tkinter import filedialog
#import tkinter as tk
from PIL import Image, ImageTk
import platform

import time
import os

##Einbindung der Module
import main
import sRam

###############################################################################
##########################_Objekte_############################################
schreiben_sRam = sRam.RamSec()
lesen_sRam = sRam.RamSec()

system_info = sRam.System()

###############################################################################
###########################_Funktionen_########################################
##Button frame_CAN0
def start_0():
    pass
def stop_0():
    pass
def dateipfad_0():
    home = os.path.expanduser("/home/akka-pi/Dokumente/Testautomatisierung_AKKA/Programme/src/CAN_Trace_PEAK/dbc_data/EV_CAN")
    datei_pfad_0 = filedialog.askopenfilename(initialdir=home,
                                            title="Datei-Auswahl")
    fenster.text1.insert(END, datei_pfad_0)
#Checkbutton überprüfen
def sigName0():
    statCheckButton0 = signalname0.get()
    # print(statCheckButton0)
def log_CAN0():
    statCheckButton0 = signalname0.get()
    # print(statCheckButton0)
    if statCheckButton0 == "OnLogCAN0":
        try:
            pass
        except:
            pass
###############################################################################
##Button frame_CAN1
def start_1():
    pass
def stop_1():
    pass
def dateipfad_1():
    home = os.path.expanduser("/home/akka-pi/Dokumente/Testautomatisierung_AKKA/Programme/src/CAN_Trace_PEAK/dbc_data/Antrieb_CAN")
    datei_pfad_1 = filedialog.askopenfilename(  initialdir=home,
                                                title="Datei-Auswahl")
    fenster.text2.insert(END, datei_pfad_1)
#Checkbutton überprüfen
def sigName1():
    statCheckButton1 = signalname1.get()
    # print(statCheckButton1)
def log_CAN1():
    statCheckButton1 = signalname1.get()
    # print(statCheckButton1)
    if statCheckButton1 == "OnLogCAN1":
        try:
            pass
        except:
            pass
###############################################################################
##Button frame_CAN2
def start_2():
    pass
def stop_2():
    pass
def dateipfad_2():
    home = os.path.expanduser("/home/akka-pi/Dokumente/Testautomatisierung_AKKA/Programme/src/CAN_Trace_PEAK/dbc_data/Komfort_CAN")
    datei_pfad_2 = filedialog.askopenfilename(  initialdir=home,
                                                title="Datei-Auswahl")
    fenster.text3.insert(END, datei_pfad_2)
#Checkbutton überprüfen
def sigName2():
    statCheckButton2 = signalname2.get()
    # print(statCheckButton2)
def log_CAN2():
    statCheckButton2 = signalname2.get()
    # print(statCheckButton2)
    if statCheckButton2 == "OnLogCAN2":
        try:
            pass
        except:
            pass
###############################################################################
##Button frame_CAN3
def start_3():
    pass
def stop_3():
    pass
def dateipfad_3():
    home = os.path.expanduser("/home/akka-pi/Dokumente/Testautomatisierung_AKKA/Programme/src/CAN_Trace_PEAK/dbc_data/Diagnose_CAN")
    datei_pfad_3 = filedialog.askopenfilename(  initialdir=home,
                                                title="Datei-Auswahl")
    fenster.text4.insert(END, datei_pfad_3)
#Checkbutton überprüfen
def sigName3():
    statCheckButton3 = signalname3.get()
    # print(statCheckButton3)
def log_CAN3():
    statCheckButton3 = signalname3.get()
    # print(statCheckButton3)
    if statCheckButton3 == "OnLogCAN3":
        try:
            pass
        except:
            pass
###############################################################################
##Button frame_GUI
def start_all():
    pass
def stop_all():
    pass
##beenden/schliessen
def end():
    main.semaphor_sRam_Sema.acquire()   #Dekrementiert -1
    schreiben_sRam.funcClear()
    schreiben_sRam.funcSec(0,1,1)
    main.semaphor_sRam_Sema.release()   #Inkrementiert +1
    ##Fenster nach 2 Sek. schließen
    fenster.after(2000,fenster.destroy)
#Checkbutton überprüfen
def sigNameALL():
    statCheckButtonALL = signalnameALL.get()
    if statCheckButtonALL == "OnLogCANALL":
        signalname0.set("OnLogCAN0")
        signalname1.set("OnLogCAN1")
        signalname2.set("OnLogCAN2")
        signalname3.set("OnLogCAN3")
    # print(statCheckButtonALL)
def log_CANALL():
    statCheckButtonALL = signalnameALL.get()
    # print(statCheckButton2)
    if statCheckButtonALL == "OnLogCANALL":
        try:
            pass
        except:
            pass

###############################################################################
#################################_GUI_#########################################
fenster = Tk()
##Fenstergröße bestimmen
#Maße des Hauptfensters
x_size = 1050     #Standard auf 750
y_size = 720    #Standard auf 500
#fenster.geometry('{}x{}'.format(x_size, y_size))
###############################################################################
#Titel
fenster.title('CAN-Trace')
###############################################################################
#Menüleiste
mBar = Menu(fenster)
mFile = Menu(mBar)
mFile1 = Menu(mBar)
mFile.add_command(label="Start", underline=0)#,command = start)
mFile.add_command(label="Stop", underline=0)#,command = stop)
mFile.add_command(label="Beenden", underline=0,command = end)
#mFile.add_separator()  #Trennstrich zwischen den label
#mFile.add_command(label="Diagnose", underline=0)#,command = ausgabe)
# mFile.add_command(label="Clear", underline=0,command = clear)

mBar.add_cascade(label="Menü",menu=mFile, underline=0)     #Menuleiste sichtbar machen
#mBar.add_cascade(label="Analyse",menu=mFile1, underline=0)     #Menuleiste sichtbar machen

fenster["menu"] = mBar
###############################################################################
#Fenster im Hauptfenster
frame_impressum = Frame(fenster)
frame_textanzeige = Frame(fenster)
frame_CAN_0 = Frame(fenster)
frame_CAN_1 = Frame(fenster)
frame_CAN_2 = Frame(fenster)
frame_CAN_3 = Frame(fenster)
# frame_ueberschrift = Frame(fenster)
# frame_text = Frame(fenster)
# frame_ueberschrift1 = Frame(fenster)
# frame_text1 = Frame(fenster)
frame_GUI = Frame(fenster)#,bg="royal blue")

#Aufteilung der Frames in Grids
frame_impressum.grid(row=0, column=0)
frame_textanzeige.grid(row=1, column=0)
frame_CAN_0.grid(row=2, column=0)
frame_CAN_1.grid(row=3, column=0)
frame_CAN_2.grid(row=4, column=0)
frame_CAN_3.grid(row=5, column=0)
# frame_button.grid(row=5,column=0)
# frame_ueberschrift.grid(row=6,column=0)
# frame_text.grid(row= 7,column=0)
# frame_ueberschrift1.grid(row=8,column=0)
# frame_text1.grid(row= 9,column=0)
frame_GUI.grid(row=10, column=0)
###############################################################################
##Bilder (Logo's) & Impressum im frame_impressum
height1 = 55
height2 = 55
height3 = 4
width1 = 160
width2 = 650
width3 = 10

image = Image.open('akka_logo.png')
image = image.resize((width1, height1))
image = ImageTk.PhotoImage(image)
fenster.label = Label(frame_impressum,
                        height=height1,
                        width=width1,
                        borderwidth=2,       #Rahmenbreite
                        relief='raised',     #Rahmen sichtbar machen
                        anchor='w',
                        image=image)
fenster.label.grid(row=0, column=0)

image1 = Image.open('akkaCover.png')
image1 = image1.resize((width2, height2))
image1 = ImageTk.PhotoImage(image1)
fenster.label = Label(frame_impressum,
                        height=height2,
                        width=width2,
                        borderwidth=2,       #Rahmenbreite
                        relief='raised',     #Rahmen sichtbar machen
                        anchor='e',
                        image=image1)
fenster.label.grid(row=0, column=1)

impressum = "CAN Trace\nVersion:\n0.1\nAKKA"
fenster.impressum = Label(frame_impressum,
                            font=('Arial',7),
                            height=height3,
                            width=width3,
                            borderwidth=2,
                            relief='raised',
                            #anchor='e',
                            text=impressum)
fenster.impressum.grid(row=0, column=2)
###############################################################################
#Text in frame_textanzeige
fenster.label1 = Label(frame_textanzeige,
                       text='Messung',
                       font=('Arial',16),
                       height=1,
                       width=75,
                       borderwidth=0,
                       relief='raised',
                       bg='#687A80')
#.grid() muss separat gesetzt werden, wenn mit config() geändert wird!
#Es gibt keinen Wert zurück! (siehe in den Funktionen oben!)
fenster.label1.grid(row=0, column=0, pady=5)

###################################################################################
##Widget/Button/Textfeld Size
###################################################################################
##Groesse Widgets
widget_hoehe = 65
widget_breite = 500

##Groesse der Buttons
button_hoehe = 1
button_breite = 9
button_rahmenbreite = 2
button_relief = 'groove'
padx_x = 5
pady_y = 5

##Groesse Textfeld
text_hoehe = 2
text_breite = 80

###################################################################################
##Widget frame_CAN_0
###################################################################################
labelframe_widget0 = LabelFrame( frame_CAN_0,
                                text="EV-CAN",
                                height=widget_hoehe,
                                width=widget_breite,
                                font=('Arial',14) )
labelframe_widget0.grid(row=0, column=0, pady=5, padx=10)

fenster.button1 = Button(labelframe_widget0,
                         text='Start CAN_0',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="sizing",
                         command=start_0, # command übergibt die Funktionen
                         bg='green').grid(row=0, column=0, padx=padx_x, pady=pady_y)

fenster.button2 = Button(labelframe_widget0,
                         text='Stop CAN_0',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=stop_0,
                         bg='yellow').grid(row=1, column=0, padx=padx_x, pady=pady_y)

fenster.button_pfad0 = Button(labelframe_widget0,
                         text='DBC-Pfad',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=dateipfad_0,
                         bg='orange').grid(row=0, rowspan=2, column=1, padx=padx_x, pady=pady_y)

##Text-Feld für die Ausgabe des Ergebnisses mit Scrollbar
fenster.scrollbar0 = Scrollbar(labelframe_widget0,
                              orient = "vertical")

fenster.text1 = Text(labelframe_widget0,
                     width = text_breite,
                     height = text_hoehe,   #Ausgabe der Anzahl der Zeilen im Textfeld
                     borderwidth=5,
                     relief='ridge',
                     yscrollcommand = fenster.scrollbar0.set)

fenster.scrollbar0["command"] = fenster.text1.yview  #Command nach text1 damit scrollbar das attribute 'text1' hat
fenster.text1.grid(row=0, rowspan=2, column=2)
fenster.scrollbar0.grid(row=0, rowspan=2, column=2, sticky = 'ns')

signalname0 = StringVar()
signalname0.set("OffLogCAN0")
fenster.checkbutton0 = Checkbutton(labelframe_widget0,
                                  text = "Logging CAN0",
                                  variable = signalname0,
                                  #borderwidth=3,
                                  #relief='groove',
                                  onvalue = "OnLogCAN0",
                                  offvalue = "OffLogCAN0",
                                  command = sigName0)
fenster.checkbutton0.grid(row=0,rowspan=2,column=3, padx=10, pady=15, sticky=NW)

###################################################################################
##Widget frame_CAN_1
###################################################################################
labelframe_widget1 = LabelFrame( frame_CAN_1,
                                text="Antrieb_CAN",
                                height=widget_hoehe,
                                width=widget_breite,
                                font=('Arial',14) )
labelframe_widget1.grid(row=0, column=0, pady=5, padx=10)

fenster.button3 = Button(labelframe_widget1,
                         text='Start CAN_1',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="sizing",
                         command=start_1, # command übergibt die Funktionen
                         bg='green').grid(row=0, column=0, padx=padx_x, pady=pady_y)

fenster.button4 = Button(labelframe_widget1,
                         text='Stop CAN_1',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=stop_1,
                         bg='yellow').grid(row=1, column=0, padx=padx_x, pady=pady_y)

fenster.button_pfad1 = Button(labelframe_widget1,
                         text='DBC-Pfad',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=dateipfad_1,
                         bg='orange').grid(row=0, rowspan=2, column=1, padx=padx_x, pady=pady_y)

##Text-Feld für die Ausgabe des Ergebnisses mit Scrollbar
fenster.scrollbar1 = Scrollbar(labelframe_widget1,
                              orient = "vertical")

fenster.text2 = Text(labelframe_widget1,
                     width = text_breite,
                     height = text_hoehe,   #Ausgabe der Anzahl der Zeilen im Textfeld
                     borderwidth=5,
                     relief='ridge',
                     yscrollcommand = fenster.scrollbar1.set)

fenster.scrollbar1["command"] = fenster.text2.yview  #Command nach text1 damit scrollbar das attribute 'text2' hat
fenster.text2.grid(row=0, rowspan = 2, column=2)
fenster.scrollbar1.grid(row=0, rowspan=2, column=2, sticky = 'ns')

signalname1 = StringVar()
signalname1.set("OffLogCAN1")
fenster.checkbutton1 = Checkbutton(labelframe_widget1,
                                  text = "Logging CAN1",
                                  variable = signalname1,
                                  #borderwidth=3,
                                  #relief='groove',
                                  onvalue = "OnLogCAN1",
                                  offvalue = "OffLogCAN1",
                                  command = sigName1)
fenster.checkbutton1.grid(row=0, rowspan=2, column=3, padx=10, pady=15, sticky=NW)

###################################################################################
##Widget frame_CAN_2
###################################################################################
labelframe_widget2 = LabelFrame( frame_CAN_2,
                                text="Komfort_CAN",
                                height=widget_hoehe,
                                width=widget_breite,
                                font=('Arial',14) )
labelframe_widget2.grid(row=0, column=0, pady = 5, padx = 10)

fenster.button5 = Button(labelframe_widget2,
                         text='Start CAN_2',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="sizing",
                         command=start_2, # command übergibt die Funktionen
                         bg='green').grid(row=0, column=0, padx=padx_x, pady=pady_y)

fenster.button6 = Button(labelframe_widget2,
                         text='Stop CAN_2',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=stop_2,
                         bg='yellow').grid(row=1, column=0, padx=padx_x, pady=pady_y)

fenster.button_pfad2 = Button(labelframe_widget2,
                         text='DBC-Pfad',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=dateipfad_2,
                         bg='orange').grid(row=0, rowspan=2, column=1, padx=padx_x, pady=pady_y)

##Text-Feld für die Ausgabe des Ergebnisses mit Scrollbar
fenster.scrollbar2 = Scrollbar(labelframe_widget2,
                              orient = "vertical")

fenster.text3 = Text(labelframe_widget2,
                     width = text_breite,
                     height = text_hoehe,   #Ausgabe der Anzahl der Zeilen im Textfeld
                     borderwidth=5,
                     relief='ridge',
                     yscrollcommand = fenster.scrollbar2.set)

fenster.scrollbar2["command"] = fenster.text3.yview  #Command nach text1 damit scrollbar das attribute 'text2' hat
fenster.text3.grid(row=0, rowspan=2, column=2)
fenster.scrollbar2.grid(row=0, rowspan=2, column=2, sticky = 'ns')

signalname2 = StringVar()
signalname2.set("OffLogCAN2")
fenster.checkbutton2 = Checkbutton(labelframe_widget2,
                                  text = "Logging CAN2",
                                  variable = signalname2,
                                  #borderwidth=3,
                                  #relief='groove',
                                  onvalue = "OnLogCAN2",
                                  offvalue = "OffLogCAN2",
                                  command = sigName2)
fenster.checkbutton2.grid(row=0, rowspan=2, column=3, padx=10, pady=15, sticky=NW)

###################################################################################
##Widget frame_CAN_3
###################################################################################
labelframe_widget3 = LabelFrame( frame_CAN_3,
                                text="Diagnose_CAN",
                                height=widget_hoehe,
                                width=widget_breite,
                                font=('Arial',14) )
labelframe_widget3.grid(row=0, column=0, pady = 5, padx = 10)

fenster.button7 = Button(labelframe_widget3,
                         text='Start CAN_3',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="sizing",
                         command=start_3, # command übergibt die Funktionen
                         bg='green').grid(row=0, column=0, padx=padx_x, pady=pady_y)

fenster.button8 = Button(labelframe_widget3,
                         text='Stop CAN_3',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=stop_3,
                         bg='yellow').grid(row=1, column=0, padx=padx_x, pady=pady_y)

fenster.button_pfad3 = Button(labelframe_widget3,
                         text='DBC-Pfad',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=button_rahmenbreite,
                         relief=button_relief,
                         cursor="dot",
                         command=dateipfad_3,
                         bg='orange').grid(row=0, rowspan=2, column=1, padx=padx_x, pady=pady_y)

##Text-Feld für die Ausgabe des Ergebnisses mit Scrollbar
fenster.scrollbar3 = Scrollbar(labelframe_widget3,
                              orient = "vertical")

fenster.text4 = Text(labelframe_widget3,
                     width = text_breite,
                     height = text_hoehe,   #Ausgabe der Anzahl der Zeilen im Textfeld
                     borderwidth=5,
                     relief='ridge',
                     yscrollcommand = fenster.scrollbar3.set)

fenster.scrollbar3["command"] = fenster.text4.yview  #Command nach text1 damit scrollbar das attribute 'text2' hat
fenster.text4.grid(row=0, rowspan = 2, column=2)
fenster.scrollbar3.grid(row=0, rowspan = 2, column=2, sticky = 'ns')

signalname3 = StringVar()
signalname3.set("OffLogCAN3")
fenster.checkbutton3 = Checkbutton(labelframe_widget3,
                                  text = "Logging CAN3",
                                  variable = signalname3,
                                  #borderwidth=3,
                                  #relief='groove',
                                  onvalue = "OnLogCAN3",
                                  offvalue = "OffLogCAN3",
                                  command = sigName3)
fenster.checkbutton3.grid(row=0, rowspan=2, column=3, padx=10, pady=15, sticky=NW)

###################################################################################
##Widget frame_GUI
###################################################################################
labelframe_widget0 = LabelFrame(frame_GUI,
                                text="Option",
                                font=('Arial',16))
labelframe_widget0.grid(row=0,column=0,pady = 10)

signalnameALL = StringVar()
signalnameALL.set("OffLogCANALL")
fenster.checkbutton = Checkbutton(labelframe_widget0,
                                  text = "Logging CAN ALL",
                                  variable = signalnameALL,
                                  #borderwidth=3,
                                  #relief='groove',
                                  onvalue = "OnLogCANALL",
                                  offvalue = "OffLogCANALL",
                                  command = sigNameALL)
fenster.checkbutton.grid(row=0,column=0, padx=10, pady=15, sticky=NW)


fenster.button0 = Button(labelframe_widget0,
                         text='Start CAN',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=3,
                         relief=b'groove',
                         cursor="sizing",
                         command=start_all,
                         bg='green').grid(row=0, column=1,padx=19, pady=17)

fenster.button01 = Button(labelframe_widget0,
                         text='Stop CAN',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=3,
                         relief=b'groove',
                         cursor="dot",
                         command=stop_all,
                         bg='yellow').grid(row=0, column=2, padx=19, pady=17)

fenster.button000 = Button(labelframe_widget0,
                         text='Beenden',
                         height=button_hoehe,
                         width = button_breite,
                         borderwidth=3,
                         relief=b'groove',
                         cursor="pirate",
                         command=end,
                         bg='red').grid(row=0, column=3, padx=19, pady=17)

###############################################################################
##Statusbar
###############################################################################
fenster.statuscode = Label(fenster,
                            text= 'Statuscode',
                            bd=1,
                            relief = 'sunken',
                            anchor = 'w',
                            fg='red')
fenster.statuscode.grid(row=11, column=0, columnspan=2, sticky=E+W)
###############################################################################                        

# ##Start der Schleife
#fenster.mainloop()