global checkPoint01
global enemy1
global lvl3serporaterWall


# this wall is behind you when you start the game
lvl10serporaterWall = Entity(model='cube', texture='brick', color=color.gray, texture_scale=(64, 10), scale=(
    220, 21, 1), collider='box', position=(5, 10, -36), collision=True)
# This is the big wall infront of you
lvl3serporaterWall = Entity(model='cube', texture='brick', color=color.gray, texture_scale=(64, 10), scale=(
    220, 21, 1), collider='box', position=(5, 10, 80), collision=True)


# Create the wall entities
lvl0wall = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(1, 21, 200),
                  collider='box', position=(30, 10, 0))

lvl0wall2 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(1, 21, 200),
                   collider='box', position=(-20, 10, 0))

lvl1wall = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(1, 21, 200),
                  collider='box', position=(100, 10, 0))

lvl1wall2 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(1, 21, 200),
                   collider='box', position=(-100, 10, 0))

lvl1wall3 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(200, 21, 1),
                   collider='box', position=(0, 10, 100))

lvl1wall4 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(64, 10), scale=(200, 21, 1),
                   collider='box', position=(0, 10, -100))

# first check[oint. starts lv 2
checkPoint01 = Entity(model='sphere', color=color.green, scale=(
    1, 1, 1), collider='box', position=(0, 3.2, 5))

checkPoint01stand = Entity(model='cube', color=color.gray, scale=(
    6, .8, 6), collider='box', position=(0, .4, 5))
