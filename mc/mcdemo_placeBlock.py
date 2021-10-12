from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#get player tile pos and save to a var
#tile positon 
while True:
    tpos = mc.player.getTilePos()
    mc.setBlock(tpos.x + 15, tpos.y - 12,tpos.z, 16)
    mc.setBlock(tpos.x + 14, tpos.y - 11,tpos.z, 16)
    mc.setBlock(tpos.x + 13, tpos.y - 10,tpos.z, 16)
    mc.setBlock(tpos.x + 12, tpos.y - 9,tpos.z, 16)
    mc.setBlock(tpos.x + 11, tpos.y - 8,tpos.z, 16)
    mc.setBlock(tpos.x + 10, tpos.y - 7,tpos.z, 16)
    mc.setBlock(tpos.x + 9, tpos.y - 6,tpos.z, 16)
    mc.setBlock(tpos.x + 8, tpos.y - 5,tpos.z, 16)
    mc.setBlock(tpos.x + 7, tpos.y - 4,tpos.z, 16)
    mc.setBlock(tpos.x + 6, tpos.y - 3,tpos.z, 16)
    mc.setBlock(tpos.x + 5, tpos.y - 2,tpos.z, 16)
    mc.setBlock(tpos.x + 4, tpos.y - 1,tpos.z, 16)
    mc.setBlock(tpos.x + 3, tpos.y - 0,tpos.z, 16)
    mc.setBlock(tpos.x + 2, tpos.y - -1,tpos.z, 16)
    mc.setBlock(tpos.x + 1, tpos.y - -2,tpos.z, 16)