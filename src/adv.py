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

# declare items

torch = Item("Torch", "A weak fire from a sconce")
battleaxe = Item("Battleaxe", "A mighty weapon. Fit for a barbarian")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['outside'].addItem(torch)

# Player Commands
take = "take item"
drop = "drop item"
continue_command = "continue"
inventory = "inventory"
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
    user_input = input('[n] Go North [e] Go East [s] Go South [w] Go West\n[f] Search [i] Inventory [q] Quit\ncommand: \n')
    # add search command for items
    re_input = re.search("[nesw]", user_input)
    re_actions = re.search("[aftdbi]", user_input)
    # If the user enters "q", quit the game.
    if user_input == 'q':
        break
    elif user_input == 'f':
        if player.current_room.items:
            loot = player.current_room.items
            while True:
                print('\nYou find: ', loot)
                action_input = input('Take [Item] [Continue]\n')
                check_action = action_input.split(" ")
                re_shortcut = re.search("[tcd]", action_input.lower())
                re_take = re.search(take, action_input.lower())
                re_drop = re.search(drop, action_input.lower())
                re_continue = re.search(continue_command, action_input.lower())
                # if check_action > 1:    
                if action_input == 'c' or re_continue:
                    break
                else:
                    gained = loot[0]
                    player.takeItem(gained)
                    player.current_room.removeItem()
                    print(f'You acquired {gained}')
                    action_input = input('Drop [Item] [Continue]\n')
                    if action_input == 'c' or re_continue:
                        break
                    else:
                        dropped = player.items.pop()
                        player.current_room.addItem(player.items)  
                        print(f"You dropped {dropped}")
                # else:


        else:
            print("\nThere is nothing here...")
    elif user_input.lower() == 'i' or inventory:
        if player.items:
            print(player.items)
        else:
            print("You have nothing...")
    elif not re_input:
        print('\nError: Invalid Input!\n')
    else:
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        
        player.move(user_input)



