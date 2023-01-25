import math
import time


# ENEMY AI
distance = math.sqrt((player.x - enemy1.x)**2 + (player.y -
                                                 enemy1.y)**2 + (player.z - enemy1.z)**2)
# if enemy1 gets too far on the z axis, add 2 to the z axis.
if enemy1.z < 11:
    enemy1.z = enemy1.z + 2
if distance < 40 and enemy1.z > 10:
    # Move the enemy1 towards the player
    enemy1.position = lerp(
        enemy1.position, player.position, time.dt * .45)
# enemy collison group
enemy1.collision_group = "Enemy"
# Keeps the Enemy off of the floor
if enemy1.y < ground.y + 1.6:
    enemy1.y = ground.y + 1.6
if enemy1.intersects(player):
    with open('enemyAttack.py', 'r') as file:
        file_enemyAttack = file.read()
        exec(file_enemyAttack)
        level01loaded = True

    if not punchy.playing:
        punchy.play()
# look at the player at all times
player_xz = player.position
player_xz.y = enemy1.position.y
enemy1.look_at(player_xz)


# ENEMY AI ENDS
