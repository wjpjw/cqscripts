from core.gamelayer import init_background_image, create_skeleton_unit
from game.world import *
from game.register_triggers import register_triggers
# This script is executed by GameLayer's init() function.
# Initializes everything from here!

# [0] global initial settings
init_background_image()

# [1] world initialization
world=World()
register_triggers(world)
