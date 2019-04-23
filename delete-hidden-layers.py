#!/usr/bin/env python

from gimpfu import *

def delete_hidden_layers(img, drawable):
  layers = img.layers
  for l in layers:
     if l.visible:
       print "delete-hidden-layers.py: Not removing visible layer %s" % (l)
     else:
       print "delete-hidden-layers.py: Removing hidden layer %s" % (l)
       img.remove_layer(l)
      

register(
  "python_fu_delete_hidden_layers",
  "Delete all hidden layers from the image",
  "Delete all hidden layers from the image",
  "Reed Hedges", "Reed Hedges",
  "2019",
  "<Image>/Image/_Delete Hidden Layers...",
  "*",   # All image types
  [],    # No options
  [],    # No return values
  delete_hidden_layers
)

main()


