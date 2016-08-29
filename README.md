# cqscripts

**python version: 2.7**

The cpp engine exposes a python object *GameLayerDelegate game_layer*, which provides graphic or compute-intensive functions. The cpp-python bridge is **boost/python library(msvc14, python2.7, x86-32)**.

## core
The core package provides more stable code, like abstraction and utilities. It is supposed to be extended but not modified.

The core.gameplayer module wraps all the cpp api, providing documentation plus default arguments.

## game
The game package is where you customerize the game based on core and the cpp engine.

## hooks
The cpp engine explicitly executes the three python files: init.py, update.py and touched.py. Their filename and path should not be changed.

init.py is called in *GameLayer::init()* function.

update.py is called in *GameLayer::update()* function. The frame rate is 60HZ.

touched.py is called in *GameLayer::onTouched()* function. On Windows it's equivalent to mouse click event.

## Why script engine? Why python?
* Compilation of large c++ projects on Visual Studio is slow.
* I don't like Lua; JS is not bad, but V8 is unfortunately unavailable on IOS devices.
* Python is good at abstraction, configuration and gluing.
