# -*- coding: utf-8 -*-

import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

from core.gamelayer import init_background_image, create_skeleton_unit
from game.world import *
from game.register_triggers import register_triggers
# This script is executed by GameLayer's init() function.
# Initializes everything from here!



# [0] global initial settings
init_background_image()

# [1] world initialization
world=World()

player1=world.me
player2=world.opponent

player1.unlock_technology(technology_name="forest")
for i in player1.unit_meta_pool:
    print i
