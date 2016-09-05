# -*- coding: utf-8 -*-

#import sys
#reload(sys)                      # reload 才能调用 setdefaultencoding 方法
#sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

#game_layer is defined in cpp engine. If there is no cpp engine, forge it with a stub.
#from .stub import GameLayerDelegate,game_layer

# Wrapping functions: explicitly specify arguments and provide doc for cpp exposed functions.
from __main__ import game_layer

def init_background_image(image="images/desert.jpg"):
    ''' Inits the background image. (cpp search path is DIR(cqscripts)/..)'''
    game_layer.initBackgroundImage(image)
    pass

def create_skeleton_unit(animation, x, y, model, height, scale=1.0, from_left_to_right=True, has_hp_bar=True):
    '''  Creates a skeleton unit.'''
    game_layer.createSkeletonUnit(animation, x, y, model, height, scale, from_left_to_right, has_hp_bar)
    pass
