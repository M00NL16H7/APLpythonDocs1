#alex L

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.player.getPos()
mc.postToChat(mc.player.getPos())
