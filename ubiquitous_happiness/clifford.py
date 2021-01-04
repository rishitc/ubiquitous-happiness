"""
The User Interface.

This file runs the UI of the project so that user can select the folder they
are interested in converting into a lab report.
"""
import os
import sys
from rich.text import Text


from ubiquitous_happiness.console import console
import ubiquitous_happiness.henry as navigator
from ubiquitous_happiness.logger import logging
from ubiquitous_happiness.folder_protocol import FolderIntegrity

SUPPORTED_IMAGE_TYPES = ["jpg", "jpeg", "png"]

if __name__ == "__main__":
    notebook = logging.getLogger(__name__)  # Create a logger for this file

    # The heading of the application
    console.rule(title=("[bold cyan]Ubiquitous Happiness - Your "
                        "[italic]annoying[/italic] report is just a few steps"
                        " away!"),
                 style="green", align="center")

    logging.info("Title printed.")

    print()

    # Explain the steps to create the report to the user
    console.print(("[bold cyan]So here are the steps you need to"
                  " follow to generate your report:"), overflow="ellipsis")
    console.print("1. Select the target folder.", overflow="ellipsis")
    console.print("2. Enter some metadata")
    console.print("3. Enjoy the generated results.", overflow="ellipsis")
    console.rule("")
    logging.info("Steps explained.")

    logging.info("File explorer launched.")
    FOLDER_PATH = navigator.file_explorer()
    logging.info("File explorer completed.")

    logging.debug("The path selected by the user is: %s",
                  FOLDER_PATH)

    if FOLDER_PATH is None:
        console.print("[bold red]ERROR:[/bold red] Folder Path is None.")
        raise FileNotFoundError("Folder path selected is None!")

    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            if os.path.splitext(file) not in SUPPORTED_IMAGE_TYPES:
                # Get the complete path to the error-causing file
                err_file = os.path.join(root, file)
                print()  # Simple blank line for formatting
                console.print(("[bold red]ERROR:[/bold red] The file "
                              f"\"{err_file}\" is [bold]not[/bold] of a "
                               "supported file type."), overflow="ellipsis")
                console.print(("[bold cyan]INFO:[/bold cyan] The supported "
                              f"file types are: {SUPPORTED_IMAGE_TYPES}"),
                              overflow="ellipsis")
                print()  # Simple blank line for formatting
                console.rule(Text("Goodbye!", style="bold #B80C09"),
                             style="#B80C09")
