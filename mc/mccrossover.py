#alex L
#Four Buttons One LED

#import MC

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

#use module for requesting data online

import requests

#use a module to control time

import time 

#setup for buttons and LED's
#^^^^^^
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
#setup each PIN number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#start infinte loop
while True:
    #wait for one second
    #time.sleep(1)
    #check first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed")
        mc.player.getPos()
        mc.postToChat(mc.player.getPos())
    elif GPIO.input(13) == GPIO.LOW:
        print("button 13 was pressed")
    elif GPIO.input(19) == GPIO.LOW:
        print("button 19 was pressed")
    elif GPIO.input(26) == GPIO.LOW:
        print("button 26 was pressed")