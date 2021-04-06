# The code for part 1: Script 1
# The below code is adapted from code found here: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog


# Function for opening the
# file explorer window
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("dat Files",
                                                      ".dat"),("csv Files", ".csv"), ("json Files", ".json"),
                                                     ("json-stat Files", ".json-stat")))

    # Change label contents
    window.destroy()

# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("600x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.pack()
button_explore.pack()

button_exit.pack()

# Let the window wait for any events
window.mainloop()

print(filename)
