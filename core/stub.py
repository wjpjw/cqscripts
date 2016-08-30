#stub creates everything that should be defined in cpp, so that these scripts can be tested before integration with cpp engine.

class GameLayerDelegate:
    def initBackgroundImage(self, image):
        print "stub: init background image"

    def createSkeletonUnit(self, animation, x, y, model, height, scale, from_left_to_right, has_hp_bar):
        print "stub: create skeleton unit: (model=", model, ", animation=", animation,")"
try:
  game_layer
except NameError:
  game_layer=GameLayerDelegate()
else:
  print "sure, it was defined."
