#!usr/bin/env python3

import rpyc
from rpyc.utils.server import ThreadedServer
from ev3dev2.motor import MoveTank,OUTPUT_B,OUTPUT_C , MediumMotor, OUTPUT_D
                                                                           

class Ev3Car(rpyc.Service):

    def __init__(self):
    
        self.My_Tank = MoveTank(OUTPUT_B,OUTPUT_C)
        self.Control = MediumMotor(OUTPUT_D)
    
    def status_check(self):
        self.Control.position = 0;

    def exposed_run(self):
        
        self.My_Tank.on(-60,-60)

    def exposed_back(self):
        
        self.My_Tank.on(30,30)    
    
    def exposed_stop(self):
        
        self.My_Tank.off()    

    def exposed_steering(self,degree=0):

        self.Control.on_for_degrees(30,degree,True,True)
    


if __name__ == '__main__':
    while input("Input 'start' for starting ") == 'start':
        s = ThreadedServer(Ev3Car, port=18812)
        s.start()
        print(s.listener)
    else :
        exit() 

