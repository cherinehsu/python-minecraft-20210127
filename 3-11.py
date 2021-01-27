from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

x,y,z = cherinehsu.player.getTilePos()

number = 1

for i in range(8):
    for j in range(number):
        cherinehsu.spawnEntity(x,y,z,60)
    number = number*2

    cherinehsu.postToChat("生成了"+str(number)+"隻蠹魚")  