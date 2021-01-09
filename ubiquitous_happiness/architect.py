"""
Generate the intermediate form of the folder structure.

This intermediate form is used for the conversion of the folder structure into
LaTeX.
"""
import os
from typing import List
from rich.text import Text
import json
import sys


from ubiquitous_happiness.console import console
from ubiquitous_happiness.logger import logging
from ubiquitous_happiness.custom_types.intermediate_rep import IR
from ubiquitous_happiness.config import DEBUG_MODE, ExitCodes


class Architect:
    """
    Generate the metadata from the folder structure.

    This class is used to check if the folder selected is of the required
    format create the Metadata from the folder selected.
    """

    SUPPORTED_IMAGE_TYPES: List[str] = [".jpg", ".jpeg", ".png"]
    OUTPUT_PATH: str = os.path.join(".", "output", "IR.json")

    def __init__(self, folder_path: str) -> None:
        """
        Initialize the Architect object.

        Check if the folder selected matches the format as expected by the
        system.

        :param folder_path: The path to the folder to conveter into a LaTeX
        file.
        :type folder_path: str
        """
        # TODO: Check if the folder has only 3 levels that correspond to:
        # 1. Section
        # 2. Subsection
        # 3. Subsubsection

        # Store the target folder path in a instance variable
        self.FOLDER_PATH: str = folder_path

        # Create the logger for the object
        self.notebook = logging.getLogger(__name__)

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_extension = os.path.splitext(file)[-1]
                if file_extension not in self.SUPPORTED_IMAGE_TYPES:
                    # Get the complete path to the error-causing file
                    err_file = os.path.join(root, file)
                    print()  # Simple blank line for formatting
                    console.print(("[bold red]ERROR:[/bold red] The file "
                                   f"\"{err_file}\" is [bold]not[/bold] of a "
                                   "supported file type."),
                                  overflow="fold")
                    console.print(("[bold cyan]INFO:[/bold cyan] The "
                                   "supported file types are:"
                                   f" {self.SUPPORTED_IMAGE_TYPES} but "
                                   f"we found file type: '{file_extension}'"
                                   ), overflow="fold")
                    print()  # Simple blank line for formatting
                    console.rule(Text("Goodbye!", style="bold #B80C09"),
                                 style="#B80C09")

                    self.notebook.error(("File with unsupported extension "
                                         "found in user selected folder. "
                                         f"Error file is: {err_file} with"
                                         f" extension {file_extension}"))
                    sys.exit(ExitCodes.UNSUPPORTED_IMAGES)

        self.notebook.info("Folder compliance scan is complete. The folder is "
                           "ready to be converted into a PDF.")

    def generate_ir(self) -> None:
        """Generate the JSON intermediate representation of the folder."""
        # TODO: Add logging statements

        # The path of the target folder is set as the top level
        # key of the intermediate representation.
        self.IR: IR.type = {
                            self.FOLDER_PATH: None
                           }
        for root, _, files in os.walk(self.FOLDER_PATH):
            if self.IR.get(root) is None:
                self.IR[root] = []

            for file in files:
                self.IR[root].append(file)

        if DEBUG_MODE is True:
            console.print(json.dumps(self.IR, indent=4))

        try:
            with open(os.path.abspath(self.OUTPUT_PATH), 'w') as file_handler:
                file_handler.write(json.dumps(self.IR, indent=4))
        except FileNotFoundError as e:
            console.print(("[bold red]ERROR:[/bold red] The target file"
                          " to dump to was not found!"))
            console.print(e)
            console.rule(Text("Goodbye!", style="bold #B80C09"),
                         style="#B80C09")
            sys.exit(ExitCodes.FILE_NOT_FOUND)

        console.print(("[bold green]SUCCESS:[/bold green] IR form generated "
                      "and written to folder!"))
