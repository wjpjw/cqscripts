# World module: an abstraction of the game world.

from engine.trigger import Trigger, Rule

class Unit:
    def __init__(self, name, damage, hp, attack_range, move_speed):
        self.name=name
        self.damage=damage
        self.hp=hp
        self.attack_range=attack_range
        self.move_speed=move_speed
    pass

class Player:
    def __init__(self, world):
        self.world=world
        self.opponent=world.opponent
        self.units=[]

    def create_unit(self, unit):
        self.units.append(unit)
    pass

class WorldState:
    PAREPARE=0
    BATTLE=1
    pass

class World:
    def __init__(self):
        self.me=Player(self)
        self.opponent=Player(self)
        self.trigger=Trigger(self)
        self.state=WorldState.PAREPARE
    pass
