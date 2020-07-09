'''
Game Items
Items are aggregate: Hint
'''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}\n{self.description}"