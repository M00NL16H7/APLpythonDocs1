#alex L
#Build House
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
GPIO.setup(13,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
#start infinte loop


while True:
    #wait for one second
    #time.sleep(1)
    #check first button
    hpos = mc.player.getTilePos()
    if GPIO.input(13) == GPIO.LOW:
		mc.setBlocks(hpos.x + 1 ,hpos.y,hpos.z,hpos.x + 10, hpos.y + 6, hpos.z + 15, 5)
		mc.setBlocks(hpos.x + 2 ,hpos.y + 1,hpos.z + 1,	hpos.x + 9, hpos.y + 5, hpos.z + 14, 0) 
		mc.setBlocks(hpos.x + 3, hpos.y + 1, hpos.z, hpos.x + 3, hpos.y + 2, hpos.z + 1, 64)
		mc.setBlocks(hpos.x + 4, hpos.y + 1, hpos.z + 4, hpos.x, hpos.y, hpos.z)
		
		
