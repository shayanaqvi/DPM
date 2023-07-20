from client import client
from cs import cs
from inform import inform_user
from messages import messages

from Tables import Tables

from rich.console import Console


console = Console()
current_level = 1


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
                        inform_user(messages["Invalid option"], "error")
                    else:
                        # return the item at the index selected by the user
                        selection = list_of_media[int(user_input_array[0]) - 1]
                        current_level += 1
                        return selection
                # if 'a' was input with no index
                elif user_input_array[0] == "a":
                    inform_user(messages["No index"], "error")
                # if any other data type is supplied
                else:
                    inform_user(messages["Invalid option"], "error")

            # if the user selects an invalid index
            except (IndexError):
                inform_user(messages["Invalid index"], "error")

        # add an item to the queue
        case 2:
            # check if an acceptible letter was input, in this case only 'a' is accepted
            match user_input_array[0]:
                case "a":
                    try:
                        # use isinstance()?
                        # check if an integer has been input after 'a'
                        if user_input_array[1].isdigit():
                            selection = list_of_media[int(user_input_array[1]) - 1]
                            # add the user's selection to the queue
                            client.findadd(type_of_media, selection)
                            inform_user(messages["Added to queue"], "affirmative")
                        elif user_input_array[1] == "":
                            inform_user(messages["No index"], "error")
                    except (IndexError):
                        inform_user(messages["Invalid index"], "error")
                case _:
                    inform_user(messages["Invalid option"], "error")
        # invalid input
        case _:
            inform_user(messages["Invalid option"], "error")


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


def get_user_input(list_of_media, type_of_media):
    user_input_unprocessed = input("➙ ")
    user_input = handle_input(user_input_unprocessed, list_of_media, type_of_media)
    return user_input


def browse():
    global current_level
    while True:
        match current_level:
            case 1:
                # Level 1: display all artists in the library
                cs()
                artists_unprocessed = client.list("artist")  # get raw output
                artists = process_output(artists_unprocessed, "artist")  # process the raw output
                Tables.display_table(artists, "Artists")  # display the artists

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
                Tables.display_table(albums, user_input_2)  # user_input is the name of the selected artist

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
                Tables.display_table(titles, f"{user_input_2}: {user_input_4}")

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
