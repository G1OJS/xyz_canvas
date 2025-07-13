from xyz_canvas.gui import xyz_mouse

# Base geometry class
class XyzObject:
    def draw(self, ax):
        raise NotImplementedError

    def get_lines(self):
        raise NotImplementedError

    def describe(self):
        raise NotImplementedError

    def get_select_point(self):
        raise NotImplementedError
    
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "lines": self.get_lines()
        }

# Geometry primitives
class Line(XyzObject):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, ax):
        x = [self.start[0], self.end[0]]
        y = [self.start[1], self.end[1]]
        z = [self.start[2], self.end[2]]
        ax.plot(x, y, z, color='blue')

    def get_lines(self):
        return [(self.start, self.end)]

    def describe(self):
        return f"Line from {self.start} to {self.end}"

    def get_select_point(self):
        return tuple(self.start)

    def translate(self, dx, dy, dz):
        self.start = (self.start[0]+dx, self.start[1]+dy, self.start[2]+dz)
        self.end = (self.end[0]+dx, self.end[1]+dy, self.end[2]+dz)


class Rectangle(XyzObject):
    def __init__(self, vertices):
        self.vertices = vertices

    def draw(self, ax):
        for i in range(4):
            s = self.vertices[i]
            e = self.vertices[(i+1)%4]
            ax.plot([s[0], e[0]], [s[1], e[1]], [s[2], e[2]], color='green')

    def get_lines(self):
        return [
            (self.vertices[i], self.vertices[(i+1)%4])
            for i in range(4)
        ]

    def describe(self):
        return f"Rectangle with vertices: {self.vertices}"

    def to_dict(self):
        return {
            "type": "Rectangle",
            "vertices": self.vertices,
            "lines": self.get_lines()
        }

    def get_select_point(self):
        return (self.vertices[0])

    def translate(self, dx, dy, dz):
            self.vertices = [(x+dx, y+dy, z+dz) for (x, y, z) in self.vertices]



# Main object creation controller
class XyzCreateObject:
    def __init__(self, plt, ax, add_cb, mode='line', grid_spacing = 0.1):
        self.plt = plt
        self.ax = ax
        self.add_cb = add_cb
        self.objects = []
        self.mode = mode
        self.grid_spacing = grid_spacing
        self.partial_marker = None
        self.tools = {
            'line': self.XyzLines(self, self.wrapped_add_cb),
            'rectangle': self.XyzRectangles(self, self.wrapped_add_cb),
            'select': self.XyzSelectMove(self, self.objects)
        }
        self.current_tool = self.tools[mode]
        self.mouse = xyz_mouse(plt, ax, self.mouse_clicked, self.mouse_movedto)
        
    def wrapped_add_cb(self,obj):
        print("add")
        self.objects.append(obj)
        obj.draw(self.ax)
        self.plt.draw()
        self.add_cb(obj)

    def mouse_clicked(self, xyz):
        snapped_xyz = self.snap_to_grid(xyz)
        self.current_tool.add_point(snapped_xyz)

    def mouse_movedto(self, xyz):
        if hasattr(self.current_tool, "mouse_movedto"):
            self.current_tool.mouse_movedto(xyz)

    def set_mode(self, new_mode):
        self.mode = new_mode
        self.current_tool = self.tools[new_mode]

    def snap_to_grid(self, xyz):
        g = self.grid_spacing
        return tuple(round(coord / g) * g for coord in xyz)

    def show_temp_marker(self, xyz):
        if self.partial_marker:
            self.partial_marker.remove()  # Remove old marker
        xs, ys, zs = xyz
        self.partial_marker = self.ax.scatter([xs], [ys], [zs], color='red', marker='o', s=50)
        self.ax.figure.canvas.draw_idle()

    def remove_temp_marker(self):
        if self.partial_marker:
            self.partial_marker.remove()
            self.partial_marker = None
            self.ax.figure.canvas.draw_idle()

    def redraw_all(self):
        self.ax.cla()
        for obj in self.objects:
            obj.draw(self.ax)
        self.ax.set_xlim([0,1])
        self.ax.set_ylim([0,1])
        self.ax.set_zlim([0,1])
        self.plt.draw()


    # Tool for creating a line from 2 points
    class XyzLines:
        def __init__(self, parent, add_cb):
            self.parent = parent
            self.start = None
            self.add_cb = add_cb

        def add_point(self, xyz):
            if self.start is None:
                self.start = xyz
                self.parent.show_temp_marker(xyz)
            else:
                line = Line(self.start, xyz)
                self.add_cb(line)
                self.start = None
                self.parent.remove_temp_marker()
            

    # Tool for creating a rectangle from 2 diagonal corners
    class XyzRectangles:
        def __init__(self, parent, add_cb):
            self.parent = parent
            self.first_corner = None
            self.add_cb = add_cb

        def add_point(self, xyz):
            if self.first_corner is None:
                self.first_corner = xyz
                self.parent.show_temp_marker(xyz)
            else:
                x1, y1, z1 = self.first_corner
                x2, y2, _ = xyz
                vertices = [
                    (x1, y1, z1),
                    (x2, y1, z1),
                    (x2, y2, z1),
                    (x1, y2, z1),
                ]
                rect = Rectangle(vertices)
                self.add_cb(rect)
                self.first_corner = None
                self.parent.remove_temp_marker()


    class XyzSelectMove:
        def __init__(self, parent, objects):
            self.parent = parent
            self.objects = objects
            self.selected = None
            self.last_xyz = None

        def add_point(self, xyz):
            # Called on mouse click: try to select an object
            if(self.selected):
                self.selected = False
            else:
                self.selected = self.find_nearest(xyz)
            self.last_xyz = xyz
            if self.selected:
                print(f"Selected: {self.selected.describe()}")

        def mouse_movedto(self, xyz):
            if self.selected and self.last_xyz:
                dx = xyz[0] - self.last_xyz[0]
                dy = xyz[1] - self.last_xyz[1]
                dz = xyz[2] - self.last_xyz[2]
                self.selected.translate(dx, dy, dz)
                self.last_xyz = xyz
                self.parent.redraw_all()

        def find_nearest(self, xyz, tol=0.1):
            closest = None
            min_dist = float('inf')
            for obj in self.objects:
                print(obj.describe())
                if not hasattr(obj, 'get_select_point'):
                    continue
                cx, cy, cz = obj.get_select_point()
                dist = ((xyz[0]-cx)**2 + (xyz[1]-cy)**2 + (xyz[2]-cz)**2)**0.5
                print(f"dist {dist}")
                if dist < tol and dist < min_dist:
                    closest = obj
                    min_dist = dist
            return closest

