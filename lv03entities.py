
global enemy1
global checkPoint03

checkPoint03 = Entity(model='sphere', color=color.green, scale=(
    1, 1, 1), collider='box', position=(25, 4.9, 95))
checkPoint03stand = Entity(model='cube', color=color.gray, scale=(
    6, .25, 6), collider='box', position=(25, 2.6, 95))

step2 = Entity(model='cube', color=color.brown, texture='brick', text_scale=(3, 3), scale=(
    6, 3, 6), collider='box', position=(25, 1, 95))

step1 = Entity(model='cube', color=color.brown, texture='brick', text_scale=(3, 3), scale=(
    5, 3, 5), collider='box', position=(18, 0.5, 95))
