# for backwards compatibility with V1.0.0, this is the existing demo code

from xyz_canvas.canvas import define_points


def on_complete(lines):
    print("Points created are:")
    for l in lines:
        print(l)

demo_3D_builder = define_points(on_complete_cb = on_complete,
                               xlim =[0,10], ylim =[-20,30], zlim=[-3,5],
                               xlabel="x", ylabel="y", zlabel="z")

# up to here....

# - Moved `plt.show()` out of `__init__` to allow users more control over plot display timing.
# - Users now must call `.show()`  explicitly when ready to display.

demo_3D_builder.plt.show()

# also note that on_complete_cb is no longer used, and 'lines' in the example above should have been 'points'
