# You are a member of a small game company specializing in text adventure games. 
# This sprint, you have been tasked with writing the battle engine for the latest title.
# Both the Hero and the Monster start with the same number of hitpoints
# Each time the user presses the enter button, the Hero attacks the monster
# The amount of damage and remaining hitpoints are displayed
# After the monster is attacked, it attacks the Hero, with damage and remaining hitpoints being displayed
# Once either the Hero or the monster dip below 1 hitpoint, they are declared dead and the winner is displayed
# HINT: Research the random.randrange library
# Extra Credit: If the Hero uses a weapon, modify the damage algorithm accordingly
# --------------------------------------------------------------------
# Track Player stats using a Player class
# Track NPC (or Monster) stats by subclassing Player and adding some customizations
# Present a working proof-of-concept for Roger's battle engine that includes loot drops
# Each battle features items looted from the previous battle as weapon choices
"test comment"
"""MVP task list: 
done - weapon selection
done - hero attacking monster
z - monster attacking hero
done - hero dies, end program
z - monster dies, drops loot (weapon)
r - updating hero inventory with loot drop (weapon)
r - monster dies, new monster to fight """


import random                                                           # import random for randomized calculations
from stats4 import Player, Opponent                                      # importing player and opponent classes

# function where the hero (user) selects the weapon to be used in the battle with the monster
def hero_weapon_selection():
    print("Debug - Moved into the hero_weapon_selection function" + "\n")
    inventory_position = 1
    
    if not hero.inventory:
        print("All you've got is a sword, so use it.")
        
        return None
    
    print("Inventory: ")
    for each in hero.inventory:
        print(str(inventory_position) + ". " + each["type"])
        inventory_position = inventory_position + 1

    hero_input = input("Enter the number of your weapon of choice: ")
    while hero_input == "":
        print("The enemy approaches, you need to choose your weapon!")
        hero_input = input("Enter the number of your weapon of choice: ")
        continue

    hero.weapon = hero.inventory[int(hero_input) - 1]
    print("Debug - selected weapon is " + str(hero.weapon["type"]))

    return None

# function that captures the hero's damage dealt
def hero_attack():                                                      
    hero_damage = hero.damage_dealt()
    monster.health = monster.health - hero_damage
    print("Debug - Monster's health should be: " + str(monster.health))
    print("Debug - hero dmg dealt is " + str(hero_damage))

    return monster.health

# function that captures the monster's damage dealt
def monster_attack():
    monster_weapon = monster.opponent_weapon()
    monster.weapon = [monster_weapon]
    monster_damage = monster.damage_dealt()
    hero.health = hero.health - monster_damage
    print("Debug - Hero's health should be: " + str(hero.health))

    return hero.health


if __name__ == "__main__":
    hero = Player()                                                         # creates hero object from Player class
    monster = Opponent()                                                    # creates monster object from Opponent subclass
    
    print("Debug - Player hp is " + str(hero.health))
    print("Debug - Monster hp is " + str(monster.health))
    

    # while hero.health > 0 and monster.health > 0:                         # loop until hit points drop below zero
    hero_weapon_selection() 
    hero_attack()   
    monster_attack()                                             # hero selects weapon

    print("Debug - hero weapon is " + hero.weapon["type"])
    print("Debug - hero damage is " + str(hero.weapon["dmg"]))
    print("Debug point - stopping")