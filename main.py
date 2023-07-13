import sys

from shuffle import shuffle_library
from browse_library import browse_library
from search import search
from playlist_opt import playlist_options

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
                browse_library()
            case "search" | "f":
                search()
            case "shuffle" | "s":
                shuffle_library()
            case "opt" | "o":
                playlist_options()
            case "help" | "h":
                help = (
                    '# Help\n'
                    'Usage:\n'
                    'Input `dpm` followed by one of the following arguments:\n'
                    '- browse (`b`)\n'
                    '- search (`f`)\n'
                    '- shuffle (`s`)\n'
                    '- opt (`o`)\n'
                    '- help (`h`)\n\n'
                    'For example, `dpm browse`, or `dpm b` will let you browse your library.'
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
                        "dpm: invalid argument provided\nInput 'dpm help' for more information",
                        style="red",
                        box=box.MINIMAL
                    )
                )


main()
