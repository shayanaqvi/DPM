from cs import cs
from shuffle import shuffle_library
from browse_library import browse_library
from search import search
from queue import queue
from Menu import Menu

from rich.console import Console
from rich.layout import Layout

# TODO
# error handling, move functions into separate files
# pipe messages/error messages to a separate panel (during interface design)
# if 'a' or 'v' is input without an index, an error is returned
# print instructions during browsing in a separate panel
# input type check for menu_opt


menu = Menu()


console = Console()
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)


def main():
    cs()
    while True:
        cs()
        menu.generate_menu(["Browse Library", "Search Library", "Shuffle Library", "Currently Playing", "Exit"])
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
                queue()
            case 5:
                cs()
                exit()
            case _:
                # error messaging in separate panel
                pass


main()
