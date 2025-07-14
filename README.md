# xyz_canvas
Interactive canvas for editing 3D geometry, using matplotlib.pyplot

This is a demo of xyz_canvas (pre-release, V0.2.1), a Python library intended to add, edit, and connect 3D wire-frame objects using only Matplotlib. 

The idea is that this will be called by code that needs the  user to define / edit these objects in 3D space.

Currently, only lines are supported. An object consists of one or more lines. Pressing 'save' fires the callback with the set of added lines as an argument.

To add a line, click two points within the axis space. The view may be rotated at any time by clicking and dragging just oustide the axis space.

# Known issues
Currently, when you add a line, both ends are pinned to the 'closest' backplane (shaded & gridded). You may add a line from one plane to another, but neither end of the line can have all three co-ordinates nonzero.
I'm experimenting with ways to overcome this without making the UI clunky. The current version here achieves this by allowing line ends to be picked up (click on them) and dragged away from their plane. However, once 'dropped' they can't be selected again.


## Installation
Install with pip:
```
pip install xyz_canvas
```

## Demo Screenshot
![Capture](https://github.com/user-attachments/assets/bef782f9-881b-49ec-9d26-ba7cdd4d5867)
