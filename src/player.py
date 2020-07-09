# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.last_room = None
        self.items = []
    
    def __str__(self):
        return f"{self.current_room.name}.  {self.current_room.description}"
    
    def move(self, direction):
        # set last room to this room to return to if there is no room in a given direction
        self.last_room = self.current_room
        # check direction
        if direction == 'n':
            new_room = self.current_room.n_to
            self.current_room = new_room
        elif direction == 'e':
            new_room = self.current_room.e_to
            self.current_room = new_room
        elif direction == 's':
            new_room = self.current_room.s_to
            self.current_room = new_room
        else:
            new_room = self.current_room.w_to
            self.current_room = new_room
        # check to see if the new room exists and turn player back if not
        if self.current_room == None:
            print('\nCANNOT GO THIS WAY\n')
            self.current_room = self.last_room

    def takeItem(self, item):
        self.items.append(item)
    def dropItem(self, item):
        self.items.remove(item)

        
    