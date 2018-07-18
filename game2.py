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

"""MVP task list: 
done - weapon selection
done - hero attacking monster
done - monster attacking hero
done - iterate through battle
done - monster dies, drops loot (weapon)
done - updating hero inventory with loot drop (weapon)
done - monster is dead, new battle begins
done - hero dies, end program """


import random                                                           # import random for randomized calculations
from stats4 import Player, Opponent                                     # importing player and opponent classes

# function where the hero (user) selects the weapon to be used in the battle with the monster
def hero_weapon_selection():
    print("Weapon selection time!")
    
    if not hero.inventory:                                              # use default weapon if hero inventory is empty
        print("Looks like all you've got is a sword, so use it.")
        hero.inventory.append(hero.weapon)
        
        return None
    
    hero_inventory()                                                    # display the hero's inventory

    hero_input = input("Enter the number of your weapon of choice: ")
    while hero_input == "":
        print("The enemy approaches, you need to choose your weapon!")
        hero_input = input("Enter the number of your weapon of choice: ")
        continue

    hero.weapon = hero.inventory[int(hero_input) - 1]                   # set hero weapon to the user selection

    return None

# function to display the hero's inventory 
def hero_inventory():
    inventory_position = 1

    print("Inventory: ")
    for each in hero.inventory:
        print(str(inventory_position) + ". " + each["type"])
        inventory_position = inventory_position + 1

    return None

# function that captures the hero's damage dealt
def hero_attack():                                                      
    hero_damage = hero.damage_dealt()
    monster.health = monster.damage_taken(hero_damage)
    # print("Debug - hero dmg dealt is " + str(hero_damage))
    # print("Debug - Monster's health should be: " + str(monster.health))
    print("Hero hit for " + str(hero_damage))
    
    return None

# function that captures the monster's damage dealt
def monster_attack():
    monster.opponent_weapon()
    monster_damage = monster.damage_dealt()
    hero.health = hero.damage_taken(monster_damage)

    print("Monster hit back for " + str(monster_damage))
    print()
    print("Hero HP: " + str(hero.health) + "      " + "Monster HP: " + str(monster.health)) # display hero and monster hp
    print("----------------------------")
    print()
    
    return None

# function to iterate through the hero/monster battle
def do_battle():
    while hero.health > 0 and monster.health > 0:                           # loop until hit points drop below zero 
        hero_attack()   
        monster_attack() 

    return None


if __name__ == "__main__":
    hero = Player()                                                         # creates hero object from Player class
    monster = Opponent()                                                    # creates monster object from Opponent subclass
        
    hero_weapon_selection()                                                 # player selects hero's weapon
    do_battle()                                                             # invoke the battle function

    print("_______________________________")

    while hero.health > 0:
        print("You've won!" + "\n" + "The monster dropped " + str(monster.weapon))
        print("You take it as the spoils of war, and stow it in your pack.")

        hero.inventory.append(monster.weapon)

        print("Looks like you're hurt, you need a healing potion..." + "\n")
        # hero.health = hero.health + random.randrange(30,70)
        hero.health = 100
        print("Your health is now " + str(hero.health) + "\n")
   
        print("Head's up, here comes the next monster.  Bash it!")
        # monster.health = random.randrange(40,70)
        monster.health = 50

        hero_weapon_selection()
        do_battle()

        continue

    else:
        print("The monster's beaten you.  It's dancing on your fallen corpse, and taking all your stuff.")


    print("Debug point - the hero's dead, stopping")