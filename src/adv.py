from room import Room
from player import Player
import textwrap

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

print("\nWelcome to Grognak's Adventure!\n")

# Write a loop that:
while True:
    print(player.current_room)
    print(f'\n{player.name}\n-------')
    user_input = input('[n] North [e] East [s] South [w] West [q] Quit\ncommand: ')
    if user_input == 'q':
        break     
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# THE INFO ABOVE IS IMPORTANT TO THE GAME 

# Personal Stretch => Print start page and add Parser for user character name
# MY PLAN

 
# gamplay loop

    # print current room name
    # print current room description use textwrap.wrap(room.description)
    # print message to continue
    # input command parser
    # move to next room or throw error

# IF NO PLAYER INPUT CUZ OUT OF TIME HARD CODE MAIN CHARACTER AS GROGNAK

# Understand
    # players need to input a direction limited to cardinal directions
    #   After each move print the name and description of the room
    # use n, s, e, w for commands or print error
