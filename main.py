from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController
from random import uniform
app = Ursina()
window.fullscreen = True

lvl = 1

# Music
with open('audio.py', 'r') as file:
    file_audio = file.read()
    exec(file_audio)

with open('player.py', 'r') as file:
    file_player = file.read()
    exec(file_player)

    # Update game
with open('levels.py', 'r') as file:
    file_levels = file.read()
    exec(file_levels)


app.run()
