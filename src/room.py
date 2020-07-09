# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def addItem(self, item):
        self.items.append(item.name)
    def removeItem(self):
        self.items.pop()

    def __str__(self):
        return f"{self.name}\n{self.description}"

class Chest:
    def __init__(self, room, rewards):
        self.room = room
        self.rewards = rewards
    def open(self):
        print(f"{self.rewards}")

