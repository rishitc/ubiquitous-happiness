"""
The User Interface.

This file runs the UI of the project so that user can select the folder they
are interested in converting into a lab report.
"""
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label, ttk


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

    # Create the root window
    window = tk.Tk()
    window.title('File Explorer')  # Set the window title
    window.geometry("600x600")  # Set the window size
    # Set the background color of the window
    window.configure(background="#E9E3E6")
    notebook.debug("Top-level window has been created.")  # Log this step

    frame_titles = tk.Frame(window)

    # Create the font styles of the title and subtitle
    TITLE_STYLE = tkFont.Font(family="Lucida Grande", size=20, weight="bold")
    SUBTITLE_STYLE = tkFont.Font(family="Lucida Grande", size=16,
                                 slant="italic")

    # Create a File Explorer label
    label_frame_title = tk.Label(window,
                                 text="Ubiquitous Happiness",
                                 height=1,
                                 fg="#07020D",
                                 bg="#E9E3E6",
                                 font=TITLE_STYLE,
                                 padx=52,
                                 pady=0)

    # Create a File Explorer label
    label_frame_subtitle = tk.Label(window,
                                    text=("That annoying report is just a"
                                          " few clicks away!"),
                                    height=1,
                                    fg="#07020D",
                                    bg="#E9E3E6",
                                    font=SUBTITLE_STYLE,
                                    padx=52,
                                    pady=0)

    # Vertical line to separate the frame title and subtitle from the body
    # of the frame
    heading_sep = ttk.Separator(window, orient="horizontal")

    # frame = tk.Frame(window)
    # label_file_explorer = tk.Label(frame,
    #                                text="The file",
    #                                height=1,
    #                                fg="blue")
    # label_file_explorer.pack(side=tk.LEFT)

    # label_file_found = tk.Label(frame,
    #                             text="The file",
    #                             height=1,
    #                             fg="blue")
    # label_file_found.pack(side=tk.RIGHT)

    # button_explore = tk.Button(window,
    #                            text="Browse Files",
    #                            command=lambda:
    #                            browseFiles(label_file_explorer))

    # # Button to exit the program
    # button_exit = tk.Button(window,
    #                         text="Exit",
    #                         command=onExit)

    label_frame_title.pack(side=tk.TOP, fill=tk.X)
    label_frame_subtitle.pack(side=tk.TOP, fill=tk.X)
    heading_sep.pack(side=tk.TOP, ipadx=600, fill=tk.X)

    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    # label_frame_title.grid(column=0, row=0)
    # label_frame_subtitle.grid(column=0, row=1)
    # s.grid(column=0, row=2, sticky='ew')
    # label_file_explorer.grid(column=0, row=3)

    # button_explore.grid(column=0, row=4)
    # button_exit.grid(column=0, row=5)

    # Start the event loop and let the window wait for any events
    window.mainloop()


if __name__ == "__main__":
    file_explorer()
