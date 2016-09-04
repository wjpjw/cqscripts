# -*- coding: utf-8 -*-

# Wrapping functions: explicitly specify arguments and provide doc for cpp exposed functions.
from .stub import GameLayerDelegate,game_layer
#game_layer is defined in cpp engine. If there is no cpp engine, forge it with a stub.

def init_background_image(image="images/desert.jpg"):
    ''' Inits the background image. (cpp search path is DIR(cqscripts)/..)'''
    game_layer.initBackgroundImage(image)
    pass

def create_skeleton_unit(animation, x, y, model, height, scale=1.0, from_left_to_right=True, has_hp_bar=True):
    '''  Creates a skeleton unit.'''
    game_layer.createSkeletonUnit(animation, x, y, model, height, scale, from_left_to_right, has_hp_bar)
    pass
