"""
Press one button and the other button changes its size!
"""
import tkinter as tk
from tkinter import messagebox

LEFT_BIG = {'relwidth' : 0.8}
LEFT_SMALL = {'relwidth' : 0.2}
RIGHT_BIG = {'relx' : 0.2, 'relwidth' : 0.8}
RIGHT_SMALL = {'relx' : 0.8, 'relwidth' : 0.2}

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 1) Create a new tkinter class
class buttons(tk.Tk):
    # TODO 2) Create a constructor
    def __init__(self):
        super().__init__()


        self.button = tk.Button(self, text='Black button!', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
        self.button_2 = tk.Button(self, text='Blue button!', fg='blue',
                                font=('courier new', 16, 'bold'), command=self.on_button_press_2)
        self.button_2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    # TODO 3) call Tk's constructor,
        self.button.bind('<ButtonRelease>', self.on_button_release)
        self.button_2.bind('<ButtonRelease>', self.on_button_release)

    # TODO 4) Create 2 buttons next to each other, side by side, with the
    #  text "Click me!". Make sure the buttons are member variables and
    #  look at the example photo for reference.

    # TODO 5) For the left button, add: command=self.left_button_pressed
    #  For the right button, add: command=self.right_button_pressed

    # TODO 6) Create a method called left_button_pressed that places the left
    #  button to small and the right button to big. For example,
    #  self.button_left.place(LEFT_SMALL)
    #  self.button_right.place(RIGHT_BIG)

    # TODO 7) Create a method called right_button_pressed and place the left
    #  button to big and the right button to small
    def on_button_press(self):
        messagebox.showinfo(None, "The black button wins!")
    def on_button_press_2(self):
        messagebox.showinfo(None, "The blue button wins!")
    def on_button_release(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')
# TODO 8) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    app = buttons()
    app.geometry("1500x800")
    app.mainloop()
    # TODO 9) Create an object of the dueling buttons class

    # TODO 10) Set the object's width and size using the geometry method

    # TODO 11) Call the object's mainloop method
