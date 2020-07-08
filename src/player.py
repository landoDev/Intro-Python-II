# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    def move(self, direction):
        self.direction = direction
    