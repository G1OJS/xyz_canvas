
import matplotlib.pyplot as plt
from xyz_canvas.xyz_canvas import xyz_mouse, xyz_lines

global n_lines

def mouse_clicked(xyz):
    global n_lines
    #print(xyz)
    lines.add(xyz)
    n_lines_in_list =len(lines.line_list) 
    if (n_lines_in_list > n_lines):
        print(f"\n{n_lines_in_list} lines in list:")
        for l in lines.line_list:
            print(l)
    n_lines = n_lines_in_list

def mouse_movedto(xyz):
   # print(mouse.movedto_xyz)
    pass

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
plt.ion()
plt.show()
plt.draw()

n_lines = 0
mouse = xyz_mouse(plt, ax, mouse_clicked, mouse_movedto)
lines = xyz_lines(plt, ax)

