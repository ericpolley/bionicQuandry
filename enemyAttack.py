global health
health = health - 1
hpDisplay.text = health
if health < 2:
    # player starts back at the beginning
    player.position = (0, 6, -10)
    player.rotation = (0, 0, 0)
    health = 5
    hpDisplay.text = health
