"""
The User Interface.

This file runs the UI of the project so that user can select the folder they
are interested in converting into a lab report.
"""
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label, ttk


from tkinter import filedialog, messagebox
from typing import Sized
from ubiquitous_happiness.logger import logging


FOLDER_PATH = None
notebook = logging.getLogger(__name__)


def browse_files(label_file_explorer):
    """
    Function for opening the file explorer window, to allow the user to select
    the target folder, to convert into a report.
    """
    FOLDER_PATH = filedialog.askdirectory(initialdir="/",
                                          title="Select the target folder")

    notebook.info(f"The FOLDER_PATH selected is: {FOLDER_PATH}")

    if FOLDER_PATH:  # If the variable is not empty
        # Change label contents
        label_file_explorer.configure(text=f"{FOLDER_PATH}")


def on_exit(window):
    """
    The question box to pop up when the exit button is clicked.
    """
    _msg = messagebox.askquestion(title="Confirm Exit.",
                                  message="Are you sure you want to exit?")

    # Check the button pressed by the user
    if _msg.lower() == "yes":
        window.quit()


def file_explorer():

    # Create the root window
    window = tk.Tk()
    window.title('File Explorer')  # Set the window title
    window.geometry("700x225")  # Set the window size
    # Set the background color of the window
    window.configure(background="#E9E3E6")
    notebook.debug("Top-level window has been created.")  # Log this step

    # A few constants to used for the font styles across the display
    FONT_NAME = "Lucida Grande"
    # Create the font styles of the title and subtitle
    TITLE_STYLE = tkFont.Font(family=FONT_NAME,
                              size=20,
                              weight="bold")
    SUBTITLE_STYLE = tkFont.Font(family=FONT_NAME,
                                 size=16,
                                 slant="italic")
    # Creating the font style of the body
    BODY_STYLE = tkFont.Font(family=FONT_NAME, size=12)
    # Creating the font style for the button
    BUTTON_STYLE = tkFont.Font(family=FONT_NAME, size=12, weight="bold")

    title_subtitle_frame = tk.Frame(bg="#E9E3E6")

    # Create a File Explorer label
    label_window_title = tk.Label(title_subtitle_frame,
                                  text="Ubiquitous Happiness",
                                  fg="#1E1923",
                                  bg="#E9E3E6",
                                  font=TITLE_STYLE,
                                  padx=52,
                                  pady=0)

    # Create a File Explorer label
    label_window_subtitle = tk.Label(title_subtitle_frame,
                                     text=("That annoying report is just a"
                                           " few clicks away!"),
                                     fg="#1E1923",
                                     bg="#E9E3E6",
                                     font=SUBTITLE_STYLE,
                                     padx=52,
                                     pady=0)
    notebook.debug("Title and subtitle label widgets have been created.")

    # Vertical line to separate the window title and subtitle from the body
    # of the window
    heading_sep = ttk.Separator(window, orient="horizontal")

    path_selected_frame = tk.Frame(bg="#E9E3E6")
    label_folder_selected_pre = tk.Label(path_selected_frame,
                                         text=("The path to the selected "
                                               "folder selected is: "),
                                         fg="#002952",
                                         bg="#E9E3E6",
                                         font=BODY_STYLE)

    label_folder_found = tk.Label(path_selected_frame,
                                  text="",
                                  fg="#1E1923",
                                  bg="#F4CE90",
                                  font=BODY_STYLE)

    button_frame = tk.Frame(bg="#E9E3E6")
    button_explore = tk.Button(button_frame,
                               text="Browse for Folder",
                               fg="#E9E3E6",
                               bg="#007EA7",
                               activebackground="#00A8E0",
                               activeforeground="#E9E3E6",
                               font=BUTTON_STYLE,
                               relief=tk.RAISED,
                               command=lambda:
                               browse_files(label_folder_found))

    # Button to exit the program
    button_confirm = tk.Button(button_frame,
                               text="Confirm",
                               fg="#E9E3E6",
                               bg="#587656",
                               activebackground="#698E67",
                               activeforeground="#E9E3E6",
                               font=BUTTON_STYLE,
                               relief=tk.RAISED,
                               command=lambda: on_exit(window))

    title_subtitle_frame.pack(side=tk.TOP, fill=tk.X)
    label_window_title.pack(side=tk.TOP, fill=tk.X)
    label_window_subtitle.pack(side=tk.TOP, fill=tk.X)

    heading_sep.pack(side=tk.TOP, ipadx=600, fill=tk.X)

    path_selected_frame.pack(side=tk.TOP, fill=tk.X, pady=50)
    label_folder_selected_pre.pack(side=tk.LEFT, padx=15, fill=tk.X)
    label_folder_found.pack(side=tk.RIGHT, padx=15, fill=tk.X, expand=tk.YES)

    button_frame.pack(side=tk.BOTTOM, fill=tk.X)
    # Buttons to display on the window
    button_explore.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X,
                        anchor=tk.N)
    button_confirm.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X,
                        anchor=tk.N, ipadx=30)

    # Start the event loop and let the window wait for any events
    window.mainloop()


if __name__ == "__main__":
    file_explorer()
