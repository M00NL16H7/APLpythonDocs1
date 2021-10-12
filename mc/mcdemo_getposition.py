#alex l
#get position in mc

#load in mc modules
#get players pos and store it in a var, and then have the variable repeat in chat

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()

mc.postToChat(pos)
mc.postToChat("Your X pos is" + str(pos.x))
mc.postToChat("Your Y pos is" + str(pos.y))
mc.postToChat("Your Z pos is" + str(pos.z))