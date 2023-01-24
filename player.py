player = FirstPersonController(
    collider='box', position=(0, 6, -10)
)
player.speed = player.speed * 2.5


def input(key):
    if key == 'q':
        quit()
    if key == 'space':
        if not jump.playing:
            jump.play()
