"""
The User Interface.

This file runs the UI of the project so that user can select the folder they
are interested in converting into a lab report.
"""
import os
import sys


from ubiquitous_happiness.console import console
from ubiquitous_happiness.henry import FOLDER_PATH, file_explorer
from ubiquitous_happiness.logger import logging
from ubiquitous_happiness.folder_protocol import FolderIntegrity

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
    console.print("2. Configure the selected files.", overflow="ellipsis")
    console.print("3. ", overflow="ellipsis")
    console.print("4. ", overflow="ellipsis")
    console.print("5. ", overflow="ellipsis")

    logging.info("Steps explained.")

    logging.info("File explorer launched.")
    file_explorer()
    logging.info("File explorer completed.")

    logging.debug("The path selected by the user is: %s", FOLDER_PATH)

    # chk: bool = False
    # fi: FolderIntegrity = FolderIntegrity()
    # if FOLDER_PATH is not None and FOLDER_PATH != "":
    #     with os.scandir(FOLDER_PATH) as root:
    #         for entry in root:
    #             if not entry.name.startswith('.'):
    #                 fi.chk_folder_base(entry)
    #     folder_contents = os.listdir(path=FOLDER_PATH)
    #     chk = fi.compile_result()

    #     if chk is False:  # If the folder is not the right format
    #         console.print("[bold red]ERROR:[/bold red] The folder format is not right!")
    #         logging.error("")
    #         sys.exit(1)

