from room import Room
from item import Item
from player import Player
import textwrap
import re

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Grognak")
player.current_room = room['outside']
print("\nWelcome to Grognak's Adventure!")

# Write a loop that:
while True:
    # * Prints the current room name
    print("\n")
    print(player.current_room)
    print(f'\n{player.name}\n-------')
    user_input = input('[n] North [e] East [s] South [w] West\n[s] Search [q] Quit\ncommand: \n')
    # add search command for items
    re_input = re.search("[nesw]", user_input)
    re_actions = re.search("[astdb]", user_input)
    # If the user enters "q", quit the game.
    if user_input == 'q':
        break
    elif not re_input:
        print('\nError: Invalid Input!\n')
    elif re_actions:
        if player.current_room.items:
            print(player.current_room.items)
            action_input = input('[t] T ')
        else:
            print("\nThere is nothing here...")
    else:
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        
        player.move(user_input)



