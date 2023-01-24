# WIN
global lvl

# if player.x > -5 and player.x < 5 and player.y > 11 and player.z > 56 and player.z < 60 and lvl == 1:
if player.intersects(checkPoint01) and lvl == 1:
    magicWand.play()
    lvl = 2
