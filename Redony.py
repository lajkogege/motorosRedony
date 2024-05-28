#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class RedonyLampa():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        #self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        #self.ts = TouchSensor(Port.S1)
        #self.gs = GyroSensor(Port.S2)
        #self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő


  
        
    def redonyMozgat(self):
        while (True):
            #ambientre kell hivatkozni nem a logikaira
            if(self.cs.ambient()>50): #ambient példányositása nem lenne rosz ötlet majd
                self.jm.run(200)
                self.jm.stop(Stop.BRAKE)
                print("Fel mozgat")
            else:
                self.jm.run(200)
                self.jm.stop(Stop.BRAKE)  
                print("Le mozgat")
                
#majd lesz erre vezérlő, meg lesz oldva
    def lampa(self):
        while(True):
            if(self.cs.ambient() > 50):
                self.ev3.speaker.beep();
                print("Villany felkapcsolva")
            else:
                self.ev3.speaker.beep();
                print("Villany lekapcsolva")        
        
        
        
#     def felMozgat():
#         while not self.ts.pressed():
#         self.km.run(200)
#         self.km.stop(Stop.BRAKE)
#         print("Fel mozgat")

#   def leMozgat():
#         while not self.cs.color(20):
#             self.km.run(200)
#             self.km.stop(Stop.BRAKE)
#             print("Le mozgat")

