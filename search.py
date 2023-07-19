from cs import cs
from client import client
from Tables import Tables

from rich.console import Console


console = Console()


def handle_input(user_input, query_results):
    input_array = []
    for item in user_input.split(" "):
        input_array.append(item)

    match len(input_array):
        case 1:
            if input_array[0] == "a":
                console.print("No index supplied")
            else:
                console.print("This operation is not supported here")
        case 2:
            match input_array[0]:
                case "a":
                    if input_array[1].isdigit():
                        selection = query_results[int(input_array[1]) - 1]
                        client.add(selection["file"])
                    elif input_array[1] == "*":
                        for item in query_results:
                            client.add(item["file"])
                    elif input_array[1] == "":
                        console.print("No index supplied")
                    else:
                        console.print("Invalid operation")
                case _:
                    console.print("Invalid operation")
        case _:
            pass
    

def main():
    cs()
    current_level = 1
    while True:
        match current_level:
            case 1:
                try:
                    # Level 1: let user search for something and return search results
                    query = input("Search: ")
                    query_results_unprocessed = client.search("any", query)
                    query_results = []
                    query_results_display = []

                    for result in query_results_unprocessed:
                        artist = result["artist"]
                        album = result["album"]
                        title = result["title"]
                        query_results_display.append(f"{result['artist']} ➙ {result['album']} ➙ {result['title']}")
                        query_results.append(result)

                    results_table_unpopulated = Tables.generate_table(["Search Results"])
                    results_table = Tables.populate_table(results_table_unpopulated, query_results_display)
                    console.print(results_table)
                    current_level += 1
                except (KeyboardInterrupt, EOFError):
                    cs()
                    return
            case 2:
                try:
                    user_input = input("➙ ")
                    handle_input(user_input, query_results)
                except (KeyboardInterrupt, EOFError):
                    cs()
                    current_level -= 1


main()
