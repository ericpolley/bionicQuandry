# WIN
global lvl
global enemy1
global checkPoint02

destroy(checkPoint02)
destroy(lvl3serporaterWall)


# ENEMY AI
with open('enemy01AI.py', 'r') as file:
    file_enemy01ai = file.read()
    exec(file_enemy01ai)
# ENEMY AI ENDS
