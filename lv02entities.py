
global enemy1
global checkPoint02

checkPoint02 = Entity(model='sphere', color=color.green, scale=(
    1, 1, 1), collider='box', position=(5, 3.2, 70))
checkPoint02stand = Entity(model='cube', color=color.gray, scale=(
    6, .8, 6), collider='box', position=(5, .4, 70))

enemy1 = Entity(model='/objects/kill.obj', texture='/objects/kill.mtl', texture_scale=(1, 1), scale=(1, 1, 1),
                position=(5, 2.5, 75), collider='box', collision=True)
