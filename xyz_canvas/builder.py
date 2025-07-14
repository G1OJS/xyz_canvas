# main.py

import matplotlib.pyplot as plt
from xyz_canvas.canvas import buttons

class make_objects:

    def __init__(self, on_change_cb):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.init_canvas()
        print("Scene initialised")

    def init_canvas(self):
        objects = []
        self.ax.set_xlim([0,1])
        self.ax.set_ylim([0,1])
        self.ax.set_zlim([0,1])
        self.buttons = buttons(plt, self.fig, self.on_button_press)
        plt.show()
    
    def add_to_scene(obj):
        self.objects.append(obj)

    def on_button_press(self,action):
        if action == 'clear':
            self.init_canvas()
        elif action == 'list':
            list_objects()
        elif action == 'exit':
            print("Exit & Close button pressed — exiting and closing window")
            plt.close()

    def list_objects():
        print(objects)
        if(len(objects)==0):
            print("No objects are present, please add some")
        else:
            print("Scene contains:")
            for i, obj in enumerate(objects):
                print(f"[{i}] {obj.describe()}")
                for line in obj.get_lines():
                    print(f"   Line: {line[0]} → {line[1]}")


