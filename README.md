# xyz_canvas
## Interactive canvas for editing 3D geometry, using only matplotlib.pyplot

### What is it?
XYZ_canvas provides the starting point to create Python code that allows defining and editing points in 3D space, using only Matplotlib and just over 200 lines of library in canvas.py. 

![Capture](https://github.com/user-attachments/assets/f86f0481-d98e-4c0e-a972-32f408f90e2c)

### How can I use it?
The demo.py program shows how simple it is to instantiate the canvas:
```
demo_3D_builder = define_points(on_complete_cb = on_complete,
                               xlim =[0,10], ylim =[-20,30], zlim=[-3,5],
                               xlabel="x", ylabel="y", zlabel="z")
```
The 'on_complete_cb' function specified is called when the save button is pressed, and the list of 3D points created is passed to it.

There are two ways to use this library:
1) Modify it for your own needs, by editing the code in canvas.py
2) Incorporate it into your own code by processing the points that it returns - by building on the code in demo.py. For example, your code could take the returned points to define a polygon which you could then display in 3D.

I intend to provide examples of this in later versions.

## Installation
Install with pip:
```
pip install xyz_canvas
```
Or simply download the canvas.py and demo.py files, and develop from there.


