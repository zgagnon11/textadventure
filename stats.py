import random

#Parent class for the player's stats
class Player:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.stamina = 100
        self.mana = 20
        self.inteligence = 20
        self.wisdom = 10
        self.charisma = 500
        self.inventory = []
        self.weapon = [{"type": "sword", "dmg": 5}]

    #Calculates the damage dealt using the strength and the randomized weapon value range
    def damage_dealt(self):
        damage = self.strength + random.randrange(self.weapon[0]["dmg"])

        return damage

    #Calculates the damage taken using the strength and the randomized weapon value range
    def damage_taken(self, damage):
        self.health = self.health - damage

        return self.health

    #Updates the players inventory based on the dropped item from the Opponent?
    def player_inventory_update(self, dropped_weapon):
        self.inventory.append(dropped_weapon)

        return self.inventory


#Class for the Opponent with inherited attributes from the Player class
class Opponent(Player):
    def __init__(self):
        self.health = 150
        self.strength = 20
        self.stamina = 200
        self.inventory = [{"type": "ax", "dmg": 10}, {"type": "mace", "dmg": 8}, {"type": "lance", "dmg": 7}, {"type": "dung pile", "dmg": 1}]
        self.weapon = []

    #Randomly sets the Opponents weapon from the inventory and sets it as the "equipped" weapon in self.weapon
    def opponent_weapon(self):
        random_weapon = random.choice(self.inventory)
        self.weapon = [random_weapon]

        return self.weapon






        