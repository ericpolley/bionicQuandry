global checkPoint01
global enemy1
global lvl3serporaterWall
# these buildings are in front of you at start
building001 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(-10, 3, 35), collision=True)

building002 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(20, 3, 35), collision=True)

building003 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(-10, 3, 55), collision=True)

building004 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(20, 3, 55), collision=True)

# these buildings are behind you at start
building005 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(-10, 3, -22), collision=True)

building006 = Entity(model='cube', texture='brick', texture_scale=(10, 10), scale=(
    20, 25, 15), collider='box', position=(20, 3, -22), collision=True)

# this wall is behind you when you start the game
lvl10serporaterWall = Entity(model='cube', texture='brick', color=color.gray, texture_scale=(10, 10), scale=(
    220, 21, 1), collider='box', position=(5, 10, -36), collision=True)
# This is the big wall infront of you
lvl3serporaterWall = Entity(model='cube', texture='brick', color=color.gray, texture_scale=(10, 10), scale=(
    220, 21, 1), collider='box', position=(5, 10, 80), collision=True)


# Create the wall entities
lvl0wall = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(1, 21, 200),
                  collider='box', position=(30, 10, 0))

lvl0wall2 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(1, 21, 200),
                   collider='box', position=(-20, 10, 0))

lvl1wall = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(1, 21, 200),
                  collider='box', position=(100, 10, 0))

lvl1wall2 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(1, 21, 200),
                   collider='box', position=(-100, 10, 0))

lvl1wall3 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(200, 21, 1),
                   collider='box', position=(0, 10, 100))

lvl1wall4 = Entity(model='cube', color=color.gray, texture="brick", texture_scale=(8, 10), scale=(200, 21, 1),
                   collider='box', position=(0, 10, -100))

# first check[oint. starts lv 2
checkPoint01 = Entity(model='cube', color=color.green, scale=(
    5, 1, 5), collider='box', position=(0, 0, 5))
