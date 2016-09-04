# -*- coding: utf-8 -*-

from .unitmetas import *
from game.unit import UnitMeta
# [0] unlock technology events:
def unlock_technology_forest(player):
    for i in forest_unit_metas:
        player.add_meta(UnitMeta(**unit_meta_dict[i]))
    pass
