from core.trigger import Trigger, Rule
from .conditions import *
from .events import *
from .world import World

def register_triggers(world):
    ''' Define triggers '''
    t=world.trigger
    rules={
        #"game_ended" : Rule(condition=conditions.hero_died,event=events.game_ended, is_throw_away=True),

    }
    t.add_rules(rules)
    pass
