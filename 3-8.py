def plantTree(x,y,z):
    cherinehsu.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    cherinehsu.setBlocks(x,y,z,x,y+4,z,17)
    
from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
x,y,z = cherinehsu.player.getTilePos()

for i in range(height):
    for j in range(8):
        for k in range(10):
            plantTree(x+i*5,y+j*8,z+k*5)