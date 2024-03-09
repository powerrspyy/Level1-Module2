"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class application(tk.Tk):
    # TODO 2) Make a constructor
    def __init__(self):
        super().__init__()
        # TODO 3) Call the Tk class's constructor
        #  super().__init__()
        self.label = tk.Label(self, text="Welcome!!!", bg='black',
                              fg='green', font=('arial', 32, 'bold'), relief='solid')
        # TODO 4) Add a text label and pick a text message to display

        # TODO 5) Place the label somewhere on your app. You can use either
        #  x and y or relx and rely
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        # TODO 6) Create a member variable for the image using the
        #  create_image function. You can use the image provided in this
        #  folder or another image from the internet
        self.img = create_image("carrots.jpg", 100, 100)
        # TODO 7) Create another label and attach to it the image object
        #  from the previous step
        self.label_image = tk.Label(self, image=self.img)
        # TODO 8) Place the label somewhere on your app
        self.label_image.place(x=125, y=200)
# TODO 5) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    app = application()
    # TODO 6) Create an object of the tkinter class

    # TODO 7) Set the app window width and height using geometry()
    app.geometry("500x500")
    # TODO 8) Declare and initialize a score variable
    score = 0

    answer = simpledialog.askstring(None, prompt = "What color is the object show below: ")
    if answer.lower() == "orange":
        score+=1
        messagebox.showinfo(title="Message", message = "Correct answer! Your score has increased by 1!")
    else:
        messagebox.showinfo(title="Message", message="Incorrect input the right answer is orange.")
    messagebox.showinfo(title="final score", message= f"Your final score is {score}")
    app.mainloop()
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable
    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.

    # TODO 12) If the answer is correct, increase the score by 1

    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question

    # TODO 14) Display the score to the user after asking the last question
