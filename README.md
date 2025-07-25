# xyz_canvas [![PyPI Downloads](https://static.pepy.tech/badge/xyz-canvas)](https://pepy.tech/projects/xyz-canvas)
## Interactive canvas for editing 3D geometry, using only matplotlib.pyplot

### What is it?
**XYZ_canvas provides the starting point to create Python code that allows defining and editing objects in 3D space, using only Matplotlib and just over 200 lines of library in canvas.py.**

This library provides you with the 3D co-ordinates of points clicked on and moved to / over, so that you can create your own code to process the points created. You can reach down into the definitions made in canvas.py to manipulate what's created during use, e.g. delete all the points as shown in the customisation example.

![Capture](https://github.com/user-attachments/assets/f53e6b01-ce03-4141-b15f-3077ab1065ad)

### How can I use it?
The "demo_V1.1.0_minimal.py" program shows how simple it is to instantiate the canvas:
```
from xyz_canvas.canvas import xyz_canvas

#instantiating the canvas:
demo = xyz_canvas(  xlim =[0,1], ylim =[0,1], zlim=[0,1],
                                xlabel="x", ylabel="y", zlabel="z"            
                               )

# showing the plot
demo.plt.show()

# note that this is so minimal that all it does is display;
# the resulting points are not used here.

print("Demo finished ...")

```
If you want to do things with the points created, look in "demo_V1.1.0_with_customisation.py". Here you'll see examples of customising the colour scheme and reacting to mouse clicks and mouse moves.

## Installation
Install with pip:
```
pip install xyz_canvas
```
Or simply download the canvas.py and demo.py files, and develop from there.

## Future plans / ideas
 - demo how to build on top of this to create objects? (might highlight extra functions needed here)
 - add snap to grid (make it settable as dx,dy,dz
 - polar / spherical co-ordinates?
 - transforms? 

