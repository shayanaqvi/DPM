from client import client


class Menu():
    """Handle menu generation"""

    def __init__(self):
        pass

    def generate_menu(self, prompts: list):
        """Generate a list of options for the user to choose from"""
        i = 1
        for item in prompts:
            print(f"{i}.", item)
            i += 1

    def list_directory(self, directory, type):
        """List a given directory"""
        list = client.lsinfo(directory)
        list_array = []
        index = 0
        menustr = ""

        for item in list:
            list_array.append(item[type])

        for item in list_array:
            if index < 9:
                print(f"0{str(index+1)} {item}")
            else:
                print(f"{str(index+1)} {item}")
            index += 1

        return list_array

    def return_query_results(self, type, query):
        """Return results of a query"""
        result = client.find(type, query)
        return_type = ["title", "album", "artist"]
        for item in result:
            print(item[return_type[0]], item[return_type[1]], item[return_type[2]])
