global checkPoint03
destroy(checkPoint03)

lvlhpDisplay.text = lvl


# ENEMY AI
with open('enemy01AI.py', 'r') as file:
    file_enemy01ai = file.read()
    exec(file_enemy01ai)
# ENEMY AI ENDS
