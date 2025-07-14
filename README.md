# xyz_canvas
## Interactive canvas for editing 3D geometry, using only matplotlib.pyplot

This is a demo of xyz_canvas (pre-release, V0.3.0), a Python library intended to add, edit, and connect 3D wire-frame objects using only Matplotlib. 

The idea is that this will be called by code that needs the  user to define / edit these objects in 3D space.

The capability being demonstrated is being able to create and edit in 3D space using only Matplotlib. The demo program itself works as described below.

### Demo progam
The demo program demo.py is minimal, as is the object creation capability of the canvas.py 'engine', but these limitations don't detract from the core idea stated above.

Currently, objects consist only of lines, which may be disconnected. An object consists of one or more lines. Pressing 'save' fires the callback with the set of added lines as an argument. To add a line, click two points within the axis space. The view may be rotated at any time by clicking and dragging just oustide the axis space.

# Known issues
As of now, there are no known issues with the capability being demonstrated; it is possible to use only the mouse (and only the main button) to create and move line ends in 3D. However, see below.

# Next Steps
I intend to make the demonstration capabilty more useful, e.g. I will add a 'delete most recent' button alongside the 'clear' (all) button, so that this could be used as-is within other software. Also note that I need to disentangle the core capability from the supporting demonstration code, as the latter isn't fully contained in demo.py and infact exists within canvas.py.


## Installation
Install with pip:
```
pip install xyz_canvas
```

## Demo Screenshot

![Capture](https://github.com/user-attachments/assets/aea93646-d451-4597-84dc-5f81d00c52bf)
