import random

#List of available genres to generate names
def genre_choices():
    print("----------")
    print("Enter the genre name or number to generate a band name")
    print("1. rock")
    print("2. glam pop")
    print("3. folk")
    print("----------")

    return None


#Takes user input
def genre_select():
    genre_choice = input("What Genre?: ")
    
    return genre_choice


#Function that handles the users input and prints the band name
def input_handle(genre_choice, rock, pop, folk):
    if genre_choice == "1" or genre_choice == "rock":
        print("Here is your rock band name: " + rock.upper())
    elif genre_choice == "2" or genre_choice == "pop":
        print("Here is your pop band name: " + pop.upper())
    elif genre_choice == "3" or genre_choice == "folk":
        print("Here is your folk band name: " + folk.upper())
    else:
        print("Please enter a valid genre!")

    return None


#Rock names
def rock_genre():
    rock_name1 = ["heavy metal", "bloody", "dying", "dead"]
    rock_name2 = ["bulldozer", "drill", "chainsaw", "hunter", "necrophagia"]
    combined_choice_rock = random.choice(rock_name1) + " " + random.choice(rock_name2)

    return combined_choice_rock


#Glam Pop names
def pop_genre():
    pop_name1 = ["glitter", "pop", "sparkle"]
    pop_name2 = ["pony", "pupper", "tits", "tiddies"]
    combined_choice_pop = random.choice(pop_name1) + " " + random.choice(pop_name2)

    return combined_choice_pop


#Folk names
def folk_genre():
    folk_name1 = ["country", "folk", "kissing"]
    folk_name2 = ["jamboree", "gabagool", "cousin"]
    combined_choice_folk = random.choice(folk_name1) + " " + random.choice(folk_name2)

    return combined_choice_folk

#Scripts with a while True to keep it running
while True:
    genre_choices()
    user_input = genre_select()
    rock = rock_genre()
    pop = pop_genre()
    folk = folk_genre()
    input_handle(user_input, rock, pop, folk)
    