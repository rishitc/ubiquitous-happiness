"""
This file contains the single console instance that can be imported into other
files.

The console object handles the mechanics of generating ANSI escape sequences
for color and style. It will auto-detect the capabilities of the terminal and
convert colors if necessary.
"""
from rich.console import Console


console = Console()
