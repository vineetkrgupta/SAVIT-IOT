import requests
# This example is a hello world example
# for using a keypad with the Raspberry Pi

import RPi.GPIO as GPIO
import time

# C1 = 15
# C2 = 16
# C3 = 1
# C4 = 4

# L1 = 5
# L2 = 6
# L3 = 10
# L4 = 11


L1 = 26
L2 = 19
L3 = 13
L4 = 6

C1 = 5
C2 = 11
C3 = 9
C4 = 10
down=0


url = "http://192.168.43.199:3000/press"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    #print(line, characters)
    global down
    GPIO.output(line, GPIO.HIGH)
    if(down==0):
        if(GPIO.input(C1) == 1):
            print(characters[0])
        if(GPIO.input(C2) == 1):
            print(characters[1])
        if(GPIO.input(C3) == 1):
            print(characters[2])
        if(GPIO.input(C4) == 1):
            print(characters[3])
        if(GPIO.input(C4) ==1 or GPIO.input(C3)==1 or GPIO.input(C2)==1 or GPIO.input(C1)==1):
            requests.get(url)
            down= 1
    if(GPIO.input(C4) ==0 and  GPIO.input(C3)==0 and GPIO.input(C2)==0 and GPIO.input(C1)==0):
        down=0
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.6)
        #requests.get(url)
except KeyboardInterrupt:
    print("\nApplication stopped!")