from Menu import Menu
from cs import cs
from client import client


menu = Menu()


# TODO
# clean up code


# let inputting 'b' function


# this code works, it will process a query and display an output. 
# it does not handle input
# def search():
#     query = input("Search: ")
#     query_result = client.search("any", query)
#     query_processed = process_query_result(query_result)

#     # print processed query result
#     for item in query_processed:
#         print(item["artist"], item["album"], item["title"])


# def process_query_result(query_result):
#     query_result_array = []
#     for item in query_result:
#         query_result_array.append(item)

#     return query_result_array

# def search():
#     levels = [0, 1, 2]
#     current_level = 1
#     while True:
#         try:
#             query = input("Search: ")
#             query_result = client.search("any", query)
#             query_processed = process_query_result(query_result)

#             # print processed query result
#             for item in query_processed:
#                 print(item["artist"], item["album"], item["title"])

#             query_option = input("Choose: ")
#             query_option_array = []
#             for item in query_option.split(" "):
#                 query_option_array.append(item)

#             if len(query_option_array) > 1:
#                 query_selection = query_processed[int(query_option_array[1]) - 1]
#                 query_selection_final = query_selection["file"]
#                 handle_cbi_output(query_option_array, query_selection_final)
#             else:
#                 query_selection = 0
#         except (ValueError, IndexError, TypeError):
#             pass


# def process_query_result(query_result):
#     query_result_array = []
#     for item in query_result:
#         query_result_array.append(item)

#     return query_result_array


# def handle_cbi_output(input_array, media_selection):
#     match input_array[0]:
#         case "a":
#             # print message when added, do this during interface
#             # design, maybe in a small box at the bottom?
#             client.add(media_selection)
#             print("Added")
#             return ""
#         case "b":
#             return ""
#         case _:
#             pass


def search():
    levels = [0, 1, 2]
    current_level = 1
    while True:
        try:
            match current_level:
                case 1:
                    query = input("Search: ")
                    query_input_array = []
                    for item in query:
                        query_input_array.append(item)

                    if len(query_input_array) == 1:
                        current_level = handle_cbi_output(query_input_array, "", current_level, levels, "search")
                    else:
                        query_result = client.search("any", query)
                        query_processed = process_query_result(query_result)

                        # print processed query result
                        for item in query_processed:
                            print(item["artist"], item["album"], item["title"])
                        current_level += 1
                case 2:
                    query_option = input("Choose: ")
                    query_option_array = []
                    for item in query_option.split(" "):
                        query_option_array.append(item)

                    query_selection = 0
                    query_selection_file = ""

                    if len(query_option_array) > 1:
                        query_selection = query_processed[int(query_option_array[1]) - 1]
                        query_selection_file = query_selection["file"]
                    else:
                        pass

                    current_level = handle_cbi_output(query_option_array, query_selection_file, current_level, levels, "choose")
                case _:
                    cs()
                    return ""
        except (ValueError, IndexError):
            pass


def process_query_result(query_result):
    query_result_array = []
    for item in query_result:
        query_result_array.append(item)

    return query_result_array


def handle_cbi_output(input_array, media_selection, current_level, available_levels, type):
    if type == "search":
        if len(input_array) > 1:
            pass
        else:
            match input_array[0]:
                case "b":
                    current_level -= 1
                    return current_level
                case _:
                    return current_level
    elif type == "choose":
        if len(input_array) > 1:
            match input_array[0]:
                case "a":
                    # print message when added, do this during interface
                    # design, maybe in a small box at the bottom?
                    client.add(media_selection)
                    print("Added")
                    return current_level
                case _:
                    print("Invalid option")
                    return current_level
        else:
            match input_array[0]:
                case "b":
                    current_level -= 1
                    return current_level
                case _:
                    return current_level
