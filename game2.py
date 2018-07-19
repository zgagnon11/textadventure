import random 
import time                                                             # import random for randomized calculations
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

# function that captures the hero's damage dealt and updates the monsters health
def hero_attack():                                                      
    hero_damage = hero.damage_dealt()
    monster.health = monster.damage_taken(hero_damage)
    print("Hero hit for " + str(hero_damage))
    
    return None

# function that captures the monster's damage dealt and updated the heros health
def monster_attack():
    monster_damage = monster.damage_dealt()
    hero.health = hero.damage_taken(monster_damage)

    print("Monster hit back for " + str(monster_damage))
    print()
    print("Hero HP: " + str(hero.health) + "      " + "Monster HP: " + str(monster.health)) # display hero and monster hp
    print("----------------------------")
    print()
    #time.sleep(.5)
    
    return None

# function to iterate through the hero/monster battle
def do_battle():
    while hero.health > 0 and monster.health > 0:                           # loop until hit points drop below zero 
        hero_attack()  
        monster_attack() 
        time.sleep(.5)

    return None


if __name__ == "__main__":
    hero = Player()                                                         # creates hero object from Player class
    monster = Opponent()                                                   # creates monster object from Opponent subclass
        
    hero_weapon_selection()                                                 # player selects hero's weapon
    do_battle()                                                             # invoke the battle function

    print("_______________________________")

    while hero.health > 0:
        print("You've won!" + "\n" + "The monster dropped " + str(monster.weapon))
        print("You take it as the spoils of war, and stow it in your pack.")

        # hero.inventory.append(monster.weapon)
        hero.player_inventory_update(monster.weapon)

        print("Looks like you're hurt, you need a healing potion..." + "\n")
        # hero.health = hero.health + random.randrange(30,70)
        hero.health = 100
        print("Your health is now " + str(hero.health) + "\n")
   
        print("Head's up, here comes the next monster.  Bash it!")
        # monster.health = random.randrange(40,70)
        monster.health = random.randrange(30, 70)

        hero_weapon_selection()
        monster.opponent_weapon()
        print(monster.opponent_weapon()) 
        do_battle()

        continue

    else:
        print("The monster's beaten you.  It's dancing on your fallen corpse, and taking all your stuff.")


    print("Debug point - the hero's dead, stopping")
#test