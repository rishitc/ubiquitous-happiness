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
from ubiquitous_happiness.architect import Architect

if __name__ == "__main__":
    notebook = logging.getLogger(__name__)  # Create a logger for this file

    # The heading of the application
    console.rule(title=("[bold cyan]Ubiquitous Happiness - Your "
                        "[italic]annoying[/italic] report is just a few steps"
                        " away!"),
                 style="green", align="center")

    notebook.info("Title printed.")

    print()  # Simple blank line for formatting

    # Explain the steps to create the report to the user
    console.print(("[bold cyan]So here are the steps you need to"
                  " follow to generate your report:"), overflow="fold")
    console.print("1. Select the target folder.", overflow="fold")
    console.print("2. Enter some metadata")
    console.print("3. Enjoy the generated results.", overflow="fold")

    print()  # Simple blank line for formatting

    console.rule("")
    notebook.info("Steps explained.")

    notebook.info("File explorer launched.")
    FOLDER_PATH = navigator.file_explorer()
    notebook.info("File explorer completed.")

    notebook.debug("The path selected by the user is: %s",
                   FOLDER_PATH)

    if FOLDER_PATH is None:
        console.print("[bold red]ERROR:[/bold red] Folder Path is None.")
        raise FileNotFoundError("Folder path selected is None!")

    # Create the architect object and run the folder scan to check if it can be
    # converted into the PDF
    buckminster = Architect(FOLDER_PATH)
    buckminster.generate_ir()
