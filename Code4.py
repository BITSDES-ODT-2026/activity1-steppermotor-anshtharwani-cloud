from machine import Pin
import time

list = [[1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1],[1,0,0,0]]

in1= Pin(14, Pin.OUT)
in2= Pin(25, Pin.OUT) 
in3= Pin(32, Pin.OUT)
in4= Pin(27, Pin.OUT)
pb = Pin(33, Pin.IN,Pin.PULL_UP)
pb1 = Pin(18 , Pin.IN,Pin.PULL_UP)

sleep = 0.003

while True:


    pb_value = pb.value()
    pb1_value = pb1.value()


    if pb_value == 0:
        for i in list:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            
            time.sleep(sleep)
            
    if pb1_value == 0:
        for i in reversed(list):
            
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
                
            time.sleep(sleep)
    






