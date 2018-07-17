import random

#Class that holds all the default stats for the Player and NPC's/Opponents
#Holds methods for shared functionality like dealing damage and taking damage etc.
class Entities:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.stamina = 100
        self.mana = 20
        self.inteligence = 20
        self.wisdom = 10
        self.charisma = 500
        self.inventory = []
        self.weapon = {}
        self.money = 0

    #Calculates the damage dealt using the strength and the randomized weapon value range
    def damage_dealt(self):
        damage = self.strength + random.randrange(self.weapon["dmg"])

        return damage

    #Calculates the damage taken using the strength and the randomized weapon value range
    def damage_taken(self, damage):
        self.health = self.health - damage

        return self.health


#Parent class for the player's stats
class Player(Entities):
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.inventory = []
        self.weapon = {"type": "sword", "dmg": 5}
        self.money = 0

    #Updates the players inventory based on the dropped item from the Opponent?
    def player_inventory_update(self, dropped_weapon):
        self.inventory.append(dropped_weapon)

        return self.inventory


#Class for the Opponent with inherited attributes from the Player class
class Opponent(Entities):
    def __init__(self):
        self.health = 150
        self.strength = 20
        self.stamina = 200
        self.inventory = [{"type": "ax", "dmg": 10}, {"type": "mace", "dmg": 8}, {"type": "lance", "dmg": 7}, {"type": "dung pile", "dmg": 1}]
        self.weapon = {"type": "ax", "dmg": 10}
        self.money = random.randrange(100)

    #Randomly sets the Opponents weapon from the inventory and sets it as the "equipped" weapon in self.weapon
    def opponent_weapon(self):
        random_weapon = random.choice(self.inventory)
        self.weapon = random_weapon

        return self.weapon

     #Gets the randomly generated money for the monster so it can be added to the players wallet later
    def get_opponent_money(self):
        return self.money


#Class to set up the functionalities of the travelling merchants
class Merchant(Entities):
    def __init__(self):
        self.inventory = [
            {"position": "1", "item": "health potion", "price": 1},
            {"position": "2", "item": "fire resin", "price": 2},
            {"position": "3", "item": "amulet", "price": 3},
            {"position": "4", "item": "stamina potion", "price": 4}
        ]

    def reduce_player_money(self):
        while self.money > 0:
            if "1" in self.inventory[0]["position"]:
                self.money = self.money - self.inventory[0]["price"]
                print("Here is your: " + self.inventory[0]["item"])
            elif "2" in self.inventory[1]["position"]:
                self.money = self.money - self.inventory[1]["price"]
                print("Here is your: " + self.inventory[1]["item"])
            elif "3" in self.inventory[2]["position"]:
                self.money = self.money - self.inventory[2]["price"]
                print("Here is your: " + self.inventory[2]["item"])
            elif "4" in self.inventory[3]["position"]:
                self.money = self.money - self.inventory[3]["price"]
                print("Here is your: " + self.inventory[3]["item"])
            else:
                print("Please enter an item number that you would like to purchase")