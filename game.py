""" 
# After your band-name generator was a wild success, your record label decided it was cheaper to just keep your program and fire you. Touting nascent but solid Python skills, you landed a job at a “game studio” specializing in “classic playstyles” working out of “Roger’s basement”. His company is on the verge of creating a technical revolution, “just like those guys from Apple or Atari or whatever.” Roger claims to be designing the greatest text adventure game ever build, “like D&D but on the computer.” You decide not to inform Roger that there are basically hundreds of D&D games on computer because, frankly, you need the money. You have seen his code, and while passable, you think you could use Object Oriented Programming (OOP) to make his code cleaner and more expressive.

# Track Player stats using a Player class
# Track NPC (or Monster) stats by subclassing Player and adding some customizations
# Present a working proof-of-concept for Roger’s battle engine that includes loot drops
# Each battle features items looted from the previous battle as weapon choices 
"""
from stats3 import Player, Opponent

hero = Player()
monster = Opponent()
opp_weapon = monster.opponent_weapon()
print("This is the opponents current weapon: " + str(opp_weapon))
#test = monster.damage_dealt()
#print(hero.damage_dealt())
#print(hero.damage_taken(test))
#print(hero.health)
print("This is the heros loot weapon: " + str(hero.player_inventory_update(opp_weapon)))
print(monster.get_opponent_money())
print(hero.weapon)
