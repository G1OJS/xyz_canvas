# main.py

import matplotlib.pyplot as plt
from xyz_canvas.objects import XyzCreateObject
from xyz_canvas.gui import xyz_buttons

def add_to_scene(obj):
    objects.append(obj)

def on_button_change(action):
    if action == 'clear':
        objects.clear()
        ax.cla()
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_zlim([0,1])
        plt.draw()
        print("Scene cleared")
    elif action == 'list':
        list_objects()
    elif action == 'line':
        print("Line button pressed — mode switching to 'line' not yet implemented (line is default)")
        # Implement mode switch: creator.set_mode('line')
    elif action == 'rectangle':
        print("Rectangle button pressed — mode switching to 'rectangle' not yet implemented")
        # Implement mode switch: creator.set_mode('rectangle')
    elif action == 'exit_close':
        print("Exit & Close button pressed — exiting and closing window")
        plt.close()
    elif action == 'exit_keep':
        print("Exit & Keep button pressed — not implemented")
        # Implement exit logic to return control but keep window open
    else:
        print(f"'{action}' button pressed — not yet implemented")


def list_objects():
    if(len(objects)==0):
        print("No objects are present, please add some")
    else:
        print("Scene contains:")
        for i, obj in enumerate(objects):
            print(f"[{i}] {obj.describe()}")
            for line in obj.get_lines():
                print(f"   Line: {line[0]} → {line[1]}")

buttons_to_show = [
    ('Clear', 'clear'),
    ('Line', 'line'),
    ('Rectangle', 'rectangle'),
    ('List', 'list'),
    ('Exit & Close', 'exit_close'),
    ('Exit & Keep', 'exit_keep'),
]


print("This is a demo of xyz_canvas (pre-release, V0.2.0), a Python library to add, edit, and connect 3D wire-frame objects\n"
      +"using only Matplotlib. The idea is that this will be called by code that needs the \n"
      +"user to define / edit these objects in 3D space.\n\n"
      +"Currently, only lines are supported but the plan is to include at least lines, rectangles, \n"
      +"arcs (circles) and helices. Shape types are seleced via the buttons next to the geometry display.\n"
      +"The clear button is implemented, as is Exit & Close and List, but the others are placeholders.\n\n"
      +"To add a line, click two points within the axis space (note that no feedback is given for the first click).\n\n"
      +"The view may be rotated at any time by clicking and dragging just oustide the axis space.\n\n"
      +"Currently, endpoints / vertices are pinned to the 'closest' backplane (shaded & gridded).\n"
      +"Methods to move vertices into general 3D space by clicking and typing co-ordinates,\n"
      +"snapping to a 3D grid / other objects,  will be added soon.\n\n")
      

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

buttons = xyz_buttons(plt, fig, on_button_change, buttons_to_show)

objects = []
creator = XyzCreateObject(plt, ax, add_to_scene)

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
plt.show()
