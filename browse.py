from client import client
from cs import cs

from rich.console import Console
from rich.table import Table
from rich import box


console = Console()
current_level = 1


def generate_table(columns: list):
    # ADD THIS TO A CLASS
    table = Table(
        box=box.SIMPLE,
        style="cyan"
    )

    table.add_column(
        "#",
        style="cyan",
        header_style="cyan"
    )

    # add columns to the table
    for name in columns:
        table.add_column(
            name,
            header_style="cyan"
        )

    return table


def populate_table(table_to_populate, population: list):
    table = table_to_populate
    for i, populant in enumerate(population):
        table.add_row(
            str(i+1),
            populant
        )

    return table


def handle_input():
    pass


def process_output(output, type_of_media):
    output_array = None
    match type_of_media:
        case "artist" | "title":
            output_array = []
            for item in output:
                output_array.append(item[type_of_media])
            return output_array
        case "album":
            output_array = []
            stop_duplication = ""
            for item in output:
                if item["album"] == stop_duplication:
                    pass
                else:
                    stop_duplication = item["album"]
                    output_array.append(item["album"])
            return output_array


def display_media(list_of_media, table_title):
    table_unpopulated = generate_table([table_title])
    table = populate_table(table_unpopulated, list_of_media)
    console.print(table)  # the table is printed here


def main():
    global current_level
    while True:
        match current_level:
            case 1:
                # Level 1: display all artists in the library
                cs()
                artists_unprocessed = client.list("artist")  # get raw output
                artists = process_output(artists_unprocessed, "artist")  # process the raw output
                display_media(artists, "Artists")  # display the artists

                current_level += 1 # go to the next level
            case 2:
                # Level 2: get input form the user
                try:
                    user_input_unprocessed = input(": ")  # unprocessed user input
                    user_input = handle_input()  # have the user's input processed
                    break
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass


main()
