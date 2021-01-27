from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()
for i in range(0,20):
    cherinehsu.setBlock(x+i+1,y-1,z+i,57)
    cherinehsu.setBlock(x+i+2,y-1,z+i,57)
    cherinehsu.setBlock(x+i+3,y-1,z+i,57)
