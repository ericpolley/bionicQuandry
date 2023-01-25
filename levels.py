global lvl  # Robot
level01loaded = False
level02loaded = False
level03loaded = False
level04loaded = False


with open('lv0entities.py', 'r') as file:
    file_lv0 = file.read()
    exec(file_lv0)


def update():
    global level04loaded
    global level03loaded
    global level02loaded
    global level01loaded

    # NEW LEVEL
    if lvl == 1:
        if level01loaded == False:
            with open('lv01entities.py', 'r') as file:
                file_entities01 = file.read()
                exec(file_entities01)
                level01loaded = True

        with open('lv01.py', 'r') as file:
            file_lv01 = file.read()
            exec(file_lv01)

# NEW LEVEL
    if lvl == 2:
        if level02loaded == False:
            with open('lv02entities.py', 'r') as file:
                file_entities2 = file.read()
                exec(file_entities2)
                level02loaded = True
        if level02loaded == True:
            with open('lv02.py', 'r') as file:
                file_lv02 = file.read()
                exec(file_lv02)

    if lvl == 3:
        if level03loaded == False:
            with open('lv03entities.py', 'r') as file:
                file_entities3 = file.read()
                exec(file_entities3)
                level03loaded = True
        if level03loaded == True:
            with open('lv03.py', 'r') as file:
                file_lv02 = file.read()
                exec(file_lv02)
    if lvl == 4:
        if level04loaded == False:
            with open('lv04entities.py', 'r') as file:
                file_entities4 = file.read()
                exec(file_entities4)
                level04loaded = True
        if level04loaded == True:
            with open('lv04.py', 'r') as file:
                file_lv04 = file.read()
                exec(file_lv04)


# player controls
walking = held_keys['a'] or \
    held_keys['d'] or \
    held_keys['s'] or \
    held_keys['w']
if walking and player.grounded:
    if not walk.playing:
        walk.play()
