from cs import cs
from shuffle import shuffle_library
from browse_library import browse_library
from search import search
from currently_playing import currently_playing
from Colours import ReturnColour
from Menu import Menu

from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


menu = Menu()
console = Console()
retcol = ReturnColour()


def main():
    """Application's main function"""
    main_menu_table = Table(
        expand=True,
        box=box.SIMPLE_HEAD,
        row_styles=["", "dim"]
    )
    main_menu_table.add_column("#", ratio=1)
    main_menu_table.add_column("Options", ratio=12)

    display_index = 1
    main_menu = menu.generate_menu([
        "Browse Library",
        "Search Library",
        "Shuffle Library",
        "Currently Playing",
        "Exit"
    ])

    # generate table
    for entry in main_menu:
        main_menu_table.add_row(
            str(display_index),
            entry
        )
        display_index += 1

    cs()
    while True:
        try:
            cs()
            main_menu_panel = Panel(
                main_menu_table,
                title="Main Menu",
                style=retcol.generate_random_colour()
            )
            console.print(main_menu_panel)
            menu_opt = int(input("Do: "))

            match menu_opt:
                case 1:
                    cs()
                    browse_library()
                case 2:
                    cs()
                    search()
                case 3:
                    cs()
                    shuffle_library()
                case 4:
                    cs()
                    currently_playing()
                case 5:
                    cs()
                    exit()
                case _:
                    pass
        except (KeyError, ValueError):
            pass
        except (KeyboardInterrupt):
            cs()
            exit()


main()
