# -*- coding: utf-8 -*-

# World module: an abstraction of the game world.
from .player import Player

class WorldState:
    PAREPARE=0
    BATTLE=1
    pass

class World:
    def __init__(self):
        self.me=Player(self)
        self.opponent=Player(self)
        self.state=WorldState.PAREPARE
    pass
