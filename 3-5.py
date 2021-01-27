from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()
for i in range(0,20):
    cherinehsu.setBlock(x,y-1,z+i,57)