import sys

from cs import cs
from shuffle import shuffle_library
from browse_library import browse_library
from search import search
from playlist_opt import playlist_options
from currently_playing import currently_playing

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()


def main():
    user_arg = sys.argv
    if len(user_arg) == 1:
        console.print(
            Panel(
                "dpm: no arguments provided\nInput 'dpm help' for more information",
                style="red",
                box=box.MINIMAL
            )
        )
    else:
        match user_arg[1]:
            case "browse" | "b":
                cs()
                browse_library()
            case "search" | "f":
                cs()
                search()
            case "shuffle" | "s":
                shuffle_library()
            case "option" | "o":
                cs()
                playlist_options(user_arg)
            case "current" | "c":
                cs()
                currently_playing()
            case "help" | "h":
                with open("help.md", "r") as help:
                    contents = help.readlines()
                    help_str = ""
                    for item in contents:
                        help_str += item
                    console.print(
                        Panel(
                            Markdown(
                                str(help_str), justify="left"
                            ),
                            style="green",
                            box=box.ROUNDED
                        )
                    )
            case _:
                console.print(
                    Panel(
                        "dpm: invalid argument provided\nInput 'dpm help' for more information",
                        style="red",
                        box=box.MINIMAL
                    )
                )
