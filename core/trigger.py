from .util import *

class  Rule:
    def __init__(self, condition, **condition_args, event, **event_args, is_throw_away=False):
        self.condition=condition
        self.condition_args=condition_args
        self.event=event
        self.event_args=event_args
        self.is_throw_away=is_throw_away

    def trigger_event(self):
        if (condition(**condition_args)==True):
            event(**event_args)
            return True
        else:
            return False
    pass

class Trigger:
    def __init__(self, world):
        self.rule_dict={}
        self.world=world
    def add_rule(self, name, rule):
        if not rule_dict.has_key(name):
            rule_dict[name]=rule

    def add_rules(self, rules):
        rule_dict.update(rules)

    def check_rule(self,name):
        if rule_dict.has_key(name):
            if rule_dict[name].trigger_event():     # check the condition, try to trigger event
                if rule_dict[name].is_throw_away:   # delete throwaway rules
                    del rule_dict[name]

    def check_rules(self):
        for name in rule_dict.keys():
            check_rule(name)
