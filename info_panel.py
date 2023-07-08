from rich.panel import Panel
from rich.console import Console
from Colours import ReturnColour


def info_panel(information):
    retcol = ReturnColour()
    console = Console()
    panel = ""
    panel = Panel(
        information,
        style=retcol.generate_random_colour()
    )
    console.print(panel)