global lvl
global checkPoint01
global checkPoint02
global enemy01

destroy(checkPoint01)


if player.intersects(checkPoint02) and lvl == 2:
    magicWand.play()
    lvl = 3

# ENEMY AI
with open('enemy01AI.py', 'r') as file:
    file_enemy01ai = file.read()
    exec(file_enemy01ai)
# ENEMY AI ENDS
