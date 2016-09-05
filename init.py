# -*- coding: utf-8 -*-
from cqscripts.game.world import *
from cqscripts.core.gamelayer import *

# This script is executed by GameLayer's init() function.
# Initializes everything from here!

# [0] global initial settings
init_background_image()

# [1] world initialization
world=World()
player1=world.me
player2=world.opponent
player1.unlock_technology(technology_name="forest")

create_label("测试",200,200)
