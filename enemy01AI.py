import math
import time


# ENEMY AI
distance = math.sqrt((player.x - enemy1.x)**2 + (player.y -
                                                 enemy1.y)**2 + (player.z - enemy1.z)**2)
# if enemy1 gets too far on the z axis, add 2 to the z axis.
if enemy1.z < 11:
    enemy1.z = enemy1.z + 2
if distance < 50:
    # Move the enemy1 towards the player
    enemy1.position = lerp(
        enemy1.position, player.position, time.dt * .45)
# ATTACK
if enemy1.intersects(player):
    enemy1.y = enemy1.y + 5
    if enemy1.x < player.x:
        enemy1.x = enemy1.x - 15
    if enemy1.x > player.x:
        enemy1.x = enemy1.x + 15
    if enemy1.z < player.z:
        enemy1.z = enemy1.z - 15
    if enemy1.z > player.z:
        enemy1.z = enemy1.z + 15

    with open('hp.py', 'r') as file:
        hp = file.read()
        exec(hp)

    if not punchy.playing:
        punchy.play()
# look at the player at all times
player_xz = player.position
player_xz.y = enemy1.position.y
enemy1.look_at(player_xz)

# Keeps the Enemy off of the floor
if enemy1.y < ground.y + 1.6:
    enemy1.y = ground.y + 1.6


# ENEMY AI ENDS
