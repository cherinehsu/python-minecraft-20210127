from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

while True:
    hits = cherinehsu.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = cherinehsu.getBlock(x,y,z)
        print(type(block))
        cherinehsu.postToChat("你打到了"+str(block))
        if block == 1:
            cherinehsu.setBlock(x,y,z,14)