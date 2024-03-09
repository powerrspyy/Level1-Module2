"""
Create a simple calculator app
"""
import tkinter as tk

class ButtonsAndTextFields(tk.Tk):
    def __init__(self):
        super().__init__()

        # Add a label

        # Add a button.
        #   What the command= option does:
        #   Specifies what to call when the button is pressed. If a method
        #   (without the parenthesis) is used it will get called when the
        #   button is pressed.
        self.button = tk.Button(self, text='Add', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press(type = 1))
        self.button.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.2)
        self.button = tk.Button(self, text='Subtract', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press(type = 2))
        self.button.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.2)

        # Add a text field that can take input from the user
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.5, relwidth=0.8, height=18)
        self.text_field2 = tk.Entry(self)
        self.text_field2.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)


        # bind(event, handler) says to call the handler (function or method)
        # when an event occurs. The events are predefined by tkinter.
        # common events: https://www.tcl.tk/man/tcl8.6/TkCmd/bind.htm#M7
        #   <KeyPress>      - a keyboard key is pressed
        #   <KeyRelease>    - a keyboard key is released
        #   <ButtonPress>   - a mouse button is pressed
        #   <ButtonRelease> - a mouse button is released
        #   <Enter>         - the mouse has entered the object
        #   <Leave>         - the mouse has left the object
        #   <Motion>        - the mouse has moved within the object
        self.text_field.bind('<KeyPress>', self.on_text_entry)

        # bind() can also be used in conjunction with the command= option
        self.button.bind('<ButtonRelease>', self.on_button_release)

        # bind() used to change background of the label as the mouse enters
        # and leaves the label object
        self.label = tk.Label(self, bg = 'white', font=('Rockwell', 20, 'normal', 'underline'), fg = 'red')
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
    def on_button_press(self, type: int):
        # Get the text from the text field and store into a variable
        f1 = self.text_field.get()
        f2 = self.text_field2.get()
        if type == 1:
        # Update the text in the label
            self.label.configure(text=int(f1) + int(f2))

        elif type == 2:
            self.label.configure(text=int(f1) - int(f2))
        elif type == 3:
            self.label.configure(text=int(f1) * int(f2))


    def on_text_entry(self, event):
        print(repr(event))
        print('  keycode ..: ' + str(event.keycode))
        print('  char: ....: ' + event.char)
        print('  keysym ...: ' + str(event.keysym))

    def on_button_release(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

    def on_button_press2(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

if __name__ == '__main__':
    app = ButtonsAndTextFields()
    app.geometry("1000x1000")
    app.mainloop()



