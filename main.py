import sys

from cs import cs
from shuffle import shuffle_library
from browse_library import browse_library
from search import search
from info_panel import info_panel
from playlist_opt import playlist_options
from Colours import colours

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
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
            case "browse":
                browse_library()
            case "search":
                search()
            case "shuffle":
                shuffle_library()
            case "opt":
                playlist_options()
            case "help":
                help = (
                    '# Help\n'
                    'Usage:\n'
                    'Input `dpm` followed by one of the following arguments:\n'
                    '- browse\n'
                    '- search\n'
                    '- shuffle\n'
                    '- opt\n'
                    '- help\n\n'
                    'For example, `dpm browse` will let you browse your library.'
                )
                console.print(
                    Panel(
                        Markdown(
                            help, justify="left"
                        ),
                        style="green",
                        box=box.MINIMAL
                    )
                )
            case _:
                console.print(
                    Panel(
                        "dpm: invalid arguments provided\nInput 'dpm help' for more information",
                        style="red",
                        box=box.MINIMAL
                    )
                )


main()
