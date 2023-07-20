from rich import box
from rich.panel import Panel
from rich.console import Console


console = Console()


def inform_user(message, message_type):
    colour = None
    match message_type:
        case "error":
            colour = "red"
        case "general":
            colour = "blue"
        case "affirmative":
            colour = "green"

    panel = Panel(
        message,
        box=box.SIMPLE,
        style=colour,
        padding=1
    )

    console.print(panel)
