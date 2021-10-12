#alex l
#places a randomly colored wool block
#square brackets = list
mcChest = ['sword', 'pickaxe', 'wool']
'''Set uo prgram for MC and two buttons
create a counter variable that starts at 0
create a list of blockdata numbers for different wool color
define a fucntion called place next
	it takes a argumebt called direction
	it changes the counter by adding the directuion arugemnt,=
	place wool block of the color from the list where the index matches the variable counter
	if the ounter is out of bounds of the index, rest it
in a forver loop
	if first button wsa pressed, placeNext(1)
	if second button was pressed, placeNext( 1)
	'''
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
GPIO.setup(13,6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
counter = 0
woolColors = [6,5,10,9,3,2]

def placeNext(direction):
	tpos = mc.player.getTilePos()
	global counter
	counter += direction
	if counter < 0:
		counter = 5
	elif counter > 5:
		counter = 0
	else: 
		pass
    mc.setBlock(tpos.x + 1, tpos.y, tpos.x, 35,woolColors[counter])
	while True:
        if GPIO.input(6) == GPIO.LOW:
            placeNext(1)
		
	  
	
