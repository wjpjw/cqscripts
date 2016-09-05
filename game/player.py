# -*- coding: utf-8 -*-

from .technology import Technology
import cqscripts.data.technologies

class Player:
    def __init__(self, world):
        self.world=world # T=World
        self.units=[]  # T=Unit
        self.technologies= {} # K=Str, V=Technology
        self.load_technologies()  # Load data!
        self.unit_meta_pool=[]  # T=UnitMeta
    def load_technologies(self):
        for k,v in cqscripts.data.technologies.technology_dict.items():
            self.technologies[k]=Technology(**v)
    def add_unit(self, unit):
        self.units.append(unit)
    def add_meta(self, meta):
        self.unit_meta_pool.append(meta)
    def unlock_technology(self, technology_name):
        self.technologies[technology_name].unlock(self)
    pass
