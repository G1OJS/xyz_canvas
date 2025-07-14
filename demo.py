# main.py

from xyz_canvas.canvas import make_objects

def on_complete(lines):
    print("Object returned: ")
    for l in lines:
        print(l)

demo_3D_builder = make_objects(on_complete_cb = on_complete)
