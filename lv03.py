# WIN
global lvl
global enemy1
global checkPoint02
global checkPoint03

destroy(checkPoint02)
destroy(lvl3serporaterWall)
lvlhpDisplay.text = lvl


if player.intersects(checkPoint03) and lvl == 3:
    magicWand.play()
    lvl = 4

# ENEMY AI
with open('enemy01AI.py', 'r') as file:
    file_enemy01ai = file.read()
    exec(file_enemy01ai)
# ENEMY AI ENDS
