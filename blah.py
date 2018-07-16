from random import randrange
import time


phealth = 100
opp_health = 100

while phealth > 0 and opp_health > 0:
    player_dmg = randrange(10)
    opp_health = opp_health - player_dmg
    print("Player hit opponent for: " + str(player_dmg))
    print("Opponent health: " + str(opp_health))
    time.sleep(.5)

    opp_dmg = randrange(10)
    phealth = phealth - opp_dmg
    print("Opponent hit PLayer for: " + str(player_dmg))
    print("Player health: " + str(phealth))
    time.sleep(.5)

if phealth > 0:
    print("the player is the winner")
else:
    print("the opponent won")

    
    