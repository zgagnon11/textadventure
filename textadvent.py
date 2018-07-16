#3 locations
#move to them and back through them

locations = {
    "river": "It's wet af",
    "castle": "It's dank af",
    "inn": "It's quaint af"
}


def get_user_input():
    user_input = input("Where do you want to go? ")

    return user_input


def retrieve_location(ipt):
    location_description = locations[ipt]

    return location_description


def travel_rules(the_input, current_location):
    if current_location == "castle":
        pass
    elif current_location == "inn":
        if the_input == "castle":
            print("Going to " + the_input)
            current_location = the_input
        #print("You need to follow the river to get to the inn")
    elif current_location == "river":
        print("Follow this to get to the inn")
        
    return None

current_location = "inn"
while True:
    print("Here are the places you can go: " + "river, castle, inn")
    the_user_input = get_user_input()
    travel_rules(the_user_input, current_location)
    #print(the_user_input)
    print("You are currently at: " + current_location)