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

    # loop through the items in population[], add them to the table
    for i, populant in enumerate(population):
        table.add_row(
            str(i+1),  # add indexes to the table
            populant
        )

    return table


def handle_input(user_input, list_of_media, type_of_media):
    global current_level

    # split the user's input into an array
    # to make parts of it easier to access
    user_input_array = []
    for item in user_input.split(" "):
        user_input_array.append(item)


    # this will check if only an integer has been input,
    # or whether a letter prepends it
    match len(user_input_array):
        # equivalent to viewing a subdirectory
        case 1:
            try:
                # use isinstance()?
                # check if the input is an integer or not
                if user_input_array[0].isdigit():
                    # this operation is not supported at level 6
                    if current_level == 6:
                        console.print("This operation is not supported here")
                    else:
                        # return the item at the index selected by the user
                        selection = list_of_media[int(user_input_array[0]) - 1]
                        current_level += 1
                        return selection
                # if 'a' was input with no index
                elif user_input_array[0] == "a":
                    console.print("No index was supplied")
                # if any other data type is supplied
                else:
                    console.print("Invalid operation")

            # if the user selects an invalid index
            except (IndexError):
                console.print("This index does not exist")

        # add an item to the queue
        case 2:
            # check if an acceptible letter was input, in this case only 'a' is accepted
            match user_input_array[0]:
                case "a":
                    # use isinstance()?
                    # check if an integer has been input after 'a'
                    if user_input_array[1].isdigit():
                        selection = list_of_media[int(user_input_array[1]) - 1]
                        # add the user's selection to the queue
                        client.findadd(type_of_media, selection)
                    elif user_input_array[1] == "":
                        console.print("No index was supplied")
                case _:
                    console.print("Invalid operation")
        # invalid input
        case _:
            console.print("Invalid operation")


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


def display_table(list_of_media, table_title):
    table_unpopulated = generate_table([table_title])
    table = populate_table(table_unpopulated, list_of_media)
    console.print(table)  # the table is printed here


def get_user_input(list_of_media, type_of_media):
    user_input_unprocessed = input(": ")
    user_input = handle_input(user_input_unprocessed, list_of_media, type_of_media)
    return user_input


def main():
    global current_level
    while True:
        match current_level:
            case 1:
                # Level 1: display all artists in the library
                cs()
                artists_unprocessed = client.list("artist")  # get raw output
                artists = process_output(artists_unprocessed, "artist")  # process the raw output
                display_table(artists, "Artists")  # display the artists

                current_level += 1 # go to the next level
            case 2:
                # Level 2: ask user to select an artist
                try:
                    user_input_2 = get_user_input(artists, "artist")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
            case 3:
                # Level 3: display albums by the selected artist
                cs()
                albums_unprocessed = client.find("artist", user_input_2)
                albums = process_output(albums_unprocessed, "album")
                display_table(albums, user_input_2)  # user_input is the name of the selected artist

                current_level += 1  # go to the next level
            case 4:
                # Level 4: ask user to select an album
                try:
                    user_input_4 = get_user_input(albums, "album")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level -= 3
            case 5:
                # Level 5: display songs in the selected album
                cs()
                titles_unprocessed = client.find("album", user_input_4)
                titles = process_output(titles_unprocessed, "title")
                display_table(titles, f"{user_input_2}: {user_input_4}")

                current_level += 1
            case 6:
                # Level 6: ask user to select titles
                try:
                    # user_input_unprocessed_6 = input(": ")
                    # handle_input(user_input_unprocessed_6, titles, "title")
                    get_user_input(titles, "title")
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level -= 3


main()
