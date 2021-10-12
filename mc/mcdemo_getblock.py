#alex l
#
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = mc.player.getTilePos

while True:
    if GPIO.input(6) == GPIO.LOW:
        p = mc.player.getTilePos()
        block = mc.getBlock(p.x, p.y - 1, p.z)
        mc.postToChat(block)
        if block == int(57):
            mc.player.setPos(p.x, p.y + 20, p.z)
        