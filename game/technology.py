# -*- coding: utf-8 -*-

class Technology:
    def __init__(self, name, description, unlock_event):
        self.name=name
        self.description=description
        self.unlock_event=unlock_event
        self.unlocked=False
    def unlock(self,player):
        self.unlocked=True
        self.unlock_event(player)
    pass
