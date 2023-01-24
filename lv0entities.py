

ground = Entity(model='plane', texture='grass', color=color.gray, texture_scale=(50, 50),
                collider='mesh', scale=(250, 1, 250))

startCube = Entity(model='cube', color=color.gold, texture="metal", texture_scale=(8, 10), scale=(4, .8, 4),
                   collider='box', position=(0, 0, -10))

sky = Sky(color=color.white)
