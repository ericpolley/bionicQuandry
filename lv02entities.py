
global enemy1
global checkPoint02

checkPoint02 = Entity(model='cube', color=color.green, scale=(
    5, 1, 5), collider='box', position=(5, 0, 70))

enemy1 = Entity(model='/kill.obj', texture='/kill.mtl', scale=(1, 1, 1),
                position=(5, 2, 70), collider='box', collision=True)
