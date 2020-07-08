# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    def __str__(self):
        return f"{self.current_room.name}.  {self.current_room.description}"
    
    def move(self, direction):
        # loop direction 
        # try:
            # check which direction player is going and set room to new room
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
        # except:
            # if direction attribute is None on Room
        
    