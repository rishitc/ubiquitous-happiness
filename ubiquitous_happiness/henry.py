"""
The User Interface.

This file runs the UI of the project so that user can select the folder they
are interested in converting into a lab report.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
from ubiquitous_happiness.logger import logging


FOLDER_PATH = None


def browseFiles(label_file_explorer):
    """
    Function for opening the file explorer window, to allow the user to select
    the target folder, to convert into a report.
    """
    FOLDER_PATH = filedialog.askdirectory(initialdir="/",
                                          title="Select the target folder")

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + FOLDER_PATH)


def onExit():
    """
    The question box to pop up when the exit button is clicked.
    """
    _msg = messagebox.askquestion(title="Confirm Exit.",
                                  message="Are you sure you want to exit?")

    # Check the button pressed by the user
    if _msg.lower() == "yes":
        exit()
    else:
        pass


def file_explorer():
    notebook = logging.getLogger(__name__)
    notebook.info("el")
    # Create the root window
    window = tk.Tk()

    # Set window title
    window.title('File Explorer')

    # Set window size
    window.geometry("500x500")

    # Set window background color
    window.config(background="white")

    # Create a File Explorer label
    label_file_title = tk.Label(window,
                                text="Ubiquitous Happiness",
                                width=100, height=2,
                                fg="blue")
    # Create a File Explorer label
    label_file_subtitle = tk.Label(window,
                                   text=("That annoying report is just a few"
                                        " clicks away"),
                                   width=100, height=2,
                                   fg="blue")
    label_file_explorer = tk.Label(window,
                                   text="",
                                   width=100, height=2,
                                   fg="blue")

    button_explore = tk.Button(window,
                               text="Browse Files",
                               command=lambda:
                               browseFiles(label_file_explorer))

    # Button to exit the program
    button_exit = tk.Button(window,
                            text="Exit",
                            command=onExit)

    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_title.grid(column=0, row=0)
    label_file_subtitle.grid(column=0, row=1)
    label_file_explorer.grid(column=0, row=2)

    button_explore.grid(column=0, row=3)

    button_exit.grid(column=0, row=4)

    # Let the window wait for any events
    window.mainloop()


if __name__ == "__main__":
    file_explorer()
