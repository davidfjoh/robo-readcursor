import Tkinter
import pyrobot

class App():
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title("Cursor Monitor")

        self.underCurVal = Tkinter.StringVar()
        self.underCurCtrl = Tkinter.Entry(self.root, width=25, textvariable=self.underCurVal)
        self.underCurCtrl.pack()
        
        
        self.robot = pyrobot.Robot()
        self.last_data = None

        self.update()
        self.underCurCtrl.focus()
        self.root.mainloop()

    def update(self):
        location = self.robot.get_mouse_pos()
        color = self.robot.get_pixel(x = location[0], y = location[1])
        if self.last_data != (location,color):
            self.underCurVal.set("%s,%s" % (location, color))
            self.last_data = (location,color)
        self.root.after(100, self.update)


if __name__ == "__main__":
    app=App()
