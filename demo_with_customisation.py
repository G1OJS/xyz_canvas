# main.py

from xyz_canvas.canvas import xyz_canvas

# callback examples

def on_click(canvas, xyz, pt_index):
    if (pt_index is not None):
        print(f"Clicked on point {pt_index} at {canvas.points_xyz[pt_index]}")
        if(len(canvas.points_xyz) >3):
            print(f"That's enough points for today! I'm deleting them all!")
            canvas.init_canvas()
    else:
        print(f"Clicked at {xyz}")
        
def on_move(canvas, xyz, selectable_pt_index, selected_pt_index):
    if (selectable_pt_index is not None):
        print(f"Moved to {xyz} near point {selectable_pt_index}" )
    if (selected_pt_index is not None):
        print(f"Moved to {xyz} carrying point {selected_pt_index}" )


#instantiating the canvas:
demo = xyz_canvas(  xlim =[0,10], ylim =[-20,30], zlim=[-3,5],
                                xlabel="x", ylabel="y", zlabel="z",            
                                 on_click_cb = on_click,
                                 on_move_cb = on_move
                               )

# Customisation examples
demo.ax.set_facecolor('grey')  # Sets background color *within plot box*
demo.fig.patch.set_facecolor('grey')  # Sets full figure background
demo.ax.xaxis.set_pane_color('lightblue')
demo.ax.yaxis.set_pane_color('lightyellow')



# the plt.show() 
demo.plt.show()

print("Demo finished ...")

