
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button

def _interleave(ends):
    a = ends[0]
    b = ends[1]
    return [a[0],b[0]], [a[1],b[1]], [a[2],b[2]]

class make_objects:

    def __init__(self, on_complete_cb):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.marker = None
        self.lines = []
        self.plotted_lines = []
        self.current_line = None
        self.selected_line_end = None
        self.init_canvas()
        self.on_complete_cb = on_complete_cb
        self.pointer = mouse_3D(plt, self.ax, self.on_pointer_click, self.on_pointer_move)
        plt.show()

    def init_canvas(self):
        self.objects = []
        self.ax.cla()
        self.ax.set_xlim([0,1])
        self.ax.set_ylim([0,1])
        self.ax.set_zlim([0,1])
        self.ax.figure.canvas.draw_idle()
        self.buttons = buttons(plt, self.fig, self.on_button_press)
        print("Scene initialised")


    def on_button_press(self,action):
        if action == 'clear':
            self.init_canvas()
        elif action == 'save':
            self.on_complete_cb(self.lines)
        elif action == 'exit':
            plt.close()

    def on_pointer_move(self, xyz):
        if(self.selected_line_end):
            l_ind, e_ind = self.selected_line_end
            # move the end away from the backplane by keeping Z as originally placed
            # and only changing x and y, at least one of which will have been set at zero
            # this could be modified to fix x if y or z is zero, and y if x or z is zero
            
            line_ends = self.lines[l_ind]
            p = self.lines[l_ind][e_ind]
            self.lines[l_ind][e_ind] = [xyz[0], xyz[1], p[2]]
            line_ends = self.lines[l_ind]

            # redraw the line
            self.ax.cla()
            self.ax.plot(*_interleave(line_ends), color='red')
            self.ax.figure.canvas.draw_idle()
        
    def on_pointer_click(self, xyz):
        if(self.selected_line_end):
            self.selected_line_end = None
        else:
            test = self.at_endpoint(xyz)
            if(test):
                self.selected_line_end = test
            else:
                if self.current_line == None:
                    self.start_line(xyz)
                else:
                    self.complete_line(xyz)
                    
    def start_line(self,xyz):
        xs, ys, zs = xyz
        self.current_line = [xs,ys,zs]
        self.marker = self.ax.scatter([xs], [ys], [zs], color='red', marker='o', s=50)
        self.ax.figure.canvas.draw_idle()

    def complete_line(self,xyz):
        xe, ye, ze = xyz
        line_ends = [self.current_line,[xe,ye,ze]]
        self.lines.append(line_ends)
        self.current_line = None
        self.marker.remove()
        self.ax.figure.canvas.draw_idle()
        self.plotted_lines.append(self.ax.plot(*_interleave(line_ends), color='red'))

    def at_endpoint(self,xyz):
        for line_index, l in enumerate(self.lines):
            for end_index, p in enumerate([l[0],l[1]]):
                if self.is_in_box(xyz,p,0.05):
                    return(line_index,end_index)
        return None

    def is_in_box(self,p1,p2,tol):
        return(abs(p1[0]-p2[0])<tol and abs(p1[1]-p2[1])<tol and abs(p1[2]-p2[2])<tol)

class buttons:
    def __init__(self, plt, fig, buttons_cb):
        self.plt = plt
        self.fig = fig
        self.buttons_cb = buttons_cb
        self.buttons = []

        # Layout settings
        button_height = 0.05
        button_width = 0.2
        spacing = 0.01
        start_y = 0.9

        buttons = [
            ('Clear canvas', 'clear'),
            ('Save last obj', 'save'),
            ('Exit', 'exit'),
            ]

        for i, (label, action) in enumerate(buttons):
            ax = fig.add_axes([0.01, start_y - i*(button_height + spacing), button_width, button_height])
            btn = Button(ax, label)
            btn.on_clicked(lambda event, act=action: self.buttons_cb(act))
            self.buttons.append(btn)


class mouse_3D:

    def __init__(self, plt, ax, on_click_cb, on_move_cb):
        self.plt = plt
        self.ax = ax
        self.on_click_cb = on_click_cb
        self.on_move_cb = on_move_cb
        self.in_axes_range_prev = False
        self.plt.connect('motion_notify_event', self.on_move)

    def on_move(self, event):
        global in_axes_range_prev
        if event.inaxes:
            if type(getattr(self.ax, 'invM', None)) is None:
                return  # Avoid calling format_coord during redraw/rotation
            s = self.ax.format_coord(event.xdata, event.ydata)
            pt, pln = self._get_pane_coords(s)
            in_axes_range_now = self._in_axes_range(pt)
            self.movedto_xyz = pt

            self.on_move_cb(pt)
            if(not (in_axes_range_now == self.in_axes_range_prev)):
                if in_axes_range_now:
                    self.ax.mouse_init(rotate_btn=0)
                    self.plt.connect('button_press_event', self.on_click)
                else:
                    self.plt.disconnect(self.on_click)
                    self.ax.mouse_init(rotate_btn=1)
                    event.button = None
                self.in_axes_range_prev = in_axes_range_now
     
    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            s = self.ax.format_coord(event.xdata, event.ydata)
            pt, pln = self._get_pane_coords(s)
            if(self._in_axes_range(pt)):
                self.on_click_cb(pt)
            
    def _get_pane_coords(self, s):
        # gets x,y,z of mouse position from s=ax.format_coord(event.xdata, event.ydata)
        if('elevation' in s):
            return None
        
        if('x pane' in s):
            pln = 'yz'
        if('y pane' in s):
            pln =  'xz'
        if('z pane' in s):
            pln =  'xy'
        s=s.split(",")
        xyz=[0,0,0]
        for valstr in s:
            valstr=valstr.replace(' pane','')
            ordinate = valstr.split("=")[0].strip()
            i = ['x','y','z'].index(ordinate)
            xyz[i]=float(valstr.split("=")[1].replace('−','-'))

        return xyz, pln


    def _in_axes_range(self, p):
        # determines if x,y and z are all in the axis ranges
        if p == None:
            return False
        x_in = self.ax.get_xlim()[0] <= p[0] <= self.ax.get_xlim()[1]
        y_in = self.ax.get_ylim()[0] <= p[1] <= self.ax.get_ylim()[1]
        z_in = self.ax.get_zlim()[0] <= p[2] <= self.ax.get_zlim()[1]
        return (x_in and y_in and z_in)
