"""
Generate the intermediate form of the folder structure.

This intermediate form is used for the conversion of the folder structure into
LaTeX.
"""
import os
from typing import List
from rich.text import Text

from ubiquitous_happiness.console import console
from ubiquitous_happiness.logger import logging


class Architect:
    """
    Generate the metadata from the folder structure.

    This class is used to check if the folder selected is of the required
    format create the Metadata from the folder selected.
    """

    SUPPORTED_IMAGE_TYPES: List[str] = ["jpg", "jpeg", "png"]

    def __init__(self, folder_path: str) -> None:
        """
        Initialize the Architect object.

        Check if the folder selected matches the format as expected by the
        system.

        :param folder_path: The path to the folder to conveter into a LaTeX
        file.
        :type folder_path: str
        """
        # Create the logger for the object
        self.notebook = logging.getLogger(__name__)

        for root, _, files in os.walk(folder_path):
            for file in files:
                if os.path.splitext(file) not in self.SUPPORTED_IMAGE_TYPES:
                    # Get the complete path to the error-causing file
                    err_file = os.path.join(root, file)
                    print()  # Simple blank line for formatting
                    console.print(("[bold red]ERROR:[/bold red] The file "
                                   f"\"{err_file}\" is [bold]not[/bold] of a "
                                   "supported file type."),
                                  overflow="fold")
                    console.print(("[bold cyan]INFO:[/bold cyan] The "
                                   "supported file types are:"
                                   f" {self.SUPPORTED_IMAGE_TYPES}"),
                                  overflow="fold")
                    print()  # Simple blank line for formatting
                    console.rule(Text("Goodbye!", style="bold #B80C09"),
                                 style="#B80C09")

                    self.notebook.error(("File with unsupported extension "
                                         "found in user selected folder. "
                                         "Error file is: "
                                         "{err_file}}"))

        self.notebook.info("Folder compliance scan is complete. The folder is "
                           "ready to be converted into a PDF.")
