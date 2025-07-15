# main.py

from xyz_canvas.canvas import define_points


def on_complete(lines):
    print("Points created are:")
    for l in lines:
        print(l)

demo_3D_builder = define_points(on_complete_cb = on_complete,
                               xlim =[0,10], ylim =[-20,30], zlim=[-3,5],
                               xlabel="x", ylabel="y", zlabel="z")
