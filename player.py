

player = FirstPersonController(
    collider='sphere', position=(0, 65, -10)
)
player.speed = player.speed * 2.5

levelDisplay = Text(
    color=color.blue, scale=2, origin=(-8.8, 9))
levelDisplay.text = "HP:"
hpDisplay = Text(
    color=color.white, scale=3, origin=(-18, 6))
hpDisplay.text = health
levelDisplay = Text(
    color=color.black, scale=2, origin=(-4.2, -9))
levelDisplay.text = "LEVEL:"
lvlhpDisplay = Text(
    color=color.black, scale=3, origin=(-18, -6))
lvlhpDisplay.text = lvl


def input(key):
    if key == 'q':
        quit()
    if key == 'space':
        if not jump.playing:
            jump.play()
        destroy(t)
        destroy(t2)
        destroy(t3)
    if key == 'enter':
        if not jump.playing:
            jump.play()
        destroy(t)
        destroy(t2)
        destroy(t3)
