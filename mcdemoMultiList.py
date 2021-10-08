#alex l	
#multi dimension arays

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#creates a line of wool colors
#make a grid of wool colors
woolLine = [13, 12, 5, 2, 4, 8,6,9,10]

woolGrid = [[0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [0, 0, 0, 15,15,15, 0, 0, 0],
            [11,11,11, 5, 0, 5, 11,11,11],
            [11,11,11, 0, 0, 0, 11,11,11],
            [11,11,11, 0, 0, 0, 11,11,11]]
            
            
            
            
           
#gets pos
pos = mc.player.getTilePos()
#this loop will place a line of wool

'''
for i, wool in enumerate(woolLine):
    print(str(i) + " is the color " + str(wool))
    mc.setBlock(pos.x + 1, pos.y, pos.z + i, 35, wool)
    '''
#this will print a grid of wool block
for i, row in enumerate(woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x + j, pos.y + i , pos.z , 35, col)

