

ground = Entity(model='cube', texture='grass', color=color.gray, texture_scale=(50, 50),
                collider='mesh', scale=(250, .01, 250))

startCube = Entity(model='cube', color=color.gold, texture="white_cube", texture_scale=(1, 1), scale=(5, .2, 5),
                   collider='box', position=(0, 1, -10))

startCubeUnder = Entity(model='sphere', color=color.gold, texture_scale=(1, 1), scale=(4, .1, 4),
                        collider='box', position=(0, .63, -10))

startCubeUnder2 = Entity(model='sphere', color=color.gold, texture_scale=(1, 1), scale=(3, .1, 3),
                         collider='box', position=(0, .3, -10))

sky = Sky(color=color.white)

# these buildings are in front of you at start
tree5 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .4, .4, .4), collider='mesh', position=(-2, 0, 35), rotation=(0, 170, 0), collision=True)

tree4 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .5), collider='mesh', position=(20, 0, 35), rotation=(0, 100, 0), collision=True)

tree6 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .4, .4, .4), collider='mesh', position=(-12, 0, 40), rotation=(0, 0, 0), collision=True)

tree7 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .5), collider='mesh', position=(15, 0, 30), rotation=(0, 130, 0), collision=True)

tree8 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .5), collider='mesh', position=(0, 0, 45), rotation=(0, 50, 0), collision=True)
tree9 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .5), collider='mesh', position=(8, 0, 38), rotation=(0, 120, 0), collision=True)

building002 = Entity(model='objects/building.obj', texture='objects/building.obj', rotation=(0, 90, 0), texture_scale=(1, 1), scale=(
    1, 1, 1), collider='mesh', position=(-2, 0, 55), collision=True)

tree3 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .45), collider='mesh', position=(20, 0, 55), rotation=(0, 150, 0), collision=True)

# these buildings are behind you at start
building001 = Entity(model='objects/building.obj', texture='objects/building.obj',  rotation=(0, 30, 0), texture_scale=(1, 1), scale=(
    1, 1, 1), collider='box', position=(-2, 0, -22), collision=True)

tree1 = Entity(model='objects/tree.obj', texture='objects/tree.obj', texture_scale=(1, 1), scale=(
    .5, .5, .6), collider='mesh', position=(20, 0, -22), rotation=(0, 180, 0), collision=True)

global t, t2, t3
t = Text('Use A S D and W to walk,',
         color=color.white, scale=3, origin=(0, -1))
t2 = Text('Use the mouse to Look Around',
          color=color.white, scale=3, origin=(0, 0))
t3 = Text('Press space To Jump',
          color=color.white, scale=3, origin=(0, 1))
