from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

while True:
    hits = cherinehsu.events.pollProjectileHits()
    if len(hits) > 0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        cherinehsu.createExplosion(x,y,z,power=100)