# -*- coding: utf-8 -*-

class UnitMeta:
    def __init__(self, name, description, damage, hp, attack_range, move_speed,attack_interval,collide_radius):
        self.name=name
        self.description=description
        self.damage=damage
        self.hp=hp
        self.attack_range=attack_range
        self.move_speed=move_speed
        self.attack_interval=attack_interval
        self.collide_radius=collide_radius
    def __str__(self):
        return self.name+": hp"+str(self.hp)+", damage:"+str(self.damage)
    pass

class Unit:
    def __init__(self, unit_meta, position):
        self.meta=unit_meta
        self.current_hp=unit_meta.hp
        self.current_speed=unit_meta.move_speed
        self.current_attack_interval=unit_meta.attack_interval
        self.current_attack_range=unit_meta.attack_range
        self.current_damage=unit_meta.damage
        self.position=position
