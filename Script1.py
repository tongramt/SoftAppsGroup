# The code for part 1: Script 1
# The below code is adapted from code found here: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
# import filedialog module
from tkinter import filedialog
import tkinter as tk
# import pandas
import pandas as pd

import pyjstat

global filename
global URL
# Function for opening the
# file explorer window
def browseFiles():

    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("csv Files", ".csv"), ))

    # Change label contents
    window.destroy()

def JSONURL():

    window2 = Tk()
    # Set window title
    window2.title('Input URL for JSON or JSON-stat files')

    # Set window size
    window2.geometry("500x100")

    # Set window background color
    window2.config(background="white")

    tk.Label(window2,
             text="URL").grid(row=0)

    e1 = tk.Entry(window2)
    button_submit = Button(window2,
                           text="Submit",
                           command=exit)
    button_exit = Button(window2,
                           text="Exit",
                           command=exit)
    e1.grid(row=0, column=1)
    button_submit.grid(row=1, column=1)
    button_exit.grid(row=2, column=1)
    tk.mainloop()

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

button_JSON = Button(window,
                        text="Enter JSON or JSON-stat URL",
                        command=JSONURL)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.pack()
button_explore.pack()
button_JSON.pack()
button_exit.pack()

# Let the window wait for any events
window.mainloop()
done = 0
if filename is not None:
    while done == 0:
        try:
            file = pd.read_csv(filename)
            done = 1
        except:
            print('The file you have selected cannot be opened please try again')

if URL is not None:
    while done == 0:
        try:
            file = pd.read_json(URL)
            done = 1
        except:
            try:
                # read from json-stat
                dataset = pyjstat.Dataset.read(filename)

                # write to dataframe
                df = dataset.write('dataframe')
                # read from dataframe
                file = pyjstat.Dataset.read(df)
                done =1
            except:
                print('The file you have selected cannot be opened please try again')

print(file.head())
