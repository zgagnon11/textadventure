# text adventure battle system
Zach Gagnon
Roger Johnson

# Requirements
- Both the Hero and the Monster start with the same number of hitpoints
- Each time the user presses the enter button, the Hero attacks the monster
- The amount of damage and remaining hitpoints are displayed
- After the monster is attacked, it attacks the Hero, with damage and remaining hitpoints being displayed
- Once either the Hero or the monster dip below 1 hitpoint, they are declared dead and the winner is displayed

- Extra Credit: If the Hero uses a weapon, modify the damage algorithm accordingly

- Track Player stats using a Player class
- Track NPC (or Monster) stats by subclassing Player and adding some customizations
- Present a working proof-of-concept for Roger's battle engine that includes loot drops
- Each battle features items looted from the previous battle as weapon choices

# Task list to MVP
- done - weapon selection
- done - hero attacking monster
- done - monster attacking hero
- done - iterate through battle
- done - monster dies, drops loot (weapon)
- done - updating hero inventory with loot drop (weapon)
- done - monster is dead, new battle begins
- done - hero dies, end program

# What does it do
Find out by running the game:
```bash
python game2.py
```
