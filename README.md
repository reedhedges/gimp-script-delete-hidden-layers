
This is a script extension for The Gimp (http://www.gimp.org) that simply
deletes any image layers that have been hidden (by clicking the "eye" button
next to the layer in the layers list.)   It's useful for cleaning up old 
layers you don't want anymore, or for removing frames from an image that will
be exported as an animated GIF.  

To install, copy `delete-hidden-layers.py` to the `plug-ins` subdirectory of
your Gimp configuration directory.  If you are using Gimp 2.8, this will be
`~/.gimp-2.8/plug-ins`:

   cp delete-hidden-layers.py ~/.gimp-2.8/plug-ins/

Next, make the script executable (Gimp ignores non-executable scripts):

  chmod +x ~/.gimp-2.8/plug-ins/delete-hidden-layers.py

Now if you run (or re-run) Gimp, you will see a new menu item in the "Images"
menu: "Delete hidden layers...".  

