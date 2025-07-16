# main.py

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

