# The code for part 1: Script 1
# The below code is adapted from code found here: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
# import filedialog module
from tkinter import filedialog
from copy import deepcopy
import tkinter as tk
# import pandas
import pandas as pd
from pyjstat import pyjstat
import json
import openpyxl
filepath = None
# Function for opening the
# file explorer window
def browseFiles():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("csv Files", ".csv"), ("json Files", ".json")))
    # Close the window once file is chosen
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
if filepath is not None:
    # Reading in regular csv files
    try:
        dataframe = pd.read_csv(filepath)
    except:
        pass
    # Reading in json files
    try:
        f = open(filepath)
        file = f.read()
        data = json.loads(file)
        dataframe = pd.json_normalize(data['results'])
    except:
        pass
    try:
        dataframe = pd.read_json(filepath, orient='index')
    except:
        pass
    # reading in differently formatted json
    try:
        dataframe = pd.read_json(filepath, orient='columns')
    except:
        pass
    # reading in json stat files
    try:
        file = open(filepath)
        dataset = pyjstat.Dataset.read(file)
        # write to dataframe
        dataframe = dataset.write('dataframe')
    except:
        pass
    try:# create a name for an excel file
        datatoexcel = pd.ExcelWriter('exported_data.xlsx')

        # write DataFrame to excel
        dataframe.to_excel(datatoexcel)

        # save the excel
        datatoexcel.save()
        print(dataframe.head(), '\n The Data has been written to an Excel File successfully.\n'
              'The file is named "exported_data.xlxs"\n'
              'The Data has', dataframe.shape[1], 'columns and', dataframe.shape[0], 'rows.')
    except:
        print('Sorry this dataset could not be opened')